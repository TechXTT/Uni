markA = 1
markB = 2

def compareMarks(markA, markB):
    if markA is None and markB is None:
        return []
    elif markA is None:
        return [markB]
    elif markB is None:
        return [markA]
    
    if markA == markB:
        return [markA, markB]
    elif markA > markB:
        return [markA]
    else:
        return [markB]
    