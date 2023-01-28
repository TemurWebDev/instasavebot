import requests



def userget():
    url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    respons = requests.get(url)
    return respons.json()


def usercreate(first_name,username,user_id):
    url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    re = requests.post(url,data={'first_name':first_name,'username':username,'user_id':user_id})
    return re.status_code





def userupdate(first_name,username,user_id,language,id):
    url = 'https://temur01.pythonanywhere.com/api/userupdate/'+id+'/'
    #print(url)
    re = requests.put(url,data={'first_name':first_name,'username':username,'user_id':user_id,'language':language})
    return re.status_code