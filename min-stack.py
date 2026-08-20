class MinStack:
  def __init__(self) -> None:
    self.stack: list[str] = []

  def push(self, val: str) -> None:
    self.stack.append(val)
  def pop(self) -> None:
    if self.stack:
      self.stack.pop()
  def top(self) -> str | None:
    if self.stack:
      return self.stack[-1]
  def getMin(self) -> str | None:
    if self.stack:
      return min(self.stack)
        
minStackObject = MinStack()
minStackObject.push("d")
