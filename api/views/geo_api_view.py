import ipaddress
import os
import pickle
import socket

from sanic import response
from sanic import Blueprint

import settings
import base_gen

bp = Blueprint('geo_api_view')


@bp.route('/')
async def root(request):
    api_resp = {
        'ip_geo_api_usage': 'http://getdata/host',
    }
    return response.json(api_resp)


@bp.route('/getdata/<host>/')
async def ip_info(request, host):
    return response.json(get_host_inf(host))

@bp.route('/selfcheck/')
async def ip_selfcheck(request):
    return response.json(get_host_inf(request.ip))
    #return response.json(request.ip)

def get_host_inf(host):
    inf = ip_check_in(host)
    inf = {
        x:inf[x] for x in inf
        if x not in settings.sanic_app.get('unnecessary_fields')
        }
    return inf

def ip_check_in(ip):
    ia = ipaddress.ip_address(socket.gethostbyname(ip))
    if ia.is_global:
        octets = str(ia).split('.')[:-1]
        a = tree
        for octet in octets:
            if a.get(octet):
                a = a[octet]
                cidrs = a['cidrs']

        for block in cidrs:
            if ia in ipaddress.ip_network(block['network']):
                return block
    else:
        return {str(ia): "Isn't global address"}


if not os.path.isfile(settings.sanic_app['data_file']):
    print('Making data...')
    base_gen.build_ip_data()

with open(settings.sanic_app['data_file'], 'rb') as file:
        tree = pickle.load(file)
        print('Data loaded')

