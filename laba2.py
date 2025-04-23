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
    i=(sum_Nt(shifr, alfabet))/(len(shifr)*(len(shifr)-1))
    return i


def sum_Nt(shifr, alfabet):
    sum_all_Nt=0
    for i in alfabet:
        Nt=shifr.count(i)
        sum_all_Nt=sum_all_Nt+(Nt*(Nt-1))
    return sum_all_Nt


alphabet = "абвгдежзийклмнопрстуфхцчшщыьъэюя"
r2="лю"
r3="вес"
r4="поет"
r5="ключ"
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
text_shifrkey=shifr_Vigenera(alphabet, text_without_probelu, rkey)

i_for_text=obchislenna_I(text_without_probelu, alphabet)
i_for_2=obchislenna_I(text_shifr2, alphabet)
i_for_3=obchislenna_I(text_shifr3, alphabet)
i_for_4=obchislenna_I(text_shifr4, alphabet)
i_for_5=obchislenna_I(text_shifr5, alphabet)
i_for_key=obchislenna_I(text_shifrkey, alphabet)
print(i_for_text)
print(i_for_2)
print(i_for_3)
print(i_for_4)
print(i_for_5)
print(i_for_key)
with open("output.txt", "a", encoding="utf-8") as file_for_write:
    print("Текст с ключем лю", text_shifr2, file=file_for_write)
    print("Текст с ключем вес", text_shifr3, file=file_for_write)
    print("Текст с ключем поет", text_shifr4, file=file_for_write)
    print("Текст с ключем ключ", text_shifr5, file=file_for_write)
    print("Текст с ключем мандолинистка", text_shifrkey, file=file_for_write)
