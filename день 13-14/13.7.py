ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    return any(word in command for word in ignore)
def convert_config_to_dict(config_filename):
    config_dict = {}
    with open(config_filename, 'r') as config:
        for line in config:
            if ignore_command(line, ignore) or line.startswith('!'):
                pass
            else:
                if not line.startswith(' '):
                    parent_key = line.strip()
                    config_dict.setdefault(line.strip(), [])
                else:
                    config_dict[parent_key].append(line.strip())
    return config_dict
for k, v in convert_config_to_dict('C:\\Users\\ks121masterov\\untitled1\\день 13-14\\config_sw1.txt').items():
    print(k,v)