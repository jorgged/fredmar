from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import horarioEmpresa, misionEmpresa, visionEmpresa, telefonoEmpresa


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        vision = visionEmpresa.objects.all()
        mision = misionEmpresa.objects.all()
        horario = horarioEmpresa.objects.all()
        telefono = telefonoEmpresa.objects.all()
        # import ipdb; ipdb.set_trace()
        context = self.get_context_data()
        context.update({
            'vision':vision,
            'mision':mision,
            'horarios':horario,
            'telefonos':telefono,
        })
        return self.render_to_response(context)