def encode_bit(bit):
    yield True ^ bit
    yield False ^ bit


def decode_bit(previous, current):
    if previous ^ current:
        yield current


def encode(signal):
    for bit in signal:
        for encoded in encode_bit(bit):
            yield encoded


def decode(signal):
    previous = None
    for current in signal:
        if previous is None:
            previous = current
        else:
            for decoded in decode_bit(previous, current):
                yield decoded
                previous = None


original_data = "0101010101"

encoded = encode(map(int, original_data))
decoded = decode(encoded)

decoded_data = "".join(map(str, list(decoded)))

print("Original data: {0}".format(original_data))
print("Encoded data: {0}".format(decoded_data))
