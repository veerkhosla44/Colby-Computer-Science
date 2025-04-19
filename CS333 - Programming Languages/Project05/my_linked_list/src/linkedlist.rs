pub struct Node<T> {
    data: T,
    next: Option<Box<Node<T>>>,
}

pub struct LinkedList<T> {
    head: Option<Box<Node<T>>>,
    size: usize,
}

impl<T> LinkedList<T> {
    pub fn new() -> Self {
        LinkedList { head: None, size: 0 }
    }

    pub fn push(&mut self, data: T) {
        let new_node = Box::new(Node {
            data,
            next: self.head.take(),
        });
        self.head = Some(new_node);
        self.size += 1;
    }

    pub fn pop(&mut self) -> Option<T> {
        self.head.take().map(|node| {
            self.head = node.next;
            self.size -= 1;
            node.data
        })
    }

    pub fn append(&mut self, data: T) {
        let new_node = Box::new(Node { data, next: None });
        let mut cursor = &mut self.head;
    
        // Traverse to the end of the list
        while let Some(ref mut next) = *cursor {
            cursor = &mut next.next;
        }
    
        // Insert the new node at the end of the list
        *cursor = Some(new_node);
        self.size += 1;
    }
    

    pub fn find<F>(&self, mut f: F) -> Option<&T>
    where
        F: FnMut(&T) -> bool,
    {
        let mut cursor = &self.head;
        while let Some(ref node) = cursor {
            if f(&node.data) {
                return Some(&node.data);
            }
            cursor = &node.next;
        }
        None
    }

    pub fn size(&self) -> usize {
        self.size
    }

    pub fn clear(&mut self) {
        self.head = None;
        self.size = 0;
    }

    pub fn map<F>(&mut self, mut f: F)
    where
        F: FnMut(&mut T),
    {
        let mut cursor = &mut self.head;
        while let Some(ref mut node) = cursor {
            f(&mut node.data);
            cursor = &mut node.next;
        }
    }
}



