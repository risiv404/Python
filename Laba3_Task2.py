# TODO Напишите функцию find_common_participants
def find_common_participants(grup1, grup2, de='|'):
    part1 = set(grup1.split(de))
    part2 = set(grup2.split(de))
    common_part = part1.intersection(part2)
    return sorted(common_part)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_part = find_common_participants(participants_first_group, participants_second_group)
print(common_part)

participants_first_group_comma = "Иван,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_part_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma, de=',')
print(common_part_comma)

# TODO Провеьте работу функции с разделителем отличным от запятой
