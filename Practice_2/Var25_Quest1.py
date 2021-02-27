def f21(x):
    if(x[0] == 'org'):
        if(x[2] == 1994):
            return 5
        elif(x[2] == 2012):
            if(x[1] == 'ejs'):
                return 3
            elif(x[1] == 'edn'):
                return 4
        elif(x[2] == 2003):
            if(x[3] == 2002):
                return 2
            elif(x[3] == 1982):
                if(x[4] == 'scaml'):
                    return 0
                elif(x[4] == 'self'):
                    return 1
    elif(x[0] == 'css'):
        if(x[4] == 'scaml'):
            return 6
        elif(x[4] == 'self'):
            if(x[3] == 1982):
                if(x[1] == 'ejs'):
                    return 7
                elif(x[1] == 'edn'):
                    return 8
            elif(x[3] == 2002):
                if(x[2] == 2003):
                    return 9
                elif(x[2] == 2012):
                    return 10
                elif(x[2] == 1994):
                    return 11

f21(['org', 'edn', 2003, 2002, 'self'])
f21(['css', 'edn', 2003, 2002, 'self'])