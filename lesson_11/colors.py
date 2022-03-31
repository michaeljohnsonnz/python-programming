class Colors():
    BLACK  = '\033[22;30;47m'
    RED    = '\033[22;31;49m'
    GREEN  = '\033[22;32;49m'
    YELLOW = '\033[22;33;49m'
    BLUE   = '\033[22;34;49m'
    PURPLE = '\033[22;35;49m'
    CYAN   = '\033[22;36;49m'
    WHITE  = '\033[22;37;49m'
    RESET  = '\033[00m'

def printColoredText(color):
    print(f'{color}This is some coloured text{Colors.RESET}')

printColoredText(Colors.BLACK)
printColoredText(Colors.RED)
printColoredText(Colors.GREEN)
printColoredText(Colors.YELLOW)
printColoredText(Colors.BLUE)
printColoredText(Colors.PURPLE)
printColoredText(Colors.CYAN)
printColoredText(Colors.WHITE)
