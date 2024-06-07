def DAVALEBIS_DAWERA():
    numbers = [float(input()) for _ in range(5)]
    result = numbers[0] * numbers[1] / numbers[2] // numbers[3] - numbers[4] + numbers[0] % numbers[4]
    print(result)
    age = int(input())
    print(18 < age < 20)
    results = [
        (5 > 3, 10 > 7, 2 > 5, -1 > -5, 100 > 50), 
        (3 < 5, 7 < 10, 5 < 2, -5 < -1, 50 < 100),  
        (3 <= 5, 7 <= 10, 5 <= 5, -5 <= -1, 50 <= 100), 
        (5 >= 3, 10 >= 7, 5 >= 5, -1 >= -5, 100 >= 50),  
        (5 != 3, 10 != 7, 5 != 5, -1 != -5, 100 != 50), 
        (5 == 5, 10 == 10, 5 == 3, -1 == -1, 100 == 50) 
    ]
    for result_set in results:
        print(*result_set)
    num_int = int(input())
    num_float = float(input())
    print(type(num_int) == type(num_float))
    print(type(1), type(2.5), type("gela"))

DAVALEBIS_DAWERA()

