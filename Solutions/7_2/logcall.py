# logcall.py

from functools import wraps

def logformat(fmt):
    def logged(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

# Original no-argument @logged decorator defined in terms of the more
# general @logformat decorator

logged = logformat('Calling {func.__name__}')


        
