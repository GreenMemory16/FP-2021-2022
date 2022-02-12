def cria_posicao(x, y):
    """
    cria_posicao: int x int -> posição
    CONSTRUTOR -> cria_posicao(x, y) recebe os valores correspondentes às coordenadas de uma posição e
                                      devolve a posição correspondente. Verifica a validade dos argumentos,
                                      gerando ValueError caso sejam inválidos
    """
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return [x, y]


def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posição -> posição
    CONSTRUTOR -> cria_copia_posicao(pos) recebe uma posição e devolve uma copia da posição
    """
    if eh_posicao(pos):
        return cria_posicao(obter_pos_x(pos), obter_pos_y(pos))


def obter_pos_x(pos):
    """
    obter_pos_x: posição -> int
    SELECIONADOR -> obter_pos_x(pos) devolve a componente x da posição
    """
    return pos[0]


def obter_pos_y(pos):
    """
    obter_pos_y: posição -> int
    SELECIONADOR -> obter_pos_y(pos) devolve a componente y da posição
    """
    return pos[1]


def eh_posicao(pos):
    """
    eh_posicao: universal -> booleano
    RECONHECEDOR -> eh_posicao(pos) devolve True caso o seu argumento seja um TAD posição e False caso contrário
    """
    if type(pos) == list and len(pos) == 2 and type(pos[0]) == int and\
            type(pos[1]) == int and pos[0] >= 0 and pos[1] >= 0:
        return True
    return False


def posicoes_iguais(pos1, pos2):
    """
    posicoes_iguais: posição x posição -> booleano
    TESTE -> posicoes_iguais(pos1, pos2) devolve True apenas se pos1 e pos2 são iguais
    """
    if obter_pos_x(pos1) == obter_pos_x(pos2) and obter_pos_y(pos1) == obter_pos_y(pos2) and\
            eh_posicao(pos1) and eh_posicao(pos2):
        return True
    return False


def posicao_para_str(pos):
    """
    posicao_para_str: posição -> string
    TRANSFORMADOR -> posicao_para_str devolve a cadeia de caracteres '(x, y)' que representa o seu
                                       argumento, sendo os valores x e y as coordenadas de p
    """
    return "({}, {})".format(obter_pos_x(pos), obter_pos_y(pos))


def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjecentes : posição -> tuplo
    obter_posicoes_adjecentes(pos) devolve um tuplo com as posições adjacentes à posição p,
                                    começando pela posição acima de p e seguindo no sentido horário.
    """
    tpl = ()
    if obter_pos_y(pos)-1 >= 0:
        tpl = tpl + (cria_posicao(obter_pos_x(pos), obter_pos_y(pos)-1),)
    tpl = tpl + (cria_posicao(obter_pos_x(pos)+1, obter_pos_y(pos)),)
    tpl = tpl + (cria_posicao(obter_pos_x(pos), obter_pos_y(pos)+1),)
    if obter_pos_x(pos)-1 >= 0:
        tpl = tpl + (cria_posicao(obter_pos_x(pos)-1, obter_pos_y(pos)),)

    return tpl


def ordenar_posicoes(tpl_pos):
    """
    ordenar_posições : tuplo -> tuplo
    ordenar_posições(tpl_pos) devolve um tuplo contento as mesmas posições do tuplo fornecido como
                               argumento , ordenadas de acordo com a ordem de leitura do prado
    """
    change = True
    lista = list(tpl_pos)
    tamanho = len(lista)-1

    while change:
        change = False
        for i in range(tamanho):
            if obter_pos_y(lista[i]) > obter_pos_y(lista[i+1]) or\
                    (obter_pos_x(lista[i]) > obter_pos_x(lista[i+1]) and
                     obter_pos_y(lista[i]) == obter_pos_y(lista[i+1])):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                change = True
        tamanho = tamanho - 1

    return tuple(lista)


# TAD Animais

def cria_animal(s, r, a):
    """
    cria_animal: string x int x int -> animal
    CONSTRUTOR -> cria_animal(s, r, a) recebe uma cadeia de caracteres s não vazia, correspondente à espécie
                                        do animal e dois valores inteiros correspondentes à frequência de
    reprodução r (maior do que 0) e à frequência de alimentação a (maior ou igual a 0) e devolve o animal.
    Animais com a frequência de alimentação maior que 0 são considerados predadores, caso contrário são
    considerados presas. O construtor verifica a validade dos seus argumentos, gerando um ValueError caso
    os argumentos sejam inválidos
    """
    if type(s) == str and s != "" and type(r) == int and type(a) == int and r > 0 and a >= 0:
        return {"s": s, "r": r, "a": a, "i": 0, "f": 0}
    raise ValueError("cria_animal: argumentos invalidos")


def cria_copia_animal(animal):
    """
    cria_copia_animal: animal -> animal
    CONSTRUTOR -> cria_copia_animal(animal) recebe um animal (predador ou presa) e devolve uma nova cópia
    """
    if eh_animal(animal):
        return cria_animal(obter_especie(animal), obter_freq_reproducao(animal), obter_freq_alimentacao(animal))


def obter_especie(animal):
    """
    obter_especie: animal -> string
    SELECIONADOR -> obter_especie(animal) devolve a cadeia de caracteres correspondente à espécie do animal
    """
    return animal["s"]


def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal -> int
    SELECIONADOR -> obter_freq_reproducao(animal) devolve a frequência de reprodução do animal
    """
    return animal["r"]


def obter_freq_alimentacao(animal):
    """
    obter_freq_alimentacao: animal -> int
    SELECIONADOR -> obter_freq_alimentacao(animal) devolve a frequência de reprodução do animal
    """
    return animal["a"]


def obter_idade(animal):
    """
    obter_idade: animal -> int
    SELECIONADOR -> obter_idade(animal) devolve a idade do animal
    """
    return animal["i"]


def obter_fome(animal):
    """
    obter_fome: animal -> int
    SELECIONADOR -> obter_fome(animal) devolve a fome do animal. As presas devolvem sempre 0
    """
    return animal["f"]


def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal
    MODIFICADOR -> aumenta_idade(animal) modifica destrutivamente o animal, incrementando o valor da sua
                                          idade em uma unidade, e devolve o próprio animal
    """
    animal["i"] += 1
    return animal


def reset_idade(animal):
    """
    reset_idade: animal -> animal
    MODIFICADOR -> reset_idade(animal) modifica destrutivamente o animal, definindo o valor da sua idade
                                        igual a 0, e devolve o próprio animal
    """
    animal["i"] = 0
    return animal


def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal
    MODIFICADOR -> aumenta_fome(animal) modifica destrutivamente o animal, definindo o valor da sua idade
                                         igual a 0, e devolve o próprio animal
    """
    if eh_predador(animal):
        animal["f"] += 1
    return animal


def reset_fome(animal):
    """
    reset_fome: animal -> animal
    MODIFICADOR -> reset_fome(animal) modifica destrutivamente o animal, defininfo o valor da sua fome
                                       igual a 0, e devolve o próprio animal. Esta função não modifica
                                       as presas
    """
    animal["f"] = 0
    return animal


def eh_animal(animal):
    """
    eh_animal: universal -> booleano
    RECONHECEDOR -> eh_animal(animal) devolve True se o seu argumento é um TAD animal, e False caso contrário
    """
    if type(animal) == dict and len(animal) == 5 and type(animal["s"]) == str and animal["s"] != "" and\
        type(animal["r"]) == int and animal["r"] > 0 and type(animal["a"]) == int and animal["a"] >= 0 and\
            type(animal["i"]) == int and animal["i"] >= 0 and type(animal["f"]) == int and animal["f"] >= 0:
        return True
    return False


def eh_predador(animal):
    """
    eh_predador: animal -> booleano
    RECONHECEDOR -> eh_predador(animal) devolve True se o seu argumento é um TAD animal predador, e False
                                         caso contrário
    """
    if eh_animal(animal):
        return obter_freq_alimentacao(animal) > 0
    return False


def eh_presa(animal):
    """
    eh_presa: animal -> booleano
    RECONHECEDOR -> eh_presa(animal) devolve True se o seu argumento é um TAD animal presa, e False
                                      caso contrário
    """
    if eh_animal(animal):
        return obter_freq_alimentacao(animal) == 0
    return False


def animais_iguais(animal1, animal2):
    """
    animais_iguais: animal x animal -> booleano
    TESTE -> animais_iguais(animal1, animal2) devolve True apenas se animal1 e animal2 são iguais
    """
    if eh_animal(animal1) and eh_animal(animal2) and obter_especie(animal1) == obter_especie(animal2) and\
            obter_idade(animal1) == obter_idade(animal2) and\
            obter_fome(animal1) == obter_fome(animal2) and \
            obter_freq_alimentacao(animal1) == obter_freq_alimentacao(animal2) and\
            obter_freq_reproducao(animal1) == obter_freq_reproducao(animal2):
        return True
    return False


def animal_para_char(animal):
    """
    animal_para_char: animal -> string
    TRANSFORMADOR -> animal_para_char(animal) devolve a cadeia de caracteres dum único elemento correspondente
                                               ao primeiro caracter  da espécie do animal passada por argumento
                                               em minúscula para presas e maiúscula para predadores
    """
    if eh_presa(animal):
        return obter_especie(animal)[0].lower()
    elif eh_predador(animal):
        return obter_especie(animal)[0].upper()


def animal_para_str(animal):
    """
    animal_para_str: animal -> string
    TRANSFORMADOR -> animal_para_str(animal) devolve uma cadeia de caracteres que representa o animal como
                                              mostrado no exemplos a seguir
    """
    if eh_presa(animal):
        return "{} [{}/{}]".format(obter_especie(animal), obter_idade(animal), obter_freq_reproducao(animal))
    elif eh_predador(animal):
        return "{} [{}/{};{}/{}]".format(obter_especie(animal), obter_idade(animal), obter_freq_reproducao(animal),
                                         obter_fome(animal), obter_freq_alimentacao(animal))


def eh_animal_fertil(animal):
    """
    eh_animal_fertil : animal -> Booleano
    eh_animal_fertil(animal) retorna True se o animal atingiu a idade de reprodução
    """
    return obter_idade(animal) >= obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    """
    eh_animal_faminto : animal -> booleano
    eh_animal_faminto(animal) retorna True se um predador atingir o valor limite de fome
    """
    return eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal)


def reproduz_animal(animal):
    """
    reproduz_animal : animal -> animal
    reproduz_animal(animal) cria uma cópia do animal passado no parâmetro e dá reset à idade do animal
    """
    novo_animal = cria_copia_animal(animal)
    reset_idade(animal)
    return novo_animal


# TAD PRADO

def cria_prado(pos, rocks, a, pos_a):
    """
    cria_prado: posição x tuplo x tuplo x tuplo -> prado
    CONSTRUTOR -> cria_prado(pos, rocks, a, pos_a) recebe uma posição pos correspondente à posição que
                                                   ocupa a montanha do canto  inferior direito do prado, um
    tuplo rocks de 0 ou mais posições correspondentes aos rochedos que não são as montanhas dos limites exteriores
    do prado, um tuplo a de 1 ou mais animais, e um tuplo pos_a da mesma dimensão que a e com as posições
    correspondentes ocupadas pelos animais, e devolve o prado que representa internamente o mapa e os
    animais presentes. O construtor verifica a validade dos argumentos, gerando um  ValueError caso sejam
    inválidos
    """
    if eh_posicao(pos) and type(rocks) == tuple and type(a) == tuple and type(pos_a) == tuple and\
       len(rocks) >= 0 and len(pos_a) == len(a) > 1 and obter_pos_y(pos) > 1 and obter_pos_x(pos) > 1:
        for i in range(len(rocks)):
            if not eh_posicao(rocks[i]) or obter_pos_x(rocks[i]) == 0 or obter_pos_y(rocks[i]) == 0 or\
               obter_pos_x(rocks[i]) >= obter_pos_x(pos) or obter_pos_y(rocks[i]) >= obter_pos_y(pos):
                raise ValueError("cria_prado: argumentos invalidos")
        for i in range(len(a)):
            if not (eh_animal(a[i]) or eh_posicao(pos_a[i])) or obter_pos_x(pos_a[i]) == 0 or\
                    obter_pos_x(pos_a[i]) >= obter_pos_x(pos) or obter_pos_y(pos_a[i]) == 0 or\
                    obter_pos_y(pos_a[i]) >= obter_pos_y(pos):
                raise ValueError("cria_prado: argumentos invalidos")
        return {"pos": pos, "rocks": rocks, "a": a, "pos_a": pos_a}
    raise ValueError("cria_prado: argumentos invalidos")


def cria_copia_prado(prado):
    """
    cria_copia_prado: prado -> prado
    CONSTRUTOR -> cria_copia_prado(prado) recebe um prado e devolve uma nova cópia do prado
    """

    # return cria_prado(cria_posicao(obter_tamanho_x(prado)-1, obter_tamanho_y(prado)-1), prado["rocks"],
                      # prado["a"], prado["pos_a"])
    return cria_prado(prado["pos"], prado["rocks"], prado["a"], prado["pos_a"])


def obter_tamanho_x(prado):
    """
    obter_tamanho_x: prado -> int
    SELETOR -> obter_tamanho_x(prado) devolve o valor inteiro que corresponde à dimensão Nx do prado
    """
    return prado["pos"][0]+1


def obter_tamanho_y(prado):
    """
    obter_tamanho_y: prado -> int
    SELETOR -> obter_tamanho_y(prado) devolve o valor inteiro que corresponde à dimensão Ny do prado
    """
    return prado["pos"][1]+1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado -> int
    SELETOR -> obter_numero_predadores(prado) devolve o número de animais predadores no prado
    """
    count = 0
    for i in prado["a"]:
        if eh_predador(i):
            count += 1
    return count


def obter_numero_presas(prado):
    """
    obter_numero_presas: prado -> int
    SELETOR -> obter_numero_presas(prado) devolve o número de animais presas no prado
    """
    count = 0
    for i in prado["a"]:
        if eh_presa(i):
            count += 1
    return count


def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado -> tuplo posições
    SELETOR -> obter_posicao_animais(prado) devolve um tuplo contendo as posições do prado ocupadas por
                                            animais , ordenadas por ordem de leitura do prado
    """
    return ordenar_posicoes(prado["pos_a"])


def obter_animal(prado, pos):
    """
    obter_animal: prado x posição -> animal
    SELETOR -> obter_animal(prado, pos) devolve o animal do prado que se encontra na posição passada
    """
    n = 0
    for posicao in prado["pos_a"]:
        if posicoes_iguais(posicao, pos):
            break
        n += 1

    return prado["a"][n]


def eliminar_animal(prado, pos):
    """
    eliminar_animal: prado x posição -> prado
    MODIFICADOR -> eliminar_animal(prado, pos) modifica destrutivamente o prado, eliminando o animal da
                                               posição pos, deixando-a livre. Devolve o próprio prado
    """
    if eh_posicao_animal(prado, pos):
        n = 0
        for i in prado["pos_a"]:
            if posicoes_iguais(pos, i):
                break
            n += 1

        # index = prado["pos_a"].index(pos)
        prado["pos_a"] = prado["pos_a"][:n] + prado["pos_a"][n+1:]
        prado["a"] = prado["a"][:n] + prado["a"][n+1:]
    return prado


def mover_animal(prado, p1, p2):
    """
    mover_animal: prado x posição x posiçao -> prado
    MODIFICADOR -> mover_animal(prado, p1, p2) modifica destrutivamente o prado, movimentando o animal da
                                               posição  p1 para p2, deixando livre a posição onde estava
    """
    if not eh_posicao_obstaculo(prado, p2):
        animal = obter_animal(prado, p1)   # guarda o animal de p2
        eliminar_animal(prado, p1)         # elimina o animal de p1
        prado = inserir_animal(prado, animal, p2)  # tira o animal de p1 e usa a funcao para meter o animal no p2

    return prado


def inserir_animal(prado, animal, pos):
    """
    inserir_animal: prado x animal x posição -> prado
    MODIFICADOR -> inserir_animal(prado, animal, pos) modifica destrutivamente o prado, acrescentando na
                                                      posição pos o animal passado como argumento
    """
    if not eh_posicao_obstaculo(prado, pos):
        prado["pos_a"] = prado["pos_a"] + (pos,)
        prado["a"] = prado["a"] + (animal, )
    return prado


def eh_prado(p):
    """
    eh_prado: universal -> booleano
    RECONHECEDOR -> eh_prado(p) devolve True caso o seu argumento seja um TAD prado e False caso contrário
    """
    if type(p) == dict and len(p) == 4 and "pos" in p and "rocks" in p and "a" in p and "pos_a" in p and\
       eh_posicao(p["pos"]) and type(p["rocks"]) == tuple and type(p["a"]) == tuple and type(p["pos_a"]) == tuple and\
       len(p["rocks"]) >= 0 and len(p["a"]) == len(p["pos_a"]) > 0 and obter_tamanho_x(p) > 2 and\
       obter_tamanho_y(p) > 2:
        for i in range(len(p["rocks"])):
            if not eh_posicao(p["rocks"][i]) or obter_pos_x(p["rocks"][i]) == 0 or obter_pos_y(p["rocks"][i]) == 0 or\
               obter_pos_x(p["rocks"][i]) >= obter_pos_x(p["pos"]) or\
               obter_pos_y(p["rocks"][i]) >= obter_pos_y(p["pos"]):
                return False
        for i in range(len(p["a"])):
            if not eh_animal(p["a"][i]) or not eh_posicao(p["pos_a"][i]):
                return False
        return True
    return False


def eh_posicao_animal(prado, pos):
    """
    eh_posicao_animal: prado x posição -> booleano
    RECONHECEDOR -> eh_posicao_animal(prado, pos) devolve True caso a posição pos esteja ocupada por um animal
                                                  e False caso contrário
    """
    for posicao in prado["pos_a"]:
        if posicoes_iguais(pos, posicao):
            return True
    return False


def eh_posicao_obstaculo(prado, pos):
    """
    eh_posiao_obstaculo: prado x posição -> booleano
    RECONHECEDOR -> eh_posicao_obstaculo(prado, pos) devolve True caso a posição pos esteja ocupada por um
                                                     rochedo, e False caso contrário
    """
    if obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 or obter_pos_x(pos) == obter_tamanho_x(prado)-1 or\
       obter_pos_y(pos) == obter_tamanho_y(prado)-1:
        return True

    for posicao in prado["rocks"]:
        if posicoes_iguais(pos, posicao):
            return True

    return False


def eh_posicao_livre(prado, pos):
    """
    eh_posicao_livre: prado x posição -> booleano
    RECONHECEDOR -> eh_posicao_livre(prado, pos) devolve True caso a posição pos corresponder a um espaço
                                                 livre, e False caso contrário
    """
    return not (eh_posicao_animal(prado, pos) or eh_posicao_obstaculo(prado, pos))


# NAO SEI SE É SUPOSTO VER-MOS OS TUPLOS DOS ANIMAIS E DAS POSICOES DOS PRADOS
def prados_iguais(prado1, prado2):
    """
    prados_iguais: prado x prado -> booleano
    TESTE -> prados_iguais(prado1, prado2) devole True se prado1 e prado2 forem iguais
    """

    """
    if eh_prado(prado1) and eh_prado(prado2) and posicoes_iguais(prado1["pos"], prado2["pos"]) and\
       ordenar_posicoes(prado1["rocks"]) == ordenar_posicoes(prado2["rocks"]) and\
       ordenar_posicoes(prado1["pos_a"]) == ordenar_posicoes(prado2["pos_a"]):
        for posicao in prado1["pos_a"]:
            if not animais_iguais(obter_animal(prado1, posicao), obter_animal(prado2, posicao)):
                return False
        return True
    """
    if eh_prado(prado1) and eh_prado(prado2) and posicoes_iguais(prado1["pos"], prado2["pos"]) and\
       len(prado1["rocks"]) == len(prado2["rocks"]) and len(prado1["pos_a"]) == len(prado2["pos_a"]):
        pos1 = ordenar_posicoes(prado1["rocks"])
        pos2 = ordenar_posicoes(prado2["rocks"])
        for i in range(len(pos1)):
            if not posicoes_iguais(pos1[i], pos2[i]):
                return False
        pos1 = ordenar_posicoes(prado1["pos_a"])
        pos2 = ordenar_posicoes(prado2["pos_a"])
        for i in range(len(pos1)):
            if not posicoes_iguais(pos1[i], pos2[i]):
                return False
        for posicao in pos1:
            if not animais_iguais(obter_animal(prado1, posicao), obter_animal(prado2, posicao)):
                return False
        return True
    return False


def prado_para_str(prado):
    """
    prado_para_str: prado -> string
    TRANSFORMADOR -> prado_para_str(prado) devolve uma cadeia de caracteres que representa o prado
    """
    prado_str = ""
    for lin in range(obter_tamanho_y(prado)):
        for col in range(obter_tamanho_x(prado)):
            if lin == 0 and col == 0 or col == obter_tamanho_x(prado)-1 and lin == 0 or\
               lin == obter_tamanho_y(prado)-1 and col == 0 or lin == obter_tamanho_y(prado)-1 and\
               col == obter_tamanho_x(prado)-1:
                prado_str += "+"
            elif lin == 0 or lin == obter_tamanho_y(prado)-1:
                prado_str += "-"
            elif col == 0 or col == obter_tamanho_x(prado)-1:
                prado_str += "|"
            elif eh_posicao_livre(prado, cria_posicao(col, lin)):
                prado_str += "."
            elif eh_posicao_obstaculo(prado, cria_posicao(col, lin)):
                prado_str += "@"
            elif eh_posicao_animal(prado, cria_posicao(col, lin)):
                prado_str += animal_para_char(obter_animal(prado, cria_posicao(col, lin)))
        if lin != obter_tamanho_y(prado)-1:
            prado_str += "\n"
    return prado_str


def obter_valor_numerico(prado, pos):
    """
    obter_valor_numerico: prado x posição -> int
    obter_valor_numerico(prado, pos) percorre o prado, e retorna o numero da célula do prado
                                     correspondente à posição do argumento
    """
    count = 0
    for lin in range(obter_tamanho_y(prado)):
        for col in range(obter_tamanho_x(prado)):
            if posicoes_iguais(pos, cria_posicao(col, lin)):
                return count
            count += 1


def obter_movimento(prado, pos):
    """
    obter_movimento: prado x posição -> posição
    obter_movimento(prado, pos) recebe a posição de um animal a mover no prado, e retorna a posição para a
                                qual o animal se vai mover. Se o animal for um predador e comer uma presa,
    atualiza o prado da forma devida e ajustando a fome do predador
    """
    pos_adjecentes = obter_posicoes_adjacentes(pos)
    possibilidades = []

    # Remove as posições de rochas das possívies posições de movimento
    for posicao in pos_adjecentes:
        if not eh_borda(prado, posicao) and not eh_posicao_obstaculo(prado, posicao) and\
           0 < obter_pos_x(pos) < obter_tamanho_x(prado)-1 and\
           0 < obter_pos_y(pos) < obter_tamanho_y(prado)-1:
            possibilidades.append(posicao)

    """
    for posicao in possibilidades:
        if eh_posicao_animal(prado, posicao) and eh_predador(obter_animal(prado, pos)) and\
           eh_presa(obter_animal(prado, posicao)):
            prado = eliminar_animal(prado, posicao)
            reset_fome(obter_animal(prado, pos))
            return posicao

    """

    # Se o animal for um predador teremos de tratar o movimento de forma diferente
    presas = []
    if eh_predador(obter_animal(prado, pos)):
        for posicao in possibilidades:
            if eh_posicao_animal(prado, posicao) and eh_presa(obter_animal(prado, posicao)):
                presas.append(posicao)

    if presas != []:
        return movimento_predador(prado, presas, pos)

    # Se houver presas à volta do predador, escolhe a presa de acordo com a regra geral
    return movimento_geral(prado, possibilidades, pos)


def movimento_predador(prado, presas, pos):
    """
    movimento_predador: prado x animal x posição -> posição
    movimento_predador(prado, presas, pos) recebe um prado, um animal(predador) e uma posição. Move o
                                           predador para comer uma presa adjecente, eliminando a presa
    """
    mov = escolhe_movimento(presas, obter_valor_numerico(prado, pos))
    prado = eliminar_animal(prado, mov)
    reset_fome(obter_animal(prado, pos))
    return mov


def movimento_geral(prado, possibilidades, pos):
    """
    movimento_geral: prado x lista x posição -> posição
    movimento_geral(prado, possibilidades, pos) recebe uma lista de posicoes adjecentes, com possibilidades
                                                para o animal na posição pos se mover. Esta função callcula
    a posição do animal para a próxima geração. Se não houver hipóteses, fica no mesmo sítio
    """
    """
    possibilidades_atualizar = possibilidades.copy()
    for posicao in possibilidades:
        if not eh_posicao_livre(prado, posicao):
            possibilidades_atualizar.remove(posicao)
    """
    n = 0
    while n < len(possibilidades):
        if not eh_posicao_livre(prado, possibilidades[n]):
            possibilidades.pop(n)
            n = n - 1
        n += 1

    if len(possibilidades) == 0:
        return pos

    return escolhe_movimento(possibilidades, obter_valor_numerico(prado, pos))


def escolhe_movimento(posicoes, numero):
    """
    escolhe_movimento: lista, int -> posição
    escolhe_movimento(posicoes, numero) recebe uma lista se posições e o número de uma célula do prado
                                        e escolhe a próxima posição de um animal de acrodo com as regras gerais
    """
    return posicoes[numero % len(posicoes)]


def eh_borda(prado, pos):
    """
    eh_borda: prado x posição -> booleano
    eh_borda(prado, pos) verifica se uma dada posição é um rochedo da borda do prado
    """
    if obter_pos_y(pos) == 0 or obter_pos_x(pos) == 0 or\
       obter_pos_x(pos) == obter_tamanho_x(prado)-1 or obter_pos_y(pos) == obter_tamanho_y(prado)-1:
        return True
    return False


def geracao(prado):
    """
    geracao: prado -> prado
    geracao(prado) simula uma geração no prado. Esta função move as presas e os predadores de acordo com as regras.
                   de cada um, aumentando ou diminuindo os seus atributos quando necessário
    """
    lista_negra = []
    for lin in range(obter_tamanho_y(prado)):
        for col in range(obter_tamanho_x(prado)):
            posicao = cria_posicao(col, lin)

            # Verifica se o animal que vamos verificar não se moveu já esta geração
            interruptor = True
            if eh_posicao_animal(prado, posicao):

                for pos in lista_negra:
                    if posicoes_iguais(pos, posicao):
                        interruptor = False

                if interruptor:
                    movimento_animal_geral(prado, posicao, lista_negra)

    lista_negra.clear()
    return prado


def movimento_animal_geral(prado, posicao, lista_negra):
    """
    movimento_animal_geral: prado x posicao x lista_negra
    movimento_animal_geral(prado, posicao, lista_negra) movimenta as presas e os predadores de acordo com as
                                                        regras de cada um. Uma presa move-se por:
    (nº célula % possibilidades) sendo o resultado disto o index da posição nas hipóteses correspondente à
    posição para onde se deve mover. Para os predadores, se houver presas à volta, ele come de acordo com a
    mesma regra anterior. Caso não haja, também segue a regra geral para as posições livres, aumentando a sua
    fome
    """
    animal = obter_animal(prado, posicao)
    aumenta_idade(animal)
    if eh_predador(animal):
        aumenta_fome(animal)

    mov = obter_movimento(prado, posicao)
    mover_animal(prado, posicao, mov)

    # Verifica se é animal fertil, gerando uma cria se for e resetando os valores da idade
    if eh_animal_fertil(animal) and eh_posicao_livre(prado, posicao):
        reset_idade(animal)
        prado = inserir_animal(prado, cria_copia_animal(animal), posicao)

    # Se for predador, verificar se morreu de fome
    if eh_predador(animal) and eh_animal_faminto(animal):
        prado = eliminar_animal(prado, mov)
    lista_negra.append(mov)


def simula_ecossistema(f, n_simulacoes, v):
    """
    simula_ecossistema: string x int x booleano -> tuplo
    simula_ecossistema(f, n_simulacoes, v) recebe o nome do ficheiro de onde retirar os dados do prado,
                                           o nº de gerações a realizar e um interruptor que decide entre
    o modo verboso e o modo quiet. O verboso imprime o prado cada vez que há um alteração no número de animais,
    enquanto o modo quiet apenas imprime o início e o fim
    """
    my_fich = open(f, "r")
    prado = procura_dados(my_fich.readlines())
    gen = 1
    presas_antes = obter_numero_presas(prado)
    predadores_antes = obter_numero_predadores(prado)

    if v:
        modo_verboso(prado, n_simulacoes, presas_antes, predadores_antes, gen)

    else:
        modo_quiet(prado, n_simulacoes)

    tuplo_saida = (obter_numero_predadores(prado), obter_numero_presas(prado))
    return tuplo_saida


def modo_verboso(prado, n_simulacoes, presas_antes, predadores_antes, gen):
    """
    modo_verboso: prado x int x int x int x int
    modo_verboso(prado, n_simulacoes, presas_antes, predadores_antes, gen) chama as funções que vao mover os
                                                                           animais no prado, imprimindo o
    mesmo se houver mudança no número de animais.
    """
    imprime_dados_prado(prado, 0)
    print(prado_para_str(prado))
    for i in range(n_simulacoes):
        prado = geracao(prado)
        prado_para_str(prado)
        if obter_numero_presas(prado) != presas_antes or obter_numero_predadores(prado) != predadores_antes:
            imprime_dados_prado(prado, gen)
            print(prado_para_str(prado))
            presas_antes = obter_numero_presas(prado)
            predadores_antes = obter_numero_predadores(prado)
        gen += 1


def modo_quiet(prado, n_simulacoes):
    """
    modo_quiet: prado x int
    modo_quiet(prado, n_simulacoes) faz as alterações no prado para as gerações, imprimindo o prado no
                                    inicio e no fim da simulação
    """
    imprime_dados_prado(prado, 0)
    print(prado_para_str(prado))
    for i in range(n_simulacoes):
        prado = geracao(prado)
    imprime_dados_prado(prado, n_simulacoes)
    print(prado_para_str(prado))


def imprime_dados_prado(prado, gen):
    """
    imprime_dados_prado: prado x int
    imprime_dados_prado(prado, gen) imprime o número de presas, predadores e a geração atual
    """
    print("Predadores: {} vs Presas: {} (Gen. {})".format(obter_numero_predadores(prado),
                                                          obter_numero_presas(prado), gen))


def procura_dados(linhas):
    """
    procura_dados: lista -> prado
    procura_dados(linhas) extrai os dados do ficheiro de texto e cria um prado com os mesmos
    """
    dados = []
    for i in linhas:
        dados.append(eval(i))

    dados_f = []
    dados_f.append(cria_posicao(dados[0][0], dados[0][1]))   # Capta o tamanho do prado

    rochas = ()
    for i in dados[1]:
        rochas = rochas + (cria_posicao(i[0], i[1]),)        # Capta as posições dos rochedos
    dados_f.append(rochas)

    animais = ()
    posicoes = ()

    # Capta os animais e as posições dos mesmos
    for i in range(2, len(dados)):
        animais = animais + (cria_animal(dados[i][0], dados[i][1], dados[i][2]),)
        posicoes = posicoes + (cria_posicao(dados[i][3][0], dados[i][3][1]),)

    dados_f.append(animais)
    dados_f.append(posicoes)
    return cria_prado(dados_f[0], dados_f[1], dados_f[2], dados_f[3])
