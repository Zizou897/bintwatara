from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail



from app.functions import *
from app.models import *
from bintWatara import settings
# Create your views here.

def verify_email(email):
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True


def home(request):
    get_infos_web = get_info_web({'publish': True})
    get_banners = get_banner({'publish':True})
    get_abouts = get_about({'publish':True})
    get_process_constructions = get_process_construction({'publish': True})
    get_teams = get_team({'publish': True})
    get_testimonies = get_testimony({'publish': True})
    get_sociaux = get_social({'publish': True})
    get_some_services = get_some_service({'publish': True})
    get_configs_web = get_config_web({'publish': True})
    get_companies_fea = get_company_feature({'publish': True})
    
    template = 'app/index.html'
    context = {
        'page':{
            'title': 'BINT-WATARA | Bienvenue',
            'text_description': 'Solutions de construction et de rénovation',
            'text_team_title': 'Nos Experts',
            'text_team_description': '',
        },
        'get_infos_web': get_infos_web,
        'get_banners': get_banners,
        'get_abouts': get_abouts,
        'get_process_constructions': get_process_constructions,
        'get_teams': get_teams,
        'get_testimonies': get_testimonies,
        'get_sociaux': get_sociaux,
        'get_some_services': get_some_services,
        'get_configs_web': get_configs_web,
        'get_companies_fea': get_companies_fea,
        'is_home': True,
    }
    return render(request, template, context)


def about(request):
    get_infos_web = get_info_web({'publish': True})
    get_sociaux = get_social({'publish': True})
    get_abouts = get_about({'publish':True})
    get_configs_web = get_config_web({'publish': True})
    get_teams = get_team({'publish': True})
    
    template = 'app/about.html'
    context = {
        'page':{
            'title': 'BINT-WATARA | A PROPOS',
            'text_description': 'Solutions de construction et de rénovation'
        },
        'get_infos_web': get_infos_web,
        'get_sociaux': get_sociaux,
        'get_abouts': get_abouts,
        'get_configs_web': get_configs_web,
        'get_teams': get_teams,
        'is_about': True,
    }
    return render(request, template, context)


def contact(request):
    get_infos_web = get_info_web({'publish': True})
    get_sociaux = get_social({'publish': True})
    get_teams_decision = get_team_decision({'publish': True})
    
    template = 'app/contact.html'
    context = {
        'page':{
            'title': 'BINT-WATARA | CONTACT',
            'text_description': 'Solutions de construction et de rénovation'
        },
        'get_infos_web': get_infos_web,
        'get_sociaux': get_sociaux,
        'get_teams_decision': get_teams_decision,
        'is_contact': True,
    }
    return render(request, template, context)


def error_page(request):
    get_infos_web = get_info_web({'publish': True})
    get_sociaux = get_social({'publish': True})
    
    template = 'app/404.html'
    context = {
        'page':{
            'title': 'BINT-WATARA | ERROR 404',
            'text_description': 'Solutions de construction et de rénovation'
        },
        'get_infos_web': get_infos_web,
        'get_sociaux': get_sociaux,
        
    }
    return render(request, template, context)


def service(request):
    get_infos_web = get_info_web({'publish': True})
    get_sociaux = get_social({'publish': True})
    get_all_services = get_all_service({'publish': True})
    get_configs_web = get_config_web({'publish': True})
    
    template = 'app/service.html'
    context = {
        'page':{
            'title': 'BINT-WATARA | SERVICE',
            'text_description': 'Solutions de construction et de rénovation'
        },
        'get_infos_web': get_infos_web,
        'get_sociaux': get_sociaux,
        'get_some_services': get_all_services,
        'get_configs_web': get_configs_web,
        'is_true': True,
        'is_service': True,
    }
    return render(request, template, context)



def team(request):
    get_infos_web = get_info_web({'publish': True})
    get_sociaux = get_social({'publish': True})
    
    template = 'app/team.html'
    context = {
        'page':{
            'title': 'BINT-WATARA | Notre équipe',
            'text_description': 'Solutions de construction et de rénovation'
        },
        'get_infos_web': get_infos_web,
        'get_sociaux': get_sociaux,
        'is_active': True,
    }
    return render(request, template, context)


# poour Enregister les e-mails
@csrf_exempt
def post_mail(request):
    success,msg = False, ''
    
    email = request.POST.get('email')
    
    if email.isspace() or not email:
        msg = 'Veuillez renseigner les champs vides'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    else:
        success = True
        news,created = Newsletter.objects.get_or_create(email=email)
        if created:
            msg = 'Vous etes maintemant abonné'
            news.save()
        else:
            msg = "vous etes déjà abonné" 
    
    
    data = {
        'msg': msg,
        'success': success
    }
    return JsonResponse(data, safe=False)



#pour avoir un RDV(Rendez-Vous)
@csrf_exempt
def get_rdv(request):
    success,msg = False, ''
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    service = request.POST.get('service')
    message = request.POST.get('message')
    
    if not name or name.isspace() or not email or email.isspace() or not phone or phone.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    else:
        success = True
        rdv,created = Appointment.objects.get_or_create(name=name, email=email, phone=phone, service=service, message=message)
        if created:
            msg = "Nous vous reviendrons d'ici peu"
            rdv.save()
            
            subject = "Prise de Rendez-Vous chez BINT-WATARA"
            message = f"Bonjour M./Mde/Mdle {name}  \nVous avez demander un rendez-vous\nNous vous contacterons d'ici peu \n\n\n\n MERCI POUR VOTRE CONFIANCE"
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            
            subjects = "BINT-WATARA"
            messages = f'bonjour M {name} a demande un RDV \nSon mail et son numero est:\n\n Telephone:{phone}\n E-mail: {email}'
            customer_email = email
            print("###############  1  #####################")
            to_lists = [settings.EMAIL_HOST_USER]
            print("###############  2  #####################")         
            print("###############  3  #####################")
            send_mail(subjects, messages, customer_email, to_lists,fail_silently=False)
            print("###############  3  #####################")        
        else:
            msg = "Ce message est déjà envoyé"
    
    data = {
        'msg': msg,
        'success': success
    }
    return JsonResponse(data, safe=False)



#pour contacter bint-watara
@csrf_exempt
def post_contact(request):
    success,msg = False, ''
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    sujet = request.POST.get('service')
    message = request.POST.get('message')
    
    if not name or name.isspace() or not email or email.isspace() or not sujet or sujet.isspace():
        msg = 'Veuillez renseigner les champs vides'
    elif verify_email(email):
        msg = 'veuillez saisir un addresse Mail correct'
    else:
        success = True
        contact,created = Contact.objects.get_or_create(name=name, email=email, sujet=sujet, message=message)
        if created:
            msg = "Merci de nous avoir contacter"
            contact.save()
            
            subject =" Merci d'avoir contacter BINT-WATARA"
            message = f"Bonjour M./Mde/Mdle {name}  \nVous avez demander contacté BINT-WATARA pour{sujet}  \nNous vous contacterons d'ici peu \n\n\n\n MERCI POUR VOTRE CONFIANCE"
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            
            subjects = "BINT-WATARA"
            messagess = f'bonjour M {name}, vous a contacté pour"{sujet}" \nSon mail et son numero est:\n\nE-mail: {email}'
            customer_email = email
            print("###############  1  #####################")
            to_lists = [settings.EMAIL_HOST_USER]
            print("###############  2  #####################")         
            print("###############  3  #####################")
            send_mail(subjects, messagess, customer_email, to_lists,fail_silently=False)
            print("###############  3  #####################")
        else:
            msg = "Merci encore"
    
    data = {
        'msg': msg,
        'success': success
    }
    return JsonResponse(data, safe=False)