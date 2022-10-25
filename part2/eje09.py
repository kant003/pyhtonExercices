# -*- coding: utf-8 -*-
import math





def test():
    assert math.isclose(get_distance(0,0, 1,1), 1.414213562), "Should be 1.414"
    assert math.isclose(get_distance(7,4, 2,3), 5.099019513), "Should be 5.0990"
    assert math.isclose(get_distance(0,0, 0,0), 0), "Should be 0"



if __name__ == "__main__":
    test()
    print("Everything passed")