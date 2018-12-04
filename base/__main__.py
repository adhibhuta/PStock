#Author: lladhibhutall 


import sys
import argparse

from .classmodule import MyClass
from .funcmodule import my_function

def main():
    print('in main')

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='google',
		        help='Name of the stock for price') #P change this to something meaningful   
    args =  parser.parse_args()
    print('Parser added')

    #my_function('hello world')

    #my_object = MyClass('Debjyoti')
    #my_object.say_name()

if __name__ == '__main__':
    main()

