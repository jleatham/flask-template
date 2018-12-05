#from myflask import app

import os

def application(environ, start_response):
    os.environ['SMARTSHEET_TOKEN'] = environ['SMARTSHEET_TOKEN']
    from myflask import app as _application
    return _application(environ, start_response)

if __name__ == "__main__":
    _application.run()
