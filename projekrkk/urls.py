from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Jenis", api.JenisViewSet)
router.register("Sublembangan", api.SublembanganViewSet)
router.register("Lembangan", api.LembanganViewSet)
router.register("Kategori", api.KategoriViewSet)
router.register("Sempadanrkk", api.SempadanrkkViewSet)
router.register("Rumusankualitiair", api.RumusankualitiairViewSet)
router.register("Agensi", api.AgensiViewSet)
router.register("Status", api.StatusViewSet)
router.register("Fasa", api.FasaViewSet)
router.register("Zontindakan", api.ZontindakanViewSet)
router.register("Projek", api.ProjekViewSet)
router.register("Sungai", api.SungaiViewSet)
router.register("Fokus", api.FokusViewSet)
router.register("Rumusankawalangunatanah", api.RumusankawalangunatanahViewSet)
router.register("Gunatanahsemasa", api.GunatanahsemasaViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("projekrkk/Jenis/", views.JenisListView.as_view(), name="projekrkk_Jenis_list"),
    path("projekrkk/Jenis/create/", views.JenisCreateView.as_view(), name="projekrkk_Jenis_create"),
    path("projekrkk/Jenis/detail/<int:pk>/", views.JenisDetailView.as_view(), name="projekrkk_Jenis_detail"),
    path("projekrkk/Jenis/update/<int:pk>/", views.JenisUpdateView.as_view(), name="projekrkk_Jenis_update"),
    path("projekrkk/Jenis/delete/<int:pk>/", views.JenisDeleteView.as_view(), name="projekrkk_Jenis_delete"),
    path("projekrkk/Sublembangan/", views.SublembanganListView.as_view(), name="projekrkk_Sublembangan_list"),
    path("projekrkk/Sublembangan/create/", views.SublembanganCreateView.as_view(), name="projekrkk_Sublembangan_create"),
    path("projekrkk/Sublembangan/detail/<int:pk>/", views.SublembanganDetailView.as_view(), name="projekrkk_Sublembangan_detail"),
    path("projekrkk/Sublembangan/update/<int:pk>/", views.SublembanganUpdateView.as_view(), name="projekrkk_Sublembangan_update"),
    path("projekrkk/Sublembangan/delete/<int:pk>/", views.SublembanganDeleteView.as_view(), name="projekrkk_Sublembangan_delete"),
    path("projekrkk/Lembangan/", views.LembanganListView.as_view(), name="projekrkk_Lembangan_list"),
    path("projekrkk/Lembangan/create/", views.LembanganCreateView.as_view(), name="projekrkk_Lembangan_create"),
    path("projekrkk/Lembangan/detail/<int:pk>/", views.LembanganDetailView.as_view(), name="projekrkk_Lembangan_detail"),
    path("projekrkk/Lembangan/update/<int:pk>/", views.LembanganUpdateView.as_view(), name="projekrkk_Lembangan_update"),
    path("projekrkk/Lembangan/delete/<int:pk>/", views.LembanganDeleteView.as_view(), name="projekrkk_Lembangan_delete"),
    path("projekrkk/Kategori/", views.KategoriListView.as_view(), name="projekrkk_Kategori_list"),
    path("projekrkk/Kategori/create/", views.KategoriCreateView.as_view(), name="projekrkk_Kategori_create"),
    path("projekrkk/Kategori/detail/<int:pk>/", views.KategoriDetailView.as_view(), name="projekrkk_Kategori_detail"),
    path("projekrkk/Kategori/update/<int:pk>/", views.KategoriUpdateView.as_view(), name="projekrkk_Kategori_update"),
    path("projekrkk/Kategori/delete/<int:pk>/", views.KategoriDeleteView.as_view(), name="projekrkk_Kategori_delete"),
    path("projekrkk/Sempadanrkk/", views.SempadanrkkListView.as_view(), name="projekrkk_Sempadanrkk_list"),
    path("projekrkk/Sempadanrkk/create/", views.SempadanrkkCreateView.as_view(), name="projekrkk_Sempadanrkk_create"),
    path("projekrkk/Sempadanrkk/detail/<int:pk>/", views.SempadanrkkDetailView.as_view(), name="projekrkk_Sempadanrkk_detail"),
    path("projekrkk/Sempadanrkk/update/<int:pk>/", views.SempadanrkkUpdateView.as_view(), name="projekrkk_Sempadanrkk_update"),
    path("projekrkk/Sempadanrkk/delete/<int:pk>/", views.SempadanrkkDeleteView.as_view(), name="projekrkk_Sempadanrkk_delete"),
    path("projekrkk/Rumusankualitiair/", views.RumusankualitiairListView.as_view(), name="projekrkk_Rumusankualitiair_list"),
    path("projekrkk/Rumusankualitiair/create/", views.RumusankualitiairCreateView.as_view(), name="projekrkk_Rumusankualitiair_create"),
    path("projekrkk/Rumusankualitiair/detail/<int:pk>/", views.RumusankualitiairDetailView.as_view(), name="projekrkk_Rumusankualitiair_detail"),
    path("projekrkk/Rumusankualitiair/update/<int:pk>/", views.RumusankualitiairUpdateView.as_view(), name="projekrkk_Rumusankualitiair_update"),
    path("projekrkk/Rumusankualitiair/delete/<int:pk>/", views.RumusankualitiairDeleteView.as_view(), name="projekrkk_Rumusankualitiair_delete"),
    path("projekrkk/Agensi/", views.AgensiListView.as_view(), name="projekrkk_Agensi_list"),
    path("projekrkk/Agensi/create/", views.AgensiCreateView.as_view(), name="projekrkk_Agensi_create"),
    path("projekrkk/Agensi/detail/<int:pk>/", views.AgensiDetailView.as_view(), name="projekrkk_Agensi_detail"),
    path("projekrkk/Agensi/update/<int:pk>/", views.AgensiUpdateView.as_view(), name="projekrkk_Agensi_update"),
    path("projekrkk/Agensi/delete/<int:pk>/", views.AgensiDeleteView.as_view(), name="projekrkk_Agensi_delete"),
    path("projekrkk/Status/", views.StatusListView.as_view(), name="projekrkk_Status_list"),
    path("projekrkk/Status/create/", views.StatusCreateView.as_view(), name="projekrkk_Status_create"),
    path("projekrkk/Status/detail/<int:pk>/", views.StatusDetailView.as_view(), name="projekrkk_Status_detail"),
    path("projekrkk/Status/update/<int:pk>/", views.StatusUpdateView.as_view(), name="projekrkk_Status_update"),
    path("projekrkk/Status/delete/<int:pk>/", views.StatusDeleteView.as_view(), name="projekrkk_Status_delete"),
    path("projekrkk/Fasa/", views.FasaListView.as_view(), name="projekrkk_Fasa_list"),
    path("projekrkk/Fasa/create/", views.FasaCreateView.as_view(), name="projekrkk_Fasa_create"),
    path("projekrkk/Fasa/detail/<int:pk>/", views.FasaDetailView.as_view(), name="projekrkk_Fasa_detail"),
    path("projekrkk/Fasa/update/<int:pk>/", views.FasaUpdateView.as_view(), name="projekrkk_Fasa_update"),
    path("projekrkk/Fasa/delete/<int:pk>/", views.FasaDeleteView.as_view(), name="projekrkk_Fasa_delete"),
    path("projekrkk/Zontindakan/", views.ZontindakanListView.as_view(), name="projekrkk_Zontindakan_list"),
    path("projekrkk/Zontindakan/create/", views.ZontindakanCreateView.as_view(), name="projekrkk_Zontindakan_create"),
    path("projekrkk/Zontindakan/detail/<int:pk>/", views.ZontindakanDetailView.as_view(), name="projekrkk_Zontindakan_detail"),
    path("projekrkk/Zontindakan/update/<int:pk>/", views.ZontindakanUpdateView.as_view(), name="projekrkk_Zontindakan_update"),
    path("projekrkk/Zontindakan/delete/<int:pk>/", views.ZontindakanDeleteView.as_view(), name="projekrkk_Zontindakan_delete"),
    path("projekrkk/Projek/", views.ProjekListView.as_view(), name="projekrkk_Projek_list"),
    path("projekrkk/Projek/create/", views.ProjekCreateView.as_view(), name="projekrkk_Projek_create"),
    path("projekrkk/Projek/detail/<int:pk>/", views.ProjekDetailView.as_view(), name="projekrkk_Projek_detail"),
    path("projekrkk/Projek/update/<int:pk>/", views.ProjekUpdateView.as_view(), name="projekrkk_Projek_update"),
    path("projekrkk/Projek/delete/<int:pk>/", views.ProjekDeleteView.as_view(), name="projekrkk_Projek_delete"),
    path("projekrkk/Sungai/", views.SungaiListView.as_view(), name="projekrkk_Sungai_list"),
    path("projekrkk/Sungai/create/", views.SungaiCreateView.as_view(), name="projekrkk_Sungai_create"),
    path("projekrkk/Sungai/detail/<int:pk>/", views.SungaiDetailView.as_view(), name="projekrkk_Sungai_detail"),
    path("projekrkk/Sungai/update/<int:pk>/", views.SungaiUpdateView.as_view(), name="projekrkk_Sungai_update"),
    path("projekrkk/Sungai/delete/<int:pk>/", views.SungaiDeleteView.as_view(), name="projekrkk_Sungai_delete"),
    path("projekrkk/Fokus/", views.FokusListView.as_view(), name="projekrkk_Fokus_list"),
    path("projekrkk/Fokus/create/", views.FokusCreateView.as_view(), name="projekrkk_Fokus_create"),
    path("projekrkk/Fokus/detail/<int:pk>/", views.FokusDetailView.as_view(), name="projekrkk_Fokus_detail"),
    path("projekrkk/Fokus/update/<int:pk>/", views.FokusUpdateView.as_view(), name="projekrkk_Fokus_update"),
    path("projekrkk/Fokus/delete/<int:pk>/", views.FokusDeleteView.as_view(), name="projekrkk_Fokus_delete"),
    path("projekrkk/Rumusankawalangunatanah/", views.RumusankawalangunatanahListView.as_view(), name="projekrkk_Rumusankawalangunatanah_list"),
    path("projekrkk/Rumusankawalangunatanah/create/", views.RumusankawalangunatanahCreateView.as_view(), name="projekrkk_Rumusankawalangunatanah_create"),
    path("projekrkk/Rumusankawalangunatanah/detail/<int:pk>/", views.RumusankawalangunatanahDetailView.as_view(), name="projekrkk_Rumusankawalangunatanah_detail"),
    path("projekrkk/Rumusankawalangunatanah/update/<int:pk>/", views.RumusankawalangunatanahUpdateView.as_view(), name="projekrkk_Rumusankawalangunatanah_update"),
    path("projekrkk/Rumusankawalangunatanah/delete/<int:pk>/", views.RumusankawalangunatanahDeleteView.as_view(), name="projekrkk_Rumusankawalangunatanah_delete"),
    path("projekrkk/Gunatanahsemasa/", views.GunatanahsemasaListView.as_view(), name="projekrkk_Gunatanahsemasa_list"),
    path("projekrkk/Gunatanahsemasa/create/", views.GunatanahsemasaCreateView.as_view(), name="projekrkk_Gunatanahsemasa_create"),
    path("projekrkk/Gunatanahsemasa/detail/<int:pk>/", views.GunatanahsemasaDetailView.as_view(), name="projekrkk_Gunatanahsemasa_detail"),
    path("projekrkk/Gunatanahsemasa/update/<int:pk>/", views.GunatanahsemasaUpdateView.as_view(), name="projekrkk_Gunatanahsemasa_update"),
    path("projekrkk/Gunatanahsemasa/delete/<int:pk>/", views.GunatanahsemasaDeleteView.as_view(), name="projekrkk_Gunatanahsemasa_delete"),

)
