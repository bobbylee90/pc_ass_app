class LinkedList():
    def __init__(self) -> None:
        self.head = None

    class Node:
        def __init__(self, val, next=None) -> None:
            self.val = val
            self.next = next

    def append(self, val):
        newnode = self.Node(val=val)
        if not self.head:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode

    def prepend(self, val):
        newnode = self.Node(val=val)
        if not self.head:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def remove(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return
        prev, temp = None, self.head

        while temp and temp.val != val:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
        

    def swap(self, valx, valy):
        if valx == valy:
            return
        prex = None
        currx = self.head
        while currx and currx.val != valx:
            prex = currx
            currx = currx.next

        prey = None
        curry = self.head
        while curry and curry.val != valy:
            prey = curry
            curry = curry.next
        if not curry or not currx:
            return
        
        if prex:
            prex.next = curry
        else:
            self.head = curry
        
        if prey:
            prey.next = currx
        else:
            self.head = currx

        temp = currx.next
        currx.next = curry.next
        curry.next = temp

    def update(self, index, newval):
        temp = self.head
        pos = 0
        while temp.next and pos != index:
            pos+=1
            temp = temp.next
        if pos == index:
            temp.val = newval


    def insert(self, val, index):
        newnode = self.Node(val=val)
        curr = self.head
        pos = 0
        if not self.head:
            self.head = newnode
        elif index == 0:
            self.prepend(val=val)
        else:
            while curr and pos+1 != index:
                pos += 1
                curr = curr.next
            if curr:
                newnode.next = curr.next
                curr.next = newnode

    def printelem(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp =temp.next
        print()

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head: self.Node = None
        self.size = 0

    class Node():
        def __init__(self, val, previous=None, next=None) -> None:
            self.val = val
            self.previous = previous
            self.next = next
        
        def get_next(self):
            return self.next
        
        def set_next(self, newnode):
            self.next = newnode

        def get_prev(self):
            return self.previous

        def set_prev(self, newnode):
            self.previous = newnode

        def get_val(self):
            return self.val
        
        def set_val(self, newval):
            self.val = newval

    def getsize(self):
        return self.size
    
    def append(self, newval):
        newnode = self.Node(val=newval)
        if not self.head:
            self.head = newnode
            self.size += 1
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        newnode.set_prev(newnode=temp)
        temp.set_next(newnode=newnode)
        self.size += 1
        
    
    def prepend(self, newval):
        newnode = self.Node(val=newval, next=self.head)
        if self.head:
            self.head.set_prev(newnode=newnode)
        self.head = newnode
        self.size += 1

    def remove(self, val):
        temp = self.head
        while temp:
            if temp.get_val() == val:
                nex = temp.get_next()
                pre = temp.get_prev()
                if nex:
                    nex.set_prev(newnode = pre)
                if pre:
                    pre.set_next(newnode = nex)
                else:
                    self.head = temp
                self.size -= 1
                return
            else:
                temp = temp.get_next()

    def printelem(self):
        temp = self.head
        while temp:
            if temp.get_prev():
                print(f"prev:[{temp.get_prev().val}]", end="|")
            print(f"curr:[{temp.val}]", end=" ")
            temp =temp.get_next()
        print()
        
if __name__ == "__main__":
    lllist = [1,2,3,4,5,6,7,8]
    dll = DoublyLinkedList()
    # for item in lllist:
    #     dll.append(item)
    #     # dll.prepend(newval=item)
    # dll.remove(val=5)
    # dll.printelem()
    ll = LinkedList()
    for item in lllist:
        ll.append(item)
    ll.printelem()
    ll.update(index=3, newval=100)
    ll.printelem()
    ll.prepend(val=1000)
    ll.printelem()
    ll.remove(val=1000)
    ll.printelem()
    ll.insert(val=600, index=6)
    ll.printelem()
    ll.remove(val=8)
    ll.printelem()
    ll.remove(val=100)
    ll.printelem()