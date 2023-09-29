import random

options_list = ('rock', 'paper', 'scissors')

machine_wins = 0
user_wins = 0

while machine_wins <3 and user_wins <3:

  
  #elegimos nuestra opcion de la lista disponible
  user_option = input('\nChoose a option: rock, paper, scissors: \n').lower()
  if user_option not in options_list:
    print('Choose a correct option')
  

  ##La maquina elige su opcion
  machine_option = options_list[random.randint(0, len(options_list)-1)]
  print('La maquina escogio: ' + machine_option)
  
  ##Ahora debemos comparar ambas opciones
  if user_option == 'rock' and machine_option == 'rock':
    print('Empate!!')
  elif user_option == 'rock' and machine_option == 'paper':
    print('La maquina Gana!!')
    machine_wins += 1
    print(machine_wins)
  elif user_option == 'rock' and machine_option == 'scissors':
    print('El humano Gana!!')
    user_wins+=1
    print(user_wins)
  elif user_option == 'paper' and machine_option == 'paper':
    print('Empate!!')
  elif user_option == 'paper' and machine_option == 'rock':
    print('El humano Gana!!')
    user_wins+=1
    print(user_wins)
  elif user_option == 'paper' and machine_option == 'scissors':
    print('La maquina Gana!!')
    machine_wins += 1
    print(machine_wins)
  elif user_option == 'scissors' and machine_option == 'paper':
    print('El humano Gana!!')
    user_wins+=1
    print(user_wins)
  elif user_option == 'scissors' and machine_option == 'rock':
    print('La maquina Gana!!')
    machine_wins += 1
    print(machine_wins)
  elif user_option == 'scissors' and machine_option == 'scissors':
    print('Empate!!')

if user_wins > 2:
  print("Felicidades Humano ganaste el juego!!")
elif machine_wins > 2:
  print("Felicidades Maquina Ganaste el juego!!")