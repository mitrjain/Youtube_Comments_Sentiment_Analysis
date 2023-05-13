#!/bin/sh

echo "Collecting video Ids"
echo "Executing command: python getVideoIds.py"
python getVideoIds.py

echo "Extracting raw comments"
echo "Executing command: python getVideoIds.py"
python getComments.py

echo "Cleaning raw comments"
echo "Executing command: python cleanText.py"
python cleanText.py

echo "Generating dataset"
echo "Executing command: python generateDataset.py"
python generateDataset.py






