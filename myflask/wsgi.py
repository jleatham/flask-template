from myflask import app
import os
os.environ['SMARTSHEET_TOKEN'] = os.environ.get('SMARTSHEET_TOKEN')

if __name__ == "__main__":
    app.run()
