from random import randint

def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]

    if len (cpf) != 11:
        print("CPF Inválido, por favor digite novamente.")

    if cpf == cpf[::-1]:
        print("CPF Inválido, por favor digite novamente.")

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def cpf_generate():
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    result = ''.join(map(str, cpf))
    return result

opcao = int(input('Qual ação deseja realizar?\n'
                  '[1] Validar um CPF\n'
                  '[2] Gerar um CPF\n'
                  'Input:'))

if opcao == 1:
    cpf = input('Digite o CPF: ')
    if cpf_validate(cpf):
        print('CPF Válido.')
    else:
        print('CPF Inválido.')


elif opcao == 2:
    cpf = cpf_generate()
    if cpf_validate(cpf):
        print(f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    else:
        print('Inválido')