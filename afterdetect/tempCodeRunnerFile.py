import re
match = re.search(r'exp(\d+)', data)
numplusone = 0
if match:
    # Extract the number
    nump