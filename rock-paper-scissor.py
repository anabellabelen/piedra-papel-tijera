import random
f= open (" puntaje.txt","a" , enconding= "utf8")
for i in range (1,4):
    user_action=input("seleccione (piedra-papel-tijera)")
    possible_actions=["piedra","papel","tijera"]
    computer_action=random.choice(possible_actions)
  #  print(computer_action)
    print("\n Tú elegiste:",user_action, ", la computadora eligió:",computer_action,"\n") 
    if  user_action == computer_action:
        print("empate!",user_action,". ambos ganaron!")
        f.write(" empate!",user_action,".ambos ganaron!")
    elif user_action=="piedra" and computer_action=="papel"
       print ("gano la computadora .\n")
       f. write("gano la computadora .\n" )
    elif user_action==" papel" and computer_action== " tijera"
       print (" gano la computadora.\n")
       f.write (" gano la computadora.\n")
    elif user_action=="papel"  and computer_action== "piedra "
       print ("gane yo.\n")
       f.write("gane yo.\n")
    elif user_action== "tijera" and computer_action== "piedra" 
       print( gano la computadora.\n")
       f.write( gano la computadora.\n")
    elif user_action== " piedra" and computer_action==" papel"
       print( gano la computadora.\n")
       f.write( gano la computadora.\n")

    else:
        print( "error seleccione correctamente!")
