from rest_framework.views import exception_handler
from rest_framework.response import Response

def api_exception_handler(e, context):
    print(e, context)
    response = exception_handler(e, context)
    if response is not None:
        if response.status_code == 404:
            response.data = {
                'message' : 'The resource you tried to access was not found',
                'details' : str(e)
            }
    else:
        response = Response({
            'message' : 'An error occured in the server.',
            'details' : str(e)
        }, status=500)

    return response