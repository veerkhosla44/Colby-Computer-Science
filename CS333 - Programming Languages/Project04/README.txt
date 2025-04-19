CS333 - Project 3 - README
Veer Khosla
03/17/2024

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   cstk.c
│   cstk.h
│   cstktest2.c
│   cstktest2.exe
│   Project4 Report.pdf
│   README.txt
│   task1.c
│   task1.exe
│   task1rust.exe
│   task1rust.pdb
│   task1rust.rs
│   task2.c
│   task2.exe
│   task2rust.exe
│   task2rust.pdb
│   task2rust.rs
│   task3.c
│   task3.exe
│   task3rust.exe
│   task3rust.pdb
│   task3rust.rs
│   toDraw2.c
│   toDraw2.exe
│
└───.vscode
        settings.json


C PROGRAMS: 

Task 1:

Compile:
gcc -o task1 task1.c

Run:
./task1

Output:
The sorted array is: 12 10 8 6 4 2 0 1 3 5 7 9 11 13 


Task 2:

Compile:
gcc -o task2 task2.c

Run:
./task2 5
./task2 10

Output:
120
3628800


Task 3:

Compile:
gcc -o cstktest2 cstktest2.c cstk.c

Run:
./cstktest2

Output:
All non-display tests passed!
You should now see the numbers from 0 to 9: 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

You should now see the string: [Max Bender: 10, Stephanie Taylor: 100]
Stephanie Taylor: 100

Compile:
gcc -o toDraw2 toDraw2.c cstk.c

Run: 
./toDraw2

Output: 
Stack is located at: 0x7ffffcbe8
i is located at: 0x7ffffcbe4
Stack starts at: 0xa00000450
Account struct is located at: 0x7ffffcbd0



Rust Programs:

Task 1:

Compile:
rustc task1rust.rs

Run:
./task1rust

Output:
count is at least 10
We've counted down to 0!
count is: 0
count is: 1
count is: 2
count is: 3
count is: 4
the number is: 10
the number is: 20
the number is: 30
the number is: 40
the number is: 50
Count is exactly 5


Task 2:

Compile:
rustc task2rust.rs

Run:
./task2rust

Output:
The result is 12
The result is 6


Task 3:

Compile:
rustc task3rust.rs

Run:
./task3rust

Output:
Sorted ints: [1, 2, 3, 4, 5]
Sorted floats: [1.4, 2.2, 3.3, 4.1, 5.5]

