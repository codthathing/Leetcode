def reverseList(head):
  currentNode = head
  prevNode = None

  while currentNode:
    nextNode = currentNode.next
    currentNode.next = prevNode
    prevNode = currentNode
    currentNode = nextNode

  return prevNode