stack = []
queue = []
top = -1
rear = -1
front = -1
text = input("Enter the String: ")
size = len(text)
for char in text:
    if len(stack) == size:
        print("The stack is full.")
    else:
        stack.append(char)
        top += 1
    if rear == (size - 1):
        print("The queue is full.")
    else:
        queue.append(char)
if size % 2 == 0:
    c = len(text)
else:
    c = (len(text) // 2) + 1
is_palindrome = True
for x in range(c):
    if top == -1:
        print("The stack is empty.")
    else:
        data = stack.pop()
        top -= 1
    if rear == top == -1:
        print("The queue is empty.")
    else:
        data_ = queue.pop(0)
    if data == data_:
        is_palindrome = True
    else:
        is_palindrome = False
        break
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
