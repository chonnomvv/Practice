import re

s ="""
<html>
<body style='background-color:#ffff'>
<h4>Click</h4>
<a href='http://www.python.org'>Here</a>
<p>
To connect to the most powerful tolls int the world.
</p>
</body>
</html>"""

body = re.sub('<.*?>','',s,0,re.I|re.S)

print(body)