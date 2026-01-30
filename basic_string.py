text = "Hello World"
print(text)
text = 'Hello World 2'
print(text[4])
print(len(text))
text = ""
print(len(text))
text = "Bob"
print(text[-1])
print(text[-2])
print(text[-3])

s1 = "hello"
s2 = "bye"
print(s1 + s2)
print(s1*4)
s1 = "hello my name is bob"
for c in s1:
    print(c)

s1 = "I like to give high fives"
s1_new = ""
for c in s1:
    if c == "i":
        s1_new += "y "
    elif c == "I":
        s1_new += "Y"
    else:
        s1_new = s1_new + c
