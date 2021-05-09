from firebase import firebase
from random import randint

url = 'https://dynamic-traffic-light-default-rtdb.firebaseio.com'
firebase = firebase.FirebaseApplication(url, None)

data = {
    "duration": randint(0, 20)
}



while True:
    # result = firebase.patch('/Duration/ruas-barat/', {"duration": randint(0, 20)})
    result1 = firebase.patch('/Duration/ruas-barat/', {"duration": randint(0, 20)})
    result2 = firebase.patch('/Duration/ruas-selatan/', {"duration": randint(0, 20)})
    result3 = firebase.patch('/Duration/ruas-timur/', {"duration": randint(0, 20)})
    result4 = firebase.patch('/Duration/ruas-utara/', {"duration": randint(0, 20)})
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
    lst = [result1["duration"], result2["duration"], result3["duration"], result4["duration"]]
    # print(result)
    # print(result1)
    print(lst)

    # {'1': 'John Doe', '2': 'Jane Doe'}