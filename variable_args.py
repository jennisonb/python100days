def sum_numbers(*nums) -> float:
    """Sums numbers passed int function.
    - nums is a parameter that accepts a variable number of arguments (numbers).

    Returns:
        int: _description_
    """
    result: float = 0.0
    # print(nums[0])
    for i in range(len(nums)):
        result += nums[i]
    return result

