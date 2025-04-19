#include "cstk.h"
#include <stdio.h>
#include <stdlib.h>

Stack* stk_create(int maxCapacity) { 
    Stack* p = malloc(sizeof(Stack));
    p->capacity = maxCapacity;
    p->data = (void **)malloc(maxCapacity * sizeof(void *));
    p->top = p->data;
    return p;
}


// int stk_empty(Stack* p) {
//     return p->top == p->data ? 1 : 0;
// }


// int stk_full(Stack* p) {
//     int currentSize = p->top - p->data; 
//     return currentSize == p->capacity ? 1 : 0;
// }

int stk_empty(Stack *stack)
{
    return stack->top == stack->data;
}

int stk_full(Stack *stack)
{
    return (stack->top - stack->data) == stack->capacity;
}



void stk_push(Stack* p, void *value) {
    if (stk_full(p)) {
        printf("Stack is full\n");
        return;
    }

    *(p->top) = value;
    (p->top)++;
}


void *stk_peek(Stack *stack) {
    if (stk_empty(stack))
    {
        printf("Stack is empty\n");
        return 0;
    }
    else
    {
        return *(stack->top - 1);
    }
}


void *stk_pop(Stack *stack) {
    if (stk_empty(stack))
    {
        printf("Stack is empty. You cannot pop!\n");
        return 0;
    }
    else
    {
        stack->top--;
        return *(stack->top);
    }
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


int stk_size(Stack *stack) {
    return stack->top - stack->data;
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


char *stk_toString(Stack *stack, char *(*toString)(void *)) {
    int capacity = 1024; // Initial capacity
    char *result = (char *)malloc(capacity * sizeof(char));
    if (!result) return NULL; // Check malloc failure

    result[0] = '\0'; // Start with an empty string
    int length = 0; // Current length of result

    for (void **current = stack->data; current < stack->top; current++) {
        char *itemString = toString(*current); // Correctly using toString
        if (!itemString) {
            free(result);
            return NULL; // Handle toString failure
        }
        int itemLength = strlen(itemString);

        // Ensure there's enough capacity
        while (length + itemLength + 2 > capacity) { 
            capacity *= 2;
            char *newResult = (char *)realloc(result, capacity * sizeof(char));
            if (!newResult) {
                free(result);
                free(itemString);
                return NULL; // Handle realloc failure
            }
            result = newResult;
        }

        // Append itemString to result
        strcat(result + length, itemString);
        length += itemLength;

        // Add separator for all but the last item
        if (current < stack->top - 1) {
            strcat(result, ", ");
            length += 2;
        }

        free(itemString); // Avoid memory leak
    }

    return result;
}
