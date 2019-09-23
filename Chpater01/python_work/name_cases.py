famous = " \tSteve Jobs\n\tZhou Enlai "
print(famous)
print(famous.rstrip())
print(famous.lstrip())
print(famous.strip())

import re
regex = re.match(r"[a-z, A-Z]+ [a-z, A-Z]+' '+[a-z, A-Z]+ [a-z, A-Z]+", famous)
print(regex)


