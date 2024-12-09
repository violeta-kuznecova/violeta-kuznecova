import random
n = int(input("Cik reizes veikt kauliņu mešanu? "))

max_summa=0
for i in range(n):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"{i+1}. metiens: {dice1} un {dice2} -> Lielākais: {max(dice1, dice2)}, Summa: {dice1 + dice2}")

 
import random

def minet_skaidri():

    min_intervals = 1
    max_intervals = 100
    skaitlis = random.randint(min_intervals, max_intervals)
    
    print(f"Minēšanas intervāls: {min_intervals} līdz {max_intervals}")
    

    minēšanas_reizes = 0
    while True:
        lietotaja_ievade = int(input("Ievadiet savu minējumu: "))
        minēšanas_reizes += 1
        
        if lietotaja_ievade < skaitlis:
            print("Lielāks")
        elif lietotaja_ievade > skaitlis:
            print("Mazāks")
        else:
            print("Uzminēts!")
            break
    
    print(f"Minēšanas reižu skaits: {minēšanas_reizes}")

minet_skaidri()
