def DAVALEBIS_DAWERA():
    cvladi = int(input("ნივთის ფასი: "))
    meore_cvladi = int(input("ნივთის რაოდენობა: "))
    print(f"ნივთის ყიდვისას შენ უნდა გადაიხადო: {cvladi * meore_cvladi} ლარი")

    asaki = int(input("რამდენი წლის ხარ?"))
    print(f"10 welshi shen iqnebi {asaki + 10} wlis")
    meorecvlad = int(input("ramdeni wlisaa sheni ojaxiswevri? "))
    print(f"shei ojaxis wevria: {meorecvlad + 10} wlis")

    print("ნომერი 3: ", 2 + 2 - 3 * 2 + 6 / 3)

    sheni_saxeli = input("chawere sheni saxeli: ")
    sheni_asaki = int(input("chawere sheni asaki: "))
    print(f"sheni saxelia: {sheni_saxeli}, sheni asakia: {sheni_asaki} weli")

    tqveni_asaki = int(input("chawere ramdeni wlis xar: "))
    mshoblis_asaki2 = int(input("chawere ramdeni wlis aris sheni mshobeli: "))
    if mshoblis_asaki2 > tqveni_asaki:
        print("10 welshi sheni mshobeli iqneba")
        print((mshoblis_asaki2 + 10) - (tqveni_asaki + 10), "wlit didi shens asakze")
    else:
        print("paps nu atyueeeb!!")

DAVALEBIS_DAWERA()