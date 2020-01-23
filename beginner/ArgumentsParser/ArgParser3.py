import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="enter number to find square", type=int)
parser.add_argument("-v", "--verbose", help="enable verbosity", action="store_true")

args = parser.parse_args()

if args.verbose:
    print("The square of {} is equal to {}".format(args.square, args.square ** 2))
else:
    print(args.square ** 2)

