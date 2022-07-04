# Reverse String with while loop
def reverse(txt, start, end):
    while start < end:
        txt[start], txt[end] = txt[end], txt[start]
        start += 1
        end -= 1
    return txt

text = list('where is it')
reverse(text, 0, len(text)-1)

# reverse with recursion
def reverse_recursion(txt, start, end):
    if start >= end:
        print(txt)
        return
    txt[start], txt[end] = txt[end], txt[start]
    reverse_recursion(txt, start+1, end-1)
text = list('mace')
reverse_recursion(text, 0, len(text)-1)