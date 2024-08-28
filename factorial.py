def factorial(n: int) -> int:
    """Returns factorial of given integer

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    result: int = 1
    if not isinstance(n, int):
        print(f"{n} is not an integer.")
        return None
    else:
        # cur_val: int = 1
        for i in range(0, n + 1):
            result *= i
            if result == 0:
                result = 1
    return result


for x in range(0,36):
    print(f"{x}: {factorial(x)}")