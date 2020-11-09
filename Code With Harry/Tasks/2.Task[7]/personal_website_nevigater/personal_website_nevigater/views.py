# I am created this file
from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1>Google</h1>
                            <a href="https://www.google.com">Google</a>
                            <h1>Facebook</h1>
                            <a href="https://www.facebook.com">Facebook</a>
                            <h1>Twitter</h1>
                            <a href="https://www.twitter.com">Twitter</a>
                            <h1>Instagram</h1>
                            <a href="https://www.instagram.com">Instagram</a>
                            <h1>CodeWithHarry</h1>
                            <a href="https://www.codewithharry.com">CodeWithHarry</a>''')