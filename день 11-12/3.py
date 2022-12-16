ignore = ["duplex", "alias", "configuration"]

with open("C:\\Users\\ks121masterov\\AppData\\Local\\Temp\\vmware-ks121masterov\\VMwareDnD\\91c5f668\\config_sw1.txt", 'r') as f:
    for line in f:
        for ignore_word in ignore:
            if ignore_word in line:
                ignore_use = 1
        if not line.startswith("!") and not ignore_use == 1:
            print(line.rstrip())
        ignore_use = 0