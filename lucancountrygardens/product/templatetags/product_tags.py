from django import template

register = template.Library()

@register.filter
def partition(lst, n):
    """
    Break a list into ``n`` lists, typically for use in columns.

    >>> lst = range(10)
    >>> for list in partition(lst, 3):
    ...     list
    [0, 1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    
    >>> lst = range(26)
    >>> for list in partition(lst, 5):
    ...     list     
    [0, 1, 2, 3, 4, 5]
    [6, 7, 8, 9, 10]
    [11, 12, 13, 14, 15]
    [16, 17, 18, 19, 20]
    [21, 22, 23, 24, 25]
    """
    try:
        n = int(n)
        lst = list(lst)
    except (ValueError, TypeError):
        raise StopIteration()
    
    start = 0
    for i in xrange(n):
        stop = start + len(lst[i::n])
        yield lst[start:stop]
        start = stop

@register.filter
def partition_horizontal(lst, n):
    """
    Break a list into groups of ``n`` pieces each.
    
    >>> partition_horizontal(range(10), 3)    
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    This allows the groups to be stacked horizontally:
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8],
     [9]]
    """
    try:
        n = int(n)
        lst = list(lst)
    except (ValueError, TypeError):
        return [lst]

    # Taken from http://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
    return [lst[i:i+n] for i in range(0, len(lst), n)]

