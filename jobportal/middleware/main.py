

class ExampleMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response
    
    def __call__(self, request):
        print("###########Before calling the view for each request")

        response = self.get_response(request)

        ip = request.META.get('REMOTE_ADDR')
        print("Your ip address is : ",ip)

        print("############after calling the view for each request")

        return response
