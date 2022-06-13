c = [2, -3, 5]
def bep(lt):   
    coeffs = [str(item) for item in lt]
    equat = f"{coeffs[0]}*x**{len(coeffs)-1}"
    for i in range(1, len(coeffs)):
        if coeffs[i][0] != '-':
            coeffs[i] = f"+{coeffs[i]}"
    for i in range(1, len(coeffs)-2):
        equat += f"{coeffs[i]}*x**{len(coeffs)-i-1}"
    equat += f"{coeffs[-2]}*x{coeffs[-1]}"
    print(equat)
    x=2
    print(eval(equat))

s1 = [1,3]
s2 = [1,-3]
res = [0]*(len(s1)+len(s2)-1)
for o1,i1 in enumerate(s1):
    for o2,i2 in enumerate(s2):
        res[o1+o2] += i1*i2
print(res)