from django.urls import path
from . import views

urlpatterns = [

    # ========================== HOME START ===========================

    path('',views.index,name='index'),

    # =========================== HOME END ============================


    # ========================== ABOUT START ===========================

    path('products', views.products, name='otleads.products'),
    path('products/<str:PR_CATEGORY>', views.single_products, name='otleads.products.category'),
    
    path('industry', views.industry, name='otleads.industry'),
    path('industry/<str:PR_INDUSTRY>', views.single_industry, name='otleads.industry.category'),

    path('contact-us', views.contact, name='otleads.contact'),
    path('contact_us', views.contact_us, name='otleads.contact_us'),
    path('contact-us-post', views.contact, name='otleads.contact-post'),

    path('shedule-metting', views.booking, name='otleads.booking'),

    path('support', views.support, name='otleads.support'),
    path('sales', views.sales, name='otleads.sales'),
    path('help', views.help, name='otleads.help'),

    path('about-us', views.about, name='otleads.about'),
    path('privcacy-policy', views.policy, name='otleads.policy'),
    path('cookies', views.cookies, name='otleads.cookies'),
    path('terms-and-condition', views.terms, name='otleads.terms'),
    path('faq', views.faq, name='otleads.faq'),

    # path('pricing', views.pricing, name='otleads.pricing'),
    path('pricing/<str:PR_PRICING_TYPE>', views.single_pricing, name='otleads.pricing.category'),
    
    path('our-client', views.client, name='otleads.client'),

    path('blog', views.blog, name='otleads.blog'),
    path('blog/<str:PR_SLUG>', views.blog_single, name='otleads.single.blog'),
    
]
