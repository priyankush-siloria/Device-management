from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import db, test

print(test,"=============")

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.device_name