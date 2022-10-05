from flask_app import app

#Importar nuestro controlador
from flask_app.controllers import users_controller
from flask_app.controllers import messages_controller

#Ejecutamos variable app
if __name__=="__main__":
    app.run(debug=True)