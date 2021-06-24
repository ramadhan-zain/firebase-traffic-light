from firebase import firebase
from random import randint
import time

url = 'https://dynamic-traffic-light-default-rtdb.firebaseio.com'
firebase = firebase.FirebaseApplication(url, None)





while True:
    selatan=randint(0,20)
    barat=randint(0,20)
    timur=randint(0,20)
    utara=randint(0,20)
    dct_car={
    'selatan':selatan,
    'barat':barat,
    'timur':timur,
    'utara':utara
    }
    # result = firebase.patch('/Duration/ruas-barat/', {"duration": randint(0, 20)})
    result = firebase.patch('/Vehicle/ruas/', dct_car)
    # result1 = firebase.patch('/Vehicle/ruas-barat/', data["barat"])
    # result3 = firebase.patch('/Vehicle/ruas-timur/', data["timur"])
    # result4 = firebase.patch('/Vehicle/ruas-utara/', data["utara"])
    # result1 = firebase.put('/dynamic-traffic-light-default-rtdb/Duration/ruas-barat', 'duration', randint(0, 20))
    # result2 = firebase.put('/dynamic-traffic-light-default-rtdb/Duration/ruas-selatan', 'duration', randint(0, 20))
    # result3 = firebase.put('/dynamic-traffic-light-default-rtdb/Duration/ruas-timur', 'duration', randint(0, 20))
    # result4 = firebase.put('/dynamic-traffic-light-default-rtdb/Duration/ruas-timur', 'duration', randint(0, 20))
    # result = firebase.delete('/dynamic-traffic-light-default-rtdb/Duration/', '-MWnSz7PPKc7SEw25Zrt')
    # -MWnTilLP615RPyGREeI
    # result = firebase.get('/Duration/', "")
    # result = firebase.get('/dynamic-traffic-light-default-rtdb/Customer', "")

    # print(result["-MWnKwf5NzrD7DqrczSs"]["hobby"])
    # print(result["ruas-timur"]["duration"])
    # print(result1 + " " + result2 + " " + result2 + " " + result4)
    # print(str(result1["duration"]) + " " + str(result2["duration"]) + " " + str(result2["duration"]) + " " + str(result4["duration"]))
    # print(result)
    # print(result1)
    print(result.values())

    # {'1': 'John Doe', '2': 'Jane Doe'}