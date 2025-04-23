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
with open("output.txt", "a", encoding="utf-8") as file_for_write:
    print("Текст с ключем лю", shifr_Vigenera(alphabet, text_without_probelu, r2), file=file_for_write)
    print("Текст с ключем вес", shifr_Vigenera(alphabet, text_without_probelu, r3), file=file_for_write)
    print("Текст с ключем поет", shifr_Vigenera(alphabet, text_without_probelu, r4), file=file_for_write)
    print("Текст с ключем ключ", shifr_Vigenera(alphabet, text_without_probelu, r5), file=file_for_write)
    print("Текст с ключем мандолинистка", shifr_Vigenera(alphabet, text_without_probelu, rkey), file=file_for_write)
