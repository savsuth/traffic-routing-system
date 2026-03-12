from src.data_collection.traffic_simulator import simulate_traffic


def test_simulator_output_columns():
    df = simulate_traffic(10)
    expected = {
        "hour",
        "weekday",
        "is_rain",
        "is_snow",
        "road_type",
        "segment_length_m",
        "effective_speed_mph",
        "travel_time_minutes",
    }
    assert expected.issubset(df.columns)
    assert len(df) == 10
