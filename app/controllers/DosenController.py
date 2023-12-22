from app.models.dosen import Dosen
from app.models.mahasiswa import Mahasiswa
from flask import jsonify

from app import response, app, db
from flask import request

def index():
    try:
        dosens = Dosen.query.all()
        return jsonify({'dosens': [
            {
                'id' : dosen.id,
                'nidn' : dosen.nidn,
                'nama' : dosen.nama,
                'phone' : dosen.phone,
                'alamat' : dosen.alamat
            } for dosen in dosens]})

    except Exception as e:
        print(e)

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_Dua == id)).all()

        if not dosen:
            return response.badRequest([], 'data not found')

        dataMahasiswa = formatMahasiswa(mahasiswa)

        data = singleDetailMahasiswa(dosen, dataMahasiswa)

        return response.success(data, "success")

    except Exception as e:
        print(e)

    
def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
                'id' : dosen.id,
                'nidn' : dosen.nidn,
                'nama' : dosen.nama,
                'phone' : dosen.phone,
                'alamat' : dosen.alamat,
                'mahasiswa' : mahasiswa
    }

    return data
        
def singleMahasiswa(mahasiswa):
    data = {
        'id': mahasiswa.id,
        'nim': mahasiswa.nim,
        'nama': mahasiswa.nama,
        'phone': mahasiswa.phone
    }
    return data


def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))
        return array
    
def addDosen():
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()

        return response.success('', 'Success')
    except Exception as e:
        print(e)

def updateDosen(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                'nidn': nidn,
                'nama': nama,
                'phone': phone,
                'alamat': alamat
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()

        if dosen:    
            if nidn is not None:
                dosen.nidn = nidn
            if nama is not None:
                dosen.nama = nama
            if phone is not None:
                dosen.phone = phone
            if alamat is not None:
                dosen.alamat = alamat

            db.session.commit()

            return "Data dosen berhasil diupdate."
        
        else:
        
            return "Dosen dengan ID tersebut tidak ditemukan."
    
    except Exception as e:
        print(e)

def deleteDosen(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badRequest([], 'Data not found')
        db.session.delete(dosen)
        db.session.commit()

        return response.success('', 'Delete successfully')
    except Exception as e:
        print(e)