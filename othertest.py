from difflib import get_close_matches, SequenceMatcher
from utils import scoreObj
#print(SequenceMatcher(None, 'acad', 'academy').ratio())

a = scoreObj(1, "kwandong chall", "bruv")
b = scoreObj(1, "kwandong", "bruv")
c = scoreObj(1, "kwandong acedmy", "bruv")

print(a)
print(b)
print(c)