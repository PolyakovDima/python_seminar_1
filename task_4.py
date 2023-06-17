def count_cranes(s):
    x = (2 * s) / 3
    petya_seryozha = x / 2
    return petya_seryozha, x

total_cranes = 18
petya_seryozha_cranes, katya_cranes = count_cranes(total_cranes)
print("Количество журавликов, сделанных Петей и Серёжей:", petya_seryozha_cranes)
print("Количество журавликов, сделанных Катей:", katya_cranes)
