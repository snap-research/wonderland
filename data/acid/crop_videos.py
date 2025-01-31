import os
import subprocess

def read_timestamps(txt_file):
    """Read the timestamps from the text file."""
    timestamps = []
    try:
        with open(txt_file, 'r') as f:
            annos = f.readlines()[1:]
            # if len(annos) < 49:
            #     return timestamps
            timestamp_start_second = int(annos[0].strip().split()[0]) / 1_000_000 # Convert microseconds to seconds
            timestamp_end_second = int(annos[-1].strip().split()[0]) / 1_000_000
            return [timestamp_start_second, timestamp_end_second]
    except:
        print(f'error opening {txt_file}')
        return []

def extract_video(video_file, timestamps, output_video):
    """Extract frames at the specified timestamps."""
    command = 'ffmpeg -ss '+str(timestamps[0])+' -to ' +str(timestamps[1]+0.5) + ' -i '+ video_file + ' -c copy '+ output_video
    print(command)
    os.system(command)
    
def extract_and_create_video(video_file, txt_file, output_video, frame_path=None):
    """Main function to extract frames based on timestamps and create a new video."""
    timestamps = read_timestamps(txt_file)
    if not timestamps:
        return

    if os.path.exists(output_video):
        return
    extract_video(video_file, timestamps, output_video)
    # command = 'ffmpeg -ss '+ str(timestamps[0]) + ' -i ' + video_file + ' -vframes 1 -f image2 ' + frame_path
    # os.system(command)


# Example usage
camera_src = '/data/ACID/acid/train/'
video_src = '/data/ACID/acid_video/train_video/'
dst_path = '/data/ACID/acid_video/train_video_croped/'
# frame_dst_path = '/data/ACID/acid_video/first_frames/'
os.makedirs(dst_path, exist_ok=True)
# os.makedirs(frame_dst_path, exist_ok=True)

for video_id in sorted(os.listdir(video_src)):
    video_path = os.path.join(video_src, video_id)
    txt_path = os.path.join(camera_src, video_id.replace('.mp4', '.txt'))
    output_path = os.path.join(dst_path, video_id.replace('.mp4', '_crop.mp4'))
    # frame_path = os.path.join(frame_dst_path, video_id.replace('.mp4', '.png'))

    extract_and_create_video(video_path, txt_path, output_path)
