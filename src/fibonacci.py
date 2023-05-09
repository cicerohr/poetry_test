# -*- coding: utf-8 -*-
"""Sequência de Fibonacci.

Este código foi criado por Mandy Wong (c) 2021.

    @author: Mandy Wong.
    @modified by: Cícero.
    @link: https://realpython.com/fibonacci-sequence-python/
"""
import timeit


class Fibonacci:
    """Sequência de Fibonacci recursiva com cache.

    Examples:
        >>> fibonacci_test = Fibonacci()
        >>> fibonacci_test(0)
        0
        >>> fibonacci_test(7)
        13
    """

    def __init__(self) -> None:
        """Inicializa o cache."""
        self.cache: list = [0, 1]

    def __call__(self, n: int) -> int:
        """Este método transforma as instâncias de Fibonacci
        em objetos chamáveis.

        Arguments:
            n (int): Número de Fibonacci solicitado.

        Returns:
            int: Número de Fibonacci solicitado.

        Raises:
            ValueError: Esperado um número inteiro positivo; obteve "{n}"
        """

        # Validar o valor de n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(
                f'Esperado um número inteiro positivo; obteve "{n}"'
            )

        # Verifique se há números de Fibonacci computados
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Calcular e armazenar em cache o número de Fibonacci solicitado
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


if __name__ == '__main__':
    fibonacci_de = Fibonacci()
    numero = 8

    inicio = timeit.default_timer()
    sequencia = [fibonacci_de(n) for n in range(numero)]
    fim = timeit.default_timer()
    print(f'{sequencia}\nTempo de execução: {fim - inicio} s')
    print(fibonacci_de(numero))
