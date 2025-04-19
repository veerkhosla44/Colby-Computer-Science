%{
#include <stdio.h>
%}

%%

[a-z] {
    int character = yytext[0] + 13; 
    if (character > 'z') {
        character -= 26;
    }
    printf("%c", character); // print new char
}

[A-Z] {
    int character = yytext[0] + 13;
    if (character > 'Z') {
        character -= 26;
    }
    printf("%c", character); // print new char
}

%%

int main() {
    yylex();
    return 0;
}
