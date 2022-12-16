trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    print(intf_vlan_mapping)
    print(trunk_template)
    trunk_conf = {}
    for intf, value in intf_vlan_mapping.items():
        trunk_conf[intf] = []
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vlans = ",".join([str(vl) for vl in value])
                trunk_conf[intf].append(f" {command} {vlans}")
            else:
                trunk_conf[intf].append(f" {command}")
    return trunk_conf
print(generate_trunk_config(trunk_config, trunk_mode_template))