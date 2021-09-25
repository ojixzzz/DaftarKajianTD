import re
from flask import Blueprint, render_template, request, \
                  flash, g, session, redirect, url_for, abort, redirect
from flaskr import db
from mongoengine.queryset.visitor import Q
from datetime import datetime, timedelta
from flaskr.mod_pendaftaran.forms import PendaftaranFormv2, PendaftaranForm, PendaftaranAmidaForm, PendaftaranQohwahForm, PendaftaranTablighForm, PendaftaranTablighForm2
from flaskr.mod_pendaftaran.models import Pendaftaran, PendaftaranAmida

mod_pendaftaran = Blueprint('pendaftaran', __name__, url_prefix='')

@mod_pendaftaran.route('/', methods=['GET', 'POST'])
def index():
    tipengaji = "rabu"
    namangaji = "#ngajiteras"
    data      = {"namangaji": namangaji}
    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    if hariini == 0:
        dt_awal = dt_awal #- timedelta(days=2)
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=2)
    #elif hariini == 3:
    #    dt_awal = dt_awal
    #elif hariini == 4:
    #    dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 5:
        dt_awal = dt_awal
    elif hariini == 6:
        dt_awal = dt_awal - timedelta(days=1)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 75, 35, 40)

@mod_pendaftaran.route('/ngajisantai/', methods=['GET', 'POST']) 
def ngajisantai():
    tipengaji = "ngajisantai"
    namangaji = "#ngajisantai"
    data      = {"namangaji": namangaji}
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

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 20, 20, 0)

@mod_pendaftaran.route('/ngajisantai/', methods=['GET', 'POST']) 
def ngajiserius():
    tipengaji = "ngajiserius"
    namangaji = "#ngajiserius"
    data      = {"namangaji": namangaji}
    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    if hariini == 0:
        dt_awal = dt_awal
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=2)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 20, 20, 0)

@mod_pendaftaran.route('/amida/', methods=['GET', 'POST']) 
def amida(): 
    tipengaji = "amida"
    namangaji = "#ngajiamida"
    data      = {"namangaji": namangaji}
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

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 25, 0, 25)

@mod_pendaftaran.route('/ngaji/', methods=['GET', 'POST'])
def tabligh():
    tipengaji = "tabligh"
    namangaji = "#tabligh"
    data      = {"namangaji": namangaji}
    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    #0 = senin
    if hariini == 0:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=2)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=3)
    elif hariini == 3:
        dt_awal = dt_awal - timedelta(days=4)
    elif hariini == 4:
        dt_awal = dt_awal - timedelta(days=5)
    elif hariini == 5:
        dt_awal = dt_awal - timedelta(days=6)
    elif hariini == 6:
        dt_awal = dt_awal #- timedelta(days=6)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 75, 35, 40)

@mod_pendaftaran.route('/kajian/', methods=['GET', 'POST'])
def tabligh2():
    tipengaji = "tabligh2"
    namangaji = "#tabligh2"
    data      = {"namangaji": namangaji}
    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    #0 = senin
    if hariini == 0:
        dt_awal = dt_awal
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=2)
    elif hariini == 3:
        dt_awal = dt_awal - timedelta(days=3)
    elif hariini == 4:
        dt_awal = dt_awal - timedelta(days=4)
    elif hariini == 5:
        dt_awal = dt_awal - timedelta(days=5)
    elif hariini == 6:
        dt_awal = dt_awal - timedelta(days=6)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 75, 35, 40)

def createform(dt_awal, dt_akhir, tipengaji, namangaji, quota_total, quota_l, quota_p):
    data = {"namangaji": namangaji}
    form = PendaftaranFormv2()
    nama_lengkap = form.nama_lengkap.data
    usia         = form.usia.data
    email        = form.email.data
    jk           = form.jk.data
    tempat_tinggal = form.tempat_tinggal.data
    nohp           = form.nohp.data
    pekerjaaan     = form.pekerjaaan.data
    hamil           = form.hamil.data
    sakit          = form.sakit.data
    donatur        = form.donatur.data

    _pendaftar_today = Pendaftaran.objects(skor=5, tipengaji=tipengaji).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > (quota_total-1):
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = Pendaftaran.objects(nohp=sessi_nohp, tipengaji=tipengaji).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now(),
                "namangaji": namangaji
            }
            if _pendaftar_user.skor > 4:
                if tipengaji=="amida":
                    return render_template("pendaftaranv2_selesai_diterima_amida.html", data=data)

                return render_template("pendaftaranv2_selesai_diterima.html", data=data)
            else:
                return render_template("pendaftaranv2_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if nama_lengkap and usia and email and jk and tempat_tinggal and nohp and pekerjaaan and hamil and sakit and donatur:
            skor = 0
            if sakit == "tidak":
                skor+=5

            data["jk"] = jk
            if jk == "akhwat":
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji=tipengaji).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > (quota_p-1):
                    return render_template("pendaftaran_selesai_full.html", data=data)
            else:
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji=tipengaji).filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > (quota_l-1):
                    return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor, tipengaji)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now(),
                "namangaji": namangaji
            }

            if skor > 4:
                if tipengaji=="amida":
                    return render_template("pendaftaranv2_selesai_diterima_amida.html", data=data)

                return render_template("pendaftaranv2_selesai_diterima.html", data=data)
            elif skor < 5:
                return render_template("pendaftaranv2_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaranv2_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaranv2.html", data=data, form=form)

# HAMIL
'''
@mod_pendaftaran.route('/ngajisantai/', methods=['GET', 'POST']) 
def ngajisantai():
    data = {}
    form = PendaftaranQohwahForm()
    email = form.email.data
    nama_lengkap = form.nama_lengkap.data
    tempat_tinggal = form.tempat_tinggal.data
    nohp = form.nohp.data
    pekerjaaan = form.pekerjaaan.data
    keluar_kota = form.keluar_kota.data
    status_interaksi = form.status_interaksi.data
    status_lingkungan = form.status_lingkungan.data
    sakit = form.sakit.data
    masalah_penciuman = form.masalah_penciuman.data
    persetujuan = form.persetujuan.data
    donatur = form.donatur.data

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

    _pendaftar_today = Pendaftaran.objects(skor=5, tipengaji="ngajisantai").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > 19:
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = Pendaftaran.objects(nohp=sessi_nohp, tipengaji="ngajisantai").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now()
            }
            if _pendaftar_user.skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and status_interaksi and sakit and masalah_penciuman and persetujuan and donatur:
            skor = 0
            if keluar_kota == "tidak":
                skor+=1
            if status_lingkungan == "tidak":
                skor+=1
            if sakit == "tidak":
                skor+=1
            if masalah_penciuman == "tidak":
                skor+=1
            if status_interaksi == "tidak":
                skor+=1

            #if len(re.findall("gedhongtengen", tempat_tinggal.lower())) > 0:
            #    skor=skor-1

            _pendaftar_today_ = Pendaftaran.objects(skor=5, tipengaji="ngajisantai").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
            if _pendaftar_today_.count() > 19:
                return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now()
            }

            if skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            elif skor < 5:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaran_qohwah.html", data=data, form=form)

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
    donatur = form.donatur.data

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
    if _pendaftar_today.count() > 24:
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
        if hamil and email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and sakit and masalah_penciuman and persetujuan and donatur:
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
            if _pendaftar_today_.count() > 24:
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
    status_interaksi = form.status_interaksi.data
    status_lingkungan = form.status_lingkungan.data
    sakit = form.sakit.data
    masalah_penciuman = form.masalah_penciuman.data
    persetujuan = form.persetujuan.data
    donatur = form.donatur.data

    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    if hariini == 0:
        dt_awal = dt_awal #- timedelta(days=2)
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=2)
    #elif hariini == 3:
    #    dt_awal = dt_awal
    #elif hariini == 4:
    #    dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 5:
        dt_awal = dt_awal
    elif hariini == 6:
        dt_awal = dt_awal - timedelta(days=1)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    #return render_template("pendaftaran_tutup.html", data=data)

    _pendaftar_today = Pendaftaran.objects(skor=5, tipengaji="rabu").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > 74:
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = Pendaftaran.objects(nohp=sessi_nohp, tipengaji="rabu").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now()
            }
            if _pendaftar_user.skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if jk and email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and status_interaksi and sakit and masalah_penciuman and persetujuan and donatur:
            skor = 0
            if keluar_kota == "tidak":
                skor+=1
            if status_lingkungan == "tidak":
                skor+=1
            if sakit == "tidak":
                skor+=1
            if masalah_penciuman == "tidak":
                skor+=1
            if status_interaksi == "tidak":
                skor+=1

            #if len(re.findall("gedhongtengen", tempat_tinggal.lower())) > 0:
            #    skor=skor-1

            if jk == "akhwat":
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji="rabu").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > 39:
                    return render_template("pendaftaran_selesai_full.html", data=data)
            else:
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji="rabu").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > 34:
                    return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now()
            }

            if skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            elif skor < 5:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaran.html", data=data, form=form)

@mod_pendaftaran.route('/ngaji/', methods=['GET', 'POST'])
def tabligh():
    data = {}
    form = PendaftaranTablighForm()
    email = form.email.data
    nama_lengkap = form.nama_lengkap.data
    jk = form.jk.data
    tempat_tinggal = form.tempat_tinggal.data
    nohp = form.nohp.data
    pekerjaaan = form.pekerjaaan.data
    keluar_kota = form.keluar_kota.data
    status_interaksi = form.status_interaksi.data
    status_lingkungan = form.status_lingkungan.data
    sakit = form.sakit.data
    masalah_penciuman = form.masalah_penciuman.data
    persetujuan = form.persetujuan.data
    donatur = form.donatur.data

    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    #0 = senin
    if hariini == 0:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=2)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=3)
    elif hariini == 3:
        dt_awal = dt_awal - timedelta(days=4)
    elif hariini == 4:
        dt_awal = dt_awal - timedelta(days=5)
    elif hariini == 5:
        dt_awal = dt_awal - timedelta(days=6)
    elif hariini == 6:
        dt_awal = dt_awal #- timedelta(days=6)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    _pendaftar_today = Pendaftaran.objects(skor=5, tipengaji="tabligh").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > 74:
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = Pendaftaran.objects(nohp=sessi_nohp, tipengaji="tabligh").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now()
            }
            if _pendaftar_user.skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if jk and email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and status_interaksi and sakit and masalah_penciuman and persetujuan and donatur:
            skor = 0
            if keluar_kota == "tidak":
                skor+=1
            if status_lingkungan == "tidak":
                skor+=1
            if sakit == "tidak":
                skor+=1
            if masalah_penciuman == "tidak":
                skor+=1
            if status_interaksi == "tidak":
                skor+=1

            if jk == "akhwat":
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji="tabligh").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > 39:
                    return render_template("pendaftaran_selesai_full.html", data=data)
            else:
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji="tabligh").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > 34:
                    return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now()
            }

            if skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            elif skor < 5:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaran_tabligh.html", data=data, form=form)

@mod_pendaftaran.route('/kajian/', methods=['GET', 'POST'])
def tabligh2():
    data = {}
    form = PendaftaranTablighForm2()
    email = form.email.data
    nama_lengkap = form.nama_lengkap.data
    jk = form.jk.data
    tempat_tinggal = form.tempat_tinggal.data
    nohp = form.nohp.data
    pekerjaaan = form.pekerjaaan.data
    keluar_kota = form.keluar_kota.data
    status_interaksi = form.status_interaksi.data
    status_lingkungan = form.status_lingkungan.data
    sakit = form.sakit.data
    masalah_penciuman = form.masalah_penciuman.data
    persetujuan = form.persetujuan.data
    donatur = form.donatur.data

    dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)

    hariini = datetime.now().weekday()
    #0 = senin
    if hariini == 0:
        dt_awal = dt_awal
    elif hariini == 1:
        dt_awal = dt_awal - timedelta(days=1)
    elif hariini == 2:
        dt_awal = dt_awal - timedelta(days=2)
    elif hariini == 3:
        dt_awal = dt_awal - timedelta(days=3)
    elif hariini == 4:
        dt_awal = dt_awal - timedelta(days=4)
    elif hariini == 5:
        dt_awal = dt_awal - timedelta(days=5)
    elif hariini == 6:
        dt_awal = dt_awal - timedelta(days=6)
    else:
        return render_template("pendaftaran_tutup.html", data=data)

    _pendaftar_today = Pendaftaran.objects(skor=5, tipengaji="tabligh2").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
    if _pendaftar_today.count() > 39:
        return render_template("pendaftaran_selesai_full.html", data=data)

    sessi_nohp = session.get('nohp')
    if nohp or sessi_nohp:
        if nohp:
            sessi_nohp = nohp
            session['nohp'] = nohp
        _pendaftar_user = Pendaftaran.objects(nohp=sessi_nohp, tipengaji="tabligh2").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir)).first()
        if _pendaftar_user:
            data = {
                "nama" : _pendaftar_user.nama_lengkap,
                "tanggal" : datetime.now()
            }
            if _pendaftar_user.skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)

    if request.method == 'POST':
        if jk and email and nama_lengkap and tempat_tinggal and nohp and pekerjaaan and keluar_kota and status_lingkungan and status_interaksi and sakit and masalah_penciuman and persetujuan and donatur:
            skor = 0
            if keluar_kota == "tidak":
                skor+=1
            if status_lingkungan == "tidak":
                skor+=1
            if sakit == "tidak":
                skor+=1
            if masalah_penciuman == "tidak":
                skor+=1
            if status_interaksi == "tidak":
                skor+=1

            if jk == "akhwat":
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji="tabligh2").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > 19:
                    return render_template("pendaftaran_selesai_full.html", data=data)
            else:
                _pendaftar_today_ = Pendaftaran.objects(jk=jk, skor=5, tipengaji="tabligh2").filter(Q(created__gte=dt_awal) & Q(created__lte=dt_akhir))
                if _pendaftar_today_.count() > 19:
                    return render_template("pendaftaran_selesai_full.html", data=data)

            form.save(skor)
            session['nohp'] = nohp

            data = {
                "nama" : nama_lengkap,
                "tanggal" : datetime.now()
            }

            if skor > 4:
                return render_template("pendaftaran_selesai_diterima.html", data=data)
            elif skor < 5:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
            else:
                return render_template("pendaftaran_selesai_ditolak.html", data=data)
        else:
            flash('Error : Coba lagi, silakan isi semua pilihan dengan benar', 'error')

    return render_template("pendaftaran_tabligh.html", data=data, form=form)
'''