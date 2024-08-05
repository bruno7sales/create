# Lista de nomes:
nomes = []

while True:
    print('1 - Inserir novo nome. ')
    print('2 - Exibir lista de nomes')
    print('3 - Ordemar a Lista.')
    print('4 - Encerrar Progama.')


    #Opção do usuário
    opcao = input('Opção do usuário: ')

    #Verifica a opção escolhida
    match opcao:
        case '1':
         novo_nome = input('Insira o novo nome: ')
         nomes.append(novo_nome)
         print(f'{novo_nome} inserido com sucesso!')
         continue
        case '2':
          print('\n LISTA DE NOMES: ')
          for nome in nomes:
            print(f'\n{nome}\n')
            continue
        case '3':
            nomes.sort()
            for nome in nomes:
                print(nome)
            print('\n Lista ordenada com sucesso!')
            continue
        case '4':
          print('Progama encerrado')
          break
        case _:
          print('Opção invalida!')
    

