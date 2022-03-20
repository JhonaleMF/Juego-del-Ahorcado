import easygui
from variables_ahorcado import message_instructions
from tkinter import messagebox
import string
import easygui
import sys

def start_game():
    """
    Función que da inicio al juego, primero el jugador ingresa el número de intentos a adivinar.
    Luego, al llamar la función 'inspeccionletter_word' el jugador ingresa la palabra para ser inspeccionada
    Al ser inspeccionada, la palabra con el número de intentos son parametros para la función 'juego_ahorcado'

    INPUT : No Aplica
             
    OUTPUT : -ingreso (str), luego se transforma a int
             -'inspeccionletter_word' (función), con la palabra a adivinar. Esta función tiene por default el valor True,
              ya que diferencia la palabra a ingresar con los demás inputs que se realizán durante el juego.
             -Ejecuta la función 'juego_ahorcado' con los parametro mencionados (ingreso y la palabra adivinar de la función 'inspeccionletter_word')
    """

    while True:        
        ingreso = easygui.enterbox("Ingrese el número de intentos para adivinar la palabra: ")

        if ingreso in [".", None]:#Verifica que no hayan puntos, ni valores None en el input
            messagebox.showinfo(message="Ingrese un valor númerico entero:", title="ERROR")  
            continue
        else:
            try: #Verifica que no hayan valores en el input ingresado que no puedan convertirse a entero, como por ejemplo caracteres especiales, letras.
                ingreso = int(ingreso)
            except:
                messagebox.showinfo(message="Ingrese un valor númerico entero:", title="ERROR")   
                continue

        break
    juego_ahorcado(inspeccionletter_word(True), ingreso) #Primero ejecuta la función para ingresar la palabra a adivinar para llamar la función 'juego_ahorcado'

def instructions():
    """
    Ejecuta la variable message_instructions  del script 'variables_ahorcado.py'
    OUTPUT: messagebox(str)
    """
    messagebox.showinfo(message= message_instructions  , title="Instrucciones")

def exit_game():   
    """
    Al llamar dicha función, deja de ejecutar el menú del juego
    OUTPUT: sys(exit)  
    """ 
    sys.exit("Exit")    

def progress():
    """
    Imprime el progreso de la palabra a adivinar, es decir, los espacios de las letras acertadas.
    OUTPUT: messagebox(str) 
    """ 
    try:
        print("Progreso palabra a adivinar:", " ".join(list_game))
    except:
        print("No has iniciado el juego")
        messagebox.showinfo(message= "No has iniciado el juego"  , title="ERROR")


def juego_ahorcado(palabra_a_adivinaru1, n_intentos):    
    """
    Convierte cada una de las letras de la palabra a adivinar en '_' 
    INPUT: palabra_a_adivinaru1 (str) palabra a adivinar
           n_intentos (int) número de intentos para adivinar la palabra
    OUTPUT: Diferentes prints y messagebox.showinfo que informan si el jugador acierta la letra o palabra completa, perdió, ganó y 
           pogreso de la palabra.
    """ 
    palabras_select = []  
    global list_game
    list_game = palabra_escondida(palabra_a_adivinaru1)
    
    while n_intentos > 0:       
       
        letra_user2 = inspeccionletter_word()    
        if len(letra_user2) > 1:
            if palabra_a_adivinaru1 == letra_user2: #Compara si el jugador ingresa una palabra completa para adivinar la palabra escondida
                for index, letter in enumerate(palabra_a_adivinaru1):        
                    if letter == letra_user2[index]:
                        list_game[index] = letter
                print("You win!:", (" ".join(list_game)))
                messagebox.showinfo(message=("You win!:", (" ".join(list_game))), title="WINNER")
                break   
            else:
                n_intentos -= 1
                print(f"Te equivocaste. {letra_user2}, no es la palabra a adivinar", (" ".join(list_game)), f". Tienes {n_intentos} intento(s)")
                messagebox.showinfo(message=(f"Te equivocaste. {letra_user2}, no es la palabra a adivinar", (" ".join(list_game)), f". Tienes {n_intentos} intento(s)"), title="YOU MISS")
                continue    
                    
        if letra_user2 not in palabras_select and letra_user2 not in palabra_a_adivinaru1:# No acierta la letra ingresada, menos intentos
            palabras_select.append(letra_user2)
            n_intentos -= 1
            print(f"Te equivocaste.Tienes {n_intentos} intentos")
            messagebox.showinfo(message=f"Te equivocaste.Tienes {n_intentos} intentos", title="YOU MISS")
            
        elif letra_user2 in palabras_select and letra_user2 not in palabra_a_adivinaru1: #Compara si la letra ya si ingreso anteriormente
            print(f"Ya habias ingresado la letra {letra_user2} -->", (" ".join(palabras_select)), " Ingrese otra por favor")
            messagebox.showinfo(message=(f"Ya habias ingresado la letra {letra_user2} -->", (" ".join(palabras_select)), " Ingrese otra por favor"), title="ERROR")
            continue       
        else:
            if letra_user2 in list_game: #Compara si la letra con la que se habia ancertado anteriormente ha sido ingresada
                print(f"Ya habias acertado con la letra {letter} -->", (" ".join(list_game)), "Ingrese otra por favor")
                messagebox.showinfo(message=(f"Ya habias acertado con la letra {letter} -->", (" ".join(list_game)), "Ingrese otra por favor"), title="ERROR")
                continue

            print("Acertaste")   
            messagebox.showinfo(message="Acertaste", title="YOU HIT")   
            for index, letter in enumerate(palabra_a_adivinaru1):        
                if letter == letra_user2:
                    list_game[index] = letter

            if not "_" in list_game:
                print("You win!:", (" ".join(list_game)))
                messagebox.showinfo(message=("You win!:", (" ".join(list_game))), title="WINNER")                
                break         
            
        print("Progreso palabra a adivinar:", " ".join(list_game))
        messagebox.showinfo(message=("Progreso palabra a adivinar:", " ".join(list_game)), title="PALABRA")   

    else:
        print(f"Perdiste!. Palabra ingresada: {palabra_a_adivinaru1}")
        messagebox.showinfo(message=f"Perdiste!. Palabra ingresada: {palabra_a_adivinaru1}", title="LOSER")   

def palabra_escondida(palabra_a):    
    """
    Convierte cada una de las letras de la palabra a adivinar en '_' 
    INPUT: palabra_a (str) palabra a adivinar
    OUTPUT: list_g (list) palabra a adivinar transformada
    """ 
    list_g = []    
    for i in palabra_a:
        list_g.append("_")
    print("Palabra a adivinar:", " ".join(list_g))
    messagebox.showinfo(message=("Palabra a adivinar:", " ".join(list_g)), title="PALABRA A ADIVINAR")
    return list_g   

def inspeccionletter_word(word = False):
    """
    Inspecciona las letras y palabras ingresadas, es decir, que no contengan ningún carácter especial, espacio en blanco o valor tipo None. 
    INPUT: (boolean) valor por default, False, que hace referencia al input de la letra o la palabra completa a adivinar, y
            True, para ingresar la palabra a adivinar
    OUTPUT: ingreso(str), palabra o letra ingresada e inspeccionada.
    """ 
    alphabets = list(string.ascii_letters)
    while True:
       
        if word == True:  #Ingresar palabra a adivinar
            ingreso = easygui.enterbox("Ingresar palabra a adivinar: ")    
                  
        else:  #Ingresar letra o palabra completa para adivinar la palabra escondida
            ingreso = easygui.enterbox("Ingrese letra o si sabes la palabra completa, ingresala: ")

        if ingreso == None: # Validad que no haya valores None
            print("Ingrese de nuevo")
            continue  

        if ingreso == "": # Validad que no haya espacios vacios
            print("Valor ingresado vacío. Ingrese de nuevo")
            messagebox.showinfo(message="Valor ingresado vacío. Ingrese de nuevo", title="ERROR")
            continue
        
        for letra in ingreso:
            if letra not in alphabets:                
                inspeccion = False
                
            else:
                inspeccion = True

        if inspeccion == False:
            print("Valor contiene algún caracter especial o es un espacio. Ingrese de nuevo")
            messagebox.showinfo(message="Valor contiene algún caracter especial o es un espacio. Ingrese de nuevo", title="ERROR")
            continue  
       
        break           
    return ingreso.upper()

