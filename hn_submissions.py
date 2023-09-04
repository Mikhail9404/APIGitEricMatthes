from operator import itemgetter

import requests

# Создание вызова API и сохранение ответа.
url = 'http://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Создание отдельного выозова API для каждой статьи.
    url = f"http://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus :{r.status_code}")
    response_dict = r.json()

    # Построение словоря для каждой статьи.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://hacker-news.firebaseio.com/v0/item/{submission_id}.json",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dict, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")