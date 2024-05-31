# 1st one
x = int(input())
y = int(input())
z = int(input())
n = int(input())

print(sorted([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!= n]))

#2nd one
n = int(input())
scores = list(map(int, input().split()))

# Find the maximum score
max_score = max(scores)

# Remove the maximum score from the list
scores = [score for score in scores if score < max_score]

# Find the new maximum score (runner-up score)
runner_up_score = max(scores)

print(runner_up_score)

#3rd one
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    second_lowest_students = [x[0] for x in students if x[1] == second_lowest_score]
    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)
        
#4th one
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average))

#5th one
def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#6th one
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, size + 1):
        line = "-".join(alphabet[size - i:size])
        print((line[::-1] + line[1:]).center(4 * size - 3, "-"))
    for i in range(size - 1, 0, -1):
        line = "-".join(alphabet[size - i:size])
        print((line[::-1] + line[1:]).center(4 * size - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#7th one
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if kevin_score > stuart_score:
        print("Kevin " + str(kevin_score))
    elif kevin_score < stuart_score:
        print("Stuart " + str(stuart_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
