from pathlib import Path
path = Path('index.html')
data = path.read_bytes()
print('size', len(data))
indexes = [i for i,b in enumerate(data) if b > 127]
print('nonascii count', len(indexes))
print('sample indexes', indexes[:20])
text = path.read_text('utf-8')
for i, line in enumerate(text.splitlines(), start=1):
    if any(ord(ch) > 127 for ch in line):
        print('line', i, repr(line))
