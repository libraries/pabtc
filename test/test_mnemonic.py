import pytest
import pabtc
import random


def test_mnemonic():
    data = bytearray.fromhex('00000000000000000000000000000000')
    mnem = 'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f')
    mnem = 'legal winner thank year wave sausage worth useful legal winner thank yellow'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('80808080808080808080808080808080')
    mnem = 'letter advice cage absurd amount doctor acoustic avoid letter advice cage above'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('ffffffffffffffffffffffffffffffff')
    mnem = 'zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('9e885d952ad362caeb4efe34a8e91bd2')
    mnem = 'ozone drill grab fiber curtain grace pudding thank cruise elder eight picnic'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('c0ba5a8e914111210f2bd131f3d5e08d')
    mnem = 'scheme spot photo card baby mountain device kick cradle pact join borrow'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('23db8160a31d3e0dca3688ed941adbf3')
    mnem = 'cat swing flag economy stadium alone churn speed unique patch report train'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data

    data = bytearray.fromhex('f30f8c1da665478f49b001d94c5fc452')
    mnem = 'vessel ladder alter error federal sibling chat ability sun glass valve picture'.split()
    mnem = [str(x) for x in mnem]
    assert pabtc.mnemonic.encode(data) == mnem
    assert pabtc.mnemonic.decode(mnem) == data


def test_mnemonic_decode_checksum_error():
    mnem = 'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about'.split()
    mnem[-1] = 'abandon'
    mnem = [str(x) for x in mnem]
    with pytest.raises(AssertionError):
        pabtc.mnemonic.decode(mnem)


def test_mnemonic_random():
    for _ in range(32):
        data = bytearray(random.randbytes(random.choice([16, 20, 24, 28, 32])))
        mnem = pabtc.mnemonic.encode(data)
        assert pabtc.mnemonic.decode(mnem) == data
