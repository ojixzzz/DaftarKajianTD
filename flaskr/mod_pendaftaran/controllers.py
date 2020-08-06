from flask import Blueprint, render_template, request, \
                  flash, g, session, redirect, url_for, abort, redirect
from flaskr import db
from mongoengine.queryset.visitor import Q
from datetime import datetime, timedelta
from flaskr.mod_pendaftaran.forms import PendaftaranForm, PendaftaranAmidaForm
from flaskr.mod_pendaftaran.models import Pendaftaran, PendaftaranAmida

mod_pendaftaran = Blueprint('pendaftaran', __name__, url_prefix='')

@mod_pendaftaran.route('/amida/', methods=['GET', 'POST']) 
def amida(): 
    data = {}
    form = PendaftaranAmidaForm()
    email = form.email.data
    nama_lengkap = form.nama_lengkap.data
    tempat_tinggal = form.tempat_tinggal.data
    nohp = form.nohp.data
    pekerjaaan = form.pekerjaaan.data
    keluar_kota = form.keluar_kota.data
    status_lingkungan = form.status_lingkungan.data
    sakit = form.sakit.data
    masalah_penciuman = form.masalah_penciuman.data
    persetujuan = form.persetujuan.data
    hamil = form.hamil.data

    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    if hariini == 2:
        dt_awal = dt_awal
    elif hariini == 3:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 4:
        dt_awal = dt_awal - timedelta(days=2)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    _pendaftar_today = PendaftaranAmida.objects(skor=4).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > 39:
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = PendaftaranAmida.objects(nohp=sessi_nohp).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now()
            }
            if _pendaftar_user.skor > 3:
                return render_template("pendaftaran_selesai_diterima_amida.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if hamil and email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and sakit and masalah_penciuman and persetujuan:
            skor = 0
            if keluar_kota == "tidak":
                skor+=1
            if status_lingkungan == "tidak":
                skor+=1
            if sakit == "tidak":
                skor+=1
            if masalah_penciuman == "tidak":
                skor+=1

            _pendaftar_today_ = PendaftaranAmida.objects(skor=4).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
            if _pendaftar_today_.count() > 39:
                return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now()
            }

            if skor > 3:
                return render_template("pendaftaran_selesai_diterima_amida.html", data=data)
            elif skor < 4:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaran_amida.html", data=data, form=form)

@mod_pendaftaran.route('/', methods=['GET', 'POST'])
def index():
    data = {}
    form = PendaftaranForm()
    email = form.email.data
    nama_lengkap = form.nama_lengkap.data
    jk = form.jk.data
    tempat_tinggal = form.tempat_tinggal.data
    nohp = form.nohp.data
    pekerjaaan = form.pekerjaaan.data
    keluar_kota = form.keluar_kota.data
    status_lingkungan = form.status_lingkungan.data
    sakit = form.sakit.data
    masalah_penciuman = form.masalah_penciuman.data
    persetujuan = form.persetujuan.data

    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    if hariini == 0:
        dt_awal = dt_awal
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=2)
    elif hariini == 3:
        dt_awal = dt_awal
    elif hariini == 4:
        dt_awal = dt_awal - timedelta(days=1)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    _pendaftar_today = Pendaftaran.objects(skor=4).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > 49:
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = Pendaftaran.objects(nohp=sessi_nohp).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now()
            }
            if _pendaftar_user.skor > 3:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if jk and email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and sakit and masalah_penciuman and persetujuan:
            skor = 0
            if keluar_kota == "tidak":
                skor+=1
            if status_lingkungan == "tidak":
                skor+=1
            if sakit == "tidak":
                skor+=1
            if masalah_penciuman == "tidak":
                skor+=1

            _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=4).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
            if _pendaftar_today_.count() > 25:
                return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now()
            }

            if skor > 3:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            elif skor < 4:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaran.html", data=data, form=form)