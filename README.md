# CrossAgeFaceRecognition
Exploring a way to verify/recognize faces with variation in age

## How to run: 

Download feature dataset and runclass.py
Navigate to file location, and give command

$python runclass.py

## issues to resolve:
### 1. Feature Extraction Code
Currently, features are extracted from image dataset using MATLAB code from https://github.com/bcsiriuschen/CARC
At the moment, features must be extracted and saved separately before applying classifiers. In progress: converting MATLAB code to python OR findng a way to run MATLAB code within python code and save features dynamically.

### 2. Basic Dataset
The dataset that we are currently using shows little to no variation in pose or illumination. Classifier results will be closer to real-world results on across-age dataset with more variation

## next steps:
### 1. New dataset
Currently we are gathering more varied cross-age dataset to test our classifier on

### 2. Finer feature extraction
Using architecture similar to that of Facebook's DeepFace network, we can improve accuracy by extracting finer features from given image. These features, in conjunction with CARC (Cross-Age Reference Coding) features, might result in a hihgly accurate cross-age recognition/verification system.
