def pythagorean_triplet():
    """
    Calculate the Pythagorean Triplet.
    :return: [int] Product of the Pythagorean Triplet.
    """
    for c in range(3, 1000):
        for b in range(2, c-1):
            for a in range(1, b-1):
                if (a + b + c) == 1000 and ((a**2) + (b**2)) == (c**2):
                    return (a * b * c)
    return None