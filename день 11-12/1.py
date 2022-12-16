f= 'open(ospf.txt)'
for line in f:
    line = line.split()
    prefix = ""
    admetric = ""
    via = ""
    nexthop = ""
    lastupdate = ""
    interface = line
    template = '{:20} {:15}'
    print(template.format('Prefix',prefix))
    print(template.format('AD/Metric',admetric.strip('[]')))
    print(template.format('Next-Hop',nexthop.strip(',')))
    print(template.format('Last update ',lastupdate.strip(',')))
    print(template.format('Outbound Interface',interface))
    print("n")