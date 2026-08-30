class ListNode:
    def __init__(self, val: int = 0, next: None = None) -> None:
        self.val: int = val
        self.next: None | ListNode = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        tempOne: ListNode | None = list1
        tempTwo: ListNode | None = list2
        head: ListNode | None = None
        temp: ListNode | None = None

        while tempOne or tempTwo:
            if tempOne and tempTwo:
                if tempOne.val <= tempTwo.val:
                    nextNode = tempOne
                    tempOne = tempOne.next
                else:
                    nextNode = tempTwo
                    tempTwo = tempTwo.next
            elif tempOne:
                nextNode = tempOne
                tempOne = tempOne.next
            elif tempTwo:
                nextNode = tempTwo
                tempTwo = tempTwo.next
            else:
                nextNode = None

            if head is None:
                head = temp = nextNode
            else:
                if temp:
                    temp.next = nextNode
                    temp = nextNode

        if temp is not None:
            temp.next = None

        return head