from flaskApp import app,socketio
import threading
from flaskApp.kvizThread import kvizThread
# x=threading.Thread(target=socketio.run, args=(app,))
# y=kvizThread('Thread 1')
# try:
#     x.start()
#     y.start()
# except Exception:
#     print('Raise exception')
#     y.raise_exception()
#     y.join()
#     print('Raised exception')
app.run(debug=True,host='0.0.0.0')