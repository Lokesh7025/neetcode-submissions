class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            if ch in mapping:
                if not stack or stack[-1]!=mapping[ch]:
                    return False
                stack.pop()
        return len(stack)==0
        