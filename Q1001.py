def abs_diff_between_sum_and_sum_of_squares(a: int, b: int) -> int:
    """
    Given two integers, find the absolute difference between:
    their sum and the sum of their squares.

    Example:
        a, b = 2, 3
        sum is 5
        sum of squares is 13
        absolute difference is 8

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: Absolute difference between the sum and the sum of squares.
    """


    sumOftwointegers = (a+b)
    sumOfTheirSquares = ((a**2) + (b**2))

    absolutedifference = abs (sumOftwointegers - sumOfTheirSquares)

    return absolutedifference

a = abs_diff_between_sum_and_sum_of_squares(2,3)
print (a)