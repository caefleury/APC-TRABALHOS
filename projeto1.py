horarios = [
    "08:00 - 08:55", #M1
    "08:55 - 09:50", #M2
    "10:00 - 10:55", #M3
    "10:55 - 11:50", #M4
    "12:00 - 12:55", #M5
    "12:55 - 13:50", #T1
    "14:00 - 14:55", #T2
    "14:55 - 15:50", #T3
    "16:00 - 16:55", #T4
    "16:55 - 17:50", #T5
    "18:00 - 18:55", #T6
    "19:00 - 19:50", #N1
    "19:50 - 20:40", #N2
    "20:50 - 21:40", #N3
    "21:40 - 22:30" #N4
]
grade = [
    ["        ","        ","        ","        ","        ","        "], #nM1 0 ["2M1","3M1","4M1","5M1","6M1","7M1"]
    ["        ","        ","        ","        ","        ","        "],#nM2 1
    ["        ","        ","        ","        ","        ","        "],#nM3 2
    ["        ","        ","        ","        ","        ","        "],#nM4 3
    ["        ","        ","        ","        ","        ","        "],#nM5 4
    ["        ","        ","        ","        ","        ","        "],#nT1 5
    ["        ","        ","        ","        ","        ","        "],#nT2 6
    ["        ","        ","        ","        ","        ","        "],#nT3 7
    ["        ","        ","        ","        ","        ","        "],#nT4 8
    ["        ","        ","        ","        ","        ","        "],#nT5 9
    ["        ","        ","        ","        ","        ","        "],#nT6 10
    ["        ","        ","        ","        ","        ","        "],#nN1 11
    ["        ","        ","        ","        ","        ","        "],#nN2 12
    ["        ","        ","        ","        ","        ","        "],#nN3 13
    ["        ","        ","        ","        ","        ","        "],#nN4 14
    ]
divisao = "+---------------+----------+----------+----------+----------+----------+----------+"
dias_da_semana = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"

def diasDaSemana():
    print(f"{divisao}\n{dias_da_semana}\n{divisao}")


def split(palavra):
    return [char for char in palavra]


def desenhadorDeGrade():
    count = 0
    diasDaSemana()
    for row in grade:
        vazio = True
        for celula in row:
            if celula != "        ":
                vazio = False
                break
        if vazio == False:
            print(f"| {horarios[count]} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} |")
            print(divisao)
        count += 1

while True:
    string = input()
    splitado = string.split()
    if string == "Hasta la vista, beibe!":
        break
    elif string == "?":
        desenhadorDeGrade()
    else:
        if splitado[0] == "+":
            soma = True
        elif splitado[0] == "-":
            soma = False
        codigo = splitado[1]
        for dth in splitado[2:]:
            for i in dth:
                if i in "MTN":
                    index = dth.index(i)
                    break
            dth_splitado = split(dth)
            if dth_splitado[index] == "M": #selecionei turno
                for hor in dth_splitado[index + 1:]: #selecionei horario do turno / row da grade
                    erro = False
                    for i in dth_splitado[:index]:
                        if grade[int(hor) - 1][int(i) - 2] == "        " and soma:
                            grade[int(hor) - 1][int(i) - 2] = codigo
                        elif grade[int(hor) - 1][int(i) - 2] == codigo and soma == False:
                            grade[int(hor) - 1][int(i) - 2] = "        "
                        else:
                            erro = True
                            print(f"!({splitado[0]} {codigo} {dth})")
                            break
                    if erro:
                        break
            elif dth_splitado[index] == "T":
                for hor in dth_splitado[index + 1:]:
                    erro = False
                    for i in dth_splitado[:index]:
                        if grade[(int(hor) - 1) + 5][int(i) - 2] == "        " and soma:
                            grade[(int(hor) - 1) + 5][int(i) - 2] = codigo
                        elif grade[(int(hor) - 1) + 5][int(i) - 2] == codigo and soma == False:
                            grade[(int(hor) - 1) + 5][int(i) - 2] = "        "
                        else:
                            erro = True
                            print(f"!({splitado[0]} {codigo} {dth})")
                            break
                    if erro:
                        break
            elif dth_splitado[index] == "N":
                for hor in dth_splitado[index + 1:]:
                    erro = False
                    for i in dth_splitado[:index]:
                        if grade[(int(hor) - 1) + 11][int(i) - 2] == "        " and soma:
                            grade[(int(hor) - 1) + 11][int(i) - 2] = codigo
                        elif grade[(int(hor) - 1) + 11][int(i) - 2] == codigo and soma == False:
                            grade[(int(hor) - 1) + 11][int(i) - 2] = "        "
                        else:
                            erro = True
                            print(f"!({splitado[0]} {codigo} {dth})")
                            break
                    if erro:
                        break