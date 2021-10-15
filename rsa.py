import argparse
from Crypto.Util.number import long_to_bytes

parser = argparse.ArgumentParser(description='Max49\'s custom rsactftool lmao.')
parser.add_argument('-p', action='store', type=int)
parser.add_argument('-q', action='store', type=int)
parser.add_argument('-n', action='store', type=int)
parser.add_argument('-e', action='store', type=int)
parser.add_argument('-d', action='store', type=int)
parser.add_argument('-ct', action='store', type=int)
parser.add_argument('-phi', action='store', type=int)
args = parser.parse_args()
p = args.p if args.p else 0
q = args.q if args.q else 0
n = args.n if args.n else 0
e = args.e if args.e else 0
d = args.d if args.d else 0
ct = args.ct if args.ct else 0
phi = args.phi if args.phi else 0

if p == 0 or q == 0 or ct == 0 or e == 0:
    raise AssertionError('Missing important values!')

if n == 0:
    n = p*q

if p == q and phi == 0:
    phi = p*(p - 1)
elif phi == 0:
    phi = (p-1)*(q-1)

if d == 0:
    d = pow(e, -1, phi)

m = pow(ct, d, n)

print("----------------")
print(f"Unciphered text: {long_to_bytes(m).decode()}")