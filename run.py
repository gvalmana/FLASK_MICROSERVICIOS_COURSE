from application import create_app, db
from application.models import Dog
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)
if __name__=='main':
    app.run(host='0.0.0.0', port= 7001)