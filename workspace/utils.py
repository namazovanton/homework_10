def load_candidates():
    """
    Открывает файл 'candidates.json'.
    Загружает данные из файла.
    """
    import os
    import json
    with open(os.path.join('..', 'data', 'candidates.json'),
              encoding='utf-8') as file:
        candidates_list = json.loads(file.read())
        return candidates_list


def get_all():
    """
    Открывает файл 'candidates.json'.
    """
    candidates = ""
    candidates_list = load_candidates()
    for person in candidates_list:
        candidate = "\nИмя кандидата: " + person["name"]+ \
                    "\nПозиция кандидата: " + person["position"]+\
                    "\nНавыки кандидата: " + person["skills"]+"\n"
        candidates += candidate
    return candidates


def get_by_pk(pk):
    """
    Открывает файл 'candidates.json'.
    Возвращает словарь с данными о конкретном кандидате.
    """
    candidates_list = load_candidates()
    for person in candidates_list:
        if person["pk"] == pk:
            candidate_loaded = "\nИмя кандидата: " + person["name"]+ \
                    "\nПозиция кандидата: " + person["position"]+\
                    "\nНавыки кандидата: " + person["skills"]+"\n"
            url_of_photo = {person["picture"]}
            return url_of_photo, candidate_loaded
        else:
            continue


def get_by_skill(skill):
    """
    Открывает файл 'candidates.json'.
    Возвращает словарь с данными о конкретном кандидате.
    """
    candidates = ""
    candidates_list = load_candidates()
    for person in candidates_list:
        if skill.lower() in person["skills"].lower():
            candidates += "\nИмя кандидата: " + person["name"]+ \
                    "\nПозиция кандидата: " + person["position"]+\
                    "\nНавыки кандидата: " + person["skills"]+"\n"
    return candidates


# abservation = get_by_skill("Python")
# print(abservation)
