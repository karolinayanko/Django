import threading
def Thread(f):
    def _inside(*a, **k):
        thr = threading.Thread(target = f, args = a, kwargs = k)
        thr.start()
    return _inside