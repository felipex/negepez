from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def index(request):
    with connection.cursor() as c:
        c.execute('select * from dw_servidores limit 5;')
        objs = dictfetchall(c)

    return render(request, 'index.html', {'objs': objs})


def servidores(request):

    select = '''select * from dw_servidores
left join dw_uo_siorg on codigo = trim(cod_siorg_uorg)
'''
    if len(request.GET.keys()) > 0:
        select += '\n' + 'where '
        for param in request.GET.keys():
            select += f"{param} like '%{request.GET[param]}%' \n"
    print(select)
    with connection.cursor() as c:
        c.execute(select)
        objs = dictfetchall(c)

    return JsonResponse({'servidores': objs})
