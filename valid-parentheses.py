class Solution:
  def isValid(self, s: list[str]) -> bool:
    stack: list[str] = []
    joinBrackets: dict[str, str] = {")": "(", "}": "{", "]": "["}

    for bracket in s:
      if bracket in joinBrackets:
        if stack and stack[-1] == joinBrackets[bracket]:
          stack.pop()
        else:
          return False
      else:
        stack.append(bracket)

    return bool(not stack)
