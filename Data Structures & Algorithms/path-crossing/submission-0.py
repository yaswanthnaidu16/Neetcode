class Solution:
    def isPathCrossing(self, p: str) -> bool:
        x = 0
        y = 0
        vis = set()
        vis.add((x, y))
        for i in p:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            if (x, y) in vis:
                return True
            vis.add((x, y))
        return False