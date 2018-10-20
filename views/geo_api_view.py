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
    api_resp = ip_check_in(host)
    return response.json(api_resp)

def ip_check_in(ip):
    ia = ipaddress.ip_address(socket.gethostbyname(ip))
    octets = str(ia).split('.')[:-1]
    a = tree
    for octet in octets:
        if a.get(octet):
            a = a[octet]
            cidrs = a['cidrs']

    for block in cidrs:
        if ia in ipaddress.ip_network(block['network']):
            return block


if not os.path.isfile(settings.sanic_app['data_file']):
    print('Making data...')
    base_gen.build_ip_data()

with open(settings.sanic_app['data_file'], 'rb') as file:
        tree = pickle.load(file)
        print('Data loaded')

