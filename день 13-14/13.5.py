def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as config:
        LOX = {"FastEthernet0/12": 10,
        "FastEthernet0/14": 11,
        "FastEthernet0/16": 17}

        for line in config:
            if line.startswith('interface'):
                iface = line.split()[-1].rstrip()
            if 'switchport access vlan' in line:
                vlan = line.split()[-1].rstrip()
                LOX[iface] = vlan
            elif 'switchport mode access' in line:
                vlan = '1'
                LOX[iface] = vlan
            elif 'switchport trunk allowed vlan' in line:
                vlan = (line.split()[-1].rstrip().split(','))
                for vid in vlan:
                    LOX.setdefault(iface, []).append(int(vid))


    return (LOX)

for i in get_int_vlan_map('C:\\Users\\ks121masterov\\Desktop\\07_files\\config_sw1.txt'):
    print(i)