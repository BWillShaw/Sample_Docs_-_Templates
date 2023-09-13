# ANSI escape codes for foreground colors
foreground_colors = {
    "Black": "\033[30m",
    "Red": "\033[31m",
    "Green": "\033[32m",
    "Yellow": "\033[33m",
    "Blue": "\033[34m",
    "Magenta": "\033[35m",
    "Cyan": "\033[36m",
    "White": "\033[37m",
    "Reset": "\033[39m"
}

# ANSI escape codes for background colors
background_colors = {
    "Black": "\033[40m",
    "Red": "\033[41m",
    "Green": "\033[42m",
    "Yellow": "\033[43m",
    "Blue": "\033[44m",
    "Magenta": "\033[45m",
    "Cyan": "\033[46m",
    "White": "\033[47m",
    "Reset": "\033[49m"
}

# Demonstrate foreground colors
print("Foreground Colors:")
for color, code in foreground_colors.items():
    print(f"{code}{color}\033[0m")

# Demonstrate background colors
print("\nBackground Colors:")
for color, code in background_colors.items():
    print(f"{code}  \033[0m {color}")

# Reset all styling at the end
print("\033[0m")
