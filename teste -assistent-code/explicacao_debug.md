# Explicação dos erros em `debug.py`

## Erros detectados e correções

1. `item1 = float(input(Preço do item 1? ))`
   - Erro: falta de aspas na string do `input()`.
   - Causa: Python tenta interpretar `Preço` como nome de variável.
   - Correção: adicionar aspas para formar `input("Preço do item 1? ")`.

2. `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
   - Erro: `input()` retorna uma string e em seguida o código tenta dividir essa string por 100.
   - Causa: operações matemáticas só funcionam com tipos numéricos (`int` ou `float`).
   - Correção: converter o valor para `float` imediatamente após o `input()`.

3. `print(" Item 2:        R$ {total_item2:.2f}")`
   - Erro: string não era formatada com `f` antes das aspas.
   - Causa: sem `f`, o Python imprime o texto literal incluindo `{total_item2:.2f}`.
   - Correção: usar `print(f" Item 2:        R$ {total_item2:.2f}")`.

4. `if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
   - Erro: indentação incorreta dentro do bloco `if`.
   - Causa: Python exige indentação para o corpo de condicionais e loops.
   - Correção: adicionar 4 espaços antes do `print()` dentro do `if`.

5. `print(f" TOTAL:         R$ {round(total, 2):.2f}")`
   - Observação: `round(total, 2)` funciona, mas é desnecessário quando já se usa formatação `:.2f`.
   - Ajuste: usar `print(f" TOTAL:         R$ {total:.2f}")` para manter o código mais claro.

## Código ajustado

O arquivo `debug.py` foi corrigido para funcionar sem erros de sintaxe ou de tipo. As principais mudanças são:

- String de prompt correta para `item1`.
- Conversão de `desconto_cupom` para `float`.
- Uso correto de f-strings em todas as linhas de impressão.
- Indentação apropriada dentro do bloco `if desconto_cupom > 0:`.
- Formatação consistente do valor final `total`.

## Resultado esperado

Ao rodar o código corrigido, o programa:

- solicita o nome do cliente
- pergunta quantidade e preço de três itens
- calcula subtotal, imposto de 10% e desconto
- exibe o total formatado corretamente

## Observação

Se `desconto_cupom` for 0, a linha de desconto não será exibida.
