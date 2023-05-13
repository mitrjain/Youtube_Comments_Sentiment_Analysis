# Python application to perform to Sentiment Analysis on YouTube Comments Dataset

## Overall prerequisites

### Python packages
- python-dotenv
- clean-text
- langdetect
- textblob
- google-api-python-client

## Overall code organization/ directory structure
- `getVideoIds.py` : python script to fetch ids of youtube videos 
- `videoIds` : directory containing .txt files which store the fetched vidoe ids asa result of executing `getVideoIds.py`
- `getComments.py` : python script which reads video ids from the `videoIds` directory and fetches comments for each video
- `cleanText.py` : python script which takes the raw comments and performs data cleaning
- `generateDataset.py` : pyhton script which takes the clean comments file and produces a dataset ready for Sentiment Analysis tasks
- `commentsDatasetLarge.csv` : A csv file, which is the result of the output of the execution of `generateDataset.py`
- `gatherData.sh` : Shell script that automates the process of collecting data, cleaning the data and creating a dataset out of it
- `processed_dataset.pkl` : Cleaned and preprocessed dataset
- `best_models` : directory containing saved LSTM and CNN models
- `Lstm.ipynb` : Fully executed notebook for LSTM models
- `CNN.ipynb` : Fully executed notebook for CNN models

## Flow of operations
The below diagram aims to explain the sequence of operations that take place when this application is run to perform Sentiment Analysis

![CS271_ Flow of operations](https://github.com/mitrjain/Youtube_Comments_Sentiment_Analysis/assets/26086412/2e761eaa-9512-409d-a535-fa29a131cde4)

## Running the application
Steps to run this application
- Make sure you have the required python packages mentioned in above sections
- Set up envornment varaibles file `.env` in the root (current) directory
```
API_KEY=""
```
- Phase 1: Execute the following command to get yotube comments, preprocess it and generate a dataset out of it: 

`gatherData.sh`

- Phase 2: Execute the Lstm.ipynb notebook
- Phase 3: Execute the CNN.ipynb notebook

## Environment specifications

### Phase 1
Following are the specifications of the environment on which this part of application was executed/tested:
- MacBook Air M1
- OS: Montery
- Memory: 16 GB
- Python version: 3.9.13

### Phase 2
Following are the specifications of the environment on which this part of application was executed/tested:
- Google Colab Notebook
- Connected to a custom GCP VM:
- - System RAM: 102.2 GB
- - Disk: 186.0 GB
