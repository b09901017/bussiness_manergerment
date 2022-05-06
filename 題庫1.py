A=float(input())

if A<=120:
    summer= A*2.1
    nonsummer= A*2.1
    #print('Summer months:',summer)
    #print('nonSummer months:',nonsummer)
if 121<=A and A<=330:
    summer=120*2.1+(A-120)*3.02 
    nonsummer=120*2.1+(A-120)*2.68 
    #print('Summer months:',summer)
    #print('nonSummer months:',nonsummer)
if 331<=A and A<=500:
    summer=120*2.1+210*3.02+(A-330)*4.39 
    nonsummer=120*2.1+210*2.68+(A-330)*3.61
    #print('Summer months:',summer)
    #print('nonSummer months:',nonsummer)
if 501<=A and A<=700:
    summer= 120*2.1+210*3.02+170*4.39+(A-500)*4.97
    nonsummer= 120*2.1+210*2.68+170*3.61+(A-500)*4.01
    print('Summer months:',summer)
    print('nonSummer months:',nonsummer)
if 701 <=A:
    summer=120*2.1+210*3.02+170*4.39+200*4.97+(A-700)*5.63
    nonsummer=  120*2.1+210*2.68+170*3.61+200*4.01+(A-700)*4.50
    #print('Summer months:',summer)
    #print('nonSummer months:',nonsummer)


print('Summer months:',summer)
print('nonSummer months:',nonsummer)



