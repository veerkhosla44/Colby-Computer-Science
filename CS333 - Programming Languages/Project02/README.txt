CS333 - Project 2 - README
Veer Khosla
3/17/24

Google Sites Website: https://sites.google.com/colby.edu/veers-cs333/home 
OS: x64 Windows 10
Directory Layout:
C:.
│   count_vowels-test.txt
│   count_vowels.exe
│   count_vowels.yy
│   encode-test.txt
│   encode.exe
│   encode.yy
│   finalrun.txt
│   firstrun.txt
│   firstRust.exe
│   firstRust.pdb
│   firstRust.rs
│   html-test-rslt.txt
│   html-test.txt
│   html.exe
│   html.yy
│   lex.yy.c
│   README.txt
│   task3output.txt
│   task3output2.txt
│
└───.vscode
        c_cpp_properties.json


Task 1:

Developed a Flex program named "encode" to perform a Caesar cipher encryption by shifting 
each alphabetic character in the input text by 13 positions in the ASCII value, 
wrapping around if necessary.

encode.yy - Flex Rule
encode-test.txt - Test Text File


 Compile:
	flex encode.yy   
	gcc -o encode lex.yy.c -lfl
	
 Run:
	encode < encode-test.txt > firstrun.txt
	encode < firstrun.txt > finalrun.txt

 Output:
	firstrun.txt: uryyb, guvf vf grfgvat zl rapbqr cebtenz! Ehaavat vg gjvpr jvyy erfhyg va fhpprffshyyl ernqvat guvf!
	finalrun.txt: hello, this is testing my encode program! Running it twice will result in successfully reading this!



Task 2:

Created a Flex program to analyze a text file, providing statistics including the total 
number of rows, characters, and occurrences of each vowel, treating both uppercase and 
lowercase instances equivalently.

count_vowels.yy - Count Vowels Rule
count_vowels-test.txt - Test Text File

 Compile:
	flex count_vowels.yy
	gcc -o count_vowels lex.yy.c -lfl
	
 Run:
	count_vowels count_vowels-test.txt

 Output:
	Number of rows: 4
	Number of characters: 144
	Number of 'a's: 11
	Number of 'e's: 18
	Number of 'i's: 8
	Number of 'o's: 13
	Number of 'u's: 5




Task 3:

Implemented a Flex program to strip an HTML file of all tags and comments, 
removing whitespace except for blank lines corresponding to <p> tags.

html.exe
html.yy
html-test.txt
html-test-rslt.txt


 Compile:
	flex html.yy
	gcc -o html lex.yy.c -lfl
	
 Run:
	html < html-test.txt > htmlOutput1.txt
	html < html-test-rslt.txt > htmlOutput2.txt

 Output:
	task3output.txt: 	ThisisapagetitleHereisaheader
				Hereissomebodytextinaparagraph

				Hereisalinktocs.colby.eduinsideaparagraph.
				<!--Hereisamulti-line
				Thisistheparagraphweshouldignorebecauseitisinacomment.
				Bonusifyouremovethis!comment-->
				Thisisthefinalparagraph.

	task3output2.txt: ThisisapagetitleHereisaheaderHereissomebodytextinaparagraphHereisalinktocs.colby.eduinsideaparagraph.Thisisthefinalparagraph.


