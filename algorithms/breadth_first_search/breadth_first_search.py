from collections import deque

graph = {}
graph['you'] = {'alice', 'bob', 'claire'}
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue = deque()
search_queue += graph['you']


def search_seller():
    search_queue = deque()
    search_queue += graph['you']
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print('''person %s is a mango seller''' % person)
            return True
        else:
            search_queue += graph[person]
    return False

def person_is_seller(person):
    return person[-1] == 'm'

result = search_seller()
