# Base de Conhecimento


## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
# Dados do Cliente
saldo_total_cc = 5000.00

# Lista de contas (Dicionário simples)
contas_fixa = {
  "Condomínio": 1540.00,
  "IPTU": 180.00,
  "Celular": 150.00,
  "Internet": 75.89,
  "Convênio": 642.89,
}

contas_variavel = {
  "Luz": 200.00,
  "Agua": 90.00,
  "Pet": 65.00,
  "Curso": 230.00,
}

de fixo gasta-se 2.408,78
de variaveis gasta-se 585,00
gastos prováveis = 2993,78

ficando = 2006,22 para outros gastos

aplicação = {
  "Reserva": 250.50,
  "Viagem": 500.00
}

Valor para gastar = 1255,72

pessoa quer gastar 1000 em roupa


# Cálculos automáticos
total_contas = sum(contas.values())
saldo_apos_contas = saldo_total - total_contas
saldo_final = saldo_apos_contas - desejo_compra_valor
...
```
Dados diretamente no prompt

Para simplicar "enjetar" dados no prompt, garantindo que o agente tenha melhor contexto
