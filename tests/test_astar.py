from src.routing.heuristics import haversine_distance


def test_haversine_non_negative():
    d = haversine_distance(42.3601, -71.0589, 42.3610, -71.0570)
    assert d >= 0
