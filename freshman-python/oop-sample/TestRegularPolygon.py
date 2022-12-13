from RegularPolygon import RegularPolygon

class TestRegularPolygon:
    """unit testing the class RegularPolygon.py"""
    def __init__(self, *args, **kwargs):
        polygon = RegularPolygon(*args, **kwargs)
        polygon.print_result()

# printing all 
if __name__ == "__main__":
    TestRegularPolygon()
    TestRegularPolygon(6,4)
    TestRegularPolygon(10, 4, 5.6, 7.8)