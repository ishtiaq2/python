import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num1', help='enter num1', type=int)
parser.add_argument('num2', help='enter num2', type=int)
args = parser.parse_args()

sum = args.num1 + args.num2
print(sum)
