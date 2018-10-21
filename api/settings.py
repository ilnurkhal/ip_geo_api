import os

base_gen = {
    'data_url' : 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-City-CSV.zip',
    'data_filename': 'ip_search_dict_tree.pkl',
    
}

sanic_app = {
    'port' : 8080,
    'host': '0.0.0.0',
    'data_file': os.path.join(os.getcwd(),base_gen['data_filename']),
    'unnecessary_fields': ["geoname_id", "registered_country_geoname_id", "represented_country_geoname_id"],
}