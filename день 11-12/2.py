with open('C:\\Users\\ks121masterov\\AppData\\Local\\Temp\\vmware-ks121masterov\\VMwareDnD\\91c5f668\\config_sw1.txt', 'r') as f:
    for line in f:
        if '!' in line:
            continue
        else:
            print (line.rstrip('\n'))