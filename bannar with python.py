import pyfiglet
from termcolor import colored
pre = colored(".....Present by *AS-ASA*.....","yellow")
bannar = input("Enter your name for coloring:")
print(pre)
bannar = colored(pyfiglet.figlet_format(bannar),"green")
print(bannar)
