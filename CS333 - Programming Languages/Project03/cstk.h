typedef struct Stack 
{
	int *data; // this is a pointer to the start of the data for the stack
	int *top; // this will point to the next place to insert in the stack
	int capacity; // this is the maximal size of the stack
} Stack;

Stack *stk_create(int);

int stk_empty(Stack *);
int stk_full(Stack *);
void stk_push(Stack *, int);
int stk_peek(Stack *);
int stk_pop(Stack *);
void stk_display(Stack *, int);
void stk_destroy (Stack *);
Stack *stk_copy(Stack *);
