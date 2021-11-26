from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
from datetime import datetime
from flaskr.mod_pendaftaran.models import Pendaftaran, PendaftaranAmida, Regencies

def getkabdt():
    data = []
    regencies = Regencies.objects(province=str("5824f56f9cc60d0553001bc3")).limit(100)
    for regency in regencies:
        data.append((regency.id, regency.name))
    return data

class PendaftaranFormv2(FlaskForm):
    nama_lengkap = TextField('Nama', [Required(message='Nama wajib diisi')])
    usia         = TextField('Usia', [Required(message='Email wajib diisi')])
    email        = TextField('Email', [Required(message='Email wajib diisi')])
    jk             = TextField('Gender', [Required(message='Jenis wajib dipilih')])
    nohp            = TextField('No.Hp', [Required(message='No.Hp wajib diisi')])
    pekerjaaan      = SelectField('Pekerjaan', [Required(message='Pekerjaan wajib diisi')])
    hamil           = TextField('Hamil', [Required(message='Hamil wajib diisi')])
    sakit           = TextField('Sakit', [Required(message='Sakit wajib dipilih')])
    donatur         = TextField('Donatur', [Required(message='Donasi wajib dipilih')])

    kabupaten = SelectField('Kabupaten', [Required(message='wajib diisi')], choices = getkabdt())
    kecamatan = SelectField('Kecamatan', choices = [])
    kelurahan = SelectField('Kelurahan', choices = [])

    instance = None
    document_class = Pendaftaran

    def __init__(self, document=None, *args, **kwargs):
        super(PendaftaranFormv2, self).__init__(*args, **kwargs)

    def save(self, skor, tipengaji):
        waktu = datetime.now()
        if self.instance is None:
            self.instance = self.document_class()
            created = waktu
        else:
            created = self.instance.created

        self.instance.nama_lengkap = self.nama_lengkap.data
        self.instance.usia = self.usia.data
        self.instance.email = self.email.data
        self.instance.jk = self.jk.data
        self.instance.nohp = self.nohp.data
        self.instance.pekerjaaan = self.pekerjaaan.data
        self.instance.hamil = self.hamil.data
        self.instance.sakit = self.sakit.data
        self.instance.donatur = self.donatur.data

        self.instance.skor = skor
        self.instance.tipengaji = tipengaji
        self.instance.created = created
        self.instance.modified = waktu

        self.instance.kabupaten = self.kabupaten.data
        self.instance.kecamatan = self.kecamatan.data
        self.instance.kelurahan = self.kelurahan.data

        self.instance.save()
        return self.instance

class PendaftaranForm(FlaskForm):
    email        = TextField('Email', [Required(message='Email wajib diisi')])
    nama_lengkap  = TextField('Nama', [Required(message='Nama wajib diisi')])
    jk             = TextField('Gender', [Required(message='Jenis wajib dipilih')])
    tempat_tinggal  = TextField('Alamat', [Required(message='Alamat wajib diisi')])
    nohp            = TextField('No.Hp', [Required(message='No.Hp wajib diisi')])
    pekerjaaan      = TextField('Pekerjaan', [Required(message='Pekerjaan wajib diisi')])
    keluar_kota      = TextField('Keluar kota', [Required(message='Keluar kota wajib dipilih')])
    status_interaksi = TextField('Status interaksi', [Required(message='Status interaksi wajib dipilih')])
    status_lingkungan = TextField('Status lingkungan', [Required(message='Status lingkungan wajib dipilih')])
    sakit              = TextField('Sakit', [Required(message='Sakit wajib dipilih')])
    masalah_penciuman  = TextField('Masalah penciuman', [Required(message='Masalah penciuman wajib dipilih')])
    persetujuan = TextField('Persetujuan', [Required(message='Persetujuan wajib dipilih')])
    donatur              = TextField('Donatur', [Required(message='Donasi wajib dipilih')])

    instance = None
    document_class = Pendaftaran

    def __init__(self, document=None, *args, **kwargs):
        super(PendaftaranForm, self).__init__(*args, **kwargs)

    def save(self, skor):
        waktu = datetime.now()
        if self.instance is None:
            self.instance = self.document_class()
            created = waktu
        else:
            created = self.instance.created

        self.instance.email = self.email.data
        self.instance.nama_lengkap = self.nama_lengkap.data
        self.instance.jk = self.jk.data
        self.instance.tempat_tinggal = self.tempat_tinggal.data
        self.instance.nohp = self.nohp.data
        self.instance.pekerjaaan = self.pekerjaaan.data
        self.instance.keluar_kota = self.keluar_kota.data
        self.instance.status_lingkungan = self.status_lingkungan.data
        self.instance.status_interaksi = self.status_interaksi.data
        self.instance.sakit = self.sakit.data
        self.instance.masalah_penciuman = self.masalah_penciuman.data
        self.instance.persetujuan = self.persetujuan.data
        self.instance.skor = skor
        self.instance.tipengaji = "rabu"
        self.instance.donatur = self.donatur.data

        self.instance.created = created
        self.instance.modified = waktu

        self.instance.save()
        return self.instance


class PendaftaranAmidaForm(FlaskForm):
    email        = TextField('Email', [Required(message='Email wajib diisi')])
    nama_lengkap  = TextField('Nama', [Required(message='Nama wajib diisi')])
    tempat_tinggal  = TextField('Alamat', [Required(message='Alamat wajib diisi')])
    nohp            = TextField('No.Hp', [Required(message='No.Hp wajib diisi')])
    pekerjaaan      = TextField('Pekerjaan', [Required(message='Pekerjaan wajib diisi')])
    keluar_kota      = TextField('Keluar kota', [Required(message='Keluar kota wajib dipilih')])
    status_lingkungan = TextField('Status lingkungan', [Required(message='Status lingkungan wajib dipilih')])
    sakit              = TextField('Sakit', [Required(message='Sakit wajib dipilih')])
    masalah_penciuman  = TextField('Masalah penciuman', [Required(message='Masalah penciuman wajib dipilih')])
    persetujuan = TextField('Persetujuan', [Required(message='Persetujuan wajib dipilih')])
    hamil             = TextField('Hamil', [Required(message='Hamil wajib dipilih')])
    donatur              = TextField('Donatur', [Required(message='Donasi wajib dipilih')])

    instance = None
    document_class = PendaftaranAmida

    def __init__(self, document=None, *args, **kwargs):
        super(PendaftaranAmidaForm, self).__init__(*args, **kwargs)

    def save(self, skor):
        waktu = datetime.now()
        if self.instance is None:
            self.instance = self.document_class()
            created = waktu
        else:
            created = self.instance.created

        self.instance.email = self.email.data
        self.instance.nama_lengkap = self.nama_lengkap.data
        self.instance.hamil = self.hamil.data
        self.instance.tempat_tinggal = self.tempat_tinggal.data
        self.instance.nohp = self.nohp.data
        self.instance.pekerjaaan = self.pekerjaaan.data
        self.instance.keluar_kota = self.keluar_kota.data
        self.instance.status_lingkungan = self.status_lingkungan.data
        self.instance.sakit = self.sakit.data
        self.instance.masalah_penciuman = self.masalah_penciuman.data
        self.instance.persetujuan = self.persetujuan.data
        self.instance.skor = skor
        self.instance.donatur = self.donatur.data

        self.instance.created = created
        self.instance.modified = waktu

        self.instance.save()
        return self.instance

class PendaftaranQohwahForm(FlaskForm):
    email        = TextField('Email', [Required(message='Email wajib diisi')])
    nama_lengkap  = TextField('Nama', [Required(message='Nama wajib diisi')])
    tempat_tinggal  = TextField('Alamat', [Required(message='Alamat wajib diisi')])
    nohp            = TextField('No.Hp', [Required(message='No.Hp wajib diisi')])
    pekerjaaan      = TextField('Pekerjaan', [Required(message='Pekerjaan wajib diisi')])
    keluar_kota      = TextField('Keluar kota', [Required(message='Keluar kota wajib dipilih')])
    status_interaksi = TextField('Status interaksi', [Required(message='Status interaksi wajib dipilih')])
    status_lingkungan = TextField('Status lingkungan', [Required(message='Status lingkungan wajib dipilih')])
    sakit              = TextField('Sakit', [Required(message='Sakit wajib dipilih')])
    masalah_penciuman  = TextField('Masalah penciuman', [Required(message='Masalah penciuman wajib dipilih')])
    persetujuan = TextField('Persetujuan', [Required(message='Persetujuan wajib dipilih')])
    donatur              = TextField('Donatur', [Required(message='Donasi wajib dipilih')])

    instance = None
    document_class = Pendaftaran

    def __init__(self, document=None, *args, **kwargs):
        super(PendaftaranQohwahForm, self).__init__(*args, **kwargs)

    def save(self, skor):
        waktu = datetime.now()
        if self.instance is None:
            self.instance = self.document_class()
            created = waktu
        else:
            created = self.instance.created

        self.instance.email = self.email.data
        self.instance.nama_lengkap = self.nama_lengkap.data
        self.instance.jk = "ikhwan"
        self.instance.tempat_tinggal = self.tempat_tinggal.data
        self.instance.nohp = self.nohp.data
        self.instance.pekerjaaan = self.pekerjaaan.data
        self.instance.keluar_kota = self.keluar_kota.data
        self.instance.status_lingkungan = self.status_lingkungan.data
        self.instance.status_interaksi = self.status_interaksi.data
        self.instance.sakit = self.sakit.data
        self.instance.masalah_penciuman = self.masalah_penciuman.data
        self.instance.persetujuan = self.persetujuan.data
        self.instance.skor = skor
        self.instance.tipengaji = "ngajisantai"
        self.instance.donatur = self.donatur.data

        self.instance.created = created
        self.instance.modified = waktu

        self.instance.save()
        return self.instance

class PendaftaranTablighForm(FlaskForm):
    email        = TextField('Email', [Required(message='Email wajib diisi')])
    nama_lengkap  = TextField('Nama', [Required(message='Nama wajib diisi')])
    jk             = TextField('Gender', [Required(message='Jenis wajib dipilih')])
    tempat_tinggal  = TextField('Alamat', [Required(message='Alamat wajib diisi')])
    nohp            = TextField('No.Hp', [Required(message='No.Hp wajib diisi')])
    pekerjaaan      = TextField('Pekerjaan', [Required(message='Pekerjaan wajib diisi')])
    keluar_kota      = TextField('Keluar kota', [Required(message='Keluar kota wajib dipilih')])
    status_interaksi = TextField('Status interaksi', [Required(message='Status interaksi wajib dipilih')])
    status_lingkungan = TextField('Status lingkungan', [Required(message='Status lingkungan wajib dipilih')])
    sakit              = TextField('Sakit', [Required(message='Sakit wajib dipilih')])
    masalah_penciuman  = TextField('Masalah penciuman', [Required(message='Masalah penciuman wajib dipilih')])
    persetujuan = TextField('Persetujuan', [Required(message='Persetujuan wajib dipilih')])
    donatur              = TextField('Donatur', [Required(message='Donasi wajib dipilih')])

    instance = None
    document_class = Pendaftaran

    def __init__(self, document=None, *args, **kwargs):
        super(PendaftaranTablighForm, self).__init__(*args, **kwargs)

    def save(self, skor):
        waktu = datetime.now()
        if self.instance is None:
            self.instance = self.document_class()
            created = waktu
        else:
            created = self.instance.created

        self.instance.email = self.email.data
        self.instance.nama_lengkap = self.nama_lengkap.data
        self.instance.jk = self.jk.data
        self.instance.tempat_tinggal = self.tempat_tinggal.data
        self.instance.nohp = self.nohp.data
        self.instance.pekerjaaan = self.pekerjaaan.data
        self.instance.keluar_kota = self.keluar_kota.data
        self.instance.status_lingkungan = self.status_lingkungan.data
        self.instance.status_interaksi = self.status_interaksi.data
        self.instance.sakit = self.sakit.data
        self.instance.masalah_penciuman = self.masalah_penciuman.data
        self.instance.persetujuan = self.persetujuan.data
        self.instance.skor = skor
        self.instance.tipengaji = "tabligh"
        self.instance.donatur = self.donatur.data

        self.instance.created = created
        self.instance.modified = waktu

        self.instance.save()
        return self.instance


class PendaftaranTablighForm2(FlaskForm):
    email        = TextField('Email', [Required(message='Email wajib diisi')])
    nama_lengkap  = TextField('Nama', [Required(message='Nama wajib diisi')])
    jk             = TextField('Gender', [Required(message='Jenis wajib dipilih')])
    tempat_tinggal  = TextField('Alamat', [Required(message='Alamat wajib diisi')])
    nohp            = TextField('No.Hp', [Required(message='No.Hp wajib diisi')])
    pekerjaaan      = TextField('Pekerjaan', [Required(message='Pekerjaan wajib diisi')])
    keluar_kota      = TextField('Keluar kota', [Required(message='Keluar kota wajib dipilih')])
    status_interaksi = TextField('Status interaksi', [Required(message='Status interaksi wajib dipilih')])
    status_lingkungan = TextField('Status lingkungan', [Required(message='Status lingkungan wajib dipilih')])
    sakit              = TextField('Sakit', [Required(message='Sakit wajib dipilih')])
    masalah_penciuman  = TextField('Masalah penciuman', [Required(message='Masalah penciuman wajib dipilih')])
    persetujuan = TextField('Persetujuan', [Required(message='Persetujuan wajib dipilih')])
    donatur              = TextField('Donatur', [Required(message='Donasi wajib dipilih')])

    instance = None
    document_class = Pendaftaran

    def __init__(self, document=None, *args, **kwargs):
        super(PendaftaranTablighForm2, self).__init__(*args, **kwargs)

    def save(self, skor):
        waktu = datetime.now()
        if self.instance is None:
            self.instance = self.document_class()
            created = waktu
        else:
            created = self.instance.created

        self.instance.email = self.email.data
        self.instance.nama_lengkap = self.nama_lengkap.data
        self.instance.jk = self.jk.data
        self.instance.tempat_tinggal = self.tempat_tinggal.data
        self.instance.nohp = self.nohp.data
        self.instance.pekerjaaan = self.pekerjaaan.data
        self.instance.keluar_kota = self.keluar_kota.data
        self.instance.status_lingkungan = self.status_lingkungan.data
        self.instance.status_interaksi = self.status_interaksi.data
        self.instance.sakit = self.sakit.data
        self.instance.masalah_penciuman = self.masalah_penciuman.data
        self.instance.persetujuan = self.persetujuan.data
        self.instance.skor = skor
        self.instance.tipengaji = "tabligh2"
        self.instance.donatur = self.donatur.data

        self.instance.created = created
        self.instance.modified = waktu

        self.instance.save()
        return self.instance

