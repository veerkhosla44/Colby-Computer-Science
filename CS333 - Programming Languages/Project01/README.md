CS333 - Project 1 - README
Veer Khosla
02/22/2024

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home
OS: x64 Windows 10

Directory Layout:
C:.
│ BankExample.c
│ README.txt
│ task1.c
│ task2.c
│ task3.c
│ task4.c
│
└───.vscode
  settings.jsonDevice name

Task 1:
The goal of this program was to see how different data types are stored in memory

Compile:
 gcc -o task1 task1.c
Run:
 ./task1
Output:
 char: 41
 short: 34 12
 int: 67 45 23 01
 long: 15 CD 5B 07 00 00 00 00
 float: 79 E9 F6 42
 double: 0B 0B EE 07 3C DD 5E 40

Task 2:
The goal of this program was to explore and understand the stack's memory layout by inspecting how local variables are stored

Compile:
 gcc -o task2 task2.c
Run:
 ./task2
Output:
 0: E8
 1: CB
 2: FF
 3: FF
 4: 07
 5: 00
 6: 00
 7: 00
 8: 50
 9: CC
 ... (continues through 99 — unchanged from source)

Task 3:
This program demonstrates dynamic memory allocation and the importance of proper memory management.

Compile:
 gcc -o task3 task3.c
Run:
 ./task3
Output:
 Memory fills up if commenting out free statement. Otherwise, memory is cleaned

Task 4:
This program lays out structs in memory and looks at the impact of variable ordering within structs.

Compile:
 gcc -o task4 task4.c
Run:
 ./task4
Output:
Version1 Memory Layout (sizeof: 12):
 0: 41 1: 00 2: 00 3: 00
 4: 78 5: 56 6: 34 7: 12
 8: 42 9: 00 10: 34 11: 12

Version2 Memory Layout (sizeof: 12):
 0: 41 1: 42 2: 00 3: 00
 4: 78 5: 56 6: 34 7: 12
 8: 34 9: 12 10: FF 11: FF

Version3 Memory Layout (sizeof: 8):
 0: 78 1: 56 2: 34 3: 12
 4: 34 5: 12 6: 41 7: 42

Task 5:
Demonstrate and analyze how improper user input can lead to unintended memory problems

Compile:
 gcc -o task5 BankExample.c
Run:
 ./task5
Output:
Please input your name for a new bank account: Veer Khosla
Thank you Veer Khosla, your new account has been initialized with balance 0.
Memory contents:
 56 65 65 72 20 4B 68 6F 73 6C 61 00 00 00 00 00

Please input your name for a new bank account: superlongname
Thank you superlongname, your new account has been initialized with balance 101.
Memory contents:
 73 75 70 65 72 6C 6F 6E 67 6E 61 6D 65 00 00 00
