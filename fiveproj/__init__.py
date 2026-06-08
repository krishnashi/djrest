from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

api = Api(app)
jwt = JWTManager(app)


from fiveproj.views.item_views import ItemsResource, ItemsListResource
from fiveproj.views.register_views import RegisterResource
from fiveproj.views.login_views import LoginResource

api.add_resource(ItemsResource, "/items")
api.add_resource(ItemsListResource, "/items/<id>")
api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")
