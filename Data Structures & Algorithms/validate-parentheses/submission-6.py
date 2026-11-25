class Solution:
    def isValid(self, s: str) -> bool:
        #use a stack -> push openings onto stack
        #if its a closing -> pop off of stack

        stack = []

        for i in s: 
            if i in '{[(' : 
                stack.append(i)

            else:
                if not stack:
                    return False
                popped = stack.pop()

                if i == ")" and popped != "(":
                    return False
                if i == "]" and popped != "[":
                    return False
                if i == "}" and popped != "{":
                    return False

        return not stack
                