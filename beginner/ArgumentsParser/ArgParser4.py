import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number1", help="enter num1", type=int)
parser.add_argument("-m", "--number2", help="enter num2", type=int)
parser.add_argument("-v", "--verbosity", help="verbose choices: 0 = addition, 1 = subtraction, 2 = multi",
                    type=int, choices=[0, 1, 2])
args = parser.parse_args()

if args.verbosity == 0:
    print("Adding {} and {} = {}".format(args.number1, args.number2, args.number1 + args.number2))
elif args.verbosity == 1:
    print("Subtracting {} from {} = {}".format(args.number2, args.number1, args.number1 - args.number2))
else:
    print("Multiplying {} and {} = {}".format(args.number1, args.number2, args.number1 * args.number2))
