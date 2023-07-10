from django.contrib.gis import admin
from django import forms

from . import models

class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 13,
            'default_lon': 103.7768501688807,
            'default_lat': 1.508835864952107, 
        }
    }


class JenisAdminForm(forms.ModelForm):

    class Meta:
        model = models.Jenis
        fields = "__all__"


class JenisAdmin(admin.ModelAdmin):
    form = JenisAdminForm
    list_display = [
        "nama_jenis",
        "last_updated",
        "created",
    ]


class SublembanganAdminForm(forms.ModelForm):

    class Meta:
        model = models.Sublembangan
        fields = "__all__"


class SublembanganAdmin(CustomGeoAdmin):
    form = SublembanganAdminForm
    list_display = [
        "kod_sublembangan",
        "nama_sublembangan",
        "luas_hektar",
        "rumusan_kawalan_gunatanah",
        "rumusan_kualiti_air",
        "zon_tindakan",
        "last_updated",
        "created",
        # "polygon_geom", 
    ]


class LembanganAdminForm(forms.ModelForm):

    class Meta:
        model = models.Lembangan
        fields = "__all__"


class LembanganAdmin(CustomGeoAdmin):
    form = LembanganAdminForm
    list_display = [
        "kod_lembangan",
        "nama_lembangan",
        "luas_hektar",
        "last_updated",
        "created",
        # "polygon_geom",
    ]


class KategoriAdminForm(forms.ModelForm):

    class Meta:
        model = models.Kategori
        fields = "__all__"


class KategoriAdmin(admin.ModelAdmin):
    form = KategoriAdminForm
    list_display = [
        "nama_kategori",
        "last_updated",
        "created",
    ]


class SempadanrkkAdminForm(forms.ModelForm):

    class Meta:
        model = models.Sempadanrkk
        fields = "__all__"


class SempadanrkkAdmin(CustomGeoAdmin):
    form = SempadanrkkAdminForm
    list_display = [
        "nama_rkk",
        "luas_hektar",
        "last_updated",
        "created",
        # "polygon_geom",
    ]


class RumusankualitiairAdminForm(forms.ModelForm):

    class Meta:
        model = models.Rumusankualitiair
        fields = "__all__"


class RumusankualitiairAdmin(CustomGeoAdmin):
    form = RumusankualitiairAdminForm
    list_display = [
        "kod_sublembangan",
        "nama_sublembangan",
        "luas_hektar",
        "rumusan_kawalan_gunatanah",
        "rumusan_kualiti_air",
        "zon_tindakan",
        "last_updated",
        "created",
        # "polygon_geom", 
    ]


class AgensiAdminForm(forms.ModelForm):

    class Meta:
        model = models.Agensi
        fields = "__all__"


class AgensiAdmin(admin.ModelAdmin):
    form = AgensiAdminForm
    list_display = [
        "nama_agensi",
        "nama_pegawai",
        "no_tel",
        "emel",
        "last_updated",
        "created",
    ]


class StatusAdminForm(forms.ModelForm):

    class Meta:
        model = models.Status
        fields = "__all__"


class StatusAdmin(admin.ModelAdmin):
    form = StatusAdminForm
    list_display = [
        "nama_status",
        "last_updated",
        "created",
    ]


class FasaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Fasa
        fields = "__all__"


class FasaAdmin(admin.ModelAdmin):
    form = FasaAdminForm
    list_display = [
        "nama_fasa",
        "last_updated",
        "created",
    ]


class ZontindakanAdminForm(forms.ModelForm):

    class Meta:
        model = models.Zontindakan
        fields = "__all__"


class ZontindakanAdmin(CustomGeoAdmin):
    form = ZontindakanAdminForm
    list_display = [
        "kod_sublembangan",
        "nama_sublembangan",
        "luas_hektar",
        "rumusan_kawalan_gunatanah",
        "rumusan_kualiti_air",
        "zon_tindakan",
        "last_updated",
        "created",
        # "polygon_geom", 
    ]


class ProjekAdminForm(forms.ModelForm):

    class Meta:
        model = models.Projek
        fields = "__all__"


class ProjekAdmin(CustomGeoAdmin):
    form = ProjekAdminForm
    list_display = [
        "kod_projek",
        "nama_projek",
        "last_updated",
        "created",
        # "kos_pelaksanaan",
        # "sasaran_pencapaian",
        # "deskripsi_cadangan",
        # "justifikasi_cadangan",
        # "catatan",
        # "mukasurat_laporan",
        # "aktif",
        # "imej",
        # "polygon_geom",
    ]


class SungaiAdminForm(forms.ModelForm):

    class Meta:
        model = models.Sungai
        fields = "__all__"


class SungaiAdmin(CustomGeoAdmin):
    form = SungaiAdminForm
    list_display = [
        "kod_lembangan",
        "kategori_sungai",
        "nama_sungai",
        "panjang_km",
        "last_updated",
        "created",
        # "polygon_geom",   
    ]


class FokusAdminForm(forms.ModelForm):

    class Meta:
        model = models.Fokus
        fields = "__all__"


class FokusAdmin(admin.ModelAdmin):
    form = FokusAdminForm
    list_display = [
        "nama_fokus",
        "last_updated",
        "created",
    ]


class RumusankawalangunatanahAdminForm(forms.ModelForm):

    class Meta:
        model = models.Rumusankawalangunatanah
        fields = "__all__"


class RumusankawalangunatanahAdmin(CustomGeoAdmin):
    form = RumusankawalangunatanahAdminForm
    list_display = [
        "kod_sublembangan",
        "nama_sublembangan",
        "luas_hektar",
        "rumusan_kawalan_gunatanah",
        "rumusan_kualiti_air",
        "zon_tindakan",
        "last_updated",
        "created",
        # "polygon_geom", 
    ]


class GunatanahsemasaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Gunatanahsemasa
        fields = "__all__"


class GunatanahsemasaAdmin(CustomGeoAdmin):
    form = GunatanahsemasaAdminForm
    list_display = [
        "upi",
        "kod_gtn",
        "no_lot",
        "mukim_id",
        "gtn2",
        "luas_hektar",
        "pbt_id",
        "gtn1",
        "teks",
        "nama",
        "status",
        "negeri_id",
        "created",
        "last_updated",
        "seksyen_id",
        "daerah_id",
        "tahun_data",
        "fcode",
        # "polygon_geom",
    ]


admin.site.register(models.Jenis, JenisAdmin)
admin.site.register(models.Sublembangan, SublembanganAdmin)
admin.site.register(models.Lembangan, LembanganAdmin)
admin.site.register(models.Kategori, KategoriAdmin)
admin.site.register(models.Sempadanrkk, SempadanrkkAdmin)
admin.site.register(models.Rumusankualitiair, RumusankualitiairAdmin)
admin.site.register(models.Agensi, AgensiAdmin)
admin.site.register(models.Status, StatusAdmin)
admin.site.register(models.Fasa, FasaAdmin)
admin.site.register(models.Zontindakan, ZontindakanAdmin)
admin.site.register(models.Projek, ProjekAdmin)
admin.site.register(models.Sungai, SungaiAdmin)
admin.site.register(models.Fokus, FokusAdmin)
admin.site.register(models.Rumusankawalangunatanah, RumusankawalangunatanahAdmin)
admin.site.register(models.Gunatanahsemasa, GunatanahsemasaAdmin)
