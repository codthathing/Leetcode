class ListNode:
  def __init__(self, val:int=0, next: None=None) -> None:
    self.val: int = val
    self.next: ListNode | None = next

class Solution:
  def reverseList(self, head: ListNode) -> None | ListNode:
    currentNode: ListNode | None = head
    prevNode = None

    while currentNode:
      nextNode: ListNode | None = currentNode.next
      currentNode.next = prevNode
      prevNode: ListNode| None = currentNode
      currentNode = nextNode

    return prevNode