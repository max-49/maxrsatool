import argparse
from math import gcd
from Crypto.Util.number import long_to_bytes, isPrime

parser = argparse.ArgumentParser(description='Max49\'s custom rsa tool lol.')
parser.add_argument('-p', help='a prime p value', action='store', type=int, required=True)
parser.add_argument('-q', help='a prime q value', action='store', type=int, required=True)
parser.add_argument('-n', help='a product of p and q', action='store', type=int)
parser.add_argument('-e', help='the public exponent', action='store', type=int)
parser.add_argument('-d', help='the private key', action='store', type=int)
parser.add_argument('-ct', help='the ciphertext', action='store', type=int, required=True)
parser.add_argument('-phi', help='the euler function of n', action='store', type=int)
parser.add_argument('--all', help='print integer, bytes, and attempted decoding of the answer', action="store_true")
args = parser.parse_args()

p = args.p
q = args.q
n = args.n
e = args.e or 65537
d = args.d
ct = args.ct
phi = args.phi

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
if args.all:
    print(f"Unciphered bytes: {long_to_bytes(m)}")
    print(f"Unciphered integer: {m}")
    print(f"Unciphered hex: {hex(m)}")
