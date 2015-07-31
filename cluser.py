import json

def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x
    return dict(map(ascii_encode, pair) for pair in data.items())

f = open('text.txt', 'r')
jstring=f.read();
f.close()

data=json.loads(jstring,object_hook=ascii_encode_dict)
print(data[1])