from colorama import init, Fore #pip._vendor.colorama ?



def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)    