import random
def roll(getal):
    dobbelstenen_rollen = []
    while len(dobbelstenen_rollen) < getal:
        number_of_throws = random.randint (1,6)
        dobbelstenen_rollen.append(number_of_throws)

    print(dobbelstenen_rollen)

def main():
    getal = int(input('Geef een positief getal'))
    roll(getal)
main()        
        
