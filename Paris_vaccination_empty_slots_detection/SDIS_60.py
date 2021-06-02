# empty slots in SDIS_60

def vaccination_SDIS_60(today):

    import requests

    url = 'https://www.doctolib.fr/availabilities.json?start_date=2021-05-12&visit_motive_ids=2810290&agenda_ids=467244-467245-458892-458893-458894-467219&insurance_sector=public&practice_ids=183218&destroy_temporary=true&limit=7'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }

    param = {
        'start_date': today,
        'visit_motive_ids': '2810290',
        'agenda_ids': '467244-467245-458892-458893-458894-467219',
        'insurance_sector': 'public',
        'practice_ids': '183218',
        'destroy_temporary': 'true',
        'limit': '7'
    }

    response = requests.get(url=url, params=param, headers=headers)
    json_data = response.json()

    if json_data['total'] == 0:
        # print('You can\'t apply at SDIS 60 at ', today, ', go to sleep!!')
        return False
    else:
        # print('Oh my god!! Please go check SDIS 60!! I think there are some empty slots!!')
        return True
