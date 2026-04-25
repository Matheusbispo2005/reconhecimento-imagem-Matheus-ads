from typing import List

TESTE_NUMEROS: List[int] = [1, 2, 3, 4, 16, 17, 18, 19, 20, 23]


def eh_primo(numero: int) -> bool:
    """Retorna True se o número informado for primo."""
    if numero <= 1:
        return False

    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= numero:
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def formatar_resultado(numero: int) -> str:
    """Retorna uma mensagem formatada com o resultado do teste de primalidade."""
    resultado = "primo" if eh_primo(numero) else "não é primo"
    return f"{numero} {resultado}"


def main() -> None:
    """Executa o teste de primalidade para uma lista de números."""
    for numero in TESTE_NUMEROS:
        print(formatar_resultado(numero))


if __name__ == "__main__":
    main()
