import os

import sanic

from views.geo_api_view import bp
import base_gen
import settings


app = sanic.Sanic()
app.blueprint(bp)

if __name__ == "__main__":
    app.run(
        host=settings.sanic_app['host'],
        port=settings.sanic_app['port']
        )