#!/usr/bin/env python3

import argparse
import sys


class ArgsClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))


class Temp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print('Temp Name: {}'.format(self.name))
        print('Temp Age: {}'.format(self.age))


def main():
    parser = argparse.ArgumentParser("Passing Args to Class")
    parser.add_argument('-n', '--name', help="enter name", type=str)
    parser.add_argument('-a', '--age', help="enter age", type=int)

    args = parser.parse_args()

    args_class = ArgsClass(args.name, args.age)
    temp = Temp('Muqadas', '2.5')
    args_class.show_data()
    temp.show_data()


if __name__ == "__main__":
    sys.exit(main())
