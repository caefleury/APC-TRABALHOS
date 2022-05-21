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
            print(f" * {aula['nome']} ({aula['codigo']}):")
            for c in range(len(sorteado)):
                print(f"     Turma {sorteado[c][0]}: {sorteado[c][1]} ({sorteado[c][2]} alunos)")
        print(f"[Carga total considerada: {int(carga_total)}h ({(carga_total/total_alunos):.2f}h/aluno)]")
    else:
        print(f'No hay {docente}...')
        
def disciplina(n,arquivos):
    materias_com_turmas = []
    nohay = True
    for arquivo in arquivos:
        with open(arquivo, encoding='utf-8') as file:
            next(file)
            reader = list(csv.reader(file))
            codigos = []
            codigos_candidatos = []
            codigos_nomes = []
            for line in reader:
                codigo = line[0]
                #nome = line[1]
                codigos.append(codigo)
                i = -1
            for codigo in codigos:
                if codigos.count(codigo) >= n and codigo not in codigos_candidatos:
                    codigos_candidatos.append(codigo)
            for codigo_candidato in codigos_candidatos:
                for line in reader:
                    if line[0] == codigo_candidato:
                        if [line[0],line[1]] not in codigos_nomes:
                            codigo_nome = [line[0],line[1]]
                            codigos_nomes.append(codigo_nome)
            for codigonome in codigos_nomes:
                turmas_candidatas = []
                turmas = {}
                for line in reader:
                    if line[0] == codigonome[0]:
                        turmas_candidatas.append(line[2])
                for turma in turmas_candidatas:
                    count = turmas_candidatas.count(turma)
                    if count >= n:
                        turmas[turma] = count
                if turmas != {}:
                    turmas = dict(sorted(turmas.items()))
                    codigonome.append(turmas)
                    materias_com_turmas.append(codigonome)
                
    materias_com_turmas = sorted(materias_com_turmas,key=operator.itemgetter(1))
    if materias_com_turmas == []:
        print(f"No hay {n}...")
    else: # escreve o print
        print(f"Turmas com pelo menos {n} docentes:")
        for materia in materias_com_turmas: 
            print(f" * {materia[1]} ({materia[0]}): ",end='') 
            lista_de_turmas = materia[2].items()
            string = []
            for turma in lista_de_turmas:
                string.append(f"{turma[0]} ({turma[1]})") 
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
        print(f'No hay {nohay}...')
    for array in arrays:
        print(f"{array[0]} matriculados em {array[1]} ({array[2]})")
            
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
    elif comando == 'FIM':
        break
    else:
        print(f"No hay {codigo}...")

