import time
import random
FlyingLong = ["albatross", "crane", "flamingo", "pelican", "crane fly", "dragonfly", "jacana", "ibex", "bat", "flying squirrel"] # Set of animals

FlyingShort = ["Hummingbird", "Bumblebee", "Swallow ", "Dragonfly ", "Finch", "Chickadee", "Moth", "Kingfisher", "Nighthawk", "Pipistrelle Bat"] # Set of animals

NonLong = ["Giraffe", "Camel", "Ostrich", "Gazelle", "Horse ", "Kangaroo", "Elephant", "Moose", "Llama", "Elk"] # Set of animals

NonShort = ["Dachshund", "Corgi", "Penguin", "Turtle", "Hedgehog", "Bulldog", "Kangaroo Rat", "Pygmy Hippo", "Chinchilla", "Warthog"] # Set of animals

sFlyingLong = ["albatros", "grulla", "flamenco", "pelícano", "típula grulla", "libélula", "jacana", "íbice", "murciélago", "ardilla voladora"] # Set of animals

sFlyingShort = ["Colibrí", "Abejorro", "Golondrina", "Libélula", "Pinzón", "Carbonero", "Polilla", "Martín Pescador", "Choquete", "Murciélago Pipistrelle"] # Set of animals

sNonLong = ["Jirafa", "Camello", "Avestruz", "Gacela", "Caballo", "Canguro", "Elefante", "Alce", "Llama", "Venado"] # Set of animals 

sNonShort = ["Perro salchicha", "Corgi", "Pingüino", "Tortuga", "Erizo", "Bulldog", "Rata canguro", "Hipopótamo pigmeo", "Chinchilla", "Facoquero"] # Set of animals


def tf(): # this is the english version of the code
        global FlyingLong
        global FlyingShort
        global NonLong
        global NonShort
        while True:
                print("Welcome to your favorite animal picker!")
                print("""
        Please choose an option: 
                A) Flying Long Leg Animal
                B) Flying Short Leg Animal
                C) Non Flying Long Leg Animal
                D) Non Flying Short Leg Animal
                E) Quit
                                   """) #Chooses which set of lists to choose from
                user_input = str(input("(A,B,C,D,E) "))
                if user_input.upper() == "A": #If you picked A then you choose from the first list
                        for i in range(3):
                                print("Printing..")
                                time.sleep(2)
                        print(" ")
                        print("These are some flying long leg animals")
                        for animal in (FlyingLong):
                                print(animal)
                        print("")
                        one = input("Do you want to spin for your chosen animal?: Y or N ")
                        if one.upper() == "Y":
                                random_one = random.choice(FlyingLong)
                                for i in range(3):
                                        print("Spinning..")
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_one)
                        if one.upper() == "N":
                                print(" ")
                                
                elif user_input.upper() == "B":
                        for i in range(3):
                                print("Printing..")
                                time.sleep(2)
                        print(" ")
                        print("These are some flying short leg animals")
                        for animal in (FlyingShort):
                                print(animal)
                        print("")
                        two = input("Do you want to spin for your chosen animal?: Y or N ")
                        if two.upper() == "Y":
                                random_two = random.choice(FlyingShort)
                                for i in range(3):
                                        print("Spinning..")
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_two)
                        if two.upper() == "N":
                                print(" ")
                elif user_input.upper() == "C":
                        for i in range(3):
                                print("Printing..")
                                time.sleep(2)
                        print(" ")
                        print("These are some non flying long leg animals")
                        for animal in (NonLong):
                                print(animal)
                        print("")
                        three = input("Do you want to spin for your chosen animal?: Y or N ")
                        if three.upper() == "Y":
                                random_three = random.choice(NonLong)
                                for i in range(3):
                                        print("Spinning..")
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_three)
                        if three.upper() == "N":
                                print(" ")
                elif user_input.upper() == "D":
                        for i in range(3):
                                print("Printing..")
                                time.sleep(2)
                        print(" ")
                        print("These are some non flying short leg animals")
                        for animal in (NonShort):
                                print(animal)
                        print("")
                        four = input("Do you want to spin for your chosen animal?: Y or N ")
                        if four.upper() == "Y":
                                random_four = random.choice(NonShort)
                                for i in range(3):
                                        print("Spinning..")
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_four)
                        if four == "N":
                                print(" ")
                elif user_input.upper() == "E": #This is how you quit the game
                        print("Quitting...")
                        break
                else: #If you did not choose from A-E you will receive this message.
                        print("Invalid option. Try again.")

def ff(): #Spanish version
        global sFlyingLong
        global sFlyongShort
        global sNonLong
        global sNonShort
        while True:
                print("Bienvenido a tu recogedor de animales favorito!")
                print("""
        Por favor elige una opción:
               A) Animal volador de patas largas
                B) Animal volador de patas cortas
                C) Animal no volador de patas largas
                D) Animal no volador de patas cortas
                E) Renunciar
                                   """)
                user_input = str(input("(A,B,C,D,E) "))
                if user_input.upper() == "A":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales voladores de patas largas.")
                        for animal in (sFlyingLong):
                                print(animal)
                        print("")
                        one = input("¿Quieres girar para tu animal elegido?: Y or N ")
                        if one.upper() == "Y":
                                random_one = random.choice(sFlyingLong)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_one)
                        if one.upper() == "N":
                                print(" ")
                                
                elif user_input.upper() == "B":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales voladores de patas cortas.")
                        for animal in (sFlyingShort):
                                print(animal)
                        print("")
                        two = input("¿Quieres girar para tu animal elegido?: Y or N ")
                        if two.upper() == "Y":
                                random_two = random.choice(sFlyingShort)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_two)
                        if two.upper() == "N":
                                print(" ")
                elif user_input.upper() == "C":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales de patas largas que no vuelan.")
                        for animal in (sNonLong):
                                print(animal)
                        print("")
                        three = input("¿Quieres girar para tu animal elegido??: Y or N ")
                        if three.upper() == "Y":
                                random_three = random.choice(sNonLong)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_three)
                        if three.upper() == "N":
                                print(" ")
                elif user_input.upper() == "D":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales de patas cortas que no vuelan.")
                        for animal in (sNonShort):
                                print(animal)
                        print("")
                        four = input("¿Quieres girar para tu animal elegido?: Y or N ")
                        if four.upper() == "Y":
                                random_four = random.choice(sNonShort)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_four)
                        if four.upper() == "N":
                                print(" ")
                elif user_input.upper() == "E":
                        print("Dejar de fumar...")
                        break
                else:
                        print("Invalid option. Try again.")
def thef(language): #The actual function
        if language == "English": #If the user picked English, then they will do the project in english
                tf()
        elif language == "Spanish": #If the user picked Spanish, then they will do the project in spanish
                ff()
thef(input("What language do you what to do this in? English or Spanish ")) #The parameter
