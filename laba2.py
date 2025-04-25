import re



def shifr_Vigenera(alpabet, text, key):
    key=masive_for_shifr_Vigenera(alphabet, key)
    text_numeration=masive_for_shifr_Vigenera(alpabet, text)
    text_after_shifr=""
    long_key=len(key)
    long_alpabet=len(alpabet)
    for i in range(len(text)):
        our_chislo=(text_numeration[i]+key[i%long_key])%long_alpabet
        text_after_shifr+=alpabet[our_chislo]

    return text_after_shifr

def delete_fromtext_probel(text):
    text_without_probels=re.sub(r"\s+", "", text)
    return text_without_probels

def masive_for_shifr_Vigenera(alphabet, key):
    arr=[]
    for i in range(len(key)):
        for j in range(len(alphabet)):
            if key[i]==alphabet[j]:
                arr.append(j)
                break

    return arr

def obchislenna_I(shifr, alfabet):
    if len(shifr)<=1:
        return 0
    i=(sum_Nt(shifr, alfabet))/(len(shifr)*(len(shifr)-1))
    return i


def sum_Nt(shifr, alfabet):
    sum_all_Nt=0
    for i in alfabet:
        Nt=shifr.count(i)
        sum_all_Nt=sum_all_Nt+(Nt*(Nt-1))
    return sum_all_Nt



def rozbitie_na_bloki(text, r):
    y_bloks=['' for _ in range(r)]
    for i in range(len(text)):
        y_bloks[i%r]+=text[i]
    return y_bloks

def index_for_all_blok(y_bloks, r, alphabet):
    fine=0
    for i in range(r):
        j=obchislenna_I(y_bloks[i], alphabet)
        fine+=j

    fine= fine/r
    return fine


def look_for_r(text, alphabet, i_glavn):
    for r in range(2, 31):
        y_bloks=rozbitie_na_bloki(text, r)
        i=index_for_all_blok(y_bloks, r, alphabet)
        if abs(i_glavn-i)<=0.003:
            return r
        
    return 0

def look_for_bukbi(text, r, alphabet):
    y_bloks=rozbitie_na_bloki(text, r)
    key=''
    for i in range(r):
        coluchestvo=[]
        for j in range(len(alphabet)):
            coluchestvo.append(y_bloks[i].count(alphabet[j]))
        max=coluchestvo[0]
        k=0
        for i in range(len(coluchestvo)):
            if max<coluchestvo[i]:
                max=coluchestvo[i]
                k=i
        if k<14:
            index_literi=32-(14-k)
        else:
            index_literi=k-14
        key+=alphabet[index_literi]


    return key

def Mg(p, t, text, alphabet):
    m=0
    for i in range(len(alphabet)):
        k=(i+t)%32
        h=p[i]*text.count(alphabet[k])
        m+=h
    return m


def key_with_Mi(text, r, alphabet, p):
    y_bloks=rozbitie_na_bloki(text, r)
    key=[]
    key_slovo=''
    for i in range(r):
        mg=[]
        for j in range(len(alphabet)):
            mg.append(Mg(p, j, y_bloks[i], alphabet))
        max=mg[0]
        k=0
        for j in range(len(alphabet)):
            if max<mg[j]:
                max=mg[j]
                k=j
        key.append(k)
        key_slovo+=alphabet[k]

    return key, key_slovo

def lomaem(shifr, key, alphabet):
    shifr_cifri=[]
    for i in range(len(shifr)):
        for j in range(len(alphabet)):
            if shifr[i]==alphabet[j]:
                shifr_cifri.append(j)
                j=len(alphabet)+8

    text=''
    n=len(key)
    for i in range(len(shifr_cifri)):
        if shifr_cifri[i]<key[i%n]:
            h=alphabet[32-(key[i%n]-shifr_cifri[i])]
        else:
            h=alphabet[shifr_cifri[i]-key[i%n]]
        text+=h
    return text


alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
p_bukov=[0.06900999295937144, 0.015628420473437897, 0.03790106437737769, 0.013323945828575486, 0.024170359545376555, 
        0.09504848567320834, 0.008367402481377833, 0.015646169957223743 , 0.054143321165076114, 0.012520781687265928, 
        0.027418515078186476,  0.04142137866157059, 0.026655287275395075, 0.05503819097261255, 0.09504848567320834, 
        0.024762009004904773, 0.03666895437791018, 0.0445822658991001, 0.04966009738550104, 0.024730947408279542, 
          0.0011640703116217704, 0.006965193262295955, 0.0023473692306782076, 0.012673131423094446, 0.007829001473207154, 
          0.003622373815961519, 0.016052928960649394,  0.019020051000183412, 0.00018489045610256834, 0.0024730947408279544 , 0.00524940982966412, 0.017571988947988094  ]


r2="лю"
r3="вес"
r4="поет"
r5="ключи"
rkey="мандолинистка"

with open("input.txt", "r", encoding="utf-8") as file:
    text_for_work = file.read()
with open("output.txt", "w"):
    pass 
text_without_probelu=delete_fromtext_probel(text_for_work)
text_shifr2=shifr_Vigenera(alphabet, text_without_probelu, r2)
text_shifr3=shifr_Vigenera(alphabet, text_without_probelu, r3)
text_shifr4=shifr_Vigenera(alphabet, text_without_probelu, r4)
text_shifr5=shifr_Vigenera(alphabet, text_without_probelu, r5)
text_shifrkey =shifr_Vigenera(alphabet, text_without_probelu, rkey)

i_for_text=obchislenna_I(text_without_probelu, alphabet)
i_for_2=obchislenna_I(text_shifr2, alphabet)
i_for_3=obchislenna_I(text_shifr3, alphabet)
i_for_4=obchislenna_I(text_shifr4, alphabet)
i_for_5=obchislenna_I(text_shifr5, alphabet)
i_for_key=obchislenna_I(text_shifrkey, alphabet)
i_0=0.0333
i_glavn=0.0553
r=look_for_r(text_shifrkey, alphabet, i_glavn)
print(look_for_r(text_shifrkey, alphabet, i_glavn))
print(look_for_bukbi(text_shifrkey, r, alphabet))
print(key_with_Mi(text_shifrkey, r, alphabet, p_bukov))
key, key_slovo=key_with_Mi(text_shifrkey, r, alphabet, p_bukov)
print(lomaem(text_shifrkey, key, alphabet))
'''print(i_for_text)
print(i_for_2)
print(i_for_3)
print(i_for_4)
print(i_for_5)
print(i_for_key)'''
with open("test.txt", "r", encoding="utf-8") as file:
    text_for_work = file.read()

text_without_probelu=delete_fromtext_probel(text_for_work)
r=look_for_r(text_without_probelu, alphabet, i_glavn)
print(look_for_r(text_without_probelu, alphabet, i_glavn))
print(look_for_bukbi(text_without_probelu, r, alphabet))
print(look_for_bukbi(text_without_probelu, r, alphabet))
print(key_with_Mi(text_without_probelu, r, alphabet, p_bukov))
key, key_slovo=key_with_Mi(text_without_probelu, r, alphabet, p_bukov)
print(lomaem(text_without_probelu, key, alphabet))
with open("output.txt", "a", encoding="utf-8") as file_for_write:
    print("Текст с ключем лю", text_shifr2, file=file_for_write)
    print("Текст с ключем вес", text_shifr3, file=file_for_write)
    print("Текст с ключем поет", text_shifr4, file=file_for_write)
    print("Текст с ключем ключ", text_shifr5, file=file_for_write)
    print("Текст с ключем мандолинистка", text_shifrkey, file=file_for_write)
    r=look_for_r(text_shifrkey, alphabet, i_glavn)
    print(look_for_r(text_shifrkey, alphabet, i_glavn), file=file_for_write)
    print(look_for_bukbi(text_shifrkey, r, alphabet), file=file_for_write)
    print(key_with_Mi(text_shifrkey, r, alphabet, p_bukov), file=file_for_write)
    key, key_slovo=key_with_Mi(text_shifrkey, r, alphabet, p_bukov)
    print(lomaem(text_shifrkey, key, alphabet), file=file_for_write)
    r=look_for_r(text_without_probelu, alphabet, i_glavn)
    print(look_for_r(text_without_probelu, alphabet, i_glavn), file=file_for_write)
    print(look_for_bukbi(text_without_probelu, r, alphabet), file=file_for_write)
    print(key_with_Mi(text_without_probelu, r, alphabet, p_bukov), file=file_for_write)
    key, key_slovo=key_with_Mi(text_without_probelu, r, alphabet, p_bukov)
    print(lomaem(text_without_probelu, key, alphabet), file=file_for_write)
