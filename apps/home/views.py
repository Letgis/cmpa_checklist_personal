from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import CMPAChecklist


@login_required(login_url="/login/")
def homepage(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/homepage.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    print(request)
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    print(request)
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print(e)
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def save_request(request):
    if request.method == 'POST':
        context = {}
        user_name = request.POST.get('user_name', None)
        location = request.POST.get('location', None)
        support = request.POST.get('support', None)
        band_pma = request.POST.get('band_pma', None)
        band_pmo = request.POST.get('band_pmo', None)
        project_code = request.POST.get('project_code', None)
        ippf = request.POST.get('ippf', None)
        deferral = request.POST.get('deferral', None)
        customer_name = request.POST.get('customer_name', None)
        contract_tcv = request.POST.get('contract_tcv', None)
        contract_length = request.POST.get('contract_length', None)
        contract_type = request.POST.get('contract_type', None)
        #annual_tcv = request.POST.get('annual_tcv', None)
        total_invoices = request.POST.get('total_invoices', None)
        billing_window = request.POST.get('billing_window', None)

        number_local = request.POST.get('number_local', None)
        number_ica = request.POST.get('number_ica', None)
        number_sub = request.POST.get('number_sub', None)

        checklist = CMPAChecklist(user_name=user_name, location=location, support=support, band_pma=band_pma,
                                  band_pmo=band_pmo, project_code=project_code, ippf=ippf,
                                  deferral=deferral, customer_name=customer_name,
                                  contract_tcv=contract_tcv, contract_length=contract_length,
                                  contract_type=contract_type,
                                  total_invoices=total_invoices, billing_window=billing_window,
                                  number_local=number_local, number_ica=number_ica,
                                  number_sub=number_sub)
        checklist.save()

        print(location, support, band_pma, band_pmo, project_code, ippf,
              deferral, customer_name, contract_tcv, contract_length,
              contract_type, total_invoices, billing_window,
              number_local, number_ica, number_sub)

        return render(request, 'home/finish.html', context=context)

    else:
        return render(request, 'home/create-request.html', context=context)


def show_checklist(request):
    view_checklist = CMPAChecklist.objects.all()
    return render(request, 'home/index.html', {"view_checklist": view_checklist})
