
# -*- coding: utf-8 -*-
"""
Code to create the submission csv file.
"""
import os
import pandas as pd
import numpy as np

FILE_PATH = os.path.realpath(__file__)
DIR, FILE_NAME = os.path.split(FILE_PATH)

OUT_FOLDER = os.path.join(os.path.dirname(DIR), "out")


def create_out_folder():
    try:
        os.makedirs(OUT_FOLDER)
    except OSError:
        if not os.path.isdir(OUT_FOLDER):
            raise


def make_submission():
    print("😗  - Submission initiated...")
    try:
        create_out_folder()
        # Perform the steps to create the submission.csv file

        # results = get_results()
        SAMPLE_SUBMISSION = os.path.join(OUT_FOLDER, "sample_submission.csv")
        sample_submission = pd.read_csv(SAMPLE_SUBMISSION)
        simple_submission = sample_submission.head()

        SIMPLE_SUBMISSION = os.path.join(OUT_FOLDER, "simple_submission.csv")
        simple_submission.to_csv(SIMPLE_SUBMISSION, index=False)

        print("🍾  - Submission successfully created.")
    except Exception:
        print("💩  - Submission failed.")
