### Ip_geo_api
Ip_geo_api help you get geo information from ip address or hostname:
(for ex. latitude, longitude, accuracy_radius, locale_code, continent_code, continent_name, country_iso_code, country_name, subdivision_1_iso_code, subdivision_1_name, city_name time_zone, is_in_european_union).

### For quick start:

> docker run -dit --name geoapi -p 8080:8080 h1dw0w/ip_geo_api

or you can set specific data language as environ:

> docker run -dit --name geoapi -e "data_lang=ru" -p 8080:8080 h1dw0w/ip_geo_api

(data_lang can be: de, en, es, fr, ja, pt-BR, ru, zh-CN ), **default data_lang is "en"**

All you need is make GET-request:

> http://host-with-container:8080/getdata/80.193.139.22 

(or some hostname instead ip)

As result you get somthing like this:
```
{
"network":"80.193.136.0/21",
"is_anonymous_proxy":"0",
"is_satellite_provider":"0",
"postal_code":"PR1",
"latitude":"53.7582",
"longitude":"-2.7229",
"accuracy_radius":"200",
"locale_code":"en",
"continent_code":"EU",
"continent_name":"Europe",
"country_iso_code":"GB",
"country_name":"United Kingdom",
"subdivision_1_iso_code":"ENG",
"subdivision_1_name":"England",
"subdivision_2_iso_code":"LAN",
"subdivision_2_name":"Lancashire",
"city_name":"Preston",
"time_zone":"Europe/London",
"is_in_european_union":"1"
}
```
