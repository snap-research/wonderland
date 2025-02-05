# acid dataset

Download the ACID and ACID-Large dataset from [Infinite Nature GitHub](https://infinite-nature.github.io/).

The dataset consists of a set of .txt files, each corresponding to a video clip. These files contain timestamps and camera poses for frames in each clip.

The dataset follows a format similar to [RealEstate10K](https://google.github.io/realestate10k/). Please follow the steps to process the dataset:

1. Download source videos with `acid/download_videos.py`.

2. Crop the videos to extract clips of interest with `acid/crop_videos.py`.

3. Caption the clips of interest with `acid/caption_frames.py`.

As each clip in ACID contains frames of the same scene, we use an image captioning model to describe the scenes.


#### Noted. [DL3DV](https://github.com/DL3DV-10K/Dataset) contains many scenes with complex camera trajectories and large view changes between consecutive keyframes. We empirically find that incorporating it during training is crucial for enhancing camera controllability. We strictly adhere to the [RealEstate10K](https://google.github.io/realestate10k/) normalization pipeline for DL3DV pose normalization. For details, please refer to Sec. 4.3 in [this work](https://tinghuiz.github.io/papers/siggraph18_mpi.pdf). 

#### We are in the process of reviewing the release of the normalized poses of DL3DV.
