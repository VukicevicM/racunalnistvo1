#algoritem urejanja
import random
def urejanje(A, urejene = []):
    if len(A) == 1:
        urejene = [A[0]] + urejene 
        return urejene
    #kupcek plastenk oznacimo z A
    #kupcek bomo predstavili kot seznam
    B = []
    #vzamemo katerokoli plasatenko iz kupcka A
    a = random.choice(A)
    A.remove(a)
    while len(A) != 0: #ponavljamo korake dokler kupcek A ni prazen
        #vzamemo se eno poljubno plastenko iz kupcka A
        b = random.choice(A)
        A.remove(b)
        #tehtamo
        #tezjo plastenko dodamo v kupcek B
        if a > b:
            B.append(a)
            a = b
        else:
            B.append(b)
    #plastenko postavimo pred vse ostale plastenke
    urejene = [a] + urejene
    #Vse plastenke iz kupčka B prestavimo na kupček A in ponavljamo od drugega koraka naprej
    #dokler ni več nobene plastenke na kupčku A ali B.
    return urejanje(B, urejene)
    
        
        
print(urejanje([2,7,3,9,17]))