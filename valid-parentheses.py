class Solution(object):
  def isValid(self, s):
    stack = []
    joinBrackets = {")": "(", "}": "{", "]": "["}

    for bracket in s:
      if bracket in joinBrackets:
        if stack and stack[-1] == joinBrackets[bracket]:
          stack.pop()
        else:
          return False
      else:
        stack.append(bracket)

    return True if not stack else False
