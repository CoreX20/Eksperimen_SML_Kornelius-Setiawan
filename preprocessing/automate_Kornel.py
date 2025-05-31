import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder


def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop NA
    df = df.dropna()

    # Drop duplicate values
    df = df.drop_duplicates()

    # Label Encoder
    encoder = LabelEncoder()
    df["Extracurricular Activities"] = encoder.fit_transform(
        df["Extracurricular Activities"]
    )

    # Simpan hasil
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
