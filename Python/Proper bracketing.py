s = input()
stack = []
for c in s:
    if c in "([{":
        stack.append(c)
    elif c in ")]}":
        if not stack:
            print("False")
            break
        if c == ")" and stack[-1] != "(":
            print("False")
            break
        elif c == "]" and stack[-1] != "[":
            print("False")
            break
        elif c == "}" and stack[-1] != "{":
            print("False")
            break
        stack.pop()
else:
    print("True" if not stack else "False")