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
        temp = self.head
        if not temp:
            return
        while temp:
            if temp.next and temp.next.val != val:
                temp = temp.next
            else:
                break
        if temp.val == val and temp.next:
            temp.next = temp.next.next

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

if __name__ == "__main__":
    lllist = [1,2,3,4,5,6,7,8]
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