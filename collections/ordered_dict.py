from collections import OrderedDict

o = OrderedDict()
o['rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)
o.move_to_end('rolf');
print(o)
