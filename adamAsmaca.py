kelime = "samanyolu"
bilinen = []
can = 5

while can != 0:
    print("Kalan hak : {}".format(can))

    for harf in kelime:
        if harf in bilinen:
            print(harf, end = " ")
        else:
            print("*",end = " ")
    harf = input("\nHarf giriniz : ")

    if harf in kelime:
        bilinen.append(harf)

    else:
        print(harf + " harfi cevapta yok")
        can = can - 1
        print("kalan can :{}".format(can))

    if set(kelime) == set(bilinen):
        print("Tebrikler")
        break

if can == 0:
    print("Caniniz kalmadi")
