import os

### NOTE: ############################################
# If python -V >= 3.9 then you will get:
# ERROR: Could not find a version that satisfies the requirement pickle (from versions: none)
# ERROR: No matching distribution found for pickle
#
# This is because it is included in Python 3.9 distrubution
# Uncomment line 11 after first run.
######################################################

# os.system('cmd /k "pip install -r requirements.txt"')

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Graphing packages
import altair as alt
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# stuff for machine
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# --- SETUP --- #

## Containers


## Functions(*skip*)

## Customize(*skip*)


# --- BODY --- #

## Header


## Dataset


## Exploration


## Model Making

### inputs

### machine

### display


## Model Import

### inputs

### predictions
