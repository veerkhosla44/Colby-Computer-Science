CS333 - Project 1 - README
Veer Khosla
02/22/2024

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   BankExample.c
│   README.txt
│   task1.c
│   task2.c
│   task3.c
│   task4.c
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
10: FF
11: 5A
12: CD
13: 4C
14: 1E
15: 43
16: 0C
17: 00
18: 00
19: 00
20: 14
21: 00
22: 00
23: 00
24: 30
25: CD
26: FF
27: FF
28: 07
29: 00
30: 00
31: 00
32: 88
33: 80
34: 2D
35: 7C
36: FD
37: 7F
38: 00
39: 00
40: 01
41: 00
42: 00
43: 00
44: 00
45: 00
46: 00
47: 00
48: E0
49: 03
50: 00
51: 00
52: 0A
53: 00
54: 00
55: 00
56: 30
57: CD
58: FF
59: FF
60: 07
61: 00
62: 00
63: 00
64: CE
65: FF
66: FF
67: FF
68: FF
69: FF
70: FF
71: FF
72: 00
73: 00
74: 00
75: 00
76: 07
77: 00
78: 00
79: 00
80: 40
81: 00
82: 00
83: 00
84: 00
85: 00
86: 00
87: 00
88: 00
89: CE
90: FF
91: FF
92: 07
93: 00
94: 00
95: 00
96: 0C
97: 74
98: 2D
99: 7C




Task 3:

This program demonstrate dynamic memory allocation and the importance of proper memory management.
  
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
