from polygons.point import Point
from polygons.polygon import Polygon


def main() -> None:
    square = Polygon()
    square.add_point(Point(1, 1))
    square.add_point(Point(1, 2))
    square.add_point(Point(2, 2))
    square.add_point(Point(2, 1))
    print(square.perimeter())


if __name__ == '__main__':
    main()
