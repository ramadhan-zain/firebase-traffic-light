from firebase import firebase

url = 'https://dynamic-traffic-light-default-rtdb.firebaseio.com'
firebase = firebase.FirebaseApplication(url, None)

lst_car =  list(firebase.get('/Vehicle/road/', "").values())

print(lst_car)