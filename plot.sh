#!/bin/bash

FILES=./data/pose/*
for f in $FILES
do
  python3 plotPose.py $f ./data/pose_dataset.json || echo "no labels"
done
