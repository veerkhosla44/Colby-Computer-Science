CS333 - Project 5 - README
Veer Khosla
4/9/2024

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   clltest.c
│   clltest.exe
│   clltest2.c
│   clltest2.exe
│   LinkedList.c
│   LinkedList.h
│   README.txt
│
└───my_linked_list
    │   .gitignore
    │   Cargo.lock
    │   Cargo.toml
    │
    ├───src
    │       linkedlist.rs
    │       main.rs
    │
    └───target
        │   .rustc_info.json
        │   CACHEDIR.TAG
        │
        └───debug
            │   .cargo-lock
            │   my_linked_list.d
            │   my_linked_list.exe
            │   my_linked_list.pdb
            │
            ├───.fingerprint
            │   ├───my_linked_list-6f1db8acf3b51a7c
            │   │       bin-my_linked_list
            │   │       bin-my_linked_list.json
            │   │       dep-bin-my_linked_list
            │   │       invoked.timestamp
            │   │       output-bin-my_linked_list
            │   │
            │   └───my_linked_list-e494764dc7af98a7
            │           invoked.timestamp
            │           output-bin-my_linked_list
            │
            ├───build
            ├───deps
            │       my_linked_list-e494764dc7af98a7.d
            │       my_linked_list.d
            │       my_linked_list.exe
            │       my_linked_list.pdb
            │
            ├───examples
            └───incremental
                ├───my_linked_list-60gtcr06xjdw
                │   │   s-gv8wpokbrw-iwp50u.lock
                │   │
                │   └───s-gv8wpokbrw-iwp50u-dz2v5nkpjcfawi7k0amko4gmc
                │           1ctyksn2ee1hzfqx.o
                │           1e0vgqtqwonlj7v.o
                │           29vlirc5on4tfqci.o
                │           2rpq177es5rzo02g.o
                │           43rpp636pdvncrw8.o
                │           44i7vuhdzmdj1qx4.o
                │           45ytksx0l4o2gsth.o
                │           4a483ffqegjh3d98.o
                │           4fk0ydem6jg96zg0.o
                │           4ww1lzmqll2gnfwt.o
                │           ay8v6jhirlr0qhs.o
                │           dep-graph.bin
                │           query-cache.bin
                │           work-products.bin
                │
                └───my_linked_list-ktc5caoyd4y1
                    │   s-gv8wok2w4r-12dqn65.lock
                    │
                    └───s-gv8wok2w4r-12dqn65-working
                            dep-graph.part.bin



TASK1: The goal was to build a generic linked list

"linkedlist.h" contains the header file
"test.c" contains the test file
"linkedlist.c" contains the implementation file

Compile:
	gcc -o clltest clltest.c linkedlist.c 
	./clltest

Output:

After initialization
value: 18
value: 16
value: 14
value: 12
value: 10
value: 8
value: 6
value: 4
value: 2
value: 0

After squaring
value: 324
value: 256
value: 196
value: 144
value: 100
value: 64
value: 36
value: 16
value: 4
value: 0

removed: 324

Found: 256

removed: 256

After removals
value: 196
value: 144
value: 100
value: 64
value: 36
value: 16
value: 4
value: 0

After append
value: 196
value: 144
value: 100
value: 64
value: 36
value: 16
value: 4
value: 0
value: 11

After clear

After appending
value: 0
value: 1
value: 2
value: 3
value: 4

popped: 0
popped: 1

After popping
value: 2
value: 3
value: 4

List size: 3



TASK1.3: The goal was to extend the testing so it uses a linkedlist with a second data type. I created a second test file and tested the linkedlist using a char data type.

"linkedlist.h" contains the header file
"test2.c" contains the test file
"linkedlist.c" contains the implementation file

Compile:
	gcc -o clltest2 clltest2.c linkedlist.c 
	./clltest2

OUTPUT:
After initialization
value: O
value: N
value: M
value: L
value: K
value: J
value: I
value: H
value: G
value: F

After moving char by 1 (adding 1)
value: P
value: O
value: N
value: M
value: L
value: K
value: J
value: I
value: H
value: G

removed: O

removed: P

After removals
value: N
value: M
value: L
value: K
value: J
value: I
value: H
value: G

After append
value: N
value: M
value: L
value: K
value: J
value: I
value: H
value: G
value: O

After clear

After appending
value: x
value: y
value: z
value: {
value: |

popped: x
popped: y

After popping
value: z
value: {
value: |

List size: 3

data from deleted node: {

After deleting index 1
value: z
value: |



Rust Tasks:
Navigate Directory:
	cd .\my_linked_list\

Compile:
	cargo build
	cargo run

Output:

TESTING INTEGER

After initialization

0
2
4
6
8
10
12
14
16
18
After squaring

0
4
16
36
64
100
144
196
256
324
After append

0
4
16
36
64
100
144
196
256
324
30
After clear

After append

0
1
2
3
4
Popped 0

Popped 1

After popping

2
3
4
Size 3

TESTING FLOAT

After initialization

9.5
8.5
7.5
6.5
5.5
4.5
3.5
2.5
1.5
0.5
After squaring

90.25
72.25
56.25
42.25
30.25
20.25
12.25
6.25
2.25
0.25
After append

90.25
72.25
56.25
42.25
30.25
20.25
12.25
6.25
2.25
0.25
30.5
After clear

After append

0
0.5
1
1.5
2
Popped 0

Popped 0.5

After popping

1
1.5
2
Size 3
