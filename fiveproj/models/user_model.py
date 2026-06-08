from enum import unique

from fiveproj import db
# from werkzeug.security import generate_password_hash,check_password_hash
#
#
# class UserModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(250), nullable=False)
#
#     def gen_pass_hash(self, raw_password):
#         self.password = generate_password_hash(raw_password)
#
#     def check_password_hash(self, password):
#         self.password = check_password_hash(self.password, password)

from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))

    def gen_pass_hash(self, password):
        self.password = generate_password_hash(password)

    def ch_pass_hash(self, password):
        return check_password_hash(self.password, password)
