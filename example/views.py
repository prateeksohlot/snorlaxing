# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Snorlaxing!!</h1>
            <h2>Embracing the Art of Chill!!</p>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)