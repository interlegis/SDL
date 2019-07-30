from django.views.generic import CreateView

from core.forms import UploadExcelForm
from core.models import ArquivoExcel
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class UploadExcelView(CreateView):
    template_name = "core/upload_excel.html"
    form_class = UploadExcelForm
    # model = ArquivoExcel

    def form_valid(self, request, form):
        print("Aí sim, garoto!")
        form.save()
        # import ipdb; ipdb.set_trace()
        return render(request, 'core/upload_excel.html')

    def form_invalid(self, request, form):
        print("Não bixo, assim não!")
        # import ipdb; ipdb.set_trace()
        return render(request, 'core/upload_excel.html')
   
    @method_decorator(login_required(login_url='http://localhost:8000/oidc/authenticate'))
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # import ipdb; ipdb.set_trace()
        files = request.POST.getlist('file')
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.form_invalid(request, form)

class GetExcelView(CreateView):
    template_name = "core/get_excel.html"
    form_class = UploadExcelForm
    # model = ArquivoExcel

    def form_valid(self, request, form):
        print("Aí sim, garoto!")
        form.save()
        # import ipdb; ipdb.set_trace()
        return render(request, 'core/upload_excel.html')

    def form_invalid(self, request, form):
        print("Não bixo, assim não!")
        # import ipdb; ipdb.set_trace()
        return render(request, 'core/upload_excel.html')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # import ipdb; ipdb.set_trace()
        files = request.POST.getlist('file')
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.form_invalid(request, form)