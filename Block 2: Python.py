# №1 Изоморфизмы
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}

    for cs, ct in zip(s, t):
        if cs in map_s_to_t:
            if map_s_to_t[cs] != ct:
                return False
        else:
            if ct in map_t_to_s:
                return False
            map_s_to_t[cs] = ct
            map_t_to_s[ct] = cs

    return True
# Время: Функция проходит по строкам один раз и делает только операции словаря со средней сложностью 𝑂(1). Итоговая сложность: 𝑂(𝑛) 
# быстрее сделать невозможно, потому что строку всё равно нужно прочитать целиком.
# Память: Хранится максимум по одному отображению на каждый уникальный символ. Итоговая сложность: 𝑂(𝑘), 
# где 𝑘 — число уникальных символов (в худшем случае 𝑘=𝑛).


# №2 Натуральная последовательность 
def missing_number_sum(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2 # сумма арифметической прогрессии
    return total - sum(nums)
# Время: 𝑂(𝑛) - один проход по массиву (и при сумме ещё константный расчёт).
# Память: 𝑂(1) - используются только несколько скалярных переменных.


# №3 Факторизация
def prime_factors(n: int) -> list[int]:
    if n <= 1:
        return []
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    if n > 1:
        factors.append(n)

    return factors
# Время: 𝑂(√𝑛) в худшем случае (для простого 𝑛 придётся проверить делители до √𝑛).
# Память: 𝑂(log⁡𝑛) - список множителей содержит не более 𝑂(log𝑛) элементов (при разложении на множители 2).
