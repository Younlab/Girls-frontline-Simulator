from django.urls import path, include

urlpatterns = [
    # 유저 정보
    path('members/', include('members.urls.api_urls')),
    # 전술 인형
    path('dolls/', include('tactical_dolls.urls.api_urls')),
]