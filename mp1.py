from multiprocessing import Process,Pipe
from random import randint

#YOLO
def random_int():
    lst = [randint(0, 20), randint(0, 20),randint(0, 20),randint(0, 20)]
    return lst
    
while True:
    def f(child_conn):
        msg = random_int()
        child_conn.send(msg)
        child_conn.close()