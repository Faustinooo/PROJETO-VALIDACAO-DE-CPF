from MOD import *
for i in range(10):
    erro = "\033[31mERRO DIGITE NOVAMENTE\033[m"
    while True:
        cpp = gerador(1)
        cpf = cpp.strip().replace(".","").replace("-","").replace(",","")
        print(cpp)
        if len(cpf) > 11 or len(cpf) < 11:
            print(erro)
            continue
        break
    conta = contacpf(a=cpf[:9])
    if conta > 9:
        conta = 0
    cpf2 = cpf[:9] + str(conta)
    conta2 = contacpf2(cpf2[:10])
    if conta2 > 9:
        conta2 = 0
    if conta == int(cpf[9]) and conta2 == int(cpf[10]):
        print(f"\033[32mCPF VÁLIDO, PRIMEIRO DÍGITO = {conta} E SEGUNDO DÍGITO = {conta2}\033[32m")
    elif conta != int(cpf[9]) and conta2 != int(cpf[10]):
        print(
            f"\033[31mCPF INVÁLIDO, AMBOS DÍGITOS NÃO COINCIDEM, PRIMEIRO DÍGITO = {conta} E SEGUNDO DÍGITO = {conta2}\033[m")
    elif conta != int(cpf[9]) and conta2 == int(cpf[10]):
        print(
            f"CPF INVÁLIDO, SEGUNDO DÍGITO NÃO COINCIDE, \033[31mPRIMEIRO DÍGITO = {conta}\033[m E \033[32mSEGUNDO DÍGITO = {conta2}\033[m")
    elif conta == int(cpf[9]) and conta2 != int(cpf[10]):
        print(
            f"CPF INVÁLIDO, SEGUNDO DÍGITO NÃO COINCIDE, \033[32mPRIMEIRO DÍGITO = {conta}\033[m E \033[31mSEGUNDO DÍGITO = {conta2}\033[m")