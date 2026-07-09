import argparse
import pabtc

# Encode and decode mnemonic phrases. The data length needs to be between 16 and 32 bytes and divisible by 4.

parser = argparse.ArgumentParser()
parser.add_argument('--encode', action='store_true', help='Hex data to encode, e.g. 0xf30f8c1da665478f49b001d94c5fc452')
parser.add_argument('--decode', action='store_true', help='Mnemonic to decode, e.g. vessel ladder ...')
parser.add_argument('args', nargs='+')
args = parser.parse_args()

if args.encode:
    data = bytearray.fromhex(args.args[0][2:])
    mnem = pabtc.mnemonic.encode(data)
    print(' '.join(mnem))

if args.decode:
    data = pabtc.mnemonic.decode(args.args)
    print(f'0x{data.hex()}')
