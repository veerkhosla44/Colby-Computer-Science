CS333 - Project 6 - README
Veer Khosla
4/24/2024

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   README.txt
│   task2a.c
│   task2b.c
│   task2c.c
│   wctest.txt
│   wordcounter.c
│   wordcounter.rs
│
├───.vscode
│       settings.json
│
└───wordcounter
    │   .gitignore
    │   Cargo.lock
    │   Cargo.toml
    │   wctest.txt
    │
    ├───src
    │       main.rs
    │
    └───target
        │   .rustc_info.json
        │   CACHEDIR.TAG
        │
        └───debug
            │   .cargo-lock
            │   wordcounter.d
            │   wordcounter.exe
            │   wordcounter.pdb
            │
            ├───.fingerprint
            │   └───wordcounter-50e2aae467e4c15e
            │           bin-wordcounter
            │           bin-wordcounter.json
            │           dep-bin-wordcounter
            │           invoked.timestamp
            │
            ├───build
            ├───deps
            │       wordcounter.d
            │       wordcounter.exe
            │       wordcounter.pdb
            │
            ├───examples
            └───incremental
                └───wordcounter-cynf7buukjk9


Part 1:

TASK 1: 
implement a word counter that counts the number of occurrences of every word in a text file

Compile:
	gcc -o wordcounter wordcounter.c
	./wordcounter wctext.txt

OUTPUT:
Top 20 words:
the: 17
of: 7
and: 6
was: 5
in: 4
with: 4
a: 3
windows: 3
broken: 2
wings: 2
central: 2
portion: 2
had: 2
been: 2
but: 2
up: 2
were: 2
these: 1
blocked: 1
wooden: 1


TASK 2:
create examples of signal handling in C

(a) Program demonstrates a SIGINT singal and makes a signal handler that catches the Ctrl+C interrupt signal. prints "Interrupted!"

    Compile:
	gcc -o test_a task2a.c
	./test_a

    OUTPUT:
    Program started. Press Ctrl+C to interrupt.
    ^CInterrupted!

(b) demonstrates handling of SIGFPE and registers a handler for the SIGFPE signal that is triggered by a floating point division by zero.

    Compile:
	gcc -o test_b task2b.c
	./test_b

    OUTPUT:
	Result: inf

(c) demonstrates handling of SIGSEGV and registers a handler for the SIGSEGV signal

    Compile:
	gcc -o test_c task2c.c
	./test_c

    OUTPUT:
    	Segmentation fault handled.



Part 2: Rust
Create wordcounter similar to task 1 but in Rust

Navigate Directory:
	cd wordcounter

Compile:
	cargo build
	cargo run

Output:

the: 17
of: 7
and: 6
was: 5
in: 4
with: 4
a: 3
windows: 3
were: 2
had: 2
but: 2
central: 2
up: 2
wings: 2
portion: 2
been: 2
broken: 2
lichen-blotched: 1
thrown: 1
erected: 1