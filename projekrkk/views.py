from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class JenisListView(generic.ListView):
    model = models.Jenis
    form_class = forms.JenisForm


class JenisCreateView(generic.CreateView):
    model = models.Jenis
    form_class = forms.JenisForm


class JenisDetailView(generic.DetailView):
    model = models.Jenis
    form_class = forms.JenisForm


class JenisUpdateView(generic.UpdateView):
    model = models.Jenis
    form_class = forms.JenisForm
    pk_url_kwarg = "pk"


class JenisDeleteView(generic.DeleteView):
    model = models.Jenis
    success_url = reverse_lazy("projekrkk_Jenis_list")


class SublembanganListView(generic.ListView):
    model = models.Sublembangan
    form_class = forms.SublembanganForm


class SublembanganCreateView(generic.CreateView):
    model = models.Sublembangan
    form_class = forms.SublembanganForm


class SublembanganDetailView(generic.DetailView):
    model = models.Sublembangan
    form_class = forms.SublembanganForm


class SublembanganUpdateView(generic.UpdateView):
    model = models.Sublembangan
    form_class = forms.SublembanganForm
    pk_url_kwarg = "pk"


class SublembanganDeleteView(generic.DeleteView):
    model = models.Sublembangan
    success_url = reverse_lazy("projekrkk_Sublembangan_list")


class LembanganListView(generic.ListView):
    model = models.Lembangan
    form_class = forms.LembanganForm


class LembanganCreateView(generic.CreateView):
    model = models.Lembangan
    form_class = forms.LembanganForm


class LembanganDetailView(generic.DetailView):
    model = models.Lembangan
    form_class = forms.LembanganForm


class LembanganUpdateView(generic.UpdateView):
    model = models.Lembangan
    form_class = forms.LembanganForm
    pk_url_kwarg = "pk"


class LembanganDeleteView(generic.DeleteView):
    model = models.Lembangan
    success_url = reverse_lazy("projekrkk_Lembangan_list")


class KategoriListView(generic.ListView):
    model = models.Kategori
    form_class = forms.KategoriForm


class KategoriCreateView(generic.CreateView):
    model = models.Kategori
    form_class = forms.KategoriForm


class KategoriDetailView(generic.DetailView):
    model = models.Kategori
    form_class = forms.KategoriForm


class KategoriUpdateView(generic.UpdateView):
    model = models.Kategori
    form_class = forms.KategoriForm
    pk_url_kwarg = "pk"


class KategoriDeleteView(generic.DeleteView):
    model = models.Kategori
    success_url = reverse_lazy("projekrkk_Kategori_list")


class SempadanrkkListView(generic.ListView):
    model = models.Sempadanrkk
    form_class = forms.SempadanrkkForm


class SempadanrkkCreateView(generic.CreateView):
    model = models.Sempadanrkk
    form_class = forms.SempadanrkkForm


class SempadanrkkDetailView(generic.DetailView):
    model = models.Sempadanrkk
    form_class = forms.SempadanrkkForm


class SempadanrkkUpdateView(generic.UpdateView):
    model = models.Sempadanrkk
    form_class = forms.SempadanrkkForm
    pk_url_kwarg = "pk"


class SempadanrkkDeleteView(generic.DeleteView):
    model = models.Sempadanrkk
    success_url = reverse_lazy("projekrkk_Sempadanrkk_list")


class RumusankualitiairListView(generic.ListView):
    model = models.Rumusankualitiair
    form_class = forms.RumusankualitiairForm


class RumusankualitiairCreateView(generic.CreateView):
    model = models.Rumusankualitiair
    form_class = forms.RumusankualitiairForm


class RumusankualitiairDetailView(generic.DetailView):
    model = models.Rumusankualitiair
    form_class = forms.RumusankualitiairForm


class RumusankualitiairUpdateView(generic.UpdateView):
    model = models.Rumusankualitiair
    form_class = forms.RumusankualitiairForm
    pk_url_kwarg = "pk"


class RumusankualitiairDeleteView(generic.DeleteView):
    model = models.Rumusankualitiair
    success_url = reverse_lazy("projekrkk_Rumusankualitiair_list")


class AgensiListView(generic.ListView):
    model = models.Agensi
    form_class = forms.AgensiForm


class AgensiCreateView(generic.CreateView):
    model = models.Agensi
    form_class = forms.AgensiForm


class AgensiDetailView(generic.DetailView):
    model = models.Agensi
    form_class = forms.AgensiForm


class AgensiUpdateView(generic.UpdateView):
    model = models.Agensi
    form_class = forms.AgensiForm
    pk_url_kwarg = "pk"


class AgensiDeleteView(generic.DeleteView):
    model = models.Agensi
    success_url = reverse_lazy("projekrkk_Agensi_list")


class StatusListView(generic.ListView):
    model = models.Status
    form_class = forms.StatusForm


class StatusCreateView(generic.CreateView):
    model = models.Status
    form_class = forms.StatusForm


class StatusDetailView(generic.DetailView):
    model = models.Status
    form_class = forms.StatusForm


class StatusUpdateView(generic.UpdateView):
    model = models.Status
    form_class = forms.StatusForm
    pk_url_kwarg = "pk"


class StatusDeleteView(generic.DeleteView):
    model = models.Status
    success_url = reverse_lazy("projekrkk_Status_list")


class FasaListView(generic.ListView):
    model = models.Fasa
    form_class = forms.FasaForm


class FasaCreateView(generic.CreateView):
    model = models.Fasa
    form_class = forms.FasaForm


class FasaDetailView(generic.DetailView):
    model = models.Fasa
    form_class = forms.FasaForm


class FasaUpdateView(generic.UpdateView):
    model = models.Fasa
    form_class = forms.FasaForm
    pk_url_kwarg = "pk"


class FasaDeleteView(generic.DeleteView):
    model = models.Fasa
    success_url = reverse_lazy("projekrkk_Fasa_list")


class ZontindakanListView(generic.ListView):
    model = models.Zontindakan
    form_class = forms.ZontindakanForm


class ZontindakanCreateView(generic.CreateView):
    model = models.Zontindakan
    form_class = forms.ZontindakanForm


class ZontindakanDetailView(generic.DetailView):
    model = models.Zontindakan
    form_class = forms.ZontindakanForm


class ZontindakanUpdateView(generic.UpdateView):
    model = models.Zontindakan
    form_class = forms.ZontindakanForm
    pk_url_kwarg = "pk"


class ZontindakanDeleteView(generic.DeleteView):
    model = models.Zontindakan
    success_url = reverse_lazy("projekrkk_Zontindakan_list")


class ProjekListView(generic.ListView):
    model = models.Projek
    form_class = forms.ProjekForm


class ProjekCreateView(generic.CreateView):
    model = models.Projek
    form_class = forms.ProjekForm


class ProjekDetailView(generic.DetailView):
    model = models.Projek
    form_class = forms.ProjekForm


class ProjekUpdateView(generic.UpdateView):
    model = models.Projek
    form_class = forms.ProjekForm
    pk_url_kwarg = "pk"


class ProjekDeleteView(generic.DeleteView):
    model = models.Projek
    success_url = reverse_lazy("projekrkk_Projek_list")


class SungaiListView(generic.ListView):
    model = models.Sungai
    form_class = forms.SungaiForm


class SungaiCreateView(generic.CreateView):
    model = models.Sungai
    form_class = forms.SungaiForm


class SungaiDetailView(generic.DetailView):
    model = models.Sungai
    form_class = forms.SungaiForm


class SungaiUpdateView(generic.UpdateView):
    model = models.Sungai
    form_class = forms.SungaiForm
    pk_url_kwarg = "pk"


class SungaiDeleteView(generic.DeleteView):
    model = models.Sungai
    success_url = reverse_lazy("projekrkk_Sungai_list")


class FokusListView(generic.ListView):
    model = models.Fokus
    form_class = forms.FokusForm


class FokusCreateView(generic.CreateView):
    model = models.Fokus
    form_class = forms.FokusForm


class FokusDetailView(generic.DetailView):
    model = models.Fokus
    form_class = forms.FokusForm


class FokusUpdateView(generic.UpdateView):
    model = models.Fokus
    form_class = forms.FokusForm
    pk_url_kwarg = "pk"


class FokusDeleteView(generic.DeleteView):
    model = models.Fokus
    success_url = reverse_lazy("projekrkk_Fokus_list")


class RumusankawalangunatanahListView(generic.ListView):
    model = models.Rumusankawalangunatanah
    form_class = forms.RumusankawalangunatanahForm


class RumusankawalangunatanahCreateView(generic.CreateView):
    model = models.Rumusankawalangunatanah
    form_class = forms.RumusankawalangunatanahForm


class RumusankawalangunatanahDetailView(generic.DetailView):
    model = models.Rumusankawalangunatanah
    form_class = forms.RumusankawalangunatanahForm


class RumusankawalangunatanahUpdateView(generic.UpdateView):
    model = models.Rumusankawalangunatanah
    form_class = forms.RumusankawalangunatanahForm
    pk_url_kwarg = "pk"


class RumusankawalangunatanahDeleteView(generic.DeleteView):
    model = models.Rumusankawalangunatanah
    success_url = reverse_lazy("projekrkk_Rumusankawalangunatanah_list")


class GunatanahsemasaListView(generic.ListView):
    model = models.Gunatanahsemasa
    form_class = forms.GunatanahsemasaForm


class GunatanahsemasaCreateView(generic.CreateView):
    model = models.Gunatanahsemasa
    form_class = forms.GunatanahsemasaForm


class GunatanahsemasaDetailView(generic.DetailView):
    model = models.Gunatanahsemasa
    form_class = forms.GunatanahsemasaForm


class GunatanahsemasaUpdateView(generic.UpdateView):
    model = models.Gunatanahsemasa
    form_class = forms.GunatanahsemasaForm
    pk_url_kwarg = "pk"


class GunatanahsemasaDeleteView(generic.DeleteView):
    model = models.Gunatanahsemasa
    success_url = reverse_lazy("projekrkk_Gunatanahsemasa_list")
