# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:   # You are not allowed to modify this class
    def __init__(self, value=None):  
        self.next = None
        self.value = value
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__

class Malloc_Library:

    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst
        None -> None -> None -> None -> None
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.free()
        >>> temp.next is None
        True
    """

    def __init__(self): # You are not allowed to modify the constructor
        self.head = None
    
    def __repr__(self):  # You are not allowed to modify this method
        current = self.head
        out = []
        while current != None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__
    
    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    
    def __setitem__(self, pos, value):
        if pos < 0 or pos >= len(self):
            raise IndexError
        
        current = self.head
        currentPos = 0

        while currentPos < pos:
            if current is None:
                raise IndexError
            current = current.next
            currentPos += 1
        if current is None:
            raise IndexError
        current.value = value


    def __getitem__(self, pos):
        if pos < 0 or pos >= len(self):
            raise IndexError
        
        current = self.head
        currentPos = 0

        while currentPos < pos:
            if current is None:
                raise IndexError
            current = current.next
            currentPos += 1
        if current is None:
            raise IndexError
        return(current.value) 
    

    def malloc(self, size):
        self.head = None
        if size == 0:
            self.head = None
            return
        
        self.head = Node(None)
        current = self.head

        for i in range(size - 1):
            if current is not None: #just bc i hated seeing the warnings
                current.next = Node(None)
                current = current.next


    def calloc(self, size):
        self.head = None
        
        if size == 0:
            return
        
        self.head = Node(0)
        current = self.head

        for i in range(size - 1):
            if current is not None:
                current.next = Node(0)
                current = current.next


    def free(self):
        current = self.head

        while current is not None:
            nextNode = current.next
            current.next = None
            current = nextNode


    def realloc(self, size):
        if size == 0:
            self.free()
            return
        
        if self.head is None:
            self.malloc(size)
            return
        
        current_length = len(self)
        
        if size > current_length:
            # Add nodes to the end
            current = self.head
            while current.next is not None:
                current = current.next
            
            for i in range(size - current_length):
                current.next = Node(None)
                current = current.next
        
        elif size < current_length:
            # Remove nodes from the end
            current = self.head
            for i in range(size - 1):
                current = current.next
            
            current.next = None



    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        if self.head is None or pointer_2.head is None:
            return
        
        if ptr1_start_idx < 0 or ptr1_start_idx >= len(self):
            return
        if ptr2_start_idx < 0 or ptr2_start_idx >= len(pointer_2):
            return
        
        current_ptr1 = self.head
        current_ptr1Pos = 0
        
        while current_ptr1Pos < ptr1_start_idx:
            current_ptr1 = current_ptr1.next
            current_ptr1Pos += 1
        
        current_ptr2 = pointer_2.head
        current_ptr2Pos = 0
        
        while current_ptr2Pos < ptr2_start_idx:
            current_ptr2 = current_ptr2.next
            current_ptr2Pos += 1
        
        count = 0
        while count < size and current_ptr1 is not None and current_ptr2 is not None:
            current_ptr2.value = current_ptr1.value
            current_ptr1 = current_ptr1.next
            current_ptr2 = current_ptr2.next
            count += 1
        




def run_tests():
    import doctest
    doctest.testmod(verbose=False)
     

if __name__ == "__main__":
     run_tests()