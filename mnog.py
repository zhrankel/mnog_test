#сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машиной той же марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }

#  д/з объединить множество людей, которые живут и работают рядом
# вывести множество людей, которые и владеют авто нужной марки, и живут и работают рядом

#BORIS KAIZER
#HOMEWORK LESSON 4

criminals = work_near & live_near
if len(criminals) > 0:
    print("The list of people living and working near the crime scene:")
    for p in criminals:
        print(p)
else:
    print("There are no persons living and working near the crime scene")


criminals = shevrole_owner & work_near & live_near

if len(criminals) > 0:
    print("It seems that offender is in list bellow:")
    for p in criminals:
        print(p)
else:
    print("Sorry, but the set of offenders is empty")





