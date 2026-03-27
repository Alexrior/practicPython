def analyze_numbers(nums):
    if len(set(nums)) == 1:
        return "Все числа равны"
    elif len(set(nums)) == len(nums):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"


numbers = list(map(int, input().split()))
print(analyze_numbers(numbers))