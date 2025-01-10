from classes import Product, ShoppingCart

import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

card_buy = ShoppingCart()

def interface() -> int:
    try:
        choice = int(input(f'Informe o que gostaria de fazer:\n1- Cadastrar Produto\n2- Listar Produtos\n3- Comprar Produto\n4- Visualizar Carrinho\n5- Sair\nEscolha: '))
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 3:
            return 3
        elif choice == 4:
            return 4
        elif choice == 5:
            return 5
        else:
            return 0
                 
    except ValueError:
        print('Digite um número conforme o anunciado.')


def register_product():
    choice = '1'
    while choice != '0':
        try:
            name: str = input('Informe o nome do produto:\nNome: ')
            price: float = float(input('Informe o valor do produto ex: 12.40:\nValor: '))
            quantity: int = int(input('Informe a quantidade em estoque:\nQuantidade: '))
            
            product: Product = Product(name, price, quantity, True)
            choice: int = input('Informe 1- Para voltar | 0- Para sair\nEscolha: ')

            with open('produtos.txt', encoding='UTF-8', mode='r') as arq:
                produtos = arq.readlines()
                produtos = [produtos[index].replace('\n', '').split()for index in range(0, len(produtos))]
                produtos = [produtos[index][0] if len(produtos[index]) == 4 else ' '.join(produtos[index][0:-3]) for index in range(0, len(produtos))]     

            if choice == '0' and name.title() not in produtos:
                with open('produtos.txt', encoding='UTF-8', mode= 'a+') as arq:
                    arq.write(f'{product.name} ')
                    arq.write(f'{product.price} ')
                    arq.write(f'{product.quantity} ')
                    arq.write(f'{product.is_in_stock}\n')
                print(f'{name.title()} cadastrado com sucesso!')
            else:
                print(f'{name.title()} já está cadastrado!')
        except ValueError:
            print('Dado inválido!')

     
def list_products():
    with open('produtos.txt', encoding='UTF-8', mode='r') as arq:
        products: list = arq.readlines()

        products = [products[index].replace('\n', '').split() for index in range(0, len(products))]

        products = [ ' '.join(products[index][0:-3])for index in range(0, len(products))]
        

    if products:
        for index in range(0, len(products)):
            print(f'Nome: {products[index]}')    
    else:
        print('Não possui nenhum produto cadastrado!')


def buy_product():
    with open('produtos.txt') as arq:
        products = arq.readlines()
        prices_products = [products[index].replace('\n', '').split()[-3] for index in range(0, len(products))]
        quantity_products = [ products[index].replace('\n', '').split()[-2] for index in range(0, len(products))]
        name_products = [ ' '.join(products[index].replace('\n', '').split()[0:-3]) for index in range(0, len(products))]

        list_products: list = []
        for index in range(0, len(products)):
            product: Product = Product(name_products[index], prices_products[index], quantity_products[index], is_in_stock=True )
            dict_product = {str(index): product}
            list_products.append(dict_product)
        
        choice = 1
        while choice != 2:
            for index in range(0, len(list_products)):
                product = list_products[index][str(index)]
                print(f'{index + 1}- Nome: {product.name} Preço: {locale.currency(product.price)}')

            product_choice = input('Informe o produto que você gostaria de comprar:\nEscolha: ')
            product_choice = str(int(product_choice) - 1)

            for index in range(0, len(list_products)):
                if product_choice in list_products[index]:
                    card_buy.add_item(list_products[index][str(index)])
        
            choice = int(input('1- Continuar comprando | 2- Sair\nEscolha: '))
           

def function_choice(choice: int):
    match choice:
        case 1:
            print('-------- Cadastrar Produto -----------')
            register_product()
        case 2:
            print('--------- Lista Produtos -------------')
            list_products()
        case 3:
            print('--------- Comprar Produto ------------')
            buy_product()
        case 4:
            print('-------- Visualizar Carrinho ---------')
        case 5:
            print('Saindo.......')
       