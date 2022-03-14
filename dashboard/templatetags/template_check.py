from django import template
from dashboard.models import SelectTemplate, PageTitle, FavIcon, MainIcon

register = template.Library()

@register.filter
def template_check(user):
    get_template_obj = SelectTemplate.objects.filter(user=user, is_active=True)
    if get_template_obj.exists():
        temp = get_template_obj[0].category
        return temp
    else:
        temp = get_template_obj[0].category
        return temp


@register.filter
def page_title(temp):
    title = PageTitle.objects.filter(active_template=temp).order_by('-id').first()
    if title :
        page_title = title.title
        return page_title
    else:
        title = PageTitle.objects.filter(active_template=0).order_by('-id').first()
        page_title = title.title
        return page_title


@register.filter
def logo(temp):
    logo = MainIcon.objects.filter(active_template=temp).order_by('-id').first()
    if logo :
        main_logo = logo.image.url
        return main_logo
    else:
        else_log = MainIcon.objects.filter(active_template=0).order_by('-id').first()
        el_logo = else_log.image.url
        return el_logo


@register.filter
def favicon(temp):
    favicon = FavIcon.objects.filter(active_template=temp).order_by('-id').first()
    if favicon :
        fav = favicon.image.url
        return fav
    else:
        else_fav = FavIcon.objects.filter(active_template=0).order_by('-id').first()
        fav = else_fav.image.url
        return fav




# get_template_obj = SelectTemplate.objects.filter(is_active=True)
# # let check is template exists or not
# if get_template_obj.exists():
#     temp = get_template_obj[0].category
#     logo = MainIcon.objects.filter(template=temp)[0]
#     print('=========== logo ==========')
#     print(logo)
#     print('=========== logo ==========')
#     return logo.image.url