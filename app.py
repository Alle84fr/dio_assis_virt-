
#_______ DADOS DO CLIENTE

saldo_total_cc = 5000.00
contas_fixas = {"Condomínio": 1540.00, "IPTU": 180.00, "Celular": 150.00, "Internet": 75.89, "Convênio": 642.89}
contas_variaveis = {"Luz": 200.00, "Agua": 90.00, "Pet": 65.00, "Curso": 230.00}
aplicacoes = {"Reserva": 250.50, "Viagem": 500.00}

total_fixo_var = sum(contas_fixas.values()) + sum(contas_variaveis.values()) 
valor_disponivel_real = 1255.72 

def alle_chat():
    global valor_disponivel_real
    print("🤓 Bem vindo/a! Vamos verificar nossos gastos hoje ou deseja sair? 💰")
    
    while True:
        print(f"\nSaldo disponível hoje: R$ {valor_disponivel_real:.2f}")
        
        #_______ Pergunta

        pergunta_inicial = input("Deseja comprar,gastar ou sair?'): ").lower().strip()

        if pergunta_inicial == 'sair':
            print("Precisando, é só chamar a Alle")
            break

        #_______ Texto

        if any(x in pergunta_inicial for x in ["senha", "acesso", "recuperar"]):
            print("\nNão tenho permissão para acessar sensíveis. Entrar no app ou entrar em contato com atendentes do banco.")
            print("NUNCA DIGITE DADOS DE ACESSO OU IMPORTANTES EM APPS QUE NÃO SEJAM OFICIAIS.")
            continue

        elif any(x in pergunta_inicial for x in ["triplicar", "investir", "rendimento"]):
            print("\nExistem muitas formas de aumentar seu rendimentos, como aplicações, melhores salários, empregos extras.")
            print("Perguntas muito específicas como esta, que depende de um humano, terá uma melhor responda quando perguntada diretamente para seu gerente.")
            continue

        elif any(x in pergunta_inicial for x in ["burra", "fracasso", "triste"]):
            print("\nTodos nós temos nossas fraqueses e momentos em que gastamos mais, isso acontece com todos.")
            print("Meu objetivo é mostrar para onde os gastos estão indo e assim, podermos nos organizar cada vez melhor")
            continue

        #_______ Valor

        valor_input = input(f"Qual valor a ser gasto com '{pergunta_inicial}'? R$ ").replace(',', '.')
        
        try:
            valor_compra = float(valor_input)
            print("\n🧐 Vamos analisar! 🧮")

            #_______ Saldo Positivo

            if valor_compra <= valor_disponivel_real:
                resto = valor_disponivel_real - valor_compra
                print(f"Já descontando o valor R$ {total_fixo_var:.2f} fixo com variável, se gastar R$ {valor_compra:.2f} ainda lhe sobrará R$ {resto:.2f}")
                print(f"Salvo você ter algum custo não pré-agendado, com valor igual ou acima de R$ {resto:.2f}, esta compra não irá lhe trazer problema financeiro")
                valor_disponivel_real = resto 

            #_______ Saldo em Risco

            else:
                resto = valor_disponivel_real - valor_compra
                print(f"Já descontando o valor R$ {saldo_total_cc:.2f} fixo e o variável, se gastar R$ {valor_compra:.2f} ainda lhe sobrará R$ {resto:.2f}")
                print(f"Esta compra pode comprometer o pagamento em dias das contas fixas e variáveis pré agendadas.")
                print(f"Esta comprando não sendo necessário, seria melhor ou dividir ou não gastar este dinheiro este mês")
                print(f"Com esta compra seu saldo será de R$ {resto:.2f}, e poderá falta R$ {abs(resto):.2f}")
                
                vezes_agua = valor_compra / contas_variaveis["Agua"]
                print(f"💡 DICA: este valor se vc não usar pode pagar conta de água por {int(vezes_agua)} meses, por exemplo")

        except ValueError:
            print("🥺 Valor inválido. Por favor, use apenas números.")

        print("\nA resposta dada foi compreendida? Respondeu à sua pergunta?")

        feedback = input("A resposta foi satisfatória? (sim/nao): ").lower().strip()
        
        if feedback == "sim":
            print("-" * 40)
            continue # Volta para a primeira pergunta
        else:
            input("O que eu poderia melhorar na minha resposta? ")
            print("Vou melhorar meu treinamento e respondo mais tarde")
            print("-" * 40)
        print("-" * 40)

#_______ Iniciar
alle_chat()
