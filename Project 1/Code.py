def corrigir_palavra(cad_car):
    """
    corrigir_palavra: cad. de caracteres -> cad. de caracteres

    Esta função recebe uma cadeia de caracteres, que descodificará as instâncias em
    que duas letras iguais (ignorando a diferença entre maiúsculas e minúsculas)
    se encontram adjecentes
    """
    cad = tuple(cad_car)
    i = 0

    while i != len(cad)-1:
        if ord(cad[i]) == ord(cad[i+1]) + 32 or ord(cad[i]) == ord(cad[i+1]) - 32:
            cad = cad[:i] + cad[i+2:]
            i = i - 1
            if i < 0:      # Caso a variável de indexação fique negativa e estrague o algoritmo
                i = 0
            if cad == ():
                break
            continue
        i = i + 1

    return ''.join(cad)


def eh_anagrama(cad_car1, cad_car2):
    """
    eh-anagrama: cad. caracteres X cad. caracteres -> booleano

    Esta função recebe duas cadeias de caracteres e compara as letras de cada uma
    (ignorando a diferença entre minúsculas e maiúsculas), retornando True caso
    sejam um anagrama uma da outra
    """
    cad1 = cad_car1.lower()
    cad2 = cad_car2.lower()

    if cad1 == cad2:   # Se as palavaras forem iguais, retorna True
        return True

    if cad1 != cad2 and (sorted(cad1) == sorted(cad2)):
        return True

    return False


def verificar_letras(frase):
    """
    verificar_letras: cadeia de caracteres -> lista

    Verifica se a frase só contém letras e retorna uma lista
    com a frase corrigida
    """
    n = 0

    for i in frase:
        if not i.isalpha():
            raise ValueError("corrigir_doc: argumento invalido")
        frase[n] = corrigir_palavra(i)
        n = n + 1

    return list(frase)


def eliminador_anagramas(frase):
    """
    eliminador_anagramas: cadeia de caracteres

    Chama a função eh_anagrama para identificar os anagramas e elimina-os
    caso eles existam
    """
    a = 0

    while a < len(frase):
        b = a
        while b < len(frase):
            if eh_anagrama(frase[a], frase[b]) and frase[a].lower() != frase[b].lower():
                frase.pop(b)
                continue
            b += 1
        a += 1


def verificar_espacos_juntos(cad):
    """
    verificar_espacos_juntos: lista

    Verifica se há dois caracteres de espaço juntos
    """
    for i in range(len(cad)-1):
        if cad[i] == cad[i+1] == " ":
            raise ValueError("corrigir_doc: argumento invalido")


def corrigir_doc(cad_car):
    """
    corrigir_doc: cad. caracteres -> cad. de caracteres

    Esta função verifica os diferentes requisitos para os argumentos.
    Corrige o documento na sua totalidade e devolve a cadeia de argumentos filtrada
    """
    if type(cad_car) != str:
        raise ValueError("corrigir_doc: argumento invalido")

    cad = list(cad_car)

    verificar_espacos_juntos(cad)

    frase = verificar_letras(cad_car.split(" "))

    eliminador_anagramas(frase)

    return ' '.join(frase)


def obter_posicao(direcao, num):
    """
    obter_posicao: cad-caracteres X inteiro -> inteiro

    Esta função recebe um movimento e uma posição, e efetua a mudança
    de digito
    """
    prox_posicao = num

    if direcao == "C" and num in (4, 5, 6, 7, 8, 9):
        prox_posicao = num - 3
    elif direcao == "B" and num in (1, 2, 3, 4, 5, 6):
        prox_posicao = num + 3
    elif direcao == "E" and num in (2, 5, 8, 3, 6, 9):
        prox_posicao = num - 1
    elif direcao == "D" and num in (1, 4, 7, 2, 5, 8):
        prox_posicao = num + 1

    return prox_posicao


def obter_digito(cad_car, num):
    """
    obter_digito: cad. caracteres X inteiro -> inteiro

    Esta função recebe um conjunto de instruções de direção e um dígito
    inicial. Efetua todos os movimentos pela ordem dada e retorna o dígito final
    """
    direcoes = tuple(cad_car)
    posicao = num

    for i in direcoes:
        posicao = obter_posicao(i, posicao)

    return posicao


def excepcoes_obter_pin(seq_mov):
    """
    excepcoes_obter_pin: tuplo

    Avalia a sequência de movimentos, levantado ValueError caso contenha estrutura inválida
    """
    if type(seq_mov) != tuple:             # Verifica se é um tuplo
        raise ValueError("obter_pin: argumento invalido")

    if not(4 <= len(seq_mov) <= 10):       # Verifica se há entre 4 e 10 conjuntos de movimentos
        raise ValueError("obter_pin: argumento invalido")

    for i in seq_mov:                      # Verifica se há strings nulas e se há instruções desconhecidas
        if i == "":
            raise ValueError("obter_pin: argumento invalido")
        for j in i:
            if j not in ("C", "B", "E", "D"):
                raise ValueError("obter_pin: argumento invalido")


def obter_pin(seq_mov):
    """
    obter_pin: tuplo -> tuplo

    Esta função verifica os dados introduzidos e traduz as instruções para
    os dígitos do código
    """
    excepcoes_obter_pin(seq_mov)

    posicao = 5
    seq_final = ()

    for i in seq_mov:
        seq_final = seq_final + (obter_digito(i, posicao),)
        posicao = obter_digito(i, posicao)

    return seq_final


def estrutura_da_cifra(arg):
    """
    estrutura_da_cifra: lista

    Verifica os possíveis erros específicos para a cifra, retornando True se
    houver algo não aceite
    """
    # Verifica se a string do elemento 0 é vazia ou se é só um traço ou começa ou acaba num traço
    if arg == "" or arg.startswith("-") or arg.endswith("-"):
        return True

    antes = ""
    for i in arg:
        if i == "-" and antes == "-":  # Verifica se há dois traços seguidos
            return True
        if not (i.isalpha() and 97 <= ord(i) <= 122) and i != "-":  # Verifica se é letra minúscula
            return True
        antes = i

    return False


def eh_entrada(arg):
    """
    eh_entrada: qualquer universal -> booleano

    Esta função verifica se a entrada BDB inserida está de acordo com as
    regras. Se for válida retorna True, caso contrário, retorna False
    """
    # Verifica se o argumento é um tuplo e se tem 3 elementos
    if type(arg) != tuple or len(arg) != 3:
        return False

    # Verifica os tipos dos elementos do tuplo
    if type(arg[0]) != str or type(arg[1]) != str or type(arg[2]) != tuple:
        return False

    if estrutura_da_cifra(arg[0]):  # Verifica a cifra
        return False

    # Verifica se a string do elemento 1 está entre chavetas e se tem 5 caracteres entre os parenteses
    if not arg[1].startswith("[") or not arg[1].endswith("]") or len(tuple(arg[1])) != 7:
        return False

    seq_num = tuple(arg[1])[1:6]

    # Verifica se só há letras minúsculas entre os parenteses
    for i in seq_num:
        if not (97 <= ord(i) <= 122):
            return False

    # Verifica se o tuplo tem 2 ou mais elementos
    if len(arg[2]) < 2:
        return False

    # Verifica se são números inteiros positivos
    for i in arg[2]:
        if type(i) != int or i <= 0:
            return False

    return True


def retirar_tracos(cad_car):
    """
    retirar_tacos: cadeia de caracteres -> tuplo

    Transforma a cadeia de caracteres num tuplo sem os traços
    """
    cad = tuple(cad_car)
    n = 0

    while n < len(cad):
        if cad[n] == "-":
            cad = cad[:n] + cad[n+1:]
            continue
        n += 1

    return cad


def traduz_seq_controlo(cad):
    """
    traduz_seq_controlo: tuplo -> cadeia de caracteres

    Cria um dicionário com as chaves sendo os caracteres e o valor sendo o número de vezes que esse
    caracter aparece. Depois itera pelo dicionário 5 vezes à procura do caracter com mais occorências
    e coloca-os numa string. Em caso de empate, segue pela ordem alfabetica
    """
    my_dic = {i: cad.count(i) for i in cad}
    maior = 0
    m = ""
    my_str = ""
    n = 0

    for j in range(5):  # Procura a letra com mais ocorrencias
        for i in my_dic:  # Em caso de empate, assume ordem alfabética
            if (my_dic[i] > maior) or (my_dic[i] == maior and ord(i) < ord(m)):
                maior = my_dic[i]
                m = i
        my_str = my_str + m  # Adiciona a letra com mais ocorrencias à string
        my_dic.pop(m)  # Retira a letra com mais occorencias do dicionário
        n = n + 1
        maior = 0
        m = ""

    return my_str


def validar_cifra(cad_car, cad_ctrl):
    """
    validar_cifra: cad. caracteres X cad. caracteres -> booleano

    Esta função verifica se a cifra inserida está de acordo com o caracter de
    segurança, retornando True se estiver e False caso contrário
    """
    cad = retirar_tracos(cad_car)

    my_str = traduz_seq_controlo(cad)

    if ("[" + my_str + "]") == cad_ctrl:
        return True

    return False


def filtrar_bdb(entradas):
    """
    filtrar_bdb: lista -> lista

    Esta função recebe uma lista de tuplos com diferentes entradas, verifica se são
    entradas BDB e retorna as que não cumprem os requisitos
    """
    if type(entradas) != list or entradas == []:
        raise ValueError("filtrar_bdb: argumento invalido")

    entradas_erradas = []

    for i in entradas:
        if eh_entrada(i):
            if not validar_cifra(i[0], i[1]):
                entradas_erradas.append(i)
        else:
            raise ValueError("filtrar_bdb: argumento invalido")

    return entradas_erradas


def obter_num_seguranca(numeros):
    """
    obter_num_seguranca: tuplo -> inteiro

    Esta função recebe um tuplo de números inteiros e retorna a menor subtração
    possível entre um par de números desse tuplo
    """
    subtracao = 0

    for i in numeros:            # ciclo para definir um valor possível para enontrar a menor subtração,
        if i > subtracao:        # pois colocar um número muito grande não é infalível
            subtracao = i

    for i in numeros:
        for j in numeros:
            if (i - j > 0) and (i - j < subtracao):
                subtracao = i - j

    return subtracao


def decifrar_texto(cad_car, num_seg):
    """
    decifrar_texto: cad. caracteres X inteiro -> cad. caracteres

    Esta função recebe uma string e um número de segurança, e decifra a string
    usando esse número, avançando num_seg + 1 posições caso o caracter tenha
    index par e num_seg - 1 posições caso ímpar
    """
    str_res = ""
    n = 0

    for i in cad_car:
        if i == "-":
            str_res = str_res + " "
        elif n % 2 == 0:
            str_res = str_res + chr(ord("a") + (ord(i) - ord("a") + num_seg + 1) % 26)
        elif n % 2 == 1:
            str_res = str_res + chr(ord("a") + (ord(i) - ord("a") + num_seg - 1) % 26)
        n += 1

    return str_res


def decifrar_bdb(lst):
    """
    decifrar_bdb: lista -> lista

    Esta função recebe uma lista com potências entradas BDB. Verifica se todas
    são válidas e retorna uma lista com o mesmo tamanho com as entradas decifradas
    """
    if type(lst) != list or lst == []:
        raise ValueError("decifrar_bdb: argumento invalido")

    lst_bdb = []
    for i in lst:
        if eh_entrada(i):
            lst_bdb.append(decifrar_texto(i[0], obter_num_seguranca(i[2])))
        else:
            raise ValueError("decifrar_bdb: argumento invalido")

    return lst_bdb


def estrutura_geral(my_dict):
    """
    estrutura_geral: dicionário -> Bool

    Verifica a estrutura do dicionário mãe, retornando True se houver algum problema
    """
    if type(my_dict) != dict or len(my_dict) != 3:
        return True

    # Verifica que as keys são as mesmas usadas nas prox. referencias
    if "name" not in my_dict.keys() or "pass" not in my_dict.keys() or "rule" not in my_dict.keys():
        return True

    if "vals" not in my_dict["rule"].keys() or "char" not in my_dict["rule"].keys():
        return True

    # Verifica que as keys são as mesmas usadas nas prox. referencias
    if type(my_dict['name']) != str or type(my_dict['pass']) != str or type(my_dict['rule']) != dict:
        return True

    # Verifica se há strings vazias
    if my_dict['name'] == '' or my_dict['pass'] == '':
        return True

    return False


def estrutura_rule(dict_rule):
    """
    estrutura_rule_ dicionário -> Bool

    Avalia a estrutura para 'vals' e para 'char'.
    """
    if type(dict_rule['vals']) != tuple or type(dict_rule['char']) != str:
        return True

    # Verifica se 'vals' tem 2 elementos e 'char' um caracter
    if len(dict_rule['vals']) != 2 or len(dict_rule['char']) != 1:
        return True

    # Verifica se os dois valores do tuplo 'vals' tems 2 inteiros
    if type(dict_rule['vals'][0]) != int or type(dict_rule['vals'][1]) != int:
        return True

    # Verificar se o primeiro elemento é maior que o segundo
    if dict_rule['vals'][0] > dict_rule['vals'][1]:
        return True

    if dict_rule['vals'][0] <= 0 or dict_rule['vals'][1] <= 0:
        return True

    if not (dict_rule['char'].isalpha() and dict_rule['char'].islower()):
        return True

    return False


def eh_utilizador(my_dict):
    """
    eh_utilizador: universal -> booleano

    Esta função verifica se o input é válido e retorna True se assim fôr
    """
    if estrutura_geral(my_dict):
        return False

    if estrutura_rule(my_dict['rule']):
        return False

    return True


def verificar_caracteres(senha):
    """
    verificar_caracteres: cad de caracteres -> inteiros

    Verifica se a senha tem 3 vogais e 2 caracteres iguais consecutivos
    e retorna o número de vogais e uma variável interruptor que assinala os dois
    caracteres consecutivos
    """
    n = 0
    m = False
    antes = ''
    for i in senha:
        if i in ('a', 'e', 'i', 'o', 'u'):
            n += 1
        if antes == i:
            m = True
        antes = i

    return n, m


def eh_senha_valida(senha, indiv_dict):
    """
    eh_senha_valida: cad. caracteres X dicionário -> booleano

    Esta função verifica se a senha de um utilizador cumpre os critérios
    gerais (ter 3 vogais e dois caracteres consecutivos) e os critéris individuais
    (a letra escolhida tem de aparecer um número de vezes que fica dentro do
    intervalo passado. Retorna True se estiver correta
    """
    n, m = verificar_caracteres(senha)
    if n < 3 or not m:
        return False

    # Cria uma lista com os caracteres como chaves e o número de instâncias deles como valores
    car_dict = {i: senha.count(i) for i in senha}

    if indiv_dict['char'] not in car_dict.keys():
        return False

    # Verifica se o número de vezes que o caracter de 'char' aparece está nos limites
    if not (indiv_dict['vals'][0] <= car_dict[indiv_dict['char']] <= indiv_dict['vals'][1]):
        return False

    return True


def filtrar_senhas(main_list):
    """
    filtrar_senhas: lista -> lista
    Esta função recebe uma lista de dicionários com nomes, senhas e regras
    de utilizadores. Levanta uma excepção caso os dicionários não tenham entradas válidas
    e retorna uma lista com dicionários dos utilizadores com senhas erradas
    """
    if type(main_list) != list or main_list == []:
        raise ValueError("filtrar_senhas: argumento invalido")

    for i in main_list:
        if not eh_utilizador(i):
            raise ValueError("filtrar_senhas: argumento invalido")

    final_list = []

    for i in main_list:
        if not eh_senha_valida(i['pass'], i['rule']):
            final_list.append(i['name'])

    return sorted(final_list)
