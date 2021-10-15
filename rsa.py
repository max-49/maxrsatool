import argparse
from math import gcd
from Crypto.Util.number import long_to_bytes, isPrime

parser = argparse.ArgumentParser(description='Max49\'s custom rsa tool lol.')
parser.add_argument('-p', action='store', type=int)
parser.add_argument('-q', action='store', type=int)
parser.add_argument('-n', action='store', type=int)
parser.add_argument('-e', action='store', type=int)
parser.add_argument('-d', action='store', type=int)
parser.add_argument('-ct', action='store', type=int)
parser.add_argument('-phi', action='store', type=int)
args = parser.parse_args()

p = args.p
q = args.q
n = args.n
e = args.e or 65537
d = args.d
ct = args.ct
phi = args.phi

if not p or not q or not ct:
    raise AssertionError('Missing important values!')

if not isPrime(p) or not isPrime(q):
    raise ValueError('p and q must both be prime!')

if not n:
    n = p*q

if p == q and not phi:
    phi = p*(p-1)
elif not phi:
    phi = (p-1)*(q-1)

if not gcd(e, phi) == 1:
    raise ValueError('φ(n) and e must be coprime!')

if not d:
    d = pow(e, -1, phi)

m = pow(ct, d, n)

print("----------------")
print(f"Unciphered text: {long_to_bytes(m).decode()}")