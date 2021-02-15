from mlproject.distance import haversine

def test_distance_two_point():
    assert type(haversine(2.380009, 48.865070, 2.3514616, 48.8566969)) == float
