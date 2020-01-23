import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="pass int arg to calculate square root", type=int)
args = parser.parse_args()
square = args.square ** 2
print(square)
