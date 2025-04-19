#include "cstk.h"

typedef struct Account {
    char *name;
    int balance;
} Account;

int main() {
    Stack *stack = stk_create(10);
    int i;

    printf("Stack is located at: %p\n", &stack);
    printf("i is located at: %p\n", &i);
    printf("Stack starts at: %p\n", stack);

    for (int i = 0; i < 5; i++) {
        int *x = (int *)malloc(sizeof(int));
        *x = i;
        stk_push(stack, x);
    }

    Account account = {"Max Bender", 10};
    printf("Account struct is located at: %p\n", &account);
    stk_push(stack, &account);

    // MARK 1 - draw current contents of stack and relevant contents of heap
    return 0;
}