import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from projekrkk import models as projekrkk_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_projekrkk_Jenis(**kwargs):
    defaults = {}
    defaults["nama_jenis"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Jenis.objects.create(**defaults)
def create_projekrkk_Sublembangan(**kwargs):
    defaults = {}
    defaults["rumusan_kawalan_gunatanah"] = ""
    defaults["luas_hektar"] = ""
    defaults["polygon_geom"] = ""
    defaults["rumusan_kualiti_air"] = ""
    defaults["nama_sublembangan"] = ""
    defaults["kod_sublembangan"] = ""
    defaults["zon_tindakan"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Sublembangan.objects.create(**defaults)
def create_projekrkk_Lembangan(**kwargs):
    defaults = {}
    defaults["polygon_geom"] = ""
    defaults["kod_lembangan"] = ""
    defaults["luas_hektar"] = ""
    defaults["nama_lembangan"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Lembangan.objects.create(**defaults)
def create_projekrkk_Kategori(**kwargs):
    defaults = {}
    defaults["nama_kategori"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Kategori.objects.create(**defaults)
def create_projekrkk_Sempadanrkk(**kwargs):
    defaults = {}
    defaults["luas_hektar"] = ""
    defaults["nama_rkk"] = ""
    defaults["polygon_geom"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Sempadanrkk.objects.create(**defaults)
def create_projekrkk_Rumusankualitiair(**kwargs):
    defaults = {}
    defaults["nama_sublembangan"] = ""
    defaults["zon_tindakan"] = ""
    defaults["luas_hektar"] = ""
    defaults["rumusan_kawalan_gunatanah"] = ""
    defaults["rumusan_kualiti_air"] = ""
    defaults["kod_sublembangan"] = ""
    defaults["polygon_geom"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Rumusankualitiair.objects.create(**defaults)
def create_projekrkk_Agensi(**kwargs):
    defaults = {}
    defaults["nama_agensi"] = ""
    defaults["no_tel"] = ""
    defaults["nama_pegawai"] = ""
    defaults["emel"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Agensi.objects.create(**defaults)
def create_projekrkk_Status(**kwargs):
    defaults = {}
    defaults["nama_status"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Status.objects.create(**defaults)
def create_projekrkk_Fasa(**kwargs):
    defaults = {}
    defaults["nama_fasa"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Fasa.objects.create(**defaults)
def create_projekrkk_Zontindakan(**kwargs):
    defaults = {}
    defaults["nama_sublembangan"] = ""
    defaults["luas_hektar"] = ""
    defaults["zon_tindakan"] = ""
    defaults["rumusan_kualiti_air"] = ""
    defaults["polygon_geom"] = ""
    defaults["rumusan_kawalan_gunatanah"] = ""
    defaults["kod_sublembangan"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Zontindakan.objects.create(**defaults)
def create_projekrkk_Projek(**kwargs):
    defaults = {}
    defaults["nama_projek"] = ""
    defaults["mukasurat_laporan"] = ""
    defaults["aktif"] = ""
    defaults["imej"] = ""
    defaults["deskripsi_cadangan"] = ""
    defaults["kod_projek"] = ""
    defaults["justifikasi_cadangan"] = ""
    defaults["kos_pelaksanaan"] = ""
    defaults["catatan"] = ""
    defaults["sasaran_pencapaian"] = ""
    defaults["polygon_geom"] = ""
    if "status" not in kwargs:
        defaults["status"] = create_projekrkk_Status()
    if "sublembangan" not in kwargs:
        defaults["sublembangan"] = create_projekrkk_Sublembangan()
    if "fokus" not in kwargs:
        defaults["fokus"] = create_projekrkk_Fokus()
    if "agensi_pembiaya" not in kwargs:
        defaults["agensi_pembiaya"] = create_projekrkk_Agensi()
    if "agensi_pelaksana" not in kwargs:
        defaults["agensi_pelaksana"] = create_projekrkk_Agensi()
    if "jenis" not in kwargs:
        defaults["jenis"] = create_projekrkk_Jenis()
    if "fasa" not in kwargs:
        defaults["fasa"] = create_projekrkk_Fasa()
    if "kategori" not in kwargs:
        defaults["kategori"] = create_projekrkk_Kategori()
    if "agensi_pemula" not in kwargs:
        defaults["agensi_pemula"] = create_projekrkk_Agensi()
    defaults.update(**kwargs)
    return projekrkk_models.Projek.objects.create(**defaults)
def create_projekrkk_Sungai(**kwargs):
    defaults = {}
    defaults["kategori_sungai"] = ""
    defaults["nama_sungai"] = ""
    defaults["kod_lembangan"] = ""
    defaults["panjang_km"] = ""
    defaults["polygon_geom"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Sungai.objects.create(**defaults)
def create_projekrkk_Fokus(**kwargs):
    defaults = {}
    defaults["nama_fokus"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Fokus.objects.create(**defaults)
def create_projekrkk_Rumusankawalangunatanah(**kwargs):
    defaults = {}
    defaults["nama_sublembangan"] = ""
    defaults["rumusan_kawalan_gunatanah"] = ""
    defaults["luas_hektar"] = ""
    defaults["polygon_geom"] = ""
    defaults["zon_tindakan"] = ""
    defaults["kod_sublembangan"] = ""
    defaults["rumusan_kualiti_air"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Rumusankawalangunatanah.objects.create(**defaults)
def create_projekrkk_Gunatanahsemasa(**kwargs):
    defaults = {}
    defaults["kod_gtn"] = ""
    defaults["no_lot"] = ""
    defaults["mukim_id"] = ""
    defaults["upi"] = ""
    defaults["gtn2"] = ""
    defaults["luas_hektar"] = ""
    defaults["pbt_id"] = ""
    defaults["gtn1"] = ""
    defaults["teks"] = ""
    defaults["nama"] = ""
    defaults["status"] = ""
    defaults["negeri_id"] = ""
    defaults["seksyen_id"] = ""
    defaults["daerah_id"] = ""
    defaults["tahun_data"] = ""
    defaults["fcode"] = ""
    defaults["polygon_geom"] = ""
    defaults.update(**kwargs)
    return projekrkk_models.Gunatanahsemasa.objects.create(**defaults)
