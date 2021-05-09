from firebase import firebase

firebase = firebase.FirebaseApplication('https://dynamic-traffic-light-default-rtdb.firebaseio.com', None)

while True:
    result1 = firebase.get('/Duration/ruas-barat/', "")
    result2 = firebase.get('/Duration/ruas-timur/', "")
    result3 = firebase.get('/Duration/ruas-selatan/', "")
    result4 = firebase.get('/Duration/ruas-utara/', "")

    # print(result1)

    lst = [result1["duration"], result2["duration"], result3["duration"], result4["duration"]]

    print(lst)