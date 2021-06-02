# condition of 19-stade-de-france site today

def vaccination_stade(today):
    from stade_next_week import stade_next_week
    import requests

    url = 'https://www.doctolib.fr/availabilities.json?start_date=2021-05-12&visit_motive_ids=2735278&agenda_ids=447491-447376-447377-447378-447388-447389-447391-447375-447373-447381-447384-447385-447492-472647-472652-447380-447390-472653-472655-447383-447490-472658-469829-470547-470548-470549-469823-469824-469825-469827-469831-469836&insurance_sector=public&practice_ids=179894&destroy_temporary=true&limit=7'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }

    param = {
        'start_date': today,
        'visit_motive_ids': '2735278',
        'agenda_ids': '447491-447376-447377-447378-447388-447389-447391-447375-447373-447381-447384-447385-447492-472647-472652-447380-447390-472653-472655-447383-447490-472658-469829-470547-470548-470549-469823-469824-469825-469827-469831-469836',
        'insurance_sector': 'public',
        'practice_ids': '179894',
        'destroy_temporary': 'true',
        'limit': '7'
    }

    response = requests.get(url=url, params=param, headers=headers)
    json_data = response.json()

    if json_data['total'] != 0:
        # print('You can apply in stade!!! Hurry up!!!')
        return True
    else:

        if stade_next_week()[0] == True:
            # print('Oh my god!! There are ', stade_next_week()[1], ' slots available at stade next week!')
            # else:
            # print('You can\'t apply even in next week, go to sleep man!!')
            return False


def stade_next_week(next_week):

    import requests

    url = 'https://www.doctolib.fr/availabilities.json?start_date=2021-05-23&visit_motive_ids=2735278&agenda_ids=447491-447376-447377-447378-447388-447389-447391-447375-447373-447381-447384-447385-447492-472647-472652-447380-447390-472653-472655-447383-447490-472658-469829-470547-470548-470549-469823-469824-469825-469827-469831-469836&insurance_sector=public&practice_ids=179894&destroy_temporary=true&limit=7'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }

    param = {
        'start_date': next_week,
        'visit_motive_ids': '2735278',
        'agenda_ids': '447491-447376-447377-447378-447388-447389-447391-447375-447373-447381-447384-447385-447492-472647-472652-447380-447390-472653-472655-447383-447490-472658-469829-470547-470548-470549-469823-469824-469825-469827-469831-469836',
        'insurance_sector': 'public',
        'practice_ids': '179894',
        'destroy_temporary': 'true',
        'limit': '7'
    }

    response = requests.get(url=url, params=param, headers=headers)
    json_data = response.json()

    if json_data['total'] == 0:
        # print('You can\'t apply even in next week, go to sleep man!!')
        return False, 0
    else:
        # print('Oh my god!! There are ', json_data['total'], ' slots available next week!')
        return True, json_data['total']
