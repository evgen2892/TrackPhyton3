# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter=','):

    group1 = first_group.split(delimiter)
    group2 = second_group.split(delimiter)

    common = list(set(group1) & set(group2))

    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(result)  # [Петров, Сидоров]

test1 = "Анна, Борис, Вера"
test2 = "Борис, Вера, Григорий"
print(find_common_participants(test1, test2))  # [Вера, Борис]