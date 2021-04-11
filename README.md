
# MIPS-Reverse

MIPS-Reverse is a tool that can generate shellcodes for the  [MIPS](https://en.wikipedia.org/wiki/MIPS_architecture) architecture that launches a **reverse shell** where you can specify the ***IP adress***, the ***port*** and the ***desired shell*** (*/bin/sh*, */bin/bash*, */bin/dash*).

## How to install
```
# 1. Install pwntools
$ pip3 install pwntools

# 2. Install the binutils for the MIPS architecture
$ apt-get install software-properties-common
$ apt-add-repository ppa:pwntools/binutils
$ apt-get update
$ apt-get install binutils-mips-linux-gnu
```

## How to use
```console
$ python3main.py [-h] -i IP -p PORT -s {bash,sh,dash} -f {asm,hex}
```

|Flag                 |Description                     |
|---------------------|--------------------------------|
|``-i``/``--ip``      |IP Adress for the reverse shell 
|``-p``/``--port``    |Port for the reverse shell  
|``-s``/``--shell``   |``sh``, ``bash`` or ``dash``    
|``-f``/``--format``  |Format of the output, it can be either ``hex`` if you want the hex-encoded version of the shellcode, or ``asm`` if you want the MIPS ASM version

### Exemple 

```
python3 main.py -i 127.0.0.1 -p 1337 -s sh -f hex
```
will output you a lovely 180 bytes reverse shell shellcode for 127.0.0.1:1337

For any question or remark, please contact me at [@Rog3rSm1th](https://twitter.com/Rog3rSm1th) on Twitter or by mail at r0g3r5@protonmail.com
