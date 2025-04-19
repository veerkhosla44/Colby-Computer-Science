CS333 - Project 3 - README
Veer Khosla
03/17/2024

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
|   2024-03-17 22-25-25.mkv
|   cstk.c
|   cstk.h
|   cstktest.c
|   cstktest.exe
|   Project3 Report.pdf
|   README.txt
|   task1.rs
|   task2.rs
|   task3.rs
|   toDraw.c
|__ toDraw.exe



cstk.h - header file forstack
cstk.c - implementation of methods in header file
cstktest.c - test code

Tasks 1, 2, and 3:

Implement a stack in c with various methods and functions

 Compile:
	gcc -o cstktest cstktest.c cstk.c
 Run:
	./cstktest
 Output:
	All non-display tests passed!
	You should now see the numbers from 0 to 9:
	Printing stack in original order:
	0 1 2 3 4 5 6 7 8 9
	Now you should see the numbers from 9 to 0:
	Printing stack in reverse order:
	9 8 7 6 5 4 3 2 1 0

Task 4:
 Compile:
	gcc -o toDraw toDraw.c cstk.c
 Run:
	./toDraw
 Output:
	Mark 1: Stack and Heap Memory
	------------------------------
	Stack Pointer (s): 0xa00000450
	Heap Memory (Stack Data)
	-------------------------------
	Address: 0xa00002330
	Top Pointer: 0xa00002330
	Capacity: 0xa00000460

	a is at 0x7ffffcbe8
	i is at 0x7ffffcbf4
	array starts at 0xa000023e0
	The original list: Printing stack in original order:
	1 2 3 4 5 6 7 8 9 10
	The reversed list: Printing stack in reverse order:
	10 9 8 7 6 5 4 3 2 1

	Mark 2: Stack and Heap Memory After Destruction
	---------------------------------------------
	Stack Pointer (s): 0xa00000450
	Heap Memory (Stack Data) Freed
	--------------------------------

