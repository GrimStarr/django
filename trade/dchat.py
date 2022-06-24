import requests


def send_discord(msg):

    payload = {
        'content': msg
    }

    header = {
        'authorization': 'OTc0MjAyNjQwMDgwNzE1Nzk2.GvaLGj.sp4KNlLMRlizhqoVCeDIdDvPwHbJcT2iFMaQFg'

    }

    r = requests.post("https://discord.com/api/v9/channels/974157991903387671/messages",
                      data=payload, headers=header)
