debugVar = True

def error(msg):
    if msg == None:
        return
    print("\nErro: " + msg)

def debug(msg):
    if msg == None or debugVar == False:
        return
    print("\nDebug: " + msg)