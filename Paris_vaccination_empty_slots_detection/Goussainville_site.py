# City of Goussainville site

def vaccination_goussainville(today):
    import requests

    url = 'https://www.doctolib.fr/availabilities.json?start_date=2021-05-12&visit_motive_ids=2858018&agenda_ids=468303-468302-461143-468300-461141-461144-461147-468301-463304-461145-468304&insurance_sector=public&practice_ids=163985&destroy_temporary=true&limit=7'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }

    param = {
        'start_date': today,
        'visit_motive_ids': '2858018',
        'agenda_ids': '468303-468302-461143-468300-461141-461144-461147-468301-463304-461145-468304',
        'insurance_sector': 'public',
        'practice_ids': '163985',
        'destroy_temporary': 'true',
        'limit': '7'
    }

    response = requests.get(url = url, params = param, headers= headers)
    json_data = response.json()

    if json_data['total'] != 0:
        # print('You can apply the one in centre de vaccination ville de goussainville at ', today,'!!! Hurry up!!!')
        return True
    else:
        # print('Now it\'s only ', today, 'no available ones, please just wait more')
        return False