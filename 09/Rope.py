from Knot import Knot 
class Rope:
    def __init__(self, length: int) -> None:
        self.segments = [Knot() for k in range(length)]
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def __repr__(self) -> str:
        return str(self.segments)

    def move_head(self, x: int, y: int) -> None:
        self.step(self.head, x, y)
        for s in range(1, len(self.segments)):
            self.follow(self.segments[s-1], self.segments[s])

    def step(self, knot: Knot, x: int, y: int) -> None:
        knot.x += x
        knot.y += y

    def knots_touching(self, x: int, y: int) -> bool:
        return abs(x) <= 1 and abs(y) <= 1

    def follow(self, lead: Knot, knot: Knot) -> None:
        diff_x = lead.x - knot.x
        diff_y = lead.y - knot.y
        if self.knots_touching(diff_x, diff_y):
            pass 
        elif diff_x == 0: 
            self.step(knot, 0, diff_y // abs(diff_y))
        elif diff_y == 0: 
            self.step(knot, diff_x // abs(diff_x), 0)
        else: 
            self.step(knot, diff_x // abs(diff_x), diff_y // abs(diff_y))