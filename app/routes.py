from app import app, response
from app.controllers import DosenController
from app.controllers import MahasiswaController
from app.controllers import userController
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return 'Hello World'

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return response.success(user, 'success')

@app.route('/dosens', methods=['GET'])
def dosens():
    return DosenController.index()

@app.route('/dosen', methods=['POST'])
def dosen():
    return DosenController.addDosen()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosenRoute(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.updateDosen(id)
    elif request.method == 'DELETE':
        return DosenController.deleteDosen(id)

@app.route('/mahasiswas', methods=['GET'])
def getAllMahasiswa():
    return MahasiswaController.getAllMahasiswa()

@app.route('/mahasiswa', methods=['POST'])
def addMahasiswa():
    return MahasiswaController.addMahasiswa()

@app.route('/mahasiswa/<id>', methods=['GET', 'PUT', 'DELETE'])
def mahasiswaRoute(id):
    if request.method == 'GET':
        return MahasiswaController.getMahasiswaByID(id)
    elif request.method == 'PUT':
        return MahasiswaController.updateMahasiswa(id)
    elif request.method == 'DELETE':
        return MahasiswaController.deleteMahasiswa(id)
    
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return userController.getAllUser()
    elif request.method == 'POST':
        return userController.addUser()

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])  
def userRoute(id):
    if request.method == 'GET':
        return userController.getUserByID(id)
    elif request.method == 'PUT':
        return userController.updateUser(id)
    elif request.method == 'DELETE':
        return userController.deleteUser(id)
    
@app.route('/login', methods=['POST'])
def logins():
    return userController.login()

@app.route('/upload', methods=['POST'])
def file():
    return userController.upload()