def equilateral(sides):
    return len(set(sides)) == 1 and sum(sides) > 0


def isosceles(sides):
    sides.sort()
    return len(set(sides)) <= 2 and sum(sides[:-1]) > sides[-1] and sum(sides) > 0



def scalene(sides):
    sides.sort()
    return len(set(sides)) == 3 and sum(sides[:-1]) > sides[-1] and sum(sides) > 0