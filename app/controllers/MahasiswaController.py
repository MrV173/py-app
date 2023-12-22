from app.models.mahasiswa import Mahasiswa
from app.models.dosen import Dosen
from flask import jsonify

from app import response, app, db
from flask import request

def getAllMahasiswa():
    try:
        mahasiswas = Mahasiswa.query.all()
        return jsonify({'Data': [
            {
                'id' : mhs.id,
                'nim': mhs.nim,
                'nama': mhs.nama,
                'phone': mhs.phone,
                'alamat': mhs.alamat,
            } for mhs in mahasiswas]})
    except Exception as e:
        print(e)

def getMahasiswaByID(id):
    try:
        mahasiswa = Mahasiswa.query.get(id)

        if mahasiswa:
            data_mahasiswa = {
                'id': mahasiswa.id,
                'nim': mahasiswa.nim,
                'nama': mahasiswa.nama,
                'phone': mahasiswa.phone,
                'alamat': mahasiswa.alamat,
            }
            return jsonify(data_mahasiswa)
        else:
            return jsonify({'error': 'Mahasiswa not found'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def addMahasiswa():
    try:
        nim = request.form.get('nim')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        dosen_satu = request.form.get('dosen_satu')
        dosen_Dua = request.form.get('dosen_Dua')

        mahasiswa = Mahasiswa(nim=nim, nama=nama, phone=phone, alamat=alamat, dosen_satu=dosen_satu, dosen_Dua=dosen_Dua)
        db.session.add(mahasiswa)
        db.session.commit()

        return response.success('', 'Add Mahasiswa is successfully')

    except Exception as e:
        print(e)

def updateMahasiswa(id):
    try: 
        nim = request.form.get('nim')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')
        dosen_satu = request.form.get('dosen_satu')
        dosen_Dua = request.form.get('dosen_Dua')

        data = [
        {
            'nim': nim,
            'nama': nama,
            'phone': phone,
            'alamat': alamat,
            'dosen_satu': dosen_satu,
            'dosen_Dua': dosen_Dua,
        }
        ]

        mahasiswa = Mahasiswa.query.filter_by(id=id).first()

        if mahasiswa:
            if nim is not None:
                mahasiswa.nim = nim
            if nama is not None: 
                mahasiswa.nama = nama
            if phone is not None:
                mahasiswa.phone = phone
            if alamat is not None:
                mahasiswa.alamat = alamat
            if dosen_satu is not None:
                mahasiswa.dosen_satu = dosen_satu
            if dosen_Dua is not None:
                mahasiswa.dosen_Dua = dosen_Dua
        
            db.session.commit()

            return "Data has been updated"
        else:
            return "Update data is failed"
    
    except Exception as e:
        print(e)

def deleteMahasiswa(id):
    try:
        mahasiswa = Mahasiswa.query.filter_by(id=id).first()
        if not mahasiswa:
            return response.badRequest([],'Data not Found')
        db.session.delete(mahasiswa)
        db.session.commit()

        return response.success('', 'Data has been deleted')
    
    except Exception as e:
        print(e)