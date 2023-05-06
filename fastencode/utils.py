from typing import List
from base64 import b64encode, b64decode

# Helper Functions
def strtoasc(x: str) -> List[int]:
    return [ord(char) for char in x]


def asctohex(x: List[int]) -> str:
    xhex = ""
    for num in x:
        xnum = hex(num)
        if len(xnum) == 3:
            xhex += "0" + xnum[2:]
        else:
            xhex += xnum[2:]
    return xhex


def hextoasc(x: str) -> List[int]:
    numbers = []
    i = 0
    while i < len(x):
        numbers.append(int(x[i : i + 2], 16))
        i += 2
    return numbers


def asctostr(x: List[int]) -> str:
    text = ""
    for num in x:
        if x == 0:
            text += "0"
            continue
        text += chr(num)
    return text


def asctobin(x: List[int]) -> str:
    result = ""
    for num in x:
        bin_rep = bin(num)[2:]
        while len(bin_rep) < 8:
            bin_rep = "0" + bin_rep
        result += bin_rep
    return result


def bintoasc(x: str) -> List[int]:
    result = []
    while x:
        result.append(int(x[:8], 2))
        x = x[8:]
    return result


class DataObj:
    hex: str = ""
    asc: List[int] = []
    str: str = ""
    bytes: bytes = b""
    bin: str = ""
    num: int = 0
    b64: bytes = ""

    def fromHex(x: str):
        d0 = DataObj()
        d0.hex = x
        d0.asc = hextoasc(x)
        d0.str = asctostr(hextoasc(x))
        d0.bin = asctobin(d0.asc)
        d0.bytes = bytes.fromhex(x)
        d0.num = int(d0.hex, 16)
        d0.b64 = b64encode(d0.bytes)
        return d0

    def fromAsc(x: List[int]):
        d0 = DataObj()
        d0.hex = asctohex(x)
        d0.asc = x
        d0.str = asctostr(x)
        d0.bin = asctobin(d0.asc)
        d0.bytes = bytes.fromhex(d0.hex)
        d0.num = int(d0.hex, 16)
        d0.b64 = b64encode(d0.bytes)
        return d0

    def fromStr(x: str):
        d0 = DataObj()
        d0.hex = asctohex(strtoasc(x))
        d0.asc = strtoasc(x)
        d0.str = x
        d0.bin = asctobin(d0.asc)
        d0.bytes = bytes.fromhex(d0.hex)
        d0.num = int(d0.hex, 16)
        d0.b64 = b64encode(d0.bytes)
        return d0

    def fromBin(x: str):
        d0 = DataObj()
        d0.hex = asctohex(bintoasc(x))
        d0.asc = bintoasc(x)
        d0.str = asctostr(bintoasc(x))
        d0.bin = x
        d0.bytes = bytes.fromhex(d0.hex)
        d0.num = int(d0.hex, 16)
        d0.b64 = b64encode(d0.bytes)
        return d0

    def fromNum(x: int):
        d0 = DataObj()
        d0.hex = hex(x)[2:]
        d0.asc = hextoasc(d0.hex)
        d0.str = asctostr(d0.asc)
        d0.bin = asctobin(d0.asc)
        d0.bytes = bytes.fromhex(d0.hex)
        d0.num = x
        d0.b64 = b64encode(d0.bytes)
        return d0

    def fromBytes(x: bytes):
        d0 = DataObj()
        d0.bytes = x
        d0.hex = x.hex()
        d0.asc = hextoasc(d0.hex)
        d0.bin = asctobin(d0.asc)
        d0.num = int(d0.hex, 16)
        d0.str = asctostr(d0.asc)
        d0.b64 = b64encode(d0.bytes)
        return d0
    
    def fromB64(x: bytes):
        return DataObj.fromBytes(b64decode(x))


    def __str__(self):
        return f"Hex: {self.hex}, ascii: {self.asc}, String: {self.str}, Number: {self.num} Binary: {self.bin} Base64: {self.b64}"

if __name__ == '__main__':
    print('You should import this file and run it directly.')