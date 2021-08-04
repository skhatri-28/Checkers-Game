from sketch import Sketch


def test_get_coordinate():
    sketch = Sketch()
    assert(sketch.get_coordinate(0) == -200)
    assert(sketch.get_coordinate(1) == -150)
    assert(sketch.get_coordinate(4) == 0)
    assert(sketch.get_coordinate(7) == 150)
