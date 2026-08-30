class MyLinkedList:

    class NewNode:
        def __init__(self, value: int) -> None:
            self.value: int = value
            self.next: MyLinkedList.NewNode | None = None

    def __init__(self) -> None:
        self.head: MyLinkedList.NewNode | None = None
        self.count = 0

    def get(self, index: int) -> int | None:
        if self.head and index <= self.count - 1:
            temp: MyLinkedList.NewNode | None = self.head

            for _ in range(index):
                if temp:
                    temp = temp.next
            if temp:
                return temp.value
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        newNode: MyLinkedList.NewNode = self.NewNode(val)

        newNode.next = self.head
        self.head = newNode

        self.count += 1
        

    def addAtTail(self, val: int) -> None:
        newNode: MyLinkedList.NewNode = self.NewNode(val)

        if not self.head:
            self.head = newNode
        else:
            temp: MyLinkedList.NewNode = self.head

            while temp.next:
                temp = temp.next
            temp.next = newNode

        self.count += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return

        if index == self.count:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = self.NewNode(val)

            temp: MyLinkedList.NewNode | None = self.head

            for _ in range(index - 1):
                if temp:
                    temp = temp.next

            if temp:
                newNode.next = temp.next
                temp.next = newNode
                self.count += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        
        temp: MyLinkedList.NewNode | None = self.head

        if index == 0 and temp:
            self.head = temp.next
        elif index == self.count - 1:
            for _ in range(index - 1):
                if temp:
                    temp = temp.next
            if temp:
                temp.next = None
        else:
            for _ in range(index - 1):
                if temp:
                    temp = temp.next
            if temp and temp.next:
                temp.next = temp.next.next


        self.count -= 1