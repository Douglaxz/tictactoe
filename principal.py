import tictactoe
import forca
import pedrapapeltesoura
import adivinhacao

#chamando a função
print("\n")
print("----------SELECIONE O JOGO QUE VOCÊ QUER JOGAR----------")
print("( 1 ) Jogo da velha")
print("( 2 ) Forca")
print("( 3 ) Pedra/Papel/Tesoura")
print("( 4 ) Adivinhação de números")
print("--------------------------------------------------------")
print("\n")
jogo = int(input("Qual a sua opção? "))
print("\n")


match jogo:
    case 1: 
        tictactoe.jogodavelha()
    case 2: 
        forca.jogoforca()
    case 3: 
        pedrapapeltesoura.pedrapapeltesoura()
    case 4: 
        adivinhacao.jogoAdivinhacao()        
