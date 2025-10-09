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
            raise IndexError("Index out of range")
        
        current = self.head
        currentPos = 0

        while currentPos < pos:
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
            currentPos += 1
        if current is None:
            raise IndexError("Index out of range")
        current.value = value


    def __getitem__(self, pos):
        if pos < 0 or pos >= len(self):
            raise IndexError("Index out of range")
        
        current = self.head
        currentPos = 0

        while currentPos < pos:
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
            currentPos += 1
        if current is None:
            raise IndexError("Index out of range")
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
        # --- YOUR CODE STARTS HERE
        pass  # remove when starting implementation 


    def free(self):
        # --- YOUR CODE STARTS HERE
        pass  # remove when starting implementation 


    def realloc(self, size):
        # --- YOUR CODE STARTS HERE
        pass  # remove when starting implementation 



    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        # --- YOUR CODE STARTS HERE
        pass  # remove when starting implementation 
    


def run_tests():
    import doctest
    doctest.testmod(verbose=True)
     

if __name__ == "__main__":
     run_tests()