# Project Overview

## Introduction
The current project focuses on detecting live bee drone sperm using the YOLO v8 library in processed videos. It aims to detect the head and tail of each live bee drone sperm. Live spermatozoa can be identified by their circular shape, while dead ones tend to be elongated. The project builds upon the [CASABee](CASABee-master) - Master project, developed by my thesis advisor, Jose Divasón Mallagaray, as a foundation for obtaining YOLO-formatted video labels and subsequent model training. The goal is to obtain the best model based on the Recall metric.

## Repository Index
* [CodeProcessVideo:](DSetsCreation\MoSpeSet\CodeProcessVideo) The video processing code can be found in this folder within the repository. It utilizes the CASABee base and creates a process to obtain annotations in YOLO format.

* [ProcessVideoInformation:](DSetsCreation\MoSpeSet\Data) Here you will find the frames of each video, the annotation fail .txt, and the frames with detection boxes and numbers to identify each box in the annotation fail for debugging purposes.

* [YAML Base Data:](DSetsCreation\MoSpeSet\YAMLBase)  Here you will find the cleaned information to create the dataset in YAML structure for YOLO V8. We need to mention that we use the [utils for processing annotations](DSetsCreation\MoSpeSet\CodeProcessVideo\VerifyTagging.ipynb) to make some changes and convert the annotations into the correct YOLO format after cleaning the failed boxes. However, there is still a blank space in the training txt files that causes some problems. The solution was to remove it from the notebooks.

* [YAMLDataSet:](DSetsCreation\MoSpeSet\YAMLDataSet) The YAML dataset with the correct configuration to be used.

* [TrainNoteBooks:](Models\MotileDetection\BExcecution) Here you will find all the notebooks used to train our models and some code to verify the results metrics.

* [ResultsModels:](https://unirioja-my.sharepoint.com/:f:/g/personal/migomesu_unirioja_es/EqVBvRk5DIVHm8mlDVJsqN4BSx5s0hYBZvsGSQkH0ygkMg?e=UffF47) Here you will be redirected to my personal folder where you can find the results of the Train Notebooks execution.

* [Extracting ROI and Tracking with the Best Model](Models\MotileDetection\PostBestModel) Here we use the best model to track the videos and extract the regions of interest (ROI) for further steps.

* [Videos](https://www.dropbox.com/scl/fi/vnyl0lbmzarkfm7jrt88h/Videos.zip?rlkey=4i3y4so9xnomins88tpgdls0z&st=ai5y6k6e&dl=0) Here you will be redirected to the zip file containing all the videos used in the processes.

* Tracking Videos: Here you will be redirect to the video tracking folder of [BotSort Method](https://unirioja-my.sharepoint.com/:f:/g/personal/migomesu_unirioja_es/Eq7PEm_kJpBCm5-nWKWT1ykBxYQcNf5CPyj1Vqhv7WsoAA?e=hdnwxc) and [ByteTrack Method](https://unirioja-my.sharepoint.com/:f:/g/personal/migomesu_unirioja_es/Ehv1VqWt6JZGrH5X9H4AgPEBV6HdowjSohCXj0Rc98cS5Q?e=ea9nDY).

## Current Progress

The training process for the mobile sperm detection model has been completed. Different sizes of neural networks based on YOLOv8 were used, along with varying input image sizes ranging from the standard size to the maximum resolution of the videos. The obtained results are as follows:

<p align="center">
  <img src="Models\MotileDetection\ResultadosModelos.png" alt="Models Results">
</p>

Based on the above, we selected the Small model with 1920 pixels as the best model.

Currently, we are processing the first frame of all the videos used in the training, validation, and testing processes using the best mobile sperm detection model. The main objective is to obtain the regions of interest (ROI) and extract each individual mobile sperm for manual labeling of the head and tail.

Additionally, we are using the best trained model to generate videos where the movement trajectories of the mobile sperm are visualized using the two tracking methods provided by the YOLO library.

## Next Steps
1. [x] Obtain the regions of interest (ROI) from the first frame of each video. You can find it [here](https://unirioja-my.sharepoint.com/:f:/g/personal/migomesu_unirioja_es/EiQ6OwZ20UNJme9Bnpp7QDMBv3sQ28NwRdytro0SRznJfQ?e=7cMSJJ).
2. [ ] Perform image labeling.
3. [ ] Build the dataset and YAML configuration file.
4. [ ] Perform PseudoLabeling by extracting the ROIs from all frames of the videos and training the model.
    * [ ] Structure sequential code for ROI extraction.
    * [ ] Create a schema for saving annotations and adding images and annotations together for the YAML file.

## Conclusion
This project aims to contribute to the field of bee reproductive biology by providing a reliable tool for drone sperm analysis, facilitating research in this crucial area.

For more information or collaboration opportunities, feel free to reach out!