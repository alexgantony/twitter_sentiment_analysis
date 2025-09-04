import random
from pathlib import Path

import numpy as np

# Data paths,
ROOT = Path.cwd().parent
DATA_DIR = ROOT / "data" / "raw"
TRAIN_FILE = DATA_DIR / "twitter_training.csv"
VAL_FILE = DATA_DIR / "twitter_validation.csv"

SAMPLE_DIR = ROOT / "data" / "sample"
SAMPLE_FILE = SAMPLE_DIR / "sample_500.csv"

# Randomness
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
