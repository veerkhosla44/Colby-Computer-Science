/*  Veer Khosla
    CS333
    4/9/2024
    linkedlist data structure
*/

#include <stdlib.h>
#include "linkedlist.h"

// creates a new LinkedList struct, initializes it, and returns it.
struct LinkedList *ll_create(){

    struct LinkedList *new_list = (LinkedList*) malloc(sizeof(struct LinkedList));

    new_list->head = NULL;
    new_list->size = 0;

    return new_list;
}

// adds a node to the front of the list, storing the given data in the node.
void ll_push(struct LinkedList *l, void *data){

    //creates a new node
    node *new_node = (node*) malloc(sizeof(node));
    new_node->data = data;

    // adds the node to the list || makes sure list is not empty
    if(l->head != NULL){
        new_node->next = l->head;
    }

    // sets new node as the head and increases size by 1
    l->head = new_node;
    l->size++;
}

// removes the node at the front of the list and returns the associated data.
void *ll_pop(struct LinkedList *l) {

    // makes sure list is not empty
    if(l->size == 0){
        return NULL;
    }

    // creates a pointer node pointing at head
    node *remove_node = l->head;

    // gets data stored in head node
    void *data = remove_node->data;

    // sets the head to the next node
    l->head = remove_node->next;

    // frees the head node
    free(remove_node);

    // subtracts one from size and returns data
    l->size--;
    return data;
}

// adds a node to the end of the list, storing the given data in the node.
void ll_append(struct LinkedList *l, void *data){

    //creates a new node
    node *new_node = (node*) malloc(sizeof(node));
    new_node->data = data;
    new_node->next = NULL;

    // makes sure list is not empty
    if ( l->head == NULL){
        l->head = new_node;
    }else{

        // creates a pointer node that points to head
        node *temp_node = l->head;

        // loops over list till the end
        while (temp_node->next != NULL){
            temp_node = temp_node->next;
        }

        // sets the new node to the next node of the last node in the list
        temp_node->next = new_node;
    }

    // adds 1 to size
    l->size++;
}

// removes the first node in the list whose data matches target given the comparison function. The function returns the pointer to the data in the removed node.
void *ll_remove(struct LinkedList *l, void *target, int (*compfunc)(void *, void *)){

    // makes sure list isn't empty
    if (l->size == 0){
        return NULL;
    }

    // creates a pointer node that points to head and a previous node
    node *curr_node = l->head;
    node *prev_node = NULL;

    // loops over the list to the end
    while (curr_node != NULL){

        // checks to see if there is a match
        if(compfunc(curr_node->data, target) == 0){

            // if match is head node 
            if (prev_node == NULL){
                
                l->head = curr_node->next;

            // if match is not head node
            }else{
                prev_node->next = curr_node->next;
            }

            //  gets data at matched node and frees it before taking 1 from size and returning data
            void *data = curr_node->data;
            free(curr_node);
            l->size--;
            return data;
        }

        // moves the loop over to the next element
        prev_node = curr_node;
        curr_node = curr_node->next;
    }

    // no match
    return NULL;

}

// returns the size of the list.
int ll_size(struct LinkedList *l){

    return l->size;
}

// removes all of the nodes from the list, freeing the associated data using the given function.
void ll_clear(struct LinkedList *l, void (*freefunc)(void *)){


    // creates a pointer node that points to head
    node *temp_node = l->head;

    // loops over the list
    while (temp_node != NULL){

        // creates a node that pionts to the next of current node
        node *next_node = temp_node->next;

        // frees the data in the current node using function
        freefunc(temp_node->data);

        // frees node
        free(temp_node);

        // sets current node to the next node
        temp_node = next_node;
    }

    // do this or should i use free(l)
    l->head = NULL;
    l->size = 0;

}

// traverses the list and applies the given function to the data at each node.
void ll_map(struct LinkedList *l, void (*mapfunc)(void *)){
    
    // makes sure that linkedlist is not empty and head is not empty
    if (l == NULL || l->head == NULL) {
        return;
    }

    // sets temp node to head node
    node *temp_node = l->head;

    // loops over the list and applies mapfunc to each element in the list
    while (temp_node != NULL) {
        
        mapfunc(temp_node->data);
        temp_node = temp_node->next;
    }

}

// removes the node at any given position in the list and returns its data
void *ll_delete(LinkedList *l, int index) {

    //  makes sure the index is valid
    if (index < 0 || index >= l->size) {
        return NULL;
    }

    // creates two pointers to loop through the index
    node *prev_node = NULL;
    node *current_node = l->head;

    // loops over the list till index
    for (int i = 0; i < index; i++) {
        prev_node = current_node;
        current_node = current_node->next;
    }
    // if node is head node
    if (prev_node == NULL) {
        l->head = current_node->next;
    // if any other node
    } else {
        prev_node->next = current_node->next;
    }

    // get data, free node, decrease size, and return data
    void *data = current_node->data;
    free(current_node);
    l->size--;
    return data;
}

// finds the first node in the list whose data matches target given the comparison function. Returns the pointer to the data if found, otherwise NULL.
void *ll_find(LinkedList *l, void *target, int (*compfunc)(void *, void *)) {
    // check if the list is empty
    if (l == NULL || l->head == NULL) {
        return NULL;
    }

    // loop through the list to find the target
    node *current_node = l->head;
    while (current_node != NULL) {
        if (compfunc(current_node->data, target) == 0) {
            return current_node->data;
        }
        current_node = current_node->next;
    }

    // if the target is not found
    return NULL;
}
