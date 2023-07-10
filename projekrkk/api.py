from rest_framework import viewsets, permissions

from . import serializers
from . import models


class JenisViewSet(viewsets.ModelViewSet):
    """ViewSet for the Jenis class"""

    queryset = models.Jenis.objects.all()
    serializer_class = serializers.JenisSerializer
    permission_classes = [permissions.IsAuthenticated]


class SublembanganViewSet(viewsets.ModelViewSet):
    """ViewSet for the Sublembangan class"""

    queryset = models.Sublembangan.objects.all()
    serializer_class = serializers.SublembanganSerializer
    permission_classes = [permissions.IsAuthenticated]


class LembanganViewSet(viewsets.ModelViewSet):
    """ViewSet for the Lembangan class"""

    queryset = models.Lembangan.objects.all()
    serializer_class = serializers.LembanganSerializer
    permission_classes = [permissions.IsAuthenticated]


class KategoriViewSet(viewsets.ModelViewSet):
    """ViewSet for the Kategori class"""

    queryset = models.Kategori.objects.all()
    serializer_class = serializers.KategoriSerializer
    permission_classes = [permissions.IsAuthenticated]


class SempadanrkkViewSet(viewsets.ModelViewSet):
    """ViewSet for the Sempadanrkk class"""

    queryset = models.Sempadanrkk.objects.all()
    serializer_class = serializers.SempadanrkkSerializer
    permission_classes = [permissions.IsAuthenticated]


class RumusankualitiairViewSet(viewsets.ModelViewSet):
    """ViewSet for the Rumusankualitiair class"""

    queryset = models.Rumusankualitiair.objects.all()
    serializer_class = serializers.RumusankualitiairSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgensiViewSet(viewsets.ModelViewSet):
    """ViewSet for the Agensi class"""

    queryset = models.Agensi.objects.all()
    serializer_class = serializers.AgensiSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Status class"""

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class FasaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Fasa class"""

    queryset = models.Fasa.objects.all()
    serializer_class = serializers.FasaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ZontindakanViewSet(viewsets.ModelViewSet):
    """ViewSet for the Zontindakan class"""

    queryset = models.Zontindakan.objects.all()
    serializer_class = serializers.ZontindakanSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjekViewSet(viewsets.ModelViewSet):
    """ViewSet for the Projek class"""

    queryset = models.Projek.objects.all()
    serializer_class = serializers.ProjekSerializer
    permission_classes = [permissions.IsAuthenticated]


class SungaiViewSet(viewsets.ModelViewSet):
    """ViewSet for the Sungai class"""

    queryset = models.Sungai.objects.all()
    serializer_class = serializers.SungaiSerializer
    permission_classes = [permissions.IsAuthenticated]


class FokusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Fokus class"""

    queryset = models.Fokus.objects.all()
    serializer_class = serializers.FokusSerializer
    permission_classes = [permissions.IsAuthenticated]


class RumusankawalangunatanahViewSet(viewsets.ModelViewSet):
    """ViewSet for the Rumusankawalangunatanah class"""

    queryset = models.Rumusankawalangunatanah.objects.all()
    serializer_class = serializers.RumusankawalangunatanahSerializer
    permission_classes = [permissions.IsAuthenticated]


class GunatanahsemasaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Gunatanahsemasa class"""

    queryset = models.Gunatanahsemasa.objects.all()
    serializer_class = serializers.GunatanahsemasaSerializer
    permission_classes = [permissions.IsAuthenticated]
