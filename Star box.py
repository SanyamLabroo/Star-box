import os
from termcolor import colored
import time

a = input("Enter your name: ")
n = int(len(a))

warning = "Please enter a valid name next time!"

if n < 4:
    time.sleep(1)
    print()
    print(colored(warning, 'red', attrs=['bold']))
    exit()

if n > 15:
    time.sleep(1)
    print()
    print(colored(warning, 'red', attrs=['bold']))
    exit()

z = n + 4

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

time.sleep(2)
print(colored("*" * z, 'blue', attrs=['bold']))
print(colored("* "+ a + " *", 'green', attrs=['bold']))
print(colored("*" * z, 'blue', attrs=['bold']))
time.sleep(1)