/* detect_garbage.c
 * Veer Khosla
 * Identify garbage heap chunks using the mark-and-sweep method
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STACK_SIZE 10
#define MAX_HEAP_SIZE 10

typedef struct _HeapChunk {
    int num_references;
    int marked;
    struct _HeapChunk **references;
} HeapChunk;

typedef struct {
    char *name;
    HeapChunk *reference;
} Var;

typedef struct {
    Var *stack;  // array of all current variables
    int num_vars_on_stack;
    HeapChunk **heap;  // array of all allocated HeapChunks
    int num_heap_chunks;
} ProgramState;

// Forward declarations
void dfsMark(HeapChunk *chunk);

ProgramState *createProgramState() {
    ProgramState *state = (ProgramState *)malloc(sizeof(ProgramState));
    state->stack = (Var *)malloc(sizeof(Var) * MAX_STACK_SIZE);
    state->heap = (HeapChunk **)malloc(sizeof(HeapChunk *) * MAX_HEAP_SIZE);
    state->num_heap_chunks = 0;
    state->num_vars_on_stack = 0;
    return state;
}

HeapChunk *HeapMalloc(ProgramState *state) {
    HeapChunk *chunk = (HeapChunk *)malloc(sizeof(HeapChunk));
    chunk->num_references = 0;
    chunk->references = NULL;
    state->heap[state->num_heap_chunks] = chunk;
    state->num_heap_chunks++;
    return chunk;
}

void setVar(ProgramState *state, char *var_name, HeapChunk *chunk) {
    int found = 0;
    for (int i = 0; i < state->num_vars_on_stack; i++) {
        if (strcmp(state->stack[i].name, var_name) == 0) {
            found = 1;
            state->stack[i].reference = chunk;
        }
    }
    if (!found) {
        state->stack[state->num_vars_on_stack].name = strdup(var_name);
        state->stack[state->num_vars_on_stack].reference = chunk;
        state->num_vars_on_stack++;
    }
}

void addReference(HeapChunk *chunk_source, HeapChunk *chunk_target) {
    if (chunk_source->num_references++ == 0)
        chunk_source->references = malloc(sizeof(HeapChunk *));
    else
        chunk_source->references = realloc(chunk_source->references, chunk_source->num_references * sizeof(HeapChunk *));
    chunk_source->references[chunk_source->num_references - 1] = chunk_target;
}

void markAndSweep(ProgramState *state) {
    // Unmark all chunks
    for (int i = 0; i < state->num_heap_chunks; i++)
        state->heap[i]->marked = 0;

    // Mark reachable chunks
    for (int i = 0; i < state->num_vars_on_stack; i++)
        dfsMark(state->stack[i].reference);

    // Identify garbage
    for (int i = 0; i < state->num_heap_chunks; i++) {
        if (!state->heap[i]->marked)
            printf("Heap chunk %d is garbage\n", i);
    }
}

void dfsMark(HeapChunk *chunk) {
    if (chunk == NULL || chunk->marked)
        return;
    chunk->marked = 1;
    for (int i = 0; i < chunk->num_references; i++)
        dfsMark(chunk->references[i]);
}

int main() {
/*
This program demonstrates the mark-and-sweep garbage collection process in C. It initializes a program state with stack variables 
and heap allocations, sets up references to form cycles, and identifies unreachable heap chunks as garbage. Specifically, 
the stack variables x, y, and z point to heap chunks a, b, and c, respectively. Heap chunk a references b, b references c, and c references a, 
forming a cycle. Additionally, a new allocation for b and d forms another isolated cycle. The mark-and-sweep process marks all reachable chunks 
from the stack and identifies unmarked chunks as garbage, highlighting the limitations of reference counting in detecting cyclic references.
*/

    ProgramState *state = createProgramState();

    // Create heap chunks
    HeapChunk *a = HeapMalloc(state);
    HeapChunk *b = HeapMalloc(state);
    HeapChunk *c = HeapMalloc(state);
    HeapChunk *d = HeapMalloc(state);

    // Set variables on the stack
    setVar(state, "x", a); // x points to a
    setVar(state, "y", b); // y points to b
    setVar(state, "z", c); // z points to c

    // Create references
    addReference(a, b); // a -> b
    addReference(b, c); // b -> c
    addReference(c, a); // c -> a (cycle a -> b -> c -> a)

    // d and a new allocation b are isolated and form a cycle
    b = HeapMalloc(state); // New b not reachable from stack
    d = HeapMalloc(state); // d not reachable from stack
    addReference(b, d); // b -> d
    addReference(d, b); // d -> b (cycle b -> d -> b)

    // Run mark and sweep
    markAndSweep(state);

    // Clean up if needed (freeing memory)
    // Depending on your implementation details, you might want to add a cleanup function

    return 0;
}
