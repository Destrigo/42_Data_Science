def ft_filter(function, iterable):
    """
    function is what you need to find inside iterable
    """
    newlist = []

    if function is None:
        newlist = [x for x in iterable if x]
    else:
        newlist = [x for x in iterable if function(x)]
    return newlist
