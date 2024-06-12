def DAVALEBIS_DAWERA():
    fruits = ["apple", "banana", "cherry"]
    [print(x) for x in fruits]
    [print(x) for x in "banana"]
    [print(x) for x in fruits if x == "banana"]
    [print(x) for x in fruits if x != "banana"]
    [print(i + 4) for i in range(100)]
    [print(i - 4) for i in range(100)]
    [print(i / 4) for i in range(100)]
    [print(i * 4) for i in range(100)]
    [print(i < 4) for i in range(100)]
    [print(i > 4) for i in range(100)]
    num = int(input("chawere ricxvi: "))
    print("0-dan " + str(num) + "-mde ricxvebis jami aris: " + str(sum(range(num + 1))))
    ricxvi1 = int(input("chawere pirveli ricxvi: "))
    ricxvi2 = int(input("chawere meore ricxvi: "))
    result_multiply = ricxvi1 * ricxvi2
    result_add = ricxvi1 + ricxvi2
    print("namravli:", result_multiply, "\njami:", result_add)

DAVALEBIS_DAWERA()
