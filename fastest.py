def pythagorean_triplet():
    """
    Calculate the Pythagorean Triplet.
    :return: [int] Product of the Pythagorean Triplet.
    """
    for c in range(3, 1000):
        c_sq = c**2
        for b in range(2, c-1):
            a = 1000 - b -c
            if ((a**2) + (b**2)) == c_sq:
                return (a * b * c)
    return None