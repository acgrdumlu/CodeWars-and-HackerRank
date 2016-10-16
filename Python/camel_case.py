import re

s = raw_input()
s = re.sub(r'([a-z]*)([A-Z])', r'\1 \2', s)
s = s.split()
print len(s)