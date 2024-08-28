import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def banner_text(text: str = " ", screen_width: int = 80):
    """Center specified text based on given width.

    Args:
        text (str, optional): The text that should be centered. Defaults to " ".
        screen_width (int, optional): Max width of the text line used for centering. Defaults to 80.

    Raises:
        ValueError: If text lenght is more than the screen width.
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger than {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = f"**{centered_text}**"
        print(output_string)


def fibonacci(n: int):
    """Return the nth fibonacci number, for positive n.

    Args:
        n (number): _description_
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        # print(result)
        n_minus2 = n_minus1
        n_minus1 = result
    return result

def color_print(text: str, effect: str) -> None:
    """Prints text with specified effect

    Args:
        text (string): _description_
        effect (string): _description_
    """
    output_string = f"{effect}{text}{RESET}"
    print(output_string)

colorama.init()
color_print("Here is some text", RED)    
colorama.deinit()