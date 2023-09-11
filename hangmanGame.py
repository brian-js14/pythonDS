import random
import os

def read():

    with open("./data.txt", "r", encoding="utf-8") as f:
        data = [line.replace("\n", "") for line in f]
        tls = (('á','a'),('á','b'),('í','i'),('ó','o'),('ú','u'))
        random_word = random.choice(data)
        for a, b in tls:
            random_word = random_word.replace(a, b)

    return random_word
            

def run():
    word = read()
    tmp = list(enumerate(word))
    new_list = ['__' for i in range(0, len(word))]
    print("¡Adivina la palabra!" + 
          "\n" + "Tu palabra contiene: " + str(len(word)) + " letras")
    print(" ".join(new_list))
    
    while list(word.upper()) != new_list:
        letter = input("Ingresa una letra: ")
        for i, j in tmp:
           if letter == j:
               new_list[i] = letter.upper()
        
        os.system("clear")
        print(" ".join(new_list))
    
    print(f'Genial tu palabra era: { word.upper() }')

if __name__ == "__main__":
    run()