

#Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters.
#For example, given "hello/world:here", return "here/world:hello"


def relativeWord(S):
    assert len(S) > 0

    front, rest = S.split("/")
    mid, back = rest.split(":")
    
    return back + "/" + mid + ":" + front



print(relativeWord("hello/world:here"))



