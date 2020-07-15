from flaskr import db
from datetime import datetime, timedelta

class Pendaftaran(db.Document):
    email = db.StringField()
    nama_lengkap = db.StringField()
    tempat_tinggal  = db.StringField()
    nohp            = db.StringField()
    pekerjaaan      = db.StringField()
    keluar_kota     = db.StringField()
    status_lingkungan = db.StringField()
    sakit             = db.StringField()
    masalah_penciuman = db.StringField()
    persetujuan       = db.StringField()
    skor              = db.IntField(default=0)
    jk              = db.StringField(default="ikhwan")

    created    = db.DateTimeField()
    modified   = db.DateTimeField()

class PendaftaranAmida(db.Document):
    email = db.StringField()
    nama_lengkap = db.StringField()
    tempat_tinggal  = db.StringField()
    nohp            = db.StringField()
    pekerjaaan      = db.StringField()
    keluar_kota     = db.StringField()
    status_lingkungan = db.StringField()
    sakit             = db.StringField()
    masalah_penciuman = db.StringField()
    persetujuan       = db.StringField()
    skor              = db.IntField(default=0)
    hamil              = db.StringField(default="tidak")

    created    = db.DateTimeField()
    modified   = db.DateTimeField()