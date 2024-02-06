# sc0rp10n's My first Crackme (Write a keygen)

| **Source** | [crackmes.one](https://crackmes.one) |
|---|---|
| **Platform** | Linux, Unix |
| **Architecture** | x86-64 |
| **Language** | C |
| **Compiler** | GCC |
| **Format** | ELF |
| **Decompiled** | [Yes](Decompilation/crackme.c) |
| **Ghidra-Export** | [Yes](Ghidra-Analysis/crackme.xml) |

A valid key is any key that follows these rules:
- Must follow the format xxxx-xxxx-xxxx-xxxx, ie 4 blocks of length 4 seperated by "-"
- The ASCII code sum of a block must be a prime number
- Every blocks ASCII code sum must be greater than the last

This is a valid key: 0001-1112-1222-4555  
The ASCII code sums are: 193, 197, 199, 211
