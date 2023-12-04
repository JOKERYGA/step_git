from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]  # Начальная инициализация очереди с соседями начального человека
    searched = []  # Список для отслеживания уже проверенных людей

    while search_queue:
        person = search_queue.popleft()

        # Проверим, был ли человек уже проверен
        if person not in searched:
            # Если не проверен, проверим, является ли он продавцом манго
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                # Если не продавец манго, добавим всех его соседей в очередь для дальнейшей проверки
                search_queue += graph[person]
                # Пометим человека как уже проверенного
                searched.append(person)

    # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго
    return False

# Пример использования (предполагается, что у вас есть граф и функция person_is_seller)
graph = {
    'you': ['alice', 'bob', 'claire'],
    'alice': ['peggy'],
    'bob': ['anuj', 'peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}


def person_is_seller(person):
    return person[-1] == 'm'  # Предположим, что продавцы манго заканчиваются на 'm'


print(search('you'))
