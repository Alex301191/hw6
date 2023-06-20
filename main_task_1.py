def get_top_3(courses, mentors):

    # добавьте сюда ваш код из Задачи 1
    all_list = []
    i = 0
    for m in mentors:
        all_list += mentors[i]
        i += 1
    all_names_list_1 = []
    all_names_list = []
    i = 0
    j = 0
    for mentor in all_list:
        name = all_list[i].split()
        all_names_list_1.append(name)
        i += 1
    i = 0
    for mentor in all_list:
        name = all_names_list_1[i][j]
        all_names_list.append(name)
        i += 1
    # уникальные имена будут в unique_names
    all_names_list_1 = all_names_list
    all_names_list_1_set = set(all_names_list_1)
    all_names_list_set = set(all_names_list)
    unique_names = all_names_list_1_set & all_names_list_set
    unique_names = list(unique_names)
    # подсчитайте встречаемость каждого имени через list.count()
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)]) # добавьте  подсчет имен
    # это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
    # используйте его как есть (или при желании можете написать свой собственный :))
    popular.sort(key=lambda x:x[1], reverse=True)
    # получите топ-три самых часто встречающихся имени из списка popular
    # подсказка: возьмите срез списка
    top_3 = popular[0:3]
    result = f"{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: {top_3[2][1]} раз(а)"
    return result


def get_unique_names(courses, mentors):

    # добавьте в список всех преподавателей со всех курсов
    # допишите сюда ваш код, который заполнит all_list. можете как складывать списки, так и использовать метод extend
    all_list = []
    i = 0
    for m in mentors:
        all_list += mentors[i]
        i += 1
    # сделайте список all_names_list, состоящий только из имен, и заполните его
    all_names_list_1 = []
    all_names_list = []
    i = 0
    j = 0
    for mentor in all_list:
        name = all_list[i].split()
        all_names_list_1.append(name)
        i += 1
    i = 0
    for mentor in all_list:
        name = all_names_list_1[i][j]
        all_names_list.append(name)
        i += 1
    # сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
    all_names_list_1 = all_names_list
    all_names_list_1_set = set(all_names_list_1)
    all_names_list_set = set(all_names_list)
    unique_names = all_names_list_1_set & all_names_list_set
    # теперь нужно отсортировать имена в алфавитном порядке. подсказка: используйте sorted() для списка
    # допишите код ниже
    all_names_sorted = sorted(unique_names)
    # допишите конструкцию вывода результата. можете использовать string.join()
    # результат будет в all_names_sorted
    all_names_sorted = ", ".join(all_names_sorted)
    result = f'Уникальные имена преподавателей: {all_names_sorted}'
    return result


def get_supernames(courses, mentors):
    result = []
    # делаем список списков имен
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(str(name).split()[0]) # допишите код здесь
        # допишите ниже код, который добавляет списки имен в общий список mentors_names:
        mentors_names.append(course_names)
    # храните здесь пары курсов, на есть совпавшие имена
    pairs = []
    # попарное сравнение "наборов" преподавателей на курсах. каждую новую пару запоминаем для исключения повторов.
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            # проверьте, что вы не сравниваете список сам с собой:
            if id1 != id2:
            # допишите ниже код для сравнения двух "наборов" преподавателей. подсказка: используйте множества
                intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
                if len(intersection_set) > 0: # допишите проверку, что результат не пустой, имена есть
                # допишите ниже код, который проверяет, что эта пара еще не встречалась
                    pair = str(intersection_set)
                # и если pair еще не встречалась, то выведите на экран два курса и список преподавателей, которые есть на обоих курсах
                    if pair not in pairs:
                        pairs.append(pair)
                    # отсортируйте имена по алфавиту. подсказка: используйте sorted() для списка
                        all_names_sorted = sorted(intersection_set)

                    # допишите конструкцию вывода результата. можете использовать string.join()
                        result.append(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
    return result
