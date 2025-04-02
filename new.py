while True:
    import random
    barvicky = ["ruzova", "modra", "zelena", "cervena", "cerna", "bila"]
    novaBarvicka = input("zadejte novou barvu")
    barvicky.append(novaBarvicka)
    print(random.choice(barvicky))
    UzNe = input("chcete pokracova ano/ne")
    if UzNe == "ne":
        break