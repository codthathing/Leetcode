class MyLinkedList(object):

    class NewNode():
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.count = 0

    def get(self, index):
        if self.head and index <= self.count - 1:
            temp = self.head

            for i in range(index):
                temp = temp.next
            
            return temp.value
        else:
            return -1
        

    def addAtHead(self, val):
        newNode = self.NewNode(val)

        newNode.next = self.head
        self.head = newNode

        self.count += 1
        

    def addAtTail(self, val):
        newNode = self.NewNode(val)

        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

        self.count += 1
        

    def addAtIndex(self, index, val):
        if index > self.count:
            return

        if index == self.count:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = self.NewNode(val)

            temp = self.head

            for i in range(index - 1):
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode
            self.count += 1

        

    def deleteAtIndex(self, index):
        if index >= self.count:
            return
        
        temp = self.head

        if index == 0:
            self.head = self.head.next
        elif index == self.count - 1:
            for i in range(index - 1):
                temp = temp.next
            temp.next = None
        else:
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next


        self.count -= 1