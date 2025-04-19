/*  Veer Khosla
    CS333
    4/9/24
    Test file for linked list operations on char data types.
*/

#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

// function that prints a character
void printChar(void *i) {
    char *a = (char *)i;
    printf("value: %c\n", *a);
}

// function that adds 1 to a character
void addChar(void *i) {
    char *a = (char *)i;
    *a = *a + 1;
}

// function that compares two characters and returns 1 if they are equal
int compChar(void *i, void *j) {
    char *a = (char *)i;
    char *b = (char *)j;
    return *a == *b;
}

int main(int argc, char *argv[]) {
    LinkedList *l_c;
    char *b;
    char *t;
    char x;

    // create a list
    l_c = ll_create();

    // push data on the list
    for (x = 'F'; x < 'K'; x++) {
        b = malloc(sizeof(char));
        *b = x;
        ll_push(l_c, b);
    }

    // printing the list and testing map
    printf("After initialization\n");
    ll_map(l_c, printChar);

    ll_map(l_c, addChar);

    printf("\nAfter adding 1 to each char\n");
    ll_map(l_c, printChar);

    // testing removing data
    t = malloc(sizeof(char));
    *t = 'P';
    b = ll_remove(l_c, t, compChar);
    if (b != NULL)
        printf("\nremoved: %c\n", *b);
    else
        printf("\nNo instance of %c\n", *t);

    *t = 'O';
    b = ll_remove(l_c, t, compChar);
    if (b != NULL)
        printf("\nremoved: %c\n", *b);
    else
        printf("\nNo instance of %c\n", *t);

    printf("\nAfter removals\n");
    ll_map(l_c, printChar);

    // testing appending data
    ll_append(l_c, t);

    printf("\nAfter append\n");
    ll_map(l_c, printChar);

    // test clearing
    ll_clear(l_c, free);

    printf("\nAfter clear\n");
    ll_map(l_c, printChar);

    // rebuild and test append and pop
    for (x = 'x'; x < 'x' + 5; x++) {
        b = malloc(sizeof(char));
        *b = x;
        ll_append(l_c, b);
    }

    printf("\nAfter appending\n");
    ll_map(l_c, printChar);

    // testing popping
    b = ll_pop(l_c);
    printf("\npopped: %c\n", *b);
    free(b);

    b = ll_pop(l_c);
    printf("popped: %c\n", *b);
    free(b);

    printf("\nAfter popping\n");
    ll_map(l_c, printChar);

    // prints size
    printf("\nList size: %d\n", ll_size(l_c));

    if (ll_size(l_c) > 1) {
        b = ll_delete(l_c, 1);
        printf("\ndata from deleted node: %c\n", *b);
        free(b);
    }

    printf("\nAfter deleting index 1\n");
    ll_map(l_c, printChar);

    ll_clear(l_c, free); // Clear all nodes and free the data including the target pointer
    
    // free the empty linked list
    free(l_c);
    return 0;
}
