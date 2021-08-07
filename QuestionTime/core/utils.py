import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    """
    Generate a random string starting from a set of chars and of fixed length.
    """
    return "".join(random.choice(chars) for _ in range(length))
