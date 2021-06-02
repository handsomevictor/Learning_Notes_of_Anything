# functions to check if there are empty slots available today, tomorrow and in 7 days
from Goussainville_site import vaccination_goussainville
from stade_site import vaccination_stade, stade_next_week
from SDIS_60 import vaccination_SDIS_60

def check_today(today):

    if vaccination_goussainville(today):
        print('goussainville is available today!')
    elif vaccination_stade(today):
        print('stade is available today!')
    elif vaccination_SDIS_60(today):
        print('Only SDIS 60 is available today!')
    else:
        print('No one is available today!')


def check_tomorrow(tomorrow):

    if vaccination_goussainville(tomorrow):
        print('goussainville is available tomorrow!')
    elif vaccination_stade(tomorrow):
        print('stade is available tomorrow!')
    elif vaccination_SDIS_60(tomorrow):
        print('Only SDIS 60 is available tomorrow!')
    else:
        print('No one is available tomorrow!')


def check_next_week(next_week):

    if vaccination_goussainville(next_week):
        print('goussainville is available 7 days later!')
    elif vaccination_stade(next_week):
        print('stade is available 7 days later!')
    elif vaccination_SDIS_60(next_week):
        print('Only SDIS 60 is available 7 days later!')
    else:
        print('No one is available 7 days later!')
