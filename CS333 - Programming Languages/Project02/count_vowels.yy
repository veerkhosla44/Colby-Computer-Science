/**
 * Vee Khosla
 * CS333
 * 02/29/24
 * 
 * counts the number of characters and rows in a file
 * counts how much each vowel [i, o, u, e, a] appears in a file 
 */

    // variables declared
    int row_count = 0;
    int char_count = 0; 
    int vowel_count[5] = {0}; // creates a int array of size 5 and sets to all 0s 


%%
\n {row_count++;} // at end of each line add 1 to row count var 
[aA] {vowel_count[0]++;} // add one to vowel each time A or a is seen
[eE] {vowel_count[1]++;} // add one to vowel each time E or e is seen
[iI] {vowel_count[2]++;} // add one to vowel each time I or i is seen
[oO] {vowel_count[3]++;} // add one to vowel each time O or o is seen
[uU] {vowel_count[4]++;} // add one to vowel each time U or u is seen
. {char_count++;} // increase the character count each time a char is seen
%%

int main( int argc, char *argv[] ) {

    // where yylex reads its input from the command line
    if (argc > 1)
        yyin = fopen( argv[1], "r" ); 

    // a function of flex that read input till it is exhausted
    yylex(); 

    // prints the results to terminal
    printf("Number of rows: %d\n", row_count);
    printf("Number of characters: %d\n", char_count);
    printf("Number of 'a's: %d\n", vowel_count[0]);
    printf("Number of 'e's: %d\n", vowel_count[1]);
    printf("Number of 'i's: %d\n", vowel_count[2]);
    printf("Number of 'o's: %d\n", vowel_count[3]);
    printf("Number of 'u's: %d\n", vowel_count[4]);
  
    return 0;
}
