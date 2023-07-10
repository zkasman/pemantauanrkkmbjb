import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Jenis_list_view(client):
    instance1 = test_helpers.create_projekrkk_Jenis()
    instance2 = test_helpers.create_projekrkk_Jenis()
    url = reverse("projekrkk_Jenis_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Jenis_create_view(client):
    url = reverse("projekrkk_Jenis_create")
    data = {
        "nama_jenis": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Jenis_detail_view(client):
    instance = test_helpers.create_projekrkk_Jenis()
    url = reverse("projekrkk_Jenis_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Jenis_update_view(client):
    instance = test_helpers.create_projekrkk_Jenis()
    url = reverse("projekrkk_Jenis_update", args=[instance.pk, ])
    data = {
        "nama_jenis": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Sublembangan_list_view(client):
    instance1 = test_helpers.create_projekrkk_Sublembangan()
    instance2 = test_helpers.create_projekrkk_Sublembangan()
    url = reverse("projekrkk_Sublembangan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Sublembangan_create_view(client):
    url = reverse("projekrkk_Sublembangan_create")
    data = {
        "rumusan_kawalan_gunatanah": "text",
        "luas_hektar": 1.0f,
        "polygon_geom": undefined,
        "rumusan_kualiti_air": "text",
        "nama_sublembangan": "text",
        "kod_sublembangan": "text",
        "zon_tindakan": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Sublembangan_detail_view(client):
    instance = test_helpers.create_projekrkk_Sublembangan()
    url = reverse("projekrkk_Sublembangan_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Sublembangan_update_view(client):
    instance = test_helpers.create_projekrkk_Sublembangan()
    url = reverse("projekrkk_Sublembangan_update", args=[instance.pk, ])
    data = {
        "rumusan_kawalan_gunatanah": "text",
        "luas_hektar": 1.0f,
        "polygon_geom": undefined,
        "rumusan_kualiti_air": "text",
        "nama_sublembangan": "text",
        "kod_sublembangan": "text",
        "zon_tindakan": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Lembangan_list_view(client):
    instance1 = test_helpers.create_projekrkk_Lembangan()
    instance2 = test_helpers.create_projekrkk_Lembangan()
    url = reverse("projekrkk_Lembangan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Lembangan_create_view(client):
    url = reverse("projekrkk_Lembangan_create")
    data = {
        "polygon_geom": undefined,
        "kod_lembangan": "text",
        "luas_hektar": 1.0f,
        "nama_lembangan": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Lembangan_detail_view(client):
    instance = test_helpers.create_projekrkk_Lembangan()
    url = reverse("projekrkk_Lembangan_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Lembangan_update_view(client):
    instance = test_helpers.create_projekrkk_Lembangan()
    url = reverse("projekrkk_Lembangan_update", args=[instance.pk, ])
    data = {
        "polygon_geom": undefined,
        "kod_lembangan": "text",
        "luas_hektar": 1.0f,
        "nama_lembangan": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Kategori_list_view(client):
    instance1 = test_helpers.create_projekrkk_Kategori()
    instance2 = test_helpers.create_projekrkk_Kategori()
    url = reverse("projekrkk_Kategori_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Kategori_create_view(client):
    url = reverse("projekrkk_Kategori_create")
    data = {
        "nama_kategori": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Kategori_detail_view(client):
    instance = test_helpers.create_projekrkk_Kategori()
    url = reverse("projekrkk_Kategori_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Kategori_update_view(client):
    instance = test_helpers.create_projekrkk_Kategori()
    url = reverse("projekrkk_Kategori_update", args=[instance.pk, ])
    data = {
        "nama_kategori": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Sempadanrkk_list_view(client):
    instance1 = test_helpers.create_projekrkk_Sempadanrkk()
    instance2 = test_helpers.create_projekrkk_Sempadanrkk()
    url = reverse("projekrkk_Sempadanrkk_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Sempadanrkk_create_view(client):
    url = reverse("projekrkk_Sempadanrkk_create")
    data = {
        "luas_hektar": 1.0f,
        "nama_rkk": "text",
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Sempadanrkk_detail_view(client):
    instance = test_helpers.create_projekrkk_Sempadanrkk()
    url = reverse("projekrkk_Sempadanrkk_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Sempadanrkk_update_view(client):
    instance = test_helpers.create_projekrkk_Sempadanrkk()
    url = reverse("projekrkk_Sempadanrkk_update", args=[instance.pk, ])
    data = {
        "luas_hektar": 1.0f,
        "nama_rkk": "text",
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Rumusankualitiair_list_view(client):
    instance1 = test_helpers.create_projekrkk_Rumusankualitiair()
    instance2 = test_helpers.create_projekrkk_Rumusankualitiair()
    url = reverse("projekrkk_Rumusankualitiair_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Rumusankualitiair_create_view(client):
    url = reverse("projekrkk_Rumusankualitiair_create")
    data = {
        "nama_sublembangan": "text",
        "zon_tindakan": "text",
        "luas_hektar": 1.0f,
        "rumusan_kawalan_gunatanah": "text",
        "rumusan_kualiti_air": "text",
        "kod_sublembangan": "text",
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Rumusankualitiair_detail_view(client):
    instance = test_helpers.create_projekrkk_Rumusankualitiair()
    url = reverse("projekrkk_Rumusankualitiair_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Rumusankualitiair_update_view(client):
    instance = test_helpers.create_projekrkk_Rumusankualitiair()
    url = reverse("projekrkk_Rumusankualitiair_update", args=[instance.pk, ])
    data = {
        "nama_sublembangan": "text",
        "zon_tindakan": "text",
        "luas_hektar": 1.0f,
        "rumusan_kawalan_gunatanah": "text",
        "rumusan_kualiti_air": "text",
        "kod_sublembangan": "text",
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Agensi_list_view(client):
    instance1 = test_helpers.create_projekrkk_Agensi()
    instance2 = test_helpers.create_projekrkk_Agensi()
    url = reverse("projekrkk_Agensi_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Agensi_create_view(client):
    url = reverse("projekrkk_Agensi_create")
    data = {
        "nama_agensi": "text",
        "no_tel": 1,
        "nama_pegawai": "text",
        "emel": "user@tempurl.com",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Agensi_detail_view(client):
    instance = test_helpers.create_projekrkk_Agensi()
    url = reverse("projekrkk_Agensi_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Agensi_update_view(client):
    instance = test_helpers.create_projekrkk_Agensi()
    url = reverse("projekrkk_Agensi_update", args=[instance.pk, ])
    data = {
        "nama_agensi": "text",
        "no_tel": 1,
        "nama_pegawai": "text",
        "emel": "user@tempurl.com",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Status_list_view(client):
    instance1 = test_helpers.create_projekrkk_Status()
    instance2 = test_helpers.create_projekrkk_Status()
    url = reverse("projekrkk_Status_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Status_create_view(client):
    url = reverse("projekrkk_Status_create")
    data = {
        "nama_status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Status_detail_view(client):
    instance = test_helpers.create_projekrkk_Status()
    url = reverse("projekrkk_Status_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Status_update_view(client):
    instance = test_helpers.create_projekrkk_Status()
    url = reverse("projekrkk_Status_update", args=[instance.pk, ])
    data = {
        "nama_status": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Fasa_list_view(client):
    instance1 = test_helpers.create_projekrkk_Fasa()
    instance2 = test_helpers.create_projekrkk_Fasa()
    url = reverse("projekrkk_Fasa_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Fasa_create_view(client):
    url = reverse("projekrkk_Fasa_create")
    data = {
        "nama_fasa": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Fasa_detail_view(client):
    instance = test_helpers.create_projekrkk_Fasa()
    url = reverse("projekrkk_Fasa_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Fasa_update_view(client):
    instance = test_helpers.create_projekrkk_Fasa()
    url = reverse("projekrkk_Fasa_update", args=[instance.pk, ])
    data = {
        "nama_fasa": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Zontindakan_list_view(client):
    instance1 = test_helpers.create_projekrkk_Zontindakan()
    instance2 = test_helpers.create_projekrkk_Zontindakan()
    url = reverse("projekrkk_Zontindakan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Zontindakan_create_view(client):
    url = reverse("projekrkk_Zontindakan_create")
    data = {
        "nama_sublembangan": "text",
        "luas_hektar": 1.0f,
        "zon_tindakan": "text",
        "rumusan_kualiti_air": "text",
        "polygon_geom": undefined,
        "rumusan_kawalan_gunatanah": "text",
        "kod_sublembangan": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Zontindakan_detail_view(client):
    instance = test_helpers.create_projekrkk_Zontindakan()
    url = reverse("projekrkk_Zontindakan_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Zontindakan_update_view(client):
    instance = test_helpers.create_projekrkk_Zontindakan()
    url = reverse("projekrkk_Zontindakan_update", args=[instance.pk, ])
    data = {
        "nama_sublembangan": "text",
        "luas_hektar": 1.0f,
        "zon_tindakan": "text",
        "rumusan_kualiti_air": "text",
        "polygon_geom": undefined,
        "rumusan_kawalan_gunatanah": "text",
        "kod_sublembangan": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Projek_list_view(client):
    instance1 = test_helpers.create_projekrkk_Projek()
    instance2 = test_helpers.create_projekrkk_Projek()
    url = reverse("projekrkk_Projek_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Projek_create_view(client):
    status = test_helpers.create_projekrkk_Status()
    sublembangan = test_helpers.create_projekrkk_Sublembangan()
    fokus = test_helpers.create_projekrkk_Fokus()
    agensi_pembiaya = test_helpers.create_projekrkk_Agensi()
    agensi_pelaksana = test_helpers.create_projekrkk_Agensi()
    jenis = test_helpers.create_projekrkk_Jenis()
    fasa = test_helpers.create_projekrkk_Fasa()
    kategori = test_helpers.create_projekrkk_Kategori()
    agensi_pemula = test_helpers.create_projekrkk_Agensi()
    url = reverse("projekrkk_Projek_create")
    data = {
        "nama_projek": "text",
        "mukasurat_laporan": "text",
        "aktif": True,
        "imej": "anImage",
        "deskripsi_cadangan": "text",
        "kod_projek": "text",
        "justifikasi_cadangan": "text",
        "kos_pelaksanaan": 1,
        "catatan": "text",
        "sasaran_pencapaian": "text",
        "polygon_geom": undefined,
        "status": status.pk,
        "sublembangan": sublembangan.pk,
        "fokus": fokus.pk,
        "agensi_pembiaya": agensi_pembiaya.pk,
        "agensi_pelaksana": agensi_pelaksana.pk,
        "jenis": jenis.pk,
        "fasa": fasa.pk,
        "kategori": kategori.pk,
        "agensi_pemula": agensi_pemula.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Projek_detail_view(client):
    instance = test_helpers.create_projekrkk_Projek()
    url = reverse("projekrkk_Projek_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Projek_update_view(client):
    status = test_helpers.create_projekrkk_Status()
    sublembangan = test_helpers.create_projekrkk_Sublembangan()
    fokus = test_helpers.create_projekrkk_Fokus()
    agensi_pembiaya = test_helpers.create_projekrkk_Agensi()
    agensi_pelaksana = test_helpers.create_projekrkk_Agensi()
    jenis = test_helpers.create_projekrkk_Jenis()
    fasa = test_helpers.create_projekrkk_Fasa()
    kategori = test_helpers.create_projekrkk_Kategori()
    agensi_pemula = test_helpers.create_projekrkk_Agensi()
    instance = test_helpers.create_projekrkk_Projek()
    url = reverse("projekrkk_Projek_update", args=[instance.pk, ])
    data = {
        "nama_projek": "text",
        "mukasurat_laporan": "text",
        "aktif": True,
        "imej": "anImage",
        "deskripsi_cadangan": "text",
        "kod_projek": "text",
        "justifikasi_cadangan": "text",
        "kos_pelaksanaan": 1,
        "catatan": "text",
        "sasaran_pencapaian": "text",
        "polygon_geom": undefined,
        "status": status.pk,
        "sublembangan": sublembangan.pk,
        "fokus": fokus.pk,
        "agensi_pembiaya": agensi_pembiaya.pk,
        "agensi_pelaksana": agensi_pelaksana.pk,
        "jenis": jenis.pk,
        "fasa": fasa.pk,
        "kategori": kategori.pk,
        "agensi_pemula": agensi_pemula.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Sungai_list_view(client):
    instance1 = test_helpers.create_projekrkk_Sungai()
    instance2 = test_helpers.create_projekrkk_Sungai()
    url = reverse("projekrkk_Sungai_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Sungai_create_view(client):
    url = reverse("projekrkk_Sungai_create")
    data = {
        "kategori_sungai": "text",
        "nama_sungai": "text",
        "kod_lembangan": "text",
        "panjang_km": 1.0f,
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Sungai_detail_view(client):
    instance = test_helpers.create_projekrkk_Sungai()
    url = reverse("projekrkk_Sungai_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Sungai_update_view(client):
    instance = test_helpers.create_projekrkk_Sungai()
    url = reverse("projekrkk_Sungai_update", args=[instance.pk, ])
    data = {
        "kategori_sungai": "text",
        "nama_sungai": "text",
        "kod_lembangan": "text",
        "panjang_km": 1.0f,
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Fokus_list_view(client):
    instance1 = test_helpers.create_projekrkk_Fokus()
    instance2 = test_helpers.create_projekrkk_Fokus()
    url = reverse("projekrkk_Fokus_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Fokus_create_view(client):
    url = reverse("projekrkk_Fokus_create")
    data = {
        "nama_fokus": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Fokus_detail_view(client):
    instance = test_helpers.create_projekrkk_Fokus()
    url = reverse("projekrkk_Fokus_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Fokus_update_view(client):
    instance = test_helpers.create_projekrkk_Fokus()
    url = reverse("projekrkk_Fokus_update", args=[instance.pk, ])
    data = {
        "nama_fokus": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Rumusankawalangunatanah_list_view(client):
    instance1 = test_helpers.create_projekrkk_Rumusankawalangunatanah()
    instance2 = test_helpers.create_projekrkk_Rumusankawalangunatanah()
    url = reverse("projekrkk_Rumusankawalangunatanah_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Rumusankawalangunatanah_create_view(client):
    url = reverse("projekrkk_Rumusankawalangunatanah_create")
    data = {
        "nama_sublembangan": "text",
        "rumusan_kawalan_gunatanah": "text",
        "luas_hektar": 1.0f,
        "polygon_geom": undefined,
        "zon_tindakan": "text",
        "kod_sublembangan": "text",
        "rumusan_kualiti_air": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Rumusankawalangunatanah_detail_view(client):
    instance = test_helpers.create_projekrkk_Rumusankawalangunatanah()
    url = reverse("projekrkk_Rumusankawalangunatanah_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Rumusankawalangunatanah_update_view(client):
    instance = test_helpers.create_projekrkk_Rumusankawalangunatanah()
    url = reverse("projekrkk_Rumusankawalangunatanah_update", args=[instance.pk, ])
    data = {
        "nama_sublembangan": "text",
        "rumusan_kawalan_gunatanah": "text",
        "luas_hektar": 1.0f,
        "polygon_geom": undefined,
        "zon_tindakan": "text",
        "kod_sublembangan": "text",
        "rumusan_kualiti_air": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Gunatanahsemasa_list_view(client):
    instance1 = test_helpers.create_projekrkk_Gunatanahsemasa()
    instance2 = test_helpers.create_projekrkk_Gunatanahsemasa()
    url = reverse("projekrkk_Gunatanahsemasa_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Gunatanahsemasa_create_view(client):
    url = reverse("projekrkk_Gunatanahsemasa_create")
    data = {
        "kod_gtn": "text",
        "no_lot": "text",
        "mukim_id": "text",
        "upi": "text",
        "gtn2": "text",
        "luas_hektar": 1.0f,
        "pbt_id": "text",
        "gtn1": "text",
        "teks": "text",
        "nama": "text",
        "status": "text",
        "negeri_id": "text",
        "seksyen_id": "text",
        "daerah_id": "text",
        "tahun_data": 1,
        "fcode": "text",
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Gunatanahsemasa_detail_view(client):
    instance = test_helpers.create_projekrkk_Gunatanahsemasa()
    url = reverse("projekrkk_Gunatanahsemasa_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Gunatanahsemasa_update_view(client):
    instance = test_helpers.create_projekrkk_Gunatanahsemasa()
    url = reverse("projekrkk_Gunatanahsemasa_update", args=[instance.pk, ])
    data = {
        "kod_gtn": "text",
        "no_lot": "text",
        "mukim_id": "text",
        "upi": "text",
        "gtn2": "text",
        "luas_hektar": 1.0f,
        "pbt_id": "text",
        "gtn1": "text",
        "teks": "text",
        "nama": "text",
        "status": "text",
        "negeri_id": "text",
        "seksyen_id": "text",
        "daerah_id": "text",
        "tahun_data": 1,
        "fcode": "text",
        "polygon_geom": undefined,
    }
    response = client.post(url, data)
    assert response.status_code == 302
