from django import forms
from projekrkk.models import Status
from projekrkk.models import Sublembangan
from projekrkk.models import Fokus
from projekrkk.models import Agensi
from projekrkk.models import Agensi
from projekrkk.models import Jenis
from projekrkk.models import Fasa
from projekrkk.models import Kategori
from projekrkk.models import Agensi
from . import models


class JenisForm(forms.ModelForm):
    class Meta:
        model = models.Jenis
        fields = [
            "nama_jenis",
        ]


class SublembanganForm(forms.ModelForm):
    class Meta:
        model = models.Sublembangan
        fields = [
            "rumusan_kawalan_gunatanah",
            "luas_hektar",
            "polygon_geom",
            "rumusan_kualiti_air",
            "nama_sublembangan",
            "kod_sublembangan",
            "zon_tindakan",
        ]


class LembanganForm(forms.ModelForm):
    class Meta:
        model = models.Lembangan
        fields = [
            "polygon_geom",
            "kod_lembangan",
            "luas_hektar",
            "nama_lembangan",
        ]


class KategoriForm(forms.ModelForm):
    class Meta:
        model = models.Kategori
        fields = [
            "nama_kategori",
        ]


class SempadanrkkForm(forms.ModelForm):
    class Meta:
        model = models.Sempadanrkk
        fields = [
            "luas_hektar",
            "nama_rkk",
            "polygon_geom",
        ]


class RumusankualitiairForm(forms.ModelForm):
    class Meta:
        model = models.Rumusankualitiair
        fields = [
            "nama_sublembangan",
            "zon_tindakan",
            "luas_hektar",
            "rumusan_kawalan_gunatanah",
            "rumusan_kualiti_air",
            "kod_sublembangan",
            "polygon_geom",
        ]


class AgensiForm(forms.ModelForm):
    class Meta:
        model = models.Agensi
        fields = [
            "nama_agensi",
            "no_tel",
            "nama_pegawai",
            "emel",
        ]


class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = [
            "nama_status",
        ]


class FasaForm(forms.ModelForm):
    class Meta:
        model = models.Fasa
        fields = [
            "nama_fasa",
        ]


class ZontindakanForm(forms.ModelForm):
    class Meta:
        model = models.Zontindakan
        fields = [
            "nama_sublembangan",
            "luas_hektar",
            "zon_tindakan",
            "rumusan_kualiti_air",
            "polygon_geom",
            "rumusan_kawalan_gunatanah",
            "kod_sublembangan",
        ]


class ProjekForm(forms.ModelForm):
    class Meta:
        model = models.Projek
        fields = [
            "nama_projek",
            "mukasurat_laporan",
            "aktif",
            "imej",
            "deskripsi_cadangan",
            "kod_projek",
            "justifikasi_cadangan",
            "kos_pelaksanaan",
            "catatan",
            "sasaran_pencapaian",
            "polygon_geom",
            "status",
            "sublembangan",
            "fokus",
            "agensi_pembiaya",
            "agensi_pelaksana",
            "jenis",
            "fasa",
            "kategori",
            "agensi_pemula",
        ]

    def __init__(self, *args, **kwargs):
        super(ProjekForm, self).__init__(*args, **kwargs)
        self.fields["status"].queryset = Status.objects.all()
        self.fields["sublembangan"].queryset = Sublembangan.objects.all()
        self.fields["fokus"].queryset = Fokus.objects.all()
        self.fields["agensi_pembiaya"].queryset = Agensi.objects.all()
        self.fields["agensi_pelaksana"].queryset = Agensi.objects.all()
        self.fields["jenis"].queryset = Jenis.objects.all()
        self.fields["fasa"].queryset = Fasa.objects.all()
        self.fields["kategori"].queryset = Kategori.objects.all()
        self.fields["agensi_pemula"].queryset = Agensi.objects.all()



class SungaiForm(forms.ModelForm):
    class Meta:
        model = models.Sungai
        fields = [
            "kategori_sungai",
            "nama_sungai",
            "kod_lembangan",
            "panjang_km",
            "polygon_geom",
        ]


class FokusForm(forms.ModelForm):
    class Meta:
        model = models.Fokus
        fields = [
            "nama_fokus",
        ]


class RumusankawalangunatanahForm(forms.ModelForm):
    class Meta:
        model = models.Rumusankawalangunatanah
        fields = [
            "nama_sublembangan",
            "rumusan_kawalan_gunatanah",
            "luas_hektar",
            "polygon_geom",
            "zon_tindakan",
            "kod_sublembangan",
            "rumusan_kualiti_air",
        ]


class GunatanahsemasaForm(forms.ModelForm):
    class Meta:
        model = models.Gunatanahsemasa
        fields = [
            "kod_gtn",
            "no_lot",
            "mukim_id",
            "upi",
            "gtn2",
            "luas_hektar",
            "pbt_id",
            "gtn1",
            "teks",
            "nama",
            "status",
            "negeri_id",
            "seksyen_id",
            "daerah_id",
            "tahun_data",
            "fcode",
            "polygon_geom",
        ]
