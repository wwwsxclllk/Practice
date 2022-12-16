
def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as config:
        interface_access = {}
        interface_trunk = {}
        for line in config:
            if line.startswith('interface'):
                iface = line.split()[-1].rstrip()
            if 'switchport access vlan' in line:
                vlan = line.split()[-1].rstrip()
                interface_access[iface] = vlan
            elif 'switchport mode access' in line:
                vlan = '1'
                interface_access[iface] = vlan
            elif 'switchport trunk allowed vlan' in line:
                vlan = (line.split()[-1].rstrip().split(','))
                for vid in vlan:
                    interface_trunk.setdefault(iface, []).append(int(vid))


    return (interface_access, interface_trunk)

for i in get_int_vlan_map('config_sw2.txt'):
    print(i)