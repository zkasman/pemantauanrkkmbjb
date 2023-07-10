from rest_framework import serializers

from . import models


class JenisSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Jenis
        fields = [
            "last_updated",
            "created",
            "nama_jenis",
        ]

class SublembanganSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sublembangan
        fields = [
            "rumusan_kawalan_gunatanah",
            "luas_hektar",
            "polygon_geom",
            "rumusan_kualiti_air",
            "last_updated",
            "created",
            "nama_sublembangan",
            "kod_sublembangan",
            "zon_tindakan",
        ]

class LembanganSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lembangan
        fields = [
            "created",
            "polygon_geom",
            "last_updated",
            "kod_lembangan",
            "luas_hektar",
            "nama_lembangan",
        ]

class KategoriSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Kategori
        fields = [
            "last_updated",
            "nama_kategori",
            "created",
        ]

class SempadanrkkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sempadanrkk
        fields = [
            "luas_hektar",
            "last_updated",
            "created",
            "nama_rkk",
            "polygon_geom",
        ]

class RumusankualitiairSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rumusankualitiair
        fields = [
            "nama_sublembangan",
            "zon_tindakan",
            "luas_hektar",
            "rumusan_kawalan_gunatanah",
            "rumusan_kualiti_air",
            "created",
            "kod_sublembangan",
            "last_updated",
            "polygon_geom",
        ]

class AgensiSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Agensi
        fields = [
            "nama_agensi",
            "last_updated",
            "no_tel",
            "created",
            "nama_pegawai",
            "emel",
        ]

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status
        fields = [
            "last_updated",
            "created",
            "nama_status",
        ]

class FasaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fasa
        fields = [
            "last_updated",
            "created",
            "nama_fasa",
        ]

class ZontindakanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Zontindakan
        fields = [
            "nama_sublembangan",
            "last_updated",
            "luas_hektar",
            "zon_tindakan",
            "rumusan_kualiti_air",
            "polygon_geom",
            "rumusan_kawalan_gunatanah",
            "created",
            "kod_sublembangan",
        ]

class ProjekSerializer(serializers.ModelSerializer):

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
            "created",
            "polygon_geom",
            "last_updated",
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

class SungaiSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sungai
        fields = [
            "kategori_sungai",
            "nama_sungai",
            "created",
            "kod_lembangan",
            "panjang_km",
            "polygon_geom",
            "last_updated",
        ]

class FokusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fokus
        fields = [
            "nama_fokus",
            "last_updated",
            "created",
        ]

class RumusankawalangunatanahSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rumusankawalangunatanah
        fields = [
            "last_updated",
            "nama_sublembangan",
            "rumusan_kawalan_gunatanah",
            "luas_hektar",
            "polygon_geom",
            "zon_tindakan",
            "kod_sublembangan",
            "created",
            "rumusan_kualiti_air",
        ]

class GunatanahsemasaSerializer(serializers.ModelSerializer):

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
            "created",
            "last_updated",
            "seksyen_id",
            "daerah_id",
            "tahun_data",
            "fcode",
            "polygon_geom",
        ]
