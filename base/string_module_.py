if __name__ == '__main__':
    s = "\nThe Quick brown "
    print(s)
    print(s.__str__())
    print(s.capitalize())
    # Capwords function is deprecated
    # print(string.capwords(s))
    lst = s.split(" ")
    print(lst)
    lst = " ".join(item.upper() for item in lst)
    print(lst)
    # print(type(lst))
    print(len(s))
    # leet = s.maketrans(s, '1234567890000')
    # print(s.translate(leet))
    sample_text = '''The textwrap module
    canbe
    used
    to
    format
    text
    for output in
        situations
        where
        pretty - printing is desired.It
        offers programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.'''
    import textwrap

    sample_text = textwrap.dedent(sample_text)
    print(textwrap.fill(sample_text, width=50))
    lst = [1,3]
    print(lst.pop)
