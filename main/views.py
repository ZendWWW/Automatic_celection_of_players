from django.shortcuts import render


#def base(request):
#return render(request, 'main/base.html')
def Map_selection_page(request):
    return render(request, 'main/Map_selection_page.html')


def home(request):
    return render(request, 'main/home.html')  # Убедитесь, что шаблон существует


def search_for_the_match(request):
    return render(request, 'main/Search_for_the_match.html')


karta_info = [
    {"id": 1,
     "description": "",
     "image_url": "css/images/img_15.png"},
    {"id": 2,
     "description": "Nuke — одна из самых сложных и тактических карт в CS2, известная своей вертикальной структурой и нестандартным расположением зон. Она требует от команд четкой координации и контроля над ключевыми позициями.",
     "image_url": "css/images/img_16.png"},
    {"id": 3,
     "description": "Dust 2 — легендарная карта, ставшая символом всей серии Counter-Strike. Её сбалансированный дизайн и продуманная геометрия сделали её одной из самых популярных карт в соревновательном режиме.",
     "image_url": "css/images/img_17.png"},
    {"id": 4,
     "description": "Ancient — одна из самых необычных и атмосферных карт в CS2, переносящая игроков в руины древнего города с храмами и джунглями. Её уникальный дизайн сочетает открытые пространства с тесными коридорами, создавая особый тактический баланс.",
     "image_url": "css/images/img_18.png"},
    {"id": 5,
     "description": "Inferno — одна из самых атмосферных и тактически насыщенных карт в CS2, отличающаяся плотной городской застройкой и интенсивным ближнебойным геймплеем. Её дизайн вдохновлён испанскими городками с узкими улочками и тесными коридорами.",
     "image_url": "css/images/img_19.png"},
    {"id": 6,
     "description": "Anubis — одна из самых необычных и атмосферных карт в CS2, выполненная в стиле древнеегипетских руин. Её уникальный дизайн сочетает открытые пространства с узкими коридорами храмов, создавая идеальный баланс между тактическим планированием и динамичными перестрелками.",
     "image_url": "css/images/img_20.png"},
    {"id": 7,
     "description": "Train — уникальная промышленная карта, действие которой происходит на железнодорожной станции и прилегающих складах. Её отличительной чертой являются длинные линии обзора и сложная система поездов, создающая нестандартные тактические ситуации.",
     "image_url": "css/images/img_21.png"}
]


def Map_info_page(request, map_id):
    """Страница с подробной информацией о товаре"""
    item = next((c for c in karta_info if c["id"] == map_id), None)
    return render(request, "main/Map_mirage_info_page.html", {"map": item})

from django.http import JsonResponse
from django.views.decorators.http import require_GET

MAPS = [
    { "name": "Mirage", "url": "karta_info/1" },
    { "name": "Dust 2", "url": "karta_info/3" },
    { "name": "Inferno", "url": "karta_info/5" },
    { "name": "Nuke", "url": "karta_info/2" },
    { "name": "Train", "url": "karta_info/7" },
    { "name": "Ancient", "url": "karta_info/4" },
    { "name": "Anubis", "url": "karta_info/6" },
]

@require_GET
def search_maps(request):
    query = request.GET.get("q", "").lower()
    if not query:
        return JsonResponse({"results": []})

    filtered = [m for m in MAPS if query in m["name"].lower()]
    return JsonResponse({"results": filtered})
