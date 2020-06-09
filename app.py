from flask import Flask 
from flask_mail import Mail, Message

def create_app():
    app = Flask(__name__)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'clintonoshobugie@gmail.com'
    app.config['MAIL_PASSWORD'] = 'mygodissogood'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEFAULT_SENDER'] = ('Anthony Herbert', 'clintonoshobugie@gmail.com')
    app.config['MAIL_MAX_EMAILS'] = 5

    mail = Mail()
    mail.init_app(app)

    @app.route('/')
    def index():
        msg = Message(
            'Flask Cheatsheet', 
            sender=('Anthony', 'clintonoshobugie@gmail.com'),
            recipients=['alanwuwong@gmail.com']
        )
        #msg.add_recipient('l7h01n+hp2hk5gk9ktc@sharklasers.com')
        #msg.body = 'This is plaintext in the message!'
        msg.html = '<b>Please see attached!</b>'

        with app.open_resource('flask_cheatsheet.pdf') as pdf:
            msg.attach('flask_cheatsheet.pdf', 'application/pdf', pdf.read())

        mail.send(msg)

        return '<h1>Sent!</h1>'

    @app.route('/bulk')
    def bulk():
        users = [{'name' : 'Anthony', 'email' : 'anthony@email.com'}]

        with mail.connect() as conn:
            for user in users:
                msg = Message('Bulk', recipients=[user['email']])
                msg.body = f'Hey {user["name"]}'
                conn.send(msg)


    return app