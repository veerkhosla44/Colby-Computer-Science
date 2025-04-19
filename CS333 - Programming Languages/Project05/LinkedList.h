/*  Veer Khosla
    CS333
    4/9/24
    header file to implement a linkedlist data structure
*/

#ifndef linkedlist
#define linkedlist

    // defines the struct of a Node
    typedef struct Node {

        void *data;
        struct Node *next; // next pointer

    } node;

    // defines the struct of a LinkedList
    typedef struct LinkedList  {

        node *head; 
        int size;

    } LinkedList;

    struct LinkedList *ll_create(); // creates a new LinkedList struct, initializes it, and returns it.

    void ll_push(struct LinkedList *l, void *data); // adds a node to the front of the list, storing the given data in the node.

    void *ll_pop(struct LinkedList *l); // removes the node at the front of the list and returns the associated data.

    void ll_append(struct LinkedList *l, void *data); // adds a node to the end of the list, storing the given data in the node.

    void *ll_remove(struct LinkedList *l, void *target, int (*compfunc)(void *, void *)); // removes the first node in the list whose data matches target given the comparison function. The function returns the pointer to the data in the removed node.

    void *ll_find(LinkedList *l, void *target, int (*compfunc)(void *, void *)); // finds the first node in the list whose data matches target given the comparison function. Returns the pointer to the data if found, otherwise NULL.

    int ll_size(struct LinkedList *l); // returns the size of the list.

    void ll_clear(struct LinkedList *l, void (*freefunc)(void *)); //  removes all of the nodes from the list, freeing the associated data using the given function.

    void ll_map(struct LinkedList *l, void (*mapfunc)(void *)); // traverses the list and applies the given function to the data at each node.

    void *ll_delete(LinkedList *l, int index); // removes the node at any given position in the list and returns its data
#endif // // end of file and if statement
