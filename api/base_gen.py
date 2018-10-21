import ipaddress
import itertools
import io
import os
import pickle
import zipfile
import csv
import codecs

import requests

import settings


def build_ip_data(data_lang=os.environ.get('data_lang') or 'en'):    
    archive = requests.get(settings.base_gen.get('data_url'))

    with zipfile.ZipFile(io.BytesIO(archive.content)) as ziped_data:
        zip_name = ziped_data.namelist()[0].split('/')[0]
        
        with ziped_data.open(
            os.path.join(zip_name, 'GeoLite2-City-Blocks-IPv4.csv')
            ) as zip_blocks:
            city_blocks = (
                i for i in csv.reader(
                    codecs.iterdecode(zip_blocks, 'utf-8'),
                    delimiter=','
                    )
            )
            
            city_blocks_fields = next(city_blocks)
            ip_blocks = []
            for x in city_blocks:
                ip_data = dict(itertools.zip_longest(city_blocks_fields, x))
                ip_data = {x:ip_data[x] for x in ip_data if ip_data[x]}
                ip_blocks.append(
                    ip_data
                )

        with ziped_data.open(
            os.path.join(
                zip_name,
                'GeoLite2-City-Locations-{}.csv'.format(data_lang))
            ) as zip_city_locations:

            city_locations = (
                i for i in csv.reader(
                    codecs.iterdecode(zip_city_locations, 'utf-8'), 
                    delimiter=','
                    )
            )
            fields = next(city_locations)
            cl = {}
            for x in city_locations:
                city_data = dict(itertools.zip_longest(fields, x))
                city_data = {
                    x:city_data[x] for x in city_data if city_data[x]
                    }
                cl[city_data['geoname_id']] = city_data

    for i in ip_blocks:
        if cl.get(i.get('geoname_id')):
            i.update(cl.get(i['geoname_id']))
    del cl

    tree = {}
    for i in ip_blocks:
        ip, mask = i['network'].split('/')
        octet_deep = int(mask) // 8
        ip_octets = ip.split('.')
        keys = ip_octets[:octet_deep]
        a = tree
        for key in keys:
            if not a.get(key):
                a[key] = {'cidrs': []}
            a = a[key]
        a['cidrs'].append(i)
    with open(settings.base_gen['data_filename'], 'wb') as file:
        pickle.dump(tree, file)