
from app.models import *


# pour la page d'accueil----------------------------------------------------

def get_info_web(data=dict()):
    return Web.objects.filter(**data).first()


def get_banner(data=dict()):
    return Banner.objects.filter(**data)


def get_about(data=dict()):
    return About.objects.filter(**data).first()


def get_process_construction(data=dict()):
    return ProcessOfConstruction.objects.filter(**data)


def get_team(data=dict()):
    return Team.objects.filter(**data)[:3]


def get_team_decision(data=dict()):
    return Team.objects.filter(**data).order_by("order")[:2]


def get_testimony(data=dict()):
    return Testimony.objects.filter(**data)


def get_social(data=dict()):
    return Social.objects.filter(**data)


def get_some_service(data=dict()):
    return Service.objects.filter(**data).order_by('order')


def get_config_web(data=dict()):
    return ConfigWeb.objects.filter(**data).first()


def get_company_feature(data=dict()):
    return CompanyFeatures.objects.filter(**data)

#---------------------------------------------------------------------------


# pour la page de service---------------------------------------------------

def get_all_service(data=dict()):
    return Service.objects.filter(**data).order_by('order')

#----------------------------------------------------------------------------