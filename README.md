# Fast Encode - Encoding Made Easy

With Fast Encode you can create **a single object** that automatically uses many encoding types.

## Overview

The Fast Encode module provides the following features:

- A single object that abstracts the following encodings: hex, ascii array, string, bytes, binary and long number.
- Many helper functions that makes changing encoding easier.

## Getting Started

- [ ] First, you need to download it from pip. `pip install fastencode`

- [ ] Then import it to your project.

```python
from fastencode import DataObj as D
```

## Creating and Using an Object

For each encoding type, there is factory function that creates a DataObj object from it.
The factory functions are: `fromHex`, `fromAsc`, `fromStr`, `fromBin`, `fromNum` and `fromBytes`.

```python
plaintext = D.fromStr('secret_msg') # This creates a Data object from a plain string
key = D.fromHex('deadbeef1234')# This creates a Data object from hex
```

Printing the DataObj will show a lot of different encoding at once:

```python
print(f'Output - {plaintext}')

Output - Hex: 7365637265745f6d7367, Ascii: [115, 101, 99, 114, 101, 116, 95, 109, 115, 103],
  String: secret_msg, Number: 544942432582961455788903
  Binary: 01110011011001010110001101110010011001010111010001011111011011010111001101100111
```

We can get to a specific encoding by using the DataObj fields: `hex`, `asc`, `str`, `bytes`, `bin` and `num`.

```python
print(key.bytes)
# prints b'\xde\xad\xbe\xef\x124'

print(key.asc) # asc is shorthand for ascii, and is a list of integer of the indvidual ascii value of every byte.
# prints [222, 173, 190, 239, 18, 52]
```

## Simple XOR exmaple

Let's take a look at a simple example of XOR-ing 2 strings. We will see how simple it is to do with fastencode.

```python
from fastencode import DataObj as D

plaintext = D.fromStr('secret_msg')
key = D.fromStr('secret_key')

xored_integer_value = plaintext.num ^ key.num # ^ is the python operand for xor
print(xored_integer_value) # prints 398878

ciphertext = D.fromNum(xored_integer_value) # Creating another Data object from the result of the xor
print(ciphertext) # prints Hex: 6161e, ascii: [97, 97, 14], String: aa, Number: 398878 Binary: 011000010110000100001110
```

_Note: In the example the result is only 3-bytes long - as expected - because the first 7 bytes match and are therefore removed._

## Forking and Contribution Ideas

- Creating a genreal function that automatically detects the type of the encoding.
- Adding base64 and base32 encodings.
