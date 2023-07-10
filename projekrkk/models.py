from django.db import models
from django.urls import reverse
from django.contrib.gis.db import models as gis_models


class Jenis(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nama_jenis = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Jenis"
        verbose_name_plural = "Jenis"

    def __str__(self):
        return str(self.nama_jenis)

    def get_absolute_url(self):
        return reverse("projekrkk_Jenis_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Jenis_update", args=(self.pk,))



class Sublembangan(models.Model):

    # Fields
    rumusan_kawalan_gunatanah = models.CharField(max_length=100, blank=True, null=True)
    luas_hektar = models.FloatField(blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()
    rumusan_kualiti_air = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    nama_sublembangan = models.CharField(max_length=100, blank=True, null=True)
    kod_sublembangan = models.CharField(max_length=30, blank=True, null=True)
    zon_tindakan = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Sub-Lembangan"
        verbose_name_plural = "Sub-Lembangan"

    def __str__(self):
        return str(self.kod_sublembangan)

    def get_absolute_url(self):
        return reverse("projekrkk_Sublembangan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Sublembangan_update", args=(self.pk,))



class Lembangan(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    kod_lembangan = models.CharField(max_length=100, blank=True, null=True)
    luas_hektar = models.FloatField(blank=True, null=True)
    nama_lembangan = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Lembangan"
        verbose_name_plural = "Lembangan"

    def __str__(self):
        return str(self.kod_lembangan)

    def get_absolute_url(self):
        return reverse("projekrkk_Lembangan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Lembangan_update", args=(self.pk,))



class Kategori(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nama_kategori = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"

    def __str__(self):
        return str(self.nama_kategori)

    def get_absolute_url(self):
        return reverse("projekrkk_Kategori_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Kategori_update", args=(self.pk,))



class Sempadanrkk(models.Model):

    # Fields
    luas_hektar = models.FloatField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    nama_rkk = models.CharField(max_length=200, blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()

    class Meta:
        verbose_name = "Sempadan Kajian"
        verbose_name_plural = "Sempadan Kajian"

    def __str__(self):
        return str(self.nama_rkk)

    def get_absolute_url(self):
        return reverse("projekrkk_Sempadanrkk_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Sempadanrkk_update", args=(self.pk,))



class Rumusankualitiair(models.Model):

    # Fields
    nama_sublembangan = models.CharField(max_length=100, blank=True, null=True)
    zon_tindakan = models.CharField(max_length=100, blank=True, null=True)
    luas_hektar = models.FloatField(blank=True, null=True)
    rumusan_kawalan_gunatanah = models.CharField(max_length=100, blank=True, null=True)
    rumusan_kualiti_air = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    kod_sublembangan = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()

    class Meta:
        verbose_name = "Rumusan Kualiti Air"
        verbose_name_plural = "Rumusan Kualiti Air"

    def __str__(self):
        return str(self.kod_sublembangan)

    def get_absolute_url(self):
        return reverse("projekrkk_Rumusankualitiair_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Rumusankualitiair_update", args=(self.pk,))



class Agensi(models.Model):

    # Fields
    nama_agensi = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    no_tel = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nama_pegawai = models.CharField(max_length=200, blank=True, null=True)
    emel = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = "Agensi"
        verbose_name_plural = "Agensi"

    def __str__(self):
        return str(self.nama_agensi)

    def get_absolute_url(self):
        return reverse("projekrkk_Agensi_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Agensi_update", args=(self.pk,))



class Status(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nama_status = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return str(self.nama_status)

    def get_absolute_url(self):
        return reverse("projekrkk_Status_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Status_update", args=(self.pk,))



class Fasa(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nama_fasa = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Fasa"
        verbose_name_plural = "Fasa"

    def __str__(self):
        return str(self.nama_fasa)

    def get_absolute_url(self):
        return reverse("projekrkk_Fasa_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Fasa_update", args=(self.pk,))



class Zontindakan(models.Model):

    # Fields
    nama_sublembangan = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    luas_hektar = models.FloatField(blank=True, null=True)
    zon_tindakan = models.CharField(max_length=100, blank=True, null=True)
    rumusan_kualiti_air = models.CharField(max_length=100, blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()
    rumusan_kawalan_gunatanah = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    kod_sublembangan = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name = "Zon Tindakan"
        verbose_name_plural = "Zon Tindakan"

    def __str__(self):
        return str(self.kod_sublembangan)

    def get_absolute_url(self):
        return reverse("projekrkk_Zontindakan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Zontindakan_update", args=(self.pk,))



class Projek(models.Model):

    # Relationships
    aktif = models.BooleanField(default=True)
    kod_projek = models.CharField(max_length=50, blank=True, null=True)
    nama_projek = models.CharField(max_length=200)
    sublembangan = models.ManyToManyField("projekrkk.Sublembangan", blank=True, related_name='+')
    fokus = models.ForeignKey("projekrkk.Fokus", on_delete=models.DO_NOTHING, blank=True, null=True)
    kategori = models.ForeignKey("projekrkk.Kategori", on_delete=models.DO_NOTHING, blank=True, null=True)
    jenis = models.ForeignKey("projekrkk.Jenis", on_delete=models.DO_NOTHING, blank=True, null=True)
    fasa = models.ManyToManyField("projekrkk.Fasa", blank=True, related_name='+')
    status = models.ForeignKey("projekrkk.Status", on_delete=models.DO_NOTHING, blank=True, null=True)
    agensi_pemula = models.ManyToManyField("projekrkk.Agensi", blank=True, related_name='+')
    agensi_pembiaya = models.ManyToManyField("projekrkk.Agensi", blank=True, related_name='+')
    agensi_pelaksana = models.ManyToManyField("projekrkk.Agensi", blank=True, related_name='+')
    kos_pelaksanaan = models.IntegerField(blank=True, null=True)
    sasaran_pencapaian = models.TextField(max_length=1000, blank=True, null=True)
    deskripsi_cadangan = models.TextField(max_length=1000, blank=True, null=True)
    justifikasi_cadangan = models.TextField(max_length=1000, blank=True, null=True)
    catatan = models.TextField(max_length=1000, blank=True, null=True)
    mukasurat_laporan = models.CharField(max_length=100, blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()
    imej = models.ImageField(upload_to="upload/images/", blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)

    class Meta:
        verbose_name = "Projek"
        verbose_name_plural = "Projek"

    def __str__(self):
        return str(self.kod_projek)

    def get_absolute_url(self):
        return reverse("projekrkk_Projek_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Projek_update", args=(self.pk,))



class Sungai(models.Model):

    # Fields
    kategori_sungai = models.CharField(max_length=100, blank=True, null=True)
    nama_sungai = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    kod_lembangan = models.CharField(max_length=100, blank=True, null=True)
    panjang_km = models.FloatField(blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)

    class Meta:
        verbose_name = "Sungai/ Parit Utama"
        verbose_name_plural = "Sungai/ Parit Utama"

    def __str__(self):
        return str(self.kod_lembangan)

    def get_absolute_url(self):
        return reverse("projekrkk_Sungai_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Sungai_update", args=(self.pk,))



class Fokus(models.Model):

    # Fields
    nama_fokus = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Fokus"
        verbose_name_plural = "Fokus"

    def __str__(self):
        return str(self.nama_fokus)

    def get_absolute_url(self):
        return reverse("projekrkk_Fokus_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Fokus_update", args=(self.pk,))



class Rumusankawalangunatanah(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    nama_sublembangan = models.CharField(max_length=100, blank=True, null=True)
    rumusan_kawalan_gunatanah = models.CharField(max_length=100, blank=True, null=True)
    luas_hektar = models.FloatField(blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()
    zon_tindakan = models.CharField(max_length=100, blank=True, null=True)
    kod_sublembangan = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    rumusan_kualiti_air = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Rumusan Kawalan Gunatanah"
        verbose_name_plural = "Rumusan Kawalan Gunatanah"

    def __str__(self):
        return str(self.kod_sublembangan)

    def get_absolute_url(self):
        return reverse("projekrkk_Rumusankawalangunatanah_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Rumusankawalangunatanah_update", args=(self.pk,))



class Gunatanahsemasa(models.Model):

    # Fields
    upi = models.CharField(max_length=16, blank=True, null=True)
    kod_gtn = models.CharField(max_length=7, blank=True, null=True)
    no_lot = models.CharField(max_length=11, blank=True, null=True)
    mukim_id = models.CharField(max_length=6, blank=True, null=True)
    gtn2 = models.CharField(max_length=50, blank=True, null=True)
    luas_hektar = models.FloatField(blank=True, null=True)
    pbt_id = models.CharField(max_length=6, blank=True, null=True)
    gtn1 = models.CharField(max_length=50, blank=True, null=True)
    teks = models.CharField(max_length=50, blank=True, null=True)
    nama = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    negeri_id = models.CharField(max_length=2, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True)
    seksyen_id = models.CharField(max_length=9, blank=True, null=True)
    daerah_id = models.CharField(max_length=4, blank=True, null=True)
    tahun_data = models.IntegerField(blank=True, null=True)
    fcode = models.CharField(max_length=6, blank=True, null=True)
    polygon_geom = gis_models.MultiPolygonField()

    class Meta:
        verbose_name = "Gunatanah Semasa"
        verbose_name_plural = "Gunatanah Semasa"

    def __str__(self):
        return str(self.upi)

    def get_absolute_url(self):
        return reverse("projekrkk_Gunatanahsemasa_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("projekrkk_Gunatanahsemasa_update", args=(self.pk,))

