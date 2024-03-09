def get_num_input(message: str) -> int:
    """Get number from user input.

    Args:
        message (string): Message to get number from user

    Returns:
        integer: number that was taken from user input
    """

    num = input(message)
    while num.isdigit() != True:
        num = input(message)
    
    return int(num)