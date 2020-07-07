import time,threading
from datetime import datetime
from flaskApp.resource.Kviz import KvizResource
from flaskApp import socketio

import ctypes 
import time 
   
class kvizThread(threading.Thread): 
    def __init__(self, name): 
        threading.Thread.__init__(self) 
        self.name = name 
    @classmethod        
    def funkcija(cls):
        kviz=KvizResource.vratiKviz(4)
        socketio.emit('pitanja',kviz['pitanja'])
        time.sleep(10*len(kviz['pitanja']))
        socketio.emit('krajKviza')

    def run(self): 
  
        # target function of the thread class 
        try: 
            while True:
                datum=datetime.now().replace(hour=12, minute=48, second=0, microsecond=0)
                if datetime.now().minute%3 == 0:
                    socketio.emit('notifikacija')
                    time.sleep(10)
                    kvizThread.funkcija()
                time.sleep(60) 
        finally: 
            print('ended') 
           
    def get_id(self): 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id
   
    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
       



