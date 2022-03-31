class Colors:
    BLACK  = "\033[22;30;49m"
    RED    = "\033[22;31;49m"
    GREEN  = "\033[22;32;49m"
    YELLOW = "\033[22;33;49m"
    BLUE   = "\033[22;34;49m"
    PURPLE = "\033[22;35;49m"
    CYAN   = "\033[22;36;49m"
    WHITE  = "\033[22;37;49m"
    RESET  = "\033[00m"

    def printColoredText(color):
        print(f"{color}This is some coloured text{Colors.RESET}")

    def __init__(self):
        self.printColoredText(Colors.BLACK)
        self.printColoredText(Colors.RED)
        self.printColoredText(Colors.GREEN)
        self.printColoredText(Colors.YELLOW)
        self.printColoredText(Colors.BLUE)
        self.printColoredText(Colors.PURPLE)
        self.printColoredText(Colors.CYAN)
        self.printColoredText(Colors.WHITE)