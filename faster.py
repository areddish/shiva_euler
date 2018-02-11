def pythagorean_triplet():
    """
    Calculate the Pythagorean Triplet.
    :return: [int] Product of the Pythagorean Triplet.
    """
    triplet_list = []

    for c in range(3, 1000):
        for b in range(2, c-1):
            for a in range(1, b-1):
                if (a + b + c) == 1000 and ((a**2) + (b**2)) == (c**2) and a < b < c:
                    return (a * b * c)
    return None