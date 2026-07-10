class CountSquares:

    def __init__(self):
        # Maps (x, y) tuple to its frequency count
        self.point_counts = defaultdict(int)
        # Keeps track of all unique points to iterate through during a query
        self.unique_points = set()

    def add(self, point: List[int]) -> None:
        pt = (point[0], point[1])
        self.point_counts[pt] += 1
        self.unique_points.add(pt)

    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]
        total_squares = 0
        
        # Treat the query point as P1. We look for a diagonal partner P3.
        for x3, y3 in self.unique_points:
            # Condition 1: They cannot be on the same horizontal or vertical line
            if x1 == x3 or y1 == y3:
                continue
                
            # Condition 2: The side lengths must be equal (it must be a square)
            if abs(x1 - x3) != abs(y1 - y3):
                continue
                
            p2 = (x1, y3)
            p4 = (x3, y1)
            p3 = (x3, y3)
            
            # Check if P2 and P4 exist in our data structure
            if p2 in self.point_counts and p4 in self.point_counts:
                # Multiply frequencies to account for duplicate points
                total_squares += self.point_counts[p3] * self.point_counts[p2] * self.point_counts[p4]
                
        return total_squares
