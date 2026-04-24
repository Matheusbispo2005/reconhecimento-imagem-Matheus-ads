# Explicação do código `num_primos.py`

Este arquivo contém a função `eh_primo(n)`, que verifica se um número inteiro `n` é primo.

## Como a função funciona

1. `if n <= 1:`
   - Números menores ou iguais a 1 não são primos.
   - A função retorna `False` nesses casos.

2. `if n <= 3:`
   - Os números 2 e 3 são primos.
   - A função retorna `True` para esses valores.

3. `if n % 2 == 0 or n % 3 == 0:`
   - Se `n` for divisível por 2 ou por 3, não é primo.
   - A função retorna `False` nesses casos.

4. Verificação por outros divisores:
   - A partir de 5, a função verifica apenas números da forma `6k - 1` e `6k + 1`.
   - Isso acontece porque todo número primo maior que 3 é da forma 6k ± 1.
   - A variável `i` começa em 5 e incrementa de 6 em 6.

5. `while i * i <= n:`
   - O loop continua enquanto `i` ao quadrado for menor ou igual a `n`.
   - Isso é suficiente para encontrar um divisor, caso exista, e torna a verificação mais eficiente.

6. `if n % i == 0 or n % (i + 2) == 0:`
   - A função testa se `n` é divisível por `i` ou por `i + 2`.
   - Se for divisível, retorna `False`.

7. `return True`
   - Se nenhum divisor for encontrado, `n` é primo.

## Bloco de teste

O trecho abaixo é executado apenas quando o arquivo é rodado diretamente:

```python
if __name__ == "__main__":
    teste_numeros = [1, 2, 3, 4, 16, 17, 18, 19, 20, 23]
    for numero in teste_numeros:
        print(f"{numero} {'primo' if eh_primo(numero) else 'não é primo'}")
```

- Ele define uma lista de números para testar.
- Para cada número, imprime se ele é primo ou não.

## Resumo

- `eh_primo(n)` retorna `True` se `n` for primo.
- A função evita verificações desnecessárias usando propriedades dos primos.
- O teste demonstra o comportamento com alguns exemplos comuns.
