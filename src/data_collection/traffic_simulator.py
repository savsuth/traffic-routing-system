import pandas as pd
import numpy as np


def simulate_traffic(num_rows=1000, random_state=42):
    rng = np.random.default_rng(random_state)

    hours = rng.integers(0, 24, size=num_rows)
    weekdays = rng.integers(0, 7, size=num_rows)
    is_rain = rng.integers(0, 2, size=num_rows)
    is_snow = rng.integers(0, 2, size=num_rows)
    road_type = rng.choice(["motorway", "primary", "secondary", "residential"], size=num_rows)
    segment_length = rng.uniform(50, 2000, size=num_rows)

    base_speed = []
    for r in road_type:
        if r == "motorway":
            base_speed.append(55)
        elif r == "primary":
            base_speed.append(40)
        elif r == "secondary":
            base_speed.append(30)
        else:
            base_speed.append(20)

    base_speed = np.array(base_speed, dtype=float)

    rush_hour_penalty = np.where(((hours >= 7) & (hours <= 9)) | ((hours >= 16) & (hours <= 18)), 0.65, 1.0)
    weather_penalty = np.where(is_rain == 1, 0.9, 1.0) * np.where(is_snow == 1, 0.75, 1.0)
    weekend_factor = np.where(weekdays >= 5, 1.05, 1.0)

    effective_speed = base_speed * rush_hour_penalty * weather_penalty * weekend_factor
    travel_time_minutes = (segment_length / 1609.34) / np.maximum(effective_speed, 5) * 60

    df = pd.DataFrame({
        "hour": hours,
        "weekday": weekdays,
        "is_rain": is_rain,
        "is_snow": is_snow,
        "road_type": road_type,
        "segment_length_m": segment_length,
        "effective_speed_mph": effective_speed,
        "travel_time_minutes": travel_time_minutes
    })

    return df


def main():
    df = simulate_traffic()
    print(df.head())
    print("\nGenerated rows:", len(df))


if __name__ == "__main__":
    main()
