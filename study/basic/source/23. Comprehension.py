numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []

# for문
for number in numbers:
    if number %2 == 1:
        odd_numbers.append(number)
        




# Comprehension 사용
# List를 만들때 for문과 if문 등을 사용하여 간결하게 만드는 방법
odd_numbers = [number for number in numbers if number % 2 == 1]

print(odd_numbers)
