import random
from datetime import date

# only for inventory table
a = [i for i in range(60, 300)]
b = [i for i in range(65, 65 + 26)]
c = [i for i in range(2000, 2025)]
f = [i for i in range(1, 30)]
d = [i for i in range(1, 13)]
# for i in range(20):
#     k = "'" + chr(random.choice(b)) + chr(random.choice(b)) + "'"
#     print("(", i, ", ", k, ", ", random.choice(a), ", ", random.choice(a), ", ", random.choice(a), ", ",random.choice(a), ", ",
#           "'" + str(date(random.choice(c), random.choice(d), random.choice(f))) + "'", ", ",
#           "'" + str(date(random.choice(c), random.choice(d), random.choice(f))) + "'", ")", end=',\n')
for i in range(20):
    k = "'" + chr(random.choice(b)) + chr(random.choice(b)) + "'"
    print("(", i, ","
            "'" + str(date(random.choice(c), random.choice(d), random.choice(f))) + "'",", ",
          random.choice(a), ", ",
          k,", ",
          random.choice(a), ", ",
          random.choice(a), ", ",
          random.choice(a), ", ",
          random.choice(a),
          ")",
        end=',\n')
