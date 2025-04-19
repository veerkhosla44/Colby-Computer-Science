#include "cstk.h"
#include <stdio.h>
#include <stdlib.h>

// int main() {
//     Stack* p = stk_create(5);
//     printf("%s\n", stk_empty(p) ? "Stack is empty" : "Stack is not empty");
//     stk_push(p, 1);
//     printf("%s\n", stk_empty(p) ? "Stack is empty" : "Stack is not empty");
//     printf("%s\n", stk_full(p) ? "Stack is full" : "Stack is not full");
//     stk_push(p, 2);   
//     stk_push(p, 3);
//     stk_push(p, 4);
//     stk_push(p, 5);
//     printf("%s\n", stk_full(p) ? "Stack is full" : "Stack is not full");
    
//     printf("%d\n", stk_peek(p));

//     // Display the stack in original order
//     stk_display(p, 0);

//     // Display the stack in reverse order
//     stk_display(p, 1);

//     // Create a copy of the stack
//     Stack* copy = stk_copy(p);

//     // Display the copy of the stack
//     printf("Copy of the stack:\n");
//     stk_display(copy, 0);

//     // Pop some values from the original stack
//     printf("Popping values from the original stack:\n");
//     printf("%d\n", stk_pop(p));
//     printf("%d\n", stk_pop(p));

//     // Display the original stack after popping
//     printf("Original stack after popping:\n");
//     stk_display(p, 0);

//     // Destroy both stacks
//     stk_destroy(p);
//     stk_destroy(copy);

//     return 0;
// }


Stack* stk_create(int maxCapacity) { 
    Stack* p = malloc(sizeof(Stack));
    p->capacity = maxCapacity;
    p->data = malloc(sizeof(int)*maxCapacity);
    p->top = p->data;
    return p;
}


int stk_empty(Stack* p) {
    return p->top == p->data ? 1 : 0;
}


int stk_full(Stack* p) {
    int currentSize = p->top - p->data; 
    return currentSize == p->capacity ? 1 : 0;
}


void stk_push(Stack* p, int value) {
    if (stk_full(p)) {
        printf("Stack is full\n");
        return;
    }

    *(p->top) = value;
    (p->top)++;
}


int stk_peek(Stack* p) {
    if (stk_empty(p)) {
        printf("Stack is empty\n");
        return 0;
    }
    return *(p->top - 1);
}


int stk_pop(Stack* p) {
    if (stk_empty(p)) {
        printf("Error: Stack is empty\n");
        return 0; // Or handle the error condition appropriately
    }
    
    // Retrieve the value from the top of the stack
    int value = *(p->top - 1);

    // Decrement the top pointer to remove the top element
    (p->top)--;

    return value; // Return the popped value
}


void stk_display(Stack* p, int reverse) {
    if (stk_empty(p)) {
        printf("Stack is empty\n");
        return;
    }

    if (reverse) {
        printf("Printing stack in reverse order:\n");
        for (int i = p->top - p->data - 1; i >= 0; i--) {
            printf("%d ", *(p->data + i));
        }
    } else {
        printf("Printing stack in original order:\n");
        for (int i = 0; i < p->top - p->data; i++) {
            printf("%d ", *(p->data + i));
        }
    }
    printf("\n");
}


void stk_destroy(Stack* p) {
    free(p->data);
    free(p);
}


Stack* stk_copy(Stack* p) {
    Stack* copy = stk_create(p->capacity);
    if (copy == NULL) {
        printf("Failed to create a copy of the stack. Memory allocation error.\n");
        return NULL;
    }

    // Copy the data from the original stack to the copy
    for (int i = 0; i < p->top - p->data; i++) {
        *(copy->data + i) = *(p->data + i);
    }

    // Set the top pointer of the copy to point to the correct location
    copy->top = copy->data + (p->top - p->data);

    return copy;
}
