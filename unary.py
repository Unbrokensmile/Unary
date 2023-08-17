import sys
import math
n = 0

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
print("Debug messages...", file=sys.stderr, flush=True)
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
b = ""
answer = ""
calculating = True
for i in message:
    b += format(ord(i), 'b').zfill(7)
number = 0
print("Debug:{}".format(message), file=sys.stderr, flush=True)
print("Debug:"+str(b), file=sys.stderr, flush=True)
l1=[]
for i in range(len(b)):
    if len(l1) == 0:
        l1.append(b[i])
    else:
        if b[i] == l1[-1][0]:
            l1[-1] += b[i]
        else:
            l1.append(b[i])
    
for i in l1:
    print(f"Debug:{i}", file=sys.stderr, flush=True)    
    if i[0] == "1":
        answer += "0 "
    else:
        answer += "00 "
    for j in range(len(i)):
        answer += "0"
    answer += " "


    

print(answer[:-1])
