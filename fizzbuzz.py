def fizz_buzz(n: int) -> str:
    """Game that returns fizz for numbers divisible by 3 
    or buzz for numbers divisible by 5.  If the number is divisible
    by both 3 and 5, return fizz buzz. Else return the number.

    Args:       
        n (int): number to check    

    Returns:
        str: fizz, buzz, fizz buzz, or the number
    """
    result: str = f"{n}"
    if not isinstance(n, int):
        print(f"{n} is not an integer.")
    else:
        if n % 3 == 0 and n % 5 == 0:
            result = "fizz buzz"
        elif n % 3 == 0:
            result = "fizz"
        elif n%5 == 0:
            result = "buzz"
    return result

for i in range(1, 101):
    print(f"{i}: {fizz_buzz(i)}")
