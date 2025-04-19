CS333 - Project 8 - README
Veer Khosla
5/9/24
Google Sites URL: 

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   .DS_Store
│   analysis.py
│   benford_sequential.c
│   bold.ppm
│   bold_parallel.ppm
│   colorize_parallel.c
│   IMG_4203.ppm
│   longer.bin
│   longer_nonBenford.bin
│   medium.bin
│   my_timing.c
│   my_timing.h
│   parallel1.c
│   parallel2.c
│   parallel3.c
│   parallel4.c
│   parallel5.c
│   parallel6.c
│   ppmIO.c
│   ppmIO.h
│   Project8 Report.pdf
│   README.txt
│   super_short.bin
│
└───benford_rust
    │   .gitignore
    │   Cargo.lock
    │   Cargo.toml
    │   longer.bin
    │
    ├───src
    │       main.rs
    │
    └───target
        │   .rustc_info.json
        │   CACHEDIR.TAG
        │
        └───release
            │   .cargo-lock
            │   benford_rust.d
            │   benford_rust.exe
            │   benford_rust.pdb
            │
            ├───.fingerprint
            │   ├───benford_rust-5d2d5a9d7b8630a2
            │   │       bin-benford_rust
            │   │       bin-benford_rust.json
            │   │       dep-bin-benford_rust
            │   │       invoked.timestamp
            │   │
            │   ├───crossbeam-deque-49568b72147d3aaa
            │   │       dep-lib-crossbeam-deque
            │   │       invoked.timestamp
            │   │       lib-crossbeam-deque
            │   │       lib-crossbeam-deque.json
            │   │
            │   ├───crossbeam-epoch-90a2d7b7f74d5a8c
            │   │       dep-lib-crossbeam-epoch
            │   │       invoked.timestamp
            │   │       lib-crossbeam-epoch
            │   │       lib-crossbeam-epoch.json
            │   │
            │   ├───crossbeam-utils-7970632b500f350f
            │   │       build-script-build-script-build
            │   │       build-script-build-script-build.json
            │   │       dep-build-script-build-script-build
            │   │       invoked.timestamp
            │   │
            │   ├───crossbeam-utils-d0f962c853191d40
            │   │       dep-lib-crossbeam-utils
            │   │       invoked.timestamp
            │   │       lib-crossbeam-utils
            │   │       lib-crossbeam-utils.json
            │   │
            │   ├───crossbeam-utils-eda676eeac18101f
            │   │       run-build-script-build-script-build
            │   │       run-build-script-build-script-build.json
            │   │
            │   ├───either-8f534ac98c55361e
            │   │       dep-lib-either
            │   │       invoked.timestamp
            │   │       lib-either
            │   │       lib-either.json
            │   │
            │   ├───rayon-core-4b128fcd13171120
            │   │       run-build-script-build-script-build
            │   │       run-build-script-build-script-build.json
            │   │
            │   ├───rayon-core-75ea95f1187863b8
            │   │       dep-lib-rayon-core
            │   │       invoked.timestamp
            │   │       lib-rayon-core
            │   │       lib-rayon-core.json
            │   │
            │   ├───rayon-core-bbcca23c23ea8b6d
            │   │       build-script-build-script-build
            │   │       build-script-build-script-build.json
            │   │       dep-build-script-build-script-build
            │   │       invoked.timestamp
            │   │
            │   └───rayon-f7be4520a05f452e
            │           dep-lib-rayon
            │           invoked.timestamp
            │           lib-rayon
            │           lib-rayon.json
            │
            ├───build
            │   ├───crossbeam-utils-7970632b500f350f
            │   │       build-script-build.exe
            │   │       build_script_build-7970632b500f350f.d
            │   │       build_script_build-7970632b500f350f.exe
            │   │       build_script_build-7970632b500f350f.pdb
            │   │       build_script_build.pdb
            │   │
            │   ├───crossbeam-utils-eda676eeac18101f
            │   │   │   invoked.timestamp
            │   │   │   output
            │   │   │   root-output
            │   │   │   stderr
            │   │   │
            │   │   └───out
            │   ├───rayon-core-4b128fcd13171120
            │   │   │   invoked.timestamp
            │   │   │   output
            │   │   │   root-output
            │   │   │   stderr
            │   │   │
            │   │   └───out
            │   └───rayon-core-bbcca23c23ea8b6d
            │           build-script-build.exe
            │           build_script_build-bbcca23c23ea8b6d.d
            │           build_script_build-bbcca23c23ea8b6d.exe
            │           build_script_build-bbcca23c23ea8b6d.pdb
            │           build_script_build.pdb
            │
            ├───deps
            │       benford_rust.d
            │       benford_rust.exe
            │       benford_rust.pdb
            │       crossbeam_deque-49568b72147d3aaa.d
            │       crossbeam_epoch-90a2d7b7f74d5a8c.d
            │       crossbeam_utils-d0f962c853191d40.d
            │       either-8f534ac98c55361e.d
            │       libcrossbeam_deque-49568b72147d3aaa.rlib
            │       libcrossbeam_deque-49568b72147d3aaa.rmeta
            │       libcrossbeam_epoch-90a2d7b7f74d5a8c.rlib
            │       libcrossbeam_epoch-90a2d7b7f74d5a8c.rmeta
            │       libcrossbeam_utils-d0f962c853191d40.rlib
            │       libcrossbeam_utils-d0f962c853191d40.rmeta
            │       libeither-8f534ac98c55361e.rlib
            │       libeither-8f534ac98c55361e.rmeta
            │       librayon-f7be4520a05f452e.rlib
            │       librayon-f7be4520a05f452e.rmeta
            │       librayon_core-75ea95f1187863b8.rlib
            │       librayon_core-75ea95f1187863b8.rmeta
            │       rayon-f7be4520a05f452e.d
            │       rayon_core-75ea95f1187863b8.d
            │
            ├───examples
            └───incremental



Task 1:
Sequential:

Compile:
	gcc -o benford_sequential my_timing.c benford_sequential.c -lm
	./benford_sequential

Output:
	There are 3217 1's
	There are 1779 2's
	There are 1121 3's
	There are 907 4's
	There are 745 5's
	There are 668 6's
	There are 591 7's
	There are 495 8's
	There are 477 9's
	It took 0.002637 seconds for the whole thing to run


Parallel:

1. Global Counter Array Protected by Single Mutex

Compile:
	gcc -o benford_par_global_single_mutex my_timing.c benford_par_global_single_mutex.c -lm lpthread
	./benford_par_global_single_mutex longer.bin

Output:
	Elapsed time: 3.3972 seconds
	Digit 1: 312705
	Digit 2: 177336
	Digit 3: 121034
	Digit 4: 92637
	Digit 5: 75909
	Digit 6: 65134
	Digit 7: 57202
	Digit 8: 51298
	Digit 9: 46745


2. Global Counter Array Protected by Array of Mutexes

Compile:
	gcc -o parallel2 my_timing.c parallel2.c -lm -lpthread
	./parallel2 longer.bin


Output:
	Elapsed time: 1.1269 seconds
	Digit 1: 312705
	Digit 2: 177336
	Digit 3: 121034
	Digit 4: 92637
	Digit 5: 75909
	Digit 6: 65134
	Digit 7: 57202
	Digit 8: 51298
	Digit 9: 46745


3. Local Counter Array, with Final Update Protected by Single Mutex

Compile:
	gcc -o parallel3 my_timing.c parallel3.c -lm -lpthread
	./parallel3 longer.bin

Output:
	Elapsed time: 0.0036 seconds
	Digit 1: 312705
	Digit 2: 177336
	Digit 3: 121034
	Digit 4: 92637
	Digit 5: 75909
	Digit 6: 65134
	Digit 7: 57202
	Digit 8: 51298
	Digit 9: 46745

4. Local Counter Array, with Final Update Protected by Array of Mutexes

Compile:
	gcc -o parallel4 my_timing.c parallel4.c -lm -lpthread
	./parallel4 longer.bin


Output:
	Elapsed time: 0.0044 seconds
	Digit 1: 312705
	Digit 2: 177336
	Digit 3: 121034
	Digit 4: 92637
	Digit 5: 75909
	Digit 6: 65134
	Digit 7: 57202
	Digit 8: 51298
	Digit 9: 46745

5. Global Counter Array of Arrays, Grouped by Thread, no Mutex

Compile:
	gcc -o parallel5 my_timing.c parallel5.c -lm -lpthread
	./parallel5 longer.bin

Output:
	Elapsed time: 0.0050 seconds
	Digit 1: 312705
	Digit 2: 177336
	Digit 3: 121034
	Digit 4: 92637
	Digit 5: 75909
	Digit 6: 65134
	Digit 7: 57202
	Digit 8: 51298
	Digit 9: 46745

6. Global Counter Array of Arrays, Grouped by Digit, no Mutex

Compile:
	gcc -o parallel6 my_timing.c parallel6.c -lm -lpthread
	./parallel6 longer.bin


Output:
	Elapsed time: 0.0100 seconds
	Digit 1: 312705
	Digit 2: 177336
	Digit 3: 121034
	Digit 4: 92637
	Digit 5: 75909
	Digit 6: 65134
	Digit 7: 57202
	Digit 8: 51298
	Digit 9: 46745



analysis.py: find means and generate graph of data

Output:
	parallel1 Mean Execution Time: 3.3234 seconds
	parallel2 Mean Execution Time: 1.0411 seconds
	parallel3 Mean Execution Time: 0.0039 seconds
	parallel4 Mean Execution Time: 0.0038 seconds
	parallel5 Mean Execution Time: 0.0048 seconds
	parallel6 Mean Execution Time: 0.0094 seconds

colorize.c:

Compile:
	gcc -o colorize_parallel -I. colorize_parallel.c ppmIO.c -lpthread -lm

	./colorize_parallel IMG_4203.ppm 1
	./colorize_parallel IMG_4203.ppm 2
	./colorize_parallel IMG_4203.ppm 4

Output:
	Images^^


Task 2:

Compile:
	cargo clean
	cargo build --release
	cargo run --release

Output:
Elapsed time: 101.5318ms seconds
	Digit 1: 627479
	Digit 2: 93529
	Digit 3: 66733
	Digit 4: 51855
	Digit 5: 42077
	Digit 6: 35454
	Digit 7: 30929
	Digit 8: 27359
	Digit 9: 24087

