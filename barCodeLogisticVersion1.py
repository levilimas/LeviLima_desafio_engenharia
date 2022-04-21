COR_TERMINAL_VERDE = '\033[1;32m'
COR_TERMINAL_VERMELHO = '\033[1;31m'
COR_TERMINAL_RESET = '\033[0;0m'

regioes = {
    'Centro-Oeste': [201, 299],
    'Nordeste': [300, 399],
    'Norte': [400, 499],
    'Sudeste': [1, 99],
    'Sul': [100, 199],
}

tipo_produto = {
    'Jóias': '001',
    'Livros': '111',
    'Eletrônicos': '333',
    'Bebidas': '555',
    'Brinquedos': '888'
}

cnpj_inativo = ['367"']


def validar_cod_barras(codigo):
    if len(codigo) == 15:
        print(COR_TERMINAL_VERDE + 'Código de barras Válido')
        return True
    else:
        print(COR_TERMINAL_VERMELHO + 'Código de barras Inválido' + COR_TERMINAL_VERMELHO)
        return False
    
def separar_trincas(codigo):
    if(validar_cod_barras):
        lista = []
        i_anterior = 0
        for i in range(0,16,3):

            if i != i_anterior:
                trinca = codigo[i_anterior:i]
                i_anterior = i
                lista.append(trinca)
        return lista
        
def verifica_localidade_origem(trinca):
    #Local de origem.
    for key, value in regioes.items():
        if value[0] <= int(trinca) <=value[1]:
            print("Local de origem: {}".format(key))

def verifica_localidade_destino(trinca):
    for key, value in regioes.items():
        if value[0] <= int(trinca) <=value[1]:
            print("Local de destino: {}".format(key))

def verifica_codigo_loggi(trinca):
    if trinca == '555':
        print('Código Loggi: {} válido'.format(trinca))
        return True
    else:
        return False

def verifica_codigo_vendedor(trinca):
    if trinca not in cnpj_inativo:
        print('Código Vendedor: {} válido'.format(trinca))
        return True
    else:
        print(COR_TERMINAL_VERMELHO+'Código Vendedor: {} inválido'.format(trinca))
        return False

def verifica_produto(trinca):
    if trinca in tipo_produto.values():
        for key, value in tipo_produto.items():
            if value == trinca:
                print("Tipo produto: {}" .format(key))
                return True
    else:
        return False

def verifica_trincas(lista):
    for i in range(0,5):
        if i == 0:
            #Local de origem.
            verifica_localidade_origem(lista[i])
        if i == 1:
            #Local de destino.
            verifica_localidade_destino(lista[i])
        if i == 2:
            #Codigo Loggi, padrão 555.
            verifica_codigo_loggi(lista[i])
        if i == 3:
            #Vendedor 
            verifica_codigo_vendedor(lista[i])
        if i == 4:
            #Produto
            verifica_produto(lista[i])
        # print(COR_TERMINAL_RESET+''+COR_TERMINAL_RESET)

codigo_de_barras = '288355555367888'

if validar_cod_barras(codigo_de_barras):
    verifica_trincas(separar_trincas(codigo_de_barras))
