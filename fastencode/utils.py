from typing import List

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


# Xor Function
def xor_ints(msg: List[int], key: List[int]) -> List[int]:
    return [a ^ b for a, b in zip(msg, key)]


# Xor possibilites
def xorposb(freqword: str, m1xm2: List[int], log=False) -> None:
    freqwordasc = strtoasc(freqword)
    for i in range(len(m1xm2) - len(freqwordasc) + 1):
        m3xfreqword = xor_ints(freqwordasc, m1xm2[i : len(freqwordasc) + i])
        if log:
            print(m3xfreqword)
        print("Xor Result: " + asctostr(m3xfreqword), end="")
        print(f"{str(i):>20}")


def only_chars(x: List[int]) -> bool:
    for char in x:
        if (char < 65 and char != 32) or (char > 90 and char < 97) or (char > 122):
            return False

    return True


# Clean Xor possibilites (Good for Crib-Dragging)
def clean_xorposb(freqword: str, m1xm2: List[int]) -> None:
    freqwordasc = strtoasc(freqword)
    for i in range(len(m1xm2) - len(freqwordasc) + 1):
        m3xfreqword = xor_ints(freqwordasc, m1xm2[i : len(freqwordasc) + i])

        if only_chars(m3xfreqword):
            print("Xor Result: " + asctostr(m3xfreqword), end="")
            print(f"{str(i):>20}")


class Data_Obj:
    hex: str = ""
    asc: List[int] = []
    dstr: str = ""
    dbytes: bytes = b""
    dbin: str = ""
    num: int = 0

    def fromHex(x: str):
        d0 = Data_Obj()
        d0.hex = x
        d0.asc = hextoasc(x)
        d0.dstr = asctostr(hextoasc(x))
        d0.dbin = asctobin(d0.asc)
        d0.dbytes = bytes.fromhex(x)
        d0.num = int(d0.hex, 16)
        return d0

    def fromAsc(x: List[int]):
        d0 = Data_Obj()
        d0.hex = asctohex(x)
        d0.asc = x
        d0.dstr = asctostr(x)
        d0.dbin = asctobin(d0.asc)
        d0.dbytes = d0.dstr.encode('ascii')
        d0.num = int(d0.hex, 16)
        return d0

    def fromStr(x: str):
        d0 = Data_Obj()
        d0.hex = asctohex(strtoasc(x))
        d0.asc = strtoasc(x)
        d0.dstr = x
        d0.dbin = asctobin(d0.asc)
        d0.dbytes = d0.dstr.encode('ascii')
        d0.num = int(d0.hex, 16)
        return d0

    def fromBin(x: str):
        d0 = Data_Obj()
        d0.hex = asctohex(bintoasc(x))
        d0.asc = bintoasc(x)
        d0.dstr = asctostr(bintoasc(x))
        d0.dbin = x
        d0.dbytes = d0.dstr.encode('ascii')
        d0.num = int(d0.hex, 16)
        return d0

    def fromNum(x: int):
        d0 = Data_Obj()
        d0.hex = hex(x)[2:]
        d0.asc = hextoasc(d0.hex)
        d0.dstr = asctostr(d0.asc)
        d0.dbin = asctobin(d0.asc)
        d0.dbytes = d0.dstr.encode('ascii')
        d0.num = x
        return d0

    def fromBytes(x: bytes):
        d0 = Data_Obj()
        d0.dbytes = x
        d0.dstr = x.decode('ascii')
        d0.asc = strtoasc(d0.dstr)
        d0.hex = asctohex(d0.asc)
        d0.dbin = asctobin(d0.asc)
        d0.num = int(d0.hex, 16)

    def __str__(self):
        return f"Hex: {self.hex}, Ascii: {self.asc}, String: {self.dstr}, Number: {self.num} Binary: {self.dbin}"

    def xor_data(d0, d1):
        return xor_ints(d0.asc, d1.asc)


if __name__ == '__main__':
    print('You should import this file and run it directly.')