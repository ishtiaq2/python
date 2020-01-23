#!/usr/bin/env python
import argparse
import sys

print("0. func print_result")


def print_result(sm, num1, num2):
    print("4. sum of {} and {} = {}".format(num1, num2, sm))
    print("5. finished with print_result")


print("1. func main")


def main():
    print("3. inside main")
    parser = argparse.ArgumentParser(description="add two digits of int type")
    parser.add_argument("-n", "--num1", help="enter num1", type=int)
    parser.add_argument("-m", "--num2", help="enter num2", type=int)
    parser.add_argument("-v", "--verbose", help="verbose mod", action="store_true")

    args = parser.parse_args()

    sm = args.num1 + args.num2

    print_result(sm, args.num1, args.num2)

    if args.verbose:
        print("6. finished with main in verbose")
    else:
        print("6. finished with main")


if __name__ == "__main__":
    print("2. inside name = main")
    sys.exit(main())
