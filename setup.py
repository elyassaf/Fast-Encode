from distutils.core import setup
setup(
  name = 'fastencode',         # How you named your package folder (MyLib)
  packages = ['fastencode'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An easy way to use different encoding: bytes, hex, ascii array, binary, long',   # Give a short description about your library
  long_description='''
# Fast Encode - Encoding Made Easy

With Fast Encode you can create **a single object** that automatically uses many encoding types.

## Overview

The Fast Encode module provides the following features:

-   A single object that abstracts the following encodings: hex, ascii array, string, bytes, binary and long number.
-   Many helper functions that makes changing encoding easier.

## Getting Started

-   [ ] First, you need to download it from pip. `pip install fastencode`

-   [ ] Then import it to your project.
``` python
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

  '''
  long_description_content_type='text/markdown'
  author = 'ES3',                   # Type in your name
  author_email = 'ourteamscare@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/elyassaf/Easy-Encoding/archive/refs/tags/v_1.0.tar.gz',    # I explain this later on
  keywords = ['encoding', 'hex', 'bytes', 'binary representation', 'decoding', 'ascii'],   # Keywords that define your package best
  install_requires=['typing'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)