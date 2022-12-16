access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}


def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    result = []
    for intf, vlan in intf_vlan_mapping.items():
        result.append(intf)
        for command in access_template:
            if command.endswith('access vlan'):
                result.append(' {} {}'.format(command, vlan))
            else:
                result.append(' {}'.format(command))
        if psecurity:
            result.extend(psecurity)
    return result


list = generate_access_config(access_config, access_mode_template)
print(list)

list = generate_access_config(access_config, access_mode_template, port_security_template)
print(list)