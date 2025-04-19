CS333 - Project 7 - README
Veer Khosla
5/9/24
Google Sites URL: 

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   detect_garbage.c
│   README.txt
│   task1a.c
│   task1b.c
│   test.exe
│   test.rs
│   testb.exe
│   timing.c
│   timing.h
│
├───.vscode
│       settings.json
│
└───memory_test
    │   .gitignore
    │   Cargo.lock
    │   Cargo.toml
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
            │   memory_test.d
            │   memory_test.exe
            │   memory_test.pdb
            │
            ├───.fingerprint
            │   └───memory_test-27b5461a85efda8a
            │           bin-memory_test
            │           bin-memory_test.json
            │           dep-bin-memory_test
            │           invoked.timestamp
            │
            ├───build
            ├───deps
            │       memory_test.d
            │       memory_test.exe
            │       memory_test.pdb
            │
            ├───examples
            └───incremental
                └───memory_test-2bojq37rcaeno
                    │   s-gw4xiocf45-dzrofc.lock
                    │
                    └───s-gw4xiocf45-dzrofc-6jh36h52344wkfklf99235m4q
                            19au1fh8qo5gmelf.o
                            1iokrre652pg97al.o
                            2kpr12y221fzadi3.o
                            2lnovf577rfirzf0.o
                            2mmr1mubgad8cu9k.o
                            317j5b8ugye649nd.o
                            3bfrp48c60azzr6i.o
                            3c3q67xch4krvcis.o
                            3conzbdowhmdbc6f.o
                            3f88tmkzfa3639i5.o
                            3smzcwplewwgrsqr.o
                            3t4894z9lfi2pw2o.o
                            4ko13hz2yxl1g5jb.o
                            4lteiuq932rmdg2j.o
                            4mi9amx57lsvv7o9.o
                            59msgja9q3epklz7.o
                            dep-graph.bin
                            lq7opn1stq13ytr.o
                            o57aplskd2qz6zv.o
                            query-cache.bin
                            tf46p08a58ypjee.o
                            vbjoic3236vykhp.o
                            work-products.bin


TASK1: try and estimate the time cost of memory management in C.

a. I used the timing files by Professor Li (Project 8) in order to do the timing.

"Task1.c" contains the implementation file for the method
"my_timing.h " contains the the header file
"my_timing.c" contains the implementation for timing

Compile:
	gcc -o test Task1.c my_timing.c
	./test 

Output:
	For Int:0.000000 sec
	For Char:0.000000 sec
	For Double:0.484000 sec

b.

Compile:
	gcc -o testb detect_garbage.c timing.c
	./testb

Output:
	Heap chunk 3 is garbage
	Heap chunk 4 is garbage
	Heap chunk 5 is garbage


Task 2:

Compile:
	cd memory_test
	cargo build
	cargo run

Output:
	Average deallocation time: 50.354µs