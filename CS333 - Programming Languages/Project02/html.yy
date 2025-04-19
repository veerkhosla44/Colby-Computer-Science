/**
 * Veer Khosla
 * CS333
 * 02/29/24
 * 
 * strip html file of all tags and comments
 * 
 */
    #include <string.h>
%%

[ \t\n]+    {if(strcmp(yytext, "<p>") != 0);}                   // removes extra whitespaces
"\<p\>"|"</p>"  {putchar('\n'); }                               // puts a '\n' in places where '<p>' appears
\<[^<>]+\>  {if(strcmp(yytext, "<p>") == 0) {printf("<p>");}}   // removes all comments and tags from the file


%%
int main( int argc, char *argv[] ) {
    if (argc > 1)
        yyin = fopen( argv[1], "r" ); 
        
    yylex(); 
    return 0;
}