from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from transparencia.models import Servidor
import json

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def index(request):
	return render(request, 'index.html', {})


def site(request):
	return render(request, 'site.html', {})

'''
    with connection.cursor() as c:
        c.execute('select * from dw_servidores limit 5;')
        objs = dictfetchall(c)

    return render(request, 'index.html', {'objs': objs})
'''

def servidores(request):

    select = '''select * from dw_servidores 
left join dw_uo_siorg on codigo = trim(cod_siorg_uorg)
'''
    if len(request.GET.keys()) > 0:
        select += '\n' + 'where '
        for param in request.GET.keys():
            select += f"{param} like '%{request.GET[param]}%' and\n"
            
        select = select[:-4]  # Tira o último AND do comando.
	    
    print("-----------")
    print(select)
    print("-----------")
    with connection.cursor() as c:
        c.execute(select)
        objs = dictfetchall(c)

    return JsonResponse({'servidores': objs})
    
    
def servidores2(request):

	ss = Servidor.objects.all()
	objs = list(ss.values())
	
	return JsonResponse({'servidores': objs})

