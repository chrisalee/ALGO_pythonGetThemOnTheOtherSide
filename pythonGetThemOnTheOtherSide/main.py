# Using only +, -, \times, \div,+,−,×,÷, and/or ||∣∣ symbols, which value, if any, is not possible on the right-hand side of the equation?

# The || operator strings digits together. For example, 3 || 4 = 34.

# 1
# 2
# 4
# 8
# 16
# =
# 13

l=[" + "," - "," * "," / ",""]
r=[1,2,4,8,16]
s=[[],[],[],[],[]]
for i in l:
    for j in l:
        for k in l:
            for m in l:
                x="1"+i+"2"+j+"4"+k+"8"+m+"16"
                y=eval(x)
                if y in r:
                    s[r.index(y)].append(x+" = "+str(int(y)))
for i in s:
    for j in i:
        print(j)
    print('_'*25)