from typing import List

from polygons.point import Point


class Polygon:
    def __init__(self) -> None:
        self.vertices: List = []

    def add_point(self, point: Point) -> None:
        self.vertices.append(point)

    def perimeter(self) -> float:
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


class PolygonFromListOfPoints(Polygon):
    def __init__(self, points: List[Point] = None) -> None:
        super().__init__()
        points = points if points else []
        self.vertices = []

        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)
