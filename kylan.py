#define some stuff

from math import sqrt

i = 1000

def something(a):
    return a+1

# python files can define whatever functions/etc they want to up here.
# everything we want executed by the command line goes inside an if statement:
# if __name__ == '__main__':, kind of like public static void main(), etc.

if __name__ == '__main__':
    print("Program prints a single statement")
    print(str(something(sqrt(i))))
    print("Cool, int to float automatic conversion")
    print("Bye")
