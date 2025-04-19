// Stack.java
// package cse41321.containers;

import java.util.NoSuchElementException;

public class Stack<E> {
    private SinglyLinkedList<E> list = new SinglyLinkedList<E>();

    public void push(E data) {
        list.insertHead(data);
    }

    public E pop() throws NoSuchElementException {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        return list.removeHead();
    }

    public E peek() throws NoSuchElementException {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        return list.getHead().getData();
    }

    public int getSize() {
        return list.getSize();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }
}
