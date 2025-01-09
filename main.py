from funcoes import interface, function_choice


choice = 4

while choice != 5 and isinstance(choice, int):
    if choice == 0:
        print('Digite um número correspondente ao anunciado!')
    choice = interface()
    function_choice(choice)

