import numpy as np
import pandas as pd


def engineer_features(df):
    df = df.copy()

    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["is_weekend"] = (df["weekday"] >= 5).astype(int)

    road_dummies = pd.get_dummies(df["road_type"], prefix="road")
    df = pd.concat([df, road_dummies], axis=1)

    return df


def main():
    sample = pd.DataFrame({
        "hour": [8, 14, 18],
        "weekday": [1, 5, 6],
        "is_rain": [0, 1, 0],
        "is_snow": [0, 0, 1],
        "road_type": ["primary", "residential", "motorway"],
        "segment_length_m": [500, 800, 1200]
    })

    features = engineer_features(sample)
    print(features)


if __name__ == "__main__":
    main()
