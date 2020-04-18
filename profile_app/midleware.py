import time


class MidlwareLog():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        diff = time.time() - start_time
        with open('log.txt', 'a') as file:
            file.write(str(diff) + ' ' + str(request) + '\n')

        return response
