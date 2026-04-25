from typing import List, NamedTuple


class Statistics(NamedTuple):
    total: float
    average: float
    maximum: float
    minimum: float


def calculate_statistics(numbers: List[int]) -> Statistics:
    """Calcula soma, média, maior e menor valor de uma lista de números."""
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return Statistics(total=total, average=average, maximum=maximum, minimum=minimum)


def format_statistics(statistics: Statistics) -> str:
    """Retorna uma string formatada com os valores calculados."""
    return (
        f"total: {statistics.total}\n"
        f"media: {statistics.average}\n"
        f"maior: {statistics.maximum}\n"
        f"menor: {statistics.minimum}"
    )


def main() -> None:
    """Executa o cálculo de estatísticas para uma lista de exemplo."""
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    statistics = calculate_statistics(numbers)
    print(format_statistics(statistics))


if __name__ == "__main__":
    main()
