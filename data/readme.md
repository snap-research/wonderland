# acid dataset

Download the ACID and ACID-Large dataset from [Infinite Nature GitHub](https://infinite-nature.github.io/).

The dataset consists of a set of .txt files, each corresponding to a video clip. These files contain timestamps and camera poses for frames in each clip.

The dataset follows a format similar to [RealEstate10K](https://google.github.io/realestate10k/). Please follow the steps to process the dataset:

Download source videos with acid/download_videos.py.
Crop the videos to extract clips of interest with acid/crop_videos.py.
Caption the clips of interest with acid/caption_frames.py.

As each clip in ACID contains frames of the same scene, we use an image captioning model to describe the scenes.

