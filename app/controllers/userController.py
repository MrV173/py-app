from app.models.user import User
from app.models.gambar import Gambar
from flask import jsonify
import datetime
import os
import uuid
from werkzeug.utils import secure_filename


from app import response, app, db, uploadConfig
from flask import request
from flask_jwt_extended import *

def upload():
    try:
        title = request.form.get('title')

        if 'file' not in request.files:
            return response.badRequest([], 'file not allowed')
        
        file = request.files['file']
        if file.filename == '':
            return response.badRequest([], 'error')
        
        if file and uploadConfig.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = "Flask-"+str(uid)+filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))

            uploads = Gambar(title=title, path=renamefile)
            db.session.add(uploads)
            db.session.commit()

            return response.success({
                'title': title,
                'path': renamefile
            }, 'Success')
        else:
            return response.badRequest([], 'file not allowed')
    except Exception as e:
        print(e)

def getAllUser():
    try:
        users = User.query.all()
        return jsonify({'Users': [
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            } for user in users
        ]})
    
    except Exception as e:
        print(e)

def getUserByID(id):
    try:
        user = User.query.get(id)

        if user:
            user_data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            }
            return jsonify(user_data)
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        print(e)

def addUser():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        user = User(name=name, email=email, level=level)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()

        return response.success('', 'User has been added successfully')
    except Exception as e:
        print(e)

def updateUser(id):
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        data = [
            {
                'name': name,
                'email': email,
                'password': password
            }
        ]

        user = User.query.filter_by(id=id).first()

        if user:
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            if password is not None:
                user.password = password
        
            db.session.commit()

            return 'Data User has been updated successfully'
        
        else:

            return 'Update data user is failed'
    except Exception as e:
        print(e)

def deleteUser(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([],'User not found')
        db.session.delete(user)
        db.session.commit()

        return response.success('', 'Data user has been deleted')
    
    except Exception as e:
        print(e)

def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'level': data.level
    }

    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([], 'email or password are wrong')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'email or password are wrong')
        
        data = singleObject(user)

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=10)

        access_token = create_access_token(data, fresh=True, expires_delta= expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            'data': data,
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 'Login Success')

    except Exception as e:
        print(e)