from jinja2 import Environment 

def create_email_html(arch):
    htmlTemplate = """
        <html>
        <head>
        <title>{{ arch }}</title>
        </head>
        <body>

        {{ data.hello }}  {{ data.world }}

        </body>
        </html>
        """
    htmlMsg = Environment().from_string(htmlTemplate).render(
        arch = arch,
        #data = data
        data = {'hello': 'hello','world':'world'}
    )
    print (htmlMsg)
