# Computing 101
- All roads lead to the CPU then the logic gates
    - Programs/RAM/IO -> CPU -> Logic Gates

## Assembly
- Is assembled into binary code
- Is as close as one can get to speaking to the computer
- **Tells the CPU what to do**
    - In terms of English,
        - Sentence -> an "instruction" in assembly
        - Verb -> the action; "operation" in assembly
        - Noun -> the action reciever; "operand" in asssembly -> data: provided data, data in use (stored in registers), data stored
- The language is as simple as can be
- Assembly language depends on the CPU architecture (different CPU architecture == different assembly *dialects*)
    - Regardless, an instruction will always be a operation + operands
    - For x86 there are two syntaxes: Intel & AT&T

- Registers -> stored directly in the CPU for easy/quick access
    - Typically the same size as the word width of the architecture
        - On 64-bit architecture, most registers will hold 64 bits
    - Can be accessed partially (syntax does reflect the history of the registers)
        - [cheatsheet](https://ggbaker.ca/295/x86.html)
    - Operations:
        - > Note: data directly mentioned in an instruction is known as the immediate value
        - mov -> move data into a register (mov rax, 1)
            - Caveat: setting a 32bit partial (and 32bit partial **only**) will zero out the register because of performance reasons
            - Caveat 2: mov doesn't *mov*e data it copies it
        - movsx -> preserves the sign from a lower partial register to a higher register (movsx rax, eax)
            - mov eax, -1 // now eax == 4294967295 and -1
            - // mov rax, eax // now rax == 4294967295 **only**
            - // movsx rax, eax // now rax == 4294967295 and -1
        - add -> add rax, rdx == rax += rdx
        - sub -> sub rax, rdx == rax -= rdx
        - imul -> imul rax, rdx == rax \*= rdx (does truncate to the width of the registers)
        - inc -> inc rax == rax += 1
        - dec -> dec rax == rax -= 1
        - neg -> neg rax == rax = 0 - rax
        - not -> negates each bit in the register
        - and -> bitwise and
        - or -> bitwise or
        - xor -> bitwise xor
        - shl -> shl rax, 10 (shift the rax register 10 bits to the left)
        - shr -> shr rax, 10 (shift the rax register 10 bits to the right)
        - sar -> sar rax, 10 (shift the rax register 10 bits to the right while also preserving the sign)
        - ror -> ror rax, 10 (rax register loops by shifting right 10)
        - rol -> rol rax, 10 (rax register loops by shifting left 10)
    - rip register -> contains the address of the next instruction (not directly read/writable)
    - rsp register -> contains the address of the stack (a region which stores temporary data)
    - > Many registers exist. Like ones for the OS, ones for floating-point numbers computation, or ones for processing large data fast

- Building executable:
```
#!/bin/bash

FILE=$1 # .s file
OUT=$2

as -o $FILE.o $FILE # Assembler
ld -o $OUT $FILE.o # Linker

rm $FILE.o
```

- .s file:
```
.intel_syntax noprefix ; tells the assembler what syntax to use (here is intel)
.global _start ; tells the assembler to make _start visible at the linker level
_start: ; tells the linker where program execution should begin (else execution starts at the top of the file)
mov rax, 1
```

## Memory
- Registers are expensive ): -> we need a place to store lots of data fairly fast
- Is used for everything & there is too much to name it all so we address them linearly
    - Note: each address is to 1 byte in memory
    - From 0x10000 (for security reasons) -to> 0x7fffffffffff (for architecture/OS purposes)
- The process' memory is initially partially filled by the OS
    - Contains:
        1. Program Binary Code
        2. Dynamically Allocated Memory (managed by libraries)
        3. Library Code
        4. The Stack
        5. OS Helper Region
        - The proccess can request more memory (known as the Dynamic Mapped Memory)

- The Stack
    - Registers and immediates can be **push**ed onto the stack or **pop**ped off the stack
        - push 0x1
        - pop rax ; rax = 0x1
    - Each stack entry is the bit width of the architecture
        - Note: even on 64-bit CPUs we can only push 32-bit immediates
    - Follows First In Last Out (FILO)
    - Is placed randomly, but typically at a higher address (because it...)
    - Grows backwards: push -> substracts 8 from rsp, pop -> adds 8 from rsp
- push rcx:
```
sub rsp, 8
mov [rsp], rcx
```
- pop rcx:
```
mov rcx, [rsp]
add rsp, 8
``` 
- [address or register-storing-address] -> references the value at the address
    - mov rax, [0x111] -> rax => value @ 0x111
    - mov [0x111], rax -> value @ 0x111 => rax
    - addresses can be calculated directly within the bracket some sort of base address + offset 
        - mov rbx, [rsp+rax\*8]
    - lea -> lea rbx, [rsp+rax\*8+5] ; rbx now contains the calculated address
    - Limited to: reg+reg\*(2 or 4 or 8)+value

- Fewer bits can be loaded by simply using partials
    - In this case storing 32bit partials **doesn't** zero out the register

- Memories stores items in little-endian (aka backwards)
    - little-endian -> LSB -to> MSB (memory)
    - big-endian -> MSB -to> LSB (register)
    - Note: only bytes are affected, not individual bits

- RIP-Relative Addressing
    - lea can directly access the rip register
    - we are able to read/write to the location the rip register is pointing towards
        - mov rax, [rip]
        - mov [rip], rax

- Writing immediate values to memory requires specifying a size
    - mov DWORD ptr [rax], 0x1111


