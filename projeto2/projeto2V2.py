import os
import csv
import operator

def carga(docente,arquivos):
    grade = []
    carga_total = 0
    total_alunos = 0
    for arquivo in arquivos:
        with open(arquivo, encoding='utf-8') as file:
            next(file)
            reader = csv.reader(file)
            for line in reader:
                if docente in ' '.join(line[4].split()[:-1]):
                    d = {
                        'codigo': line[0],
                        'nome': line[1],
                        'turma':[line[2]],
                        'hora' : [line[4].split()[-1].replace('(','').replace(')','')],
                        'alunos': [line[-2]]
                        }
                    if int(''.join(d['alunos'])) >= 6:
                        carga_total += float(''.join(d['hora']).replace('h',''))
                        total_alunos += float(''.join(d['alunos'])) 
                    existe = False
                    for aula in grade:
                        if d['codigo'] in aula['codigo']:
                            existe = True
                            aula['turma'].append(''.join(d['turma']))
                            aula['hora'].append(''.join(d['hora']))
                            aula['alunos'].append(''.join(d['alunos']))
                    if existe == False:
                        grade.append(d)
                    
    if grade != []:
        grade.sort(key=operator.itemgetter('nome'))
        print(f"{docente}:")
        for aula in grade:
            sorteado = sorted(zip(aula['turma'], aula['hora'],aula['alunos']))
            print(f" * {aula['nome']} ({aula['codigo']}): ")
            for c in range(len(sorteado)):
                print(f"     Turma {sorteado[c][0]}: {sorteado[c][1]} ({sorteado[c][2]} alunos)")
        print(f"[Carga total considerada: {int(carga_total)}h ({(carga_total/total_alunos):.2f}h/aluno)]")
    else:
        print(f'No hay {docente}...')
        
def disciplina(n,arquivos):
    materias = []
    sorted(materias,key=operator.itemgetter(2))
    for materia in materias:
        if len(materia) == 2:
            materias.remove(materia)
    
    nohay = True
    for arquivo in arquivos:
        with open(arquivo, encoding='utf-8') as file:
            next(file)
            reader = list(csv.reader(file))
            for line in reader:
                codigo = line[0]
                nome = line[1]
                i = 1
                if codigo not in materias:
                    for row in reader:
                        if row[0] == codigo:
                            i += 1
                if i >= n:
                    materia = []
                    materia.append(codigo)
                    materia.append(nome)
                    materias.append(materia)

            """# ------ ordem alfabetica ------
            
            for materia in materias:
                for line in reader:
                    if line[0] == materia:
                        materias_por_nome.append(line[1])
                        break
            materias_por_nome = sorted(materias_por_nome)
            materias_por_codigo_sorted = []
            for materia in materias_por_nome:
                for line in reader:
                    if line[1] == materia:
                        materias_por_codigo_sorted.append(line[0])
                        break
            # ----------------------------- #"""

            for materia in materias: 
                turmas = []
                turmas_com_n = {}
                for line in reader:
                    if line[0] == materia[0]:
                        turmas.append(line[2])
                for turma in sorted(turmas):
                    if sorted(turmas).count(turma) >= n:
                        turmas_com_n[turma] = n
                        nohay = False
                if turmas_com_n != {}:
                    materia.append(turmas_com_n)

    if nohay:
        print(f"No hay {n}...")
    else: # escreve o print
        print(f"Turmas com pelo menos {n} docentes:")
        for materia in materias: 
            for line in reader:
                if line[0] == materia:
                    turmas.append(line[2])
            for turma in sorted(turmas):
                if turmas.count(turma) >= n:
                    maior_que_n = True
                    nohay = False
                    turmas_com_n[turma] = turmas.count(turma)
            for row in reader:
                if row[0] == materia:
                    nome_da_materia = row[1]
                    break
            for key in turmas_com_n:
                turmas_com_n[key] = str(turmas_com_n[key])
            if maior_que_n:
                print(f" * {nome_da_materia} ({materia}): ",end='') 
                lista_de_turmas = turmas_com_n.items()
                #print(lista_de_turmas)
                key_list = list(turmas_com_n)
                string = []
                for key,value in lista_de_turmas:
                        string.append(f"{key} ({value})") 
                print(', '.join(string))
            
def matriculas(codigos,arquivos):
    arrays = []
    nohays = []
    for arquivo in arquivos:
        with open(arquivo, encoding='utf-8') as file:
            next(file)
            reader = list(csv.reader(file))
            for codigo in codigos:
                turmas = []
                array = []
                matriculados = 0
                for row in reader:
                    if row[0] == codigo:
                        nome = row [1]
                        if row[2] not in turmas:
                            turmas.append(row[2])
                            matriculados += int(row[7])
                if matriculados == 0:
                    nohays.append(codigo)
                else:
                    array.append(matriculados)
                    array.append(nome)
                    array.append(codigo)

                    arrays.append(array)
    arrays = sorted(arrays, key=operator.itemgetter(1))
    arrays = sorted(arrays, key=operator.itemgetter(0), reverse=True)
    for array in arrays:
        for nohay in nohays:
            if nohay == array[2]:
                nohays.remove(nohay)
    nohays = list( dict.fromkeys(nohays) )
    for nohay in nohays:
        print(f'No hay {nohay}...↩')
    for array in arrays:
        print(f"{array[0]} matriculados em {array[1]} ({array[2]})")
            
#Código,Nome,Turma,Ano-Período,Docente,Horário,Qtde Vagas Ofertadas,Qtde Vagas Ocupadas,Local
def leiaArquivo(arquivo):
    arquivos_lidos = [arquivo]
    while True:
        string = input().split()
        comando = string[0]
        parametro = ' '.join(string[1:])
        codigos = string[1:]
        if comando == 'carga':
            carga(parametro,arquivos_lidos)
        elif comando == 'disciplina':
            disciplina(int(parametro),arquivos_lidos)
        elif comando == 'matriculas':
            matriculas(codigos,arquivos_lidos)
        elif comando == 'FIM':
            break
        elif comando == 'leia':
            if parametro not in arquivos_lidos:
                arquivos_lidos.append(parametro)
        # def procurar -. true 

# CHECAR SE PASSOU PELO LEIA ANTES DE PEDIR FIM

while True:
    string = input().split()
    comando = string[0]
    codigo = ' '.join(string[1:])
    matriculax = string[1:]
    if comando == 'leia':
        nohay = False
        arq = string[1]
        leiaArquivo(arq)
        break
    elif comando == 'matriculas':
        for matricula in matriculax:
            print(f"No hay {matricula}...")
    else:
        print(f"No hay {codigo}...")

