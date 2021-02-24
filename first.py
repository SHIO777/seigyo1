import webiopi


webiopi.setDebug()

@webiopi.macro
def recieve(val):
    """
    flowchart
    file  open
    file >> val write
    file save
    file close
    """
    webiopi.debug(val)
    path = "/home/pi/first.txt"
    f = open(path, "w")
    f.write(val)
    f.close()

