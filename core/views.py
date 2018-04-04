from django.views.generic import CreateView

from core.forms import UploadExcelForm
from core.models import ArquivoExcel


class UploadExcelView(CreateView):
    template_name = "core/upload_excel.html"
    form_class = UploadExcelForm
    # model = ArquivoExcel

    def form_valid(self, form):
        import ipdb; ipdb.set_trace()
        pass

    def form_invalid(self, form):
        import ipdb; ipdb.set_trace()
        pass

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     import ipdb; ipdb.set_trace()
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)