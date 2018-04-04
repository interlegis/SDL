from django.forms import ModelForm

from core.models import ArquivoExcel


class UploadExcelForm(ModelForm):

    class Meta:
        model = ArquivoExcel
        fields = ['arquivo']