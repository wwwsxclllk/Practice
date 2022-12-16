result = []
with open('C:\\Users\\ks121masterov\\AppData\\Local\Temp\\vmware-ks121masterov\VMwareDnD\\5fb9ef08\\CAM_table.txt', 'r') as f:
    for line in f:
        words = line.split()
        template = '{:15} {:15} {:15}'
        if words and words[0].isdigit():
            vlan, mac, _, ports = words
            result.append([int(vlan), mac, ports])
for vlan, mac, intf in sorted(result):
    print(f"{vlan:<9}{mac:20}{intf}")