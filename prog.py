import argparse

parser = argparse.ArgumentParser(description="Echo the input")
parser.add_argument("x", type=int, help="The base")
parser.add_argument("y", type=int, help="The exponent")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="count", default=0)

args = parser.parse_args()
answer = args.x ** args.y

if args.verbose >= 2:
    print(f"The power of {args.x} to the {args.y} is {answer}")
elif args.verbose == 1:
    print(f"{args.x}^{args.y} = {answer}")
else:
    print(f"{args.verbose=}")
    print(answer)