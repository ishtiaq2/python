# Useful links: Flask
# flask.pocoo.org
# flask.pocoo.org/docs/0.10/patterns/viewdecorators/
# https://www.djangoproject.com
#redit, pintrest

def my_decorator(call_back_func):
    print('first statement inside my_decorator')
    print('followed by a web call...')
    def make_a_web_call():
        print ('I am a web_call_func, I am followed by call_back_func()')
        call_back_func()
        print ('finished with call_back_func inside make_a_web_call')
    print ('my_decorator returning make_a_web_call')
    return make_a_web_call

#one way of using decorators
'''def call_back_func():
    print('I am a call_back_func')

make_a_web_call = my_decorator(call_back_func)
make_a_web_call()'''

#second way of using decorators
@my_decorator
def call_back_func():
    print('I am a call_back_func')

call_back_func()

