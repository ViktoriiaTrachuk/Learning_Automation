#Option1 
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
print(correct_tail("Fox", "x"))

# #Option2
def correct_tail(body, tail):
    return tail == body[-len(tail):]
    
print(correct_tail("tree", "fox"))

# #Option3
def correct_tail(body, tail):
    return body.endswith(tail)
print(correct_tail("body", "tail"))

# #Option4

def correct_tail(body, tail):
    return body[-1] == tail
print(correct_tail("Fox", "x"))
