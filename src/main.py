
# -*- coding: utf-8 -*-
"""
Main file with the whole process.
"""
import os
import pandas as pd
import numpy as np

from submit import make_submission

FILE_PATH = os.path.realpath(__file__)
DIR, FILE_NAME = os.path.split(FILE_PATH)

IN_FOLDER = os.path.join(os.path.dirname(DIR), "in")

# Input data paths
BREED_LABELS = os.path.join(IN_FOLDER, "breed_labels.csv")
COLOR_LABELS = os.path.join(IN_FOLDER, "color_labels.csv")
STATE_LABELS = os.path.join(IN_FOLDER, "state_labels.csv")

if __name__ == "__main__":
    breed_labels = pd.read_csv(BREED_LABELS)
    color_labels = pd.read_csv(COLOR_LABELS)
    state_labels = pd.read_csv(STATE_LABELS)

    make_submission()
