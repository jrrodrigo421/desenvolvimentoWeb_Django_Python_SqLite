from django.shortcuts import render

# Create your views here.
from cadastros.models import Cidade


def lista_cidades(request):

    qs = Cidade.objects.all()
    qs_capitais = Cidade.objects.filter(capital=True)

    '''
        query = 'SELECT * FROM cidade'
        query = 'SELECT * FROM cidade WERE capital = TRUE'
        cursor = db.connect().execute(query)
        data = cursor.fetch()
    
    '''