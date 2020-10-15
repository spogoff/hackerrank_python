if __name__ == '__main__':
    nested_students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        nested_students.append([name,score])


second_highest = sorted(list(set([score for name, score in nested_students])))[1]
print('\n'.join(name for name, score in sorted(nested_students) if score == second_highest))
