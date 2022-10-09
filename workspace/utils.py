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
    Выводит всех кандидатов.
    """
    candidates = ""
    candidates_list = load_candidates()
    for person in candidates_list:
        candidate = "\nИмя кандидата: " + person["name"] + \
                    "\nПозиция кандидата: " + person["position"] +\
                    "\nНавыки кандидата: " + person["skills"]+"\n"
        candidates += candidate
    return candidates


def get_by_pk(pk):
    """
    Возвращает данные о конкретном кандидате по номеру.
    """
    candidates_list = load_candidates()
    for person in candidates_list:
        if person["pk"] == pk:
            candidate_loaded = "\nИмя кандидата: " + person["name"] + \
                    "\nПозиция кандидата: " + person["position"] +\
                    "\nНавыки кандидата: " + person["skills"]+"\n"
            url_of_photo = {person["picture"]}
            return url_of_photo, candidate_loaded
        else:
            continue


def get_by_skill(skill):
    """
    Ищет совпадения по навыкам у кандидатов.
    Возвращает тех кандидатов, у которых совпадения есть.
    """
    candidates = ""
    candidates_list = load_candidates()
    for person in candidates_list:
        if skill.lower() in person["skills"].lower():
            candidates += "\nИмя кандидата: " + person["name"] + \
                    "\nПозиция кандидата: " + person["position"] +\
                    "\nНавыки кандидата: " + person["skills"]+"\n"
    return candidates
