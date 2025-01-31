from PIL import Image
import os
from lavis.models import load_model_and_preprocess
import torch
import json
import cv2

def main():

    # Caption all the videos
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
    model, vis_processors, _ = load_model_and_preprocess(name="blip2_t5", model_type="pretrain_flant5xxl", is_eval=True, device=device)
    
    video_src = '/data/ACID/acid_large_video'
    camera_src = '/data/ACID/acid_large'
    dst = '/data/ACID/acid_large_caption'
    # ['acid/train/', 'acid/validation/', 'acid/test/', 'acid_large/']
    os.makedirs(dst, exist_ok=True)
    all_captions = {}
    for vid_path in os.listdir(video_src):
        try:
            vid = vid_path.split('.')[0]
            video_file = os.path.join(video_src, vid_path)
            caption_path = os.path.join(dst, f'{vid}.summary_text.json')
            if os.path.exists(caption_path):
                print('exists')
                continue
            camera_path = f'{camera_src}/{vid}.txt'
            timestamps = []
            with open(camera_path, 'r') as f:
                annos = f.readlines()[1:]
                
            timestamp_mid_second = int(annos[len(annos)//2].strip().split()[0]) / 1_000_000
            
            video = cv2.VideoCapture(video_file)
            fps = video.get(cv2.CAP_PROP_FPS)
            frame_index = int(fps * timestamp_mid_second)
            video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
            ret, frame = video.read()
            if not ret:
                video.release()
                print(f"Cannot read frame at index {frame_index} {video_file}")
                continue
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            video.release()

            image = vis_processors["eval"](image).unsqueeze(0).to(device)
            caption = model.generate({"image": image, "prompt": "Your task is to caption the images using a neutral tone and avoid passive voice. \
    DO NOT bundle items under general terms like ornaments and accessories. If you have name for an object, use it instead of just 'object'. \
    Do NOT add abstract thoughts or emotions it may evoke. Omit describing the style in the image. \
    Describe the image content directly."})

            with open(caption_path, "w") as outfile:
                json.dump({'text':caption[0]}, outfile)
            print(f"read frame at index {frame_index} {video_file}")
        except:
            print(f"Cannot read frame at index {frame_index} {video_file}")
            
        all_captions[vid] = caption[0]
    caption_path = os.path.join(dst, f'all_summary_text.json')
    with open(caption_path, "w") as outfile:
        json.dump(all_captions, outfile)
        
if __name__ == '__main__':
    main()