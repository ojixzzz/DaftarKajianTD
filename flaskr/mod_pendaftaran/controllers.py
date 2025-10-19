import re, json
from flask import Blueprint, render_template, request, \
                  flash, g, session, redirect, url_for, abort
from flaskr import db
from mongoengine.queryset.visitor import Q
from datetime import datetime, timedelta
from flaskr.mod_pendaftaran.forms import PendaftaranFormv2, PendaftaranForm, PendaftaranAmidaForm, PendaftaranQohwahForm, PendaftaranTablighForm, PendaftaranTablighForm2
from flaskr.mod_pendaftaran.models import Pendaftaran, PendaftaranAmida, Provinces, Regencies, Districts, Villages

mod_pendaftaran = Blueprint('pendaftaran', __name__, url_prefix='')

@mod_pendaftaran.route('/kulonprogo/', methods=['GET', 'POST'])
def kulonprogo():
    return redirect('https://sedekah.terasdakwah.com/campaign/kp')

@mod_pendaftaran.route('/lombok/', methods=['GET', 'POST'])
def lombok():
    return redirect('https://sedekah.terasdakwah.com/campaign/qurbanlombok')

@mod_pendaftaran.route('/palu/', methods=['GET', 'POST'])
def palu():
    return redirect('https://sedekah.terasdakwah.com/campaign/qurbanpalu')

@mod_pendaftaran.route('/qurban/', methods=['GET', 'POST'])
def qurban():
    return redirect('https://sedekah.terasdakwah.com/campaign/qurbanasyik')

@mod_pendaftaran.route('/keluarga/', methods=['GET', 'POST'])
def keluarga():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSemlZiDom09XfvnuRqqPFQr9yonIEPFRVqIYTVqXrDwWHYXvg/viewform?usp=dialog')

@mod_pendaftaran.route('/nikah/', methods=['GET', 'POST'])
def nikah():
    return redirect('https://bebaju.my.canva.site/teras-dakwah-wedding-invitation')

@mod_pendaftaran.route('/literasi/', methods=['GET', 'POST'])
def literasi():
    return redirect('https://forms.gle/M75K4jNdtDVpiBe17')

@mod_pendaftaran.route('/sbs/', methods=['GET', 'POST'])
def sbs():
    return redirect('https://forms.gle/9Far1UDT35wu3Ri7A')

@mod_pendaftaran.route('/kmip/', methods=['GET', 'POST'])
def kmip():
    return redirect('https://forms.gle/V61sHJWbvm4dXvRV6')

@mod_pendaftaran.route('/cds/', methods=['GET', 'POST'])
def cds():
    return redirect('https://forms.gle/wYrACFKmdw4x68Ja8')

@mod_pendaftaran.route('/sirah/', methods=['GET', 'POST'])
def sirah():
    return redirect('https://forms.gle/JKP2YyAHW1azD7Km9')

@mod_pendaftaran.route('/camp/', methods=['GET', 'POST'])
def camp():
    return redirect("https://sasaguid.my.canva.site/teras-camp-2024")

@mod_pendaftaran.route('/makna/', methods=['GET', 'POST'])
def makna():
    return redirect("https://forms.gle/vFJE8KLWCRUtU1E97")

@mod_pendaftaran.route('/shb/', methods=['GET', 'POST'])
def shb():
    return redirect("https://forms.gle/Ti3Ei4fEUJq2jzmK9")

@mod_pendaftaran.route('/pranikah/', methods=['GET', 'POST'])
def pranikah():
    return redirect("https://forms.gle/v8DRYZaWxVvLwoVt6")

@mod_pendaftaran.route('/sbq/', methods=['GET', 'POST'])
def sbq():
    return redirect("https://forms.gle/MHzzeVy9TkpyvWE67")

@mod_pendaftaran.route('/gaza/', methods=['GET', 'POST'])
def gaza():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfPBQ3g6UTmDi4dIH3db4SJPDUIr-_cjnI_-LXOff5lb3VC7Q/viewform")

@mod_pendaftaran.route('/kareema/', methods=['GET', 'POST'])
def kareema():
    return redirect("https://docs.google.com/forms/d/1aot24aWZJrq2jPtYhgAbUXQFNIMeT9xfZUc_rm89N38/edit")

@mod_pendaftaran.route('/nongki/', methods=['GET', 'POST'])
def nongki():
    return redirect("https://docs.google.com/forms/d/1kPv_ZW1qvQNiEHCCxQ8v7JUpNWOarWpxk0FgQp8VPGU/edit")

@mod_pendaftaran.route('/beqen/', methods=['GET', 'POST'])
def beqen():
    return redirect("https://docs.google.com/forms/d/1HsQrr0-UdoYNaE2P2xsk6iyPl2EtzRlKpAKe4M2ExQo/viewform?edit_requested=true")

@mod_pendaftaran.route('/keren/', methods=['GET', 'POST'])
def keren():
    return redirect("https://docs.google.com/forms/d/10yFlpNAMvjoBSltal1ufWmrkP-HDO4gwGd9vGQewsLo/viewform")

@mod_pendaftaran.route('/akbar/', methods=['GET', 'POST'])
def akbar():
    return redirect("https://docs.google.com/forms/d/1tr-jYVklAgEZBV7i30Q2UdBpgDKrPNvyZbvrhkfFi7E/edit")

@mod_pendaftaran.route('/cantik/', methods=['GET', 'POST'])
def cantik():
    return redirect("https://forms.gle/tzvkg3yfBTFQxRZ98")

@mod_pendaftaran.route('/curhat/', methods=['GET', 'POST'])
def curhat():
    return redirect("https://docs.google.com/forms/d/1kggcrRq0_FHGzhCV7LuphKo9zhIdbk8fk6HQoFe9e6k/edit")

@mod_pendaftaran.route('/puasasyawal/', methods=['GET', 'POST'])
def puasasyawal():
    return redirect("https://forms.gle/S1g14wLMqodAmsph6")

@mod_pendaftaran.route('/syawalan/', methods=['GET', 'POST'])
def syawalan():
    return redirect("https://forms.gle/AvRpxkDbXfNKkb9m9")

@mod_pendaftaran.route('/caricinta/', methods=['GET', 'POST'])
def caricinta():
    return redirect("https://forms.gle/MwHYoR2QtKSuGqu79")

@mod_pendaftaran.route('/cinta/', methods=['GET', 'POST'])
def cinta():
    return redirect("https://forms.gle/agjgVrpoWDXFgmxa6")

@mod_pendaftaran.route('/program/', methods=['GET', 'POST'])
def program():
    return redirect("https://linktr.ee/programTD")

@mod_pendaftaran.route('/ummi/', methods=['GET', 'POST'])
def ummi():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfzidTj4HFN7wXo2kkngGw6qkDyQaJz87q7q6f9R-E2nisWmw/viewform")

@mod_pendaftaran.route('/team/', methods=['GET', 'POST'])
def team():
    return redirect("https://forms.gle/sVy6wr2hWVc7BJ7q9")

@mod_pendaftaran.route('/survei/', methods=['GET', 'POST'])
def survei():
    return redirect("https://forms.gle/jcF6wEeFFvz6gcoR9")

@mod_pendaftaran.route('/ngaji/', methods=['GET', 'POST'])
def ngaji():
    return redirect("https://forms.gle/LBoAHzeT7zwhiHSU7")

@mod_pendaftaran.route('/rating/', methods=['GET', 'POST'])
def rating():
    return redirect("https://forms.gle/MaitZTDbbgqhz5su9")

@mod_pendaftaran.route('/relawan/', methods=['GET', 'POST'])
def relawan():
    return redirect("https://forms.gle/JQ8b6mzK5G3XnSHK8")

@mod_pendaftaran.route('/kpk/', methods=['GET', 'POST'])
def kpk():
    return redirect("https://forms.gle/8iduTUVh55bPaPyA7")

@mod_pendaftaran.route('/pahlawan/', methods=['GET', 'POST'])
def pahlawan():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdAFChYN_T2lSulur-gAE3nhQ71l4Py07XVr2NmlM_hnvqGkg/viewform")

@mod_pendaftaran.route('/hadits/', methods=['GET', 'POST'])
def hadits():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScqXASeqz6JRkbHU_2VgB9oSTr5ldqP63lxamI2g8DGqcXFCg/viewform?usp=sf_link")

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
    #else:
    #    return render_template("pendaftaran_tutup.html", data=data)

    #return render_template("pendaftaran_tutup.html", data=data)
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 370, 170, 200)

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
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 200, 100, 100)

@mod_pendaftaran.route('/ngajiserius/', methods=['GET', 'POST']) 
def ngajiserius():
    return redirect("https://s.id/ngajiseriusonline")
    # tipengaji = "ngajiserius"
    # namangaji = "#ngajiserius"
    # data      = {"namangaji": namangaji}
    # dt_awal = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 0, minute = 0, second = 0)
    # dt_akhir = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour = 23, minute = 59, second = 59)
    # 
    # hariini = datetime.now().weekday()
    # if hariini == 0:
    #     dt_awal = dt_awal
    # elif hariini == 1:
    #     dt_awal = dt_awal - timedelta(days=1)
    # elif hariini == 2:
    #     dt_awal = dt_awal - timedelta(days=2)
    # else:
    #     return render_template("pendaftaran_tutup.html", data=data)
    # 
    #return render_template("pendaftaran_tutup.html", data=data)
    # return createform(dt_awal, dt_akhir, tipengaji, namangaji, 20, 20, 0)

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
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 100, 0, 100)

@mod_pendaftaran.route('/ngajix/', methods=['GET', 'POST'])
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
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 500, 220, 280)

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
    return createform(dt_awal, dt_akhir, tipengaji, namangaji, 500, 220, 280)

def createform(dt_awal, dt_akhir, tipengaji, namangaji, quota_total, quota_l, quota_p):
    data = {"namangaji": namangaji}
    form = PendaftaranFormv2()
    nama_lengkap = form.nama_lengkap.data
    usia         = form.usia.data
    email        = form.email.data
    jk           = form.jk.data
    nohp           = form.nohp.data
    pekerjaaan     = form.pekerjaaan.data
    hamil           = form.hamil.data
    sakit          = form.sakit.data
    donatur        = form.donatur.data

    kabupaten = form.kabupaten.data
    kecamatan = form.kecamatan.data
    kelurahan = form.kelurahan.data

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
        if nama_lengkap and usia and email and jk and nohp and pekerjaaan and hamil and sakit and donatur and kabupaten and kecamatan and kelurahan:
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


@mod_pendaftaran.route('/get_kab/<id>', methods=['GET'])
def get_kab(id):
    data = [{'id': '', 'name': 'Kabupaten/Kota'}]
    if id != "":
        regencies = Regencies.objects(province=id).limit(100)
        for regency in regencies:
            data.append({'id': str(regency.id), 'name': regency.name})
    return json.dumps(data)

@mod_pendaftaran.route('/get_kec/<id>', methods=['GET'])
def get_kec(id):
    data = [{'id': '', 'name': 'Kecamatan'}]
    if id != "":
        districts = Districts.objects(regency=id).limit(100)
        for datax in districts:
            data.append({'id': str(datax.id), 'name': datax.name})
    return json.dumps(data)

@mod_pendaftaran.route('/get_desa/<id>', methods=['GET'])
def get_desa(id):
    data = [{'id': '', 'name': 'Kelurahan'}]
    if id != "":
        vilages = Villages.objects(district=id).limit(100)
        for datax in vilages:
            data.append({'id': str(datax.id), 'name': datax.name})
    return json.dumps(data)
