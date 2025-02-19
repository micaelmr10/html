
cpf=[0,8,3,2,4,6,8,8,5,1,0]
multi=cpf[0]*10,cpf[1]*9,cpf[2]*8,cpf[3]*7,cpf[4]*6,cpf[5]*5,cpf[6]*4,cpf[7]*3,cpf[8]*2
soma=sum (multi)
div1=soma%11
if (div1<0):
    p=0
else:
    p=11-div1
multi=cpf[0]*11,cpf[1]*10,cpf[2]*9,cpf[3]*8,cpf[4]*7,cpf[5]*6,cpf[6]*5,cpf[7]*4,cpf[8]*2
nsoma=sum(multi)
ndiv1=nsoma%11
if (ndiv1<2):
    pb=0
else:
    pb=11-ndiv1
# print(multi)
# print(soma)
# print(div1)
print(p)
print(pb)