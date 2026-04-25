# Explicação do código `num_primos.py`

Este arquivo contém uma função para verificar se um número inteiro é primo e um bloco de execução para testar alguns exemplos.

## Estrutura do código

- `TESTE_NUMEROS` contém a lista de números usados no teste.
- `eh_primo(numero)` verifica se um número é primo.
- `formatar_resultado(numero)` monta a mensagem de saída.
- `main()` executa os testes e imprime os resultados.

## Como `eh_primo(numero)` funciona

1. `numero <= 1`
   - Números menores ou iguais a 1 não são primos.
   - Retorna `False`.

2. `numero <= 3`
   - 2 e 3 são primos.
   - Retorna `True`.

3. `numero % 2 == 0 or numero % 3 == 0`
   - Números pares maiores que 2 ou divisíveis por 3 não são primos.
   - Retorna `False`.

4. Verificação com outros divisores:
   - A função testa divisores a partir de 5.
   - Ela usa um padrão de incremento de 6 em 6 para verificar apenas os candidatos `6k - 1` e `6k + 1`.
   - Isso reduz a quantidade de verificações sem perder precisão.

5. `while divisor * divisor <= numero:`
   - O loop para quando o divisor ultrapassa a raiz quadrada de `numero`.
   - Se não encontrar divisor até esse ponto, o número é primo.

6. `if numero % divisor == 0 or numero % (divisor + 2) == 0:`
   - Verifica se `numero` é divisível por `divisor` ou `divisor + 2`.
   - Retorna `False` se um divisor for encontrado.

7. `return True`
   - Se não houver divisor válido, o número é primo.

## Como a saída é montada

- `formatar_resultado(numero)` retorna uma string como:
  - `"17 primo"`
  - `"20 não é primo"`

## Execução principal

No bloco:

```python
if __name__ == "__main__":
    main()
```

- `main()` percorre `TESTE_NUMEROS`.
- Para cada número, imprime o resultado formatado.

## Vantagens do código atualizado

- Nomes de funções e variáveis mais claros.
- Funções pequenas e separadas em responsabilidades.
- Uso de tipagem simples com `int` e `List[int]`.
- Bloco `main()` deixa a execução mais organizada.
