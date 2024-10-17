from django.urls import path
from . import views

urlpatterns = [

    # ============================ INDUSTRY URL'S ==============================
    path('add-industry', views.cbtIndustryViewSet.as_view({'post': 'addIndustry'})),
    path('update-industry/<int:PR_INDUSTRY_ID>', views.cbtIndustryViewSet.as_view({'post': 'UpdateIndustry'})),
    path('industry-list', views.cbtIndustryViewSet.as_view({'post': 'industryList'})),
    path('fetch-industry-data', views.cbtIndustryViewSet.as_view({'post': 'fetchIndustryData'})),

    # ============================== PRODUCT URL'S ==============================
    path('add-product', views.cbtProductViewSet.as_view({'post': 'addProduct'})),
    path('update-product/<int:PR_PRODUCT_ID>', views.cbtProductViewSet.as_view({'post': 'UpdateProduct'})),
    path('product-list', views.cbtProductViewSet.as_view({'post': 'productList'})),
    path('fetch-product-data', views.cbtProductViewSet.as_view({'post': 'fetchProductData'})),

    # ============================== PRICING URL'S ==============================
    path('add-pricing', views.cbtPricingViewSet.as_view({'post': 'addPricing'})),
    path('update-pricing/<int:PR_PRICING_ID>', views.cbtPricingViewSet.as_view({'post': 'addPricing'})),
    path('pricing-list', views.cbtPricingViewSet.as_view({'post': 'pricingList'})),
    path('fetch-pricing-data', views.cbtPricingViewSet.as_view({'post': 'fetchPricingData'})),

    # ============================== PLAN URL'S ==============================
    path('add-plan', views.cbtPlanViewSet.as_view({'post': 'addPlan'})),
    path('update-plan/<int:PR_PLAN_ID>', views.cbtPlanViewSet.as_view({'post': 'addPlan'})),
    path('plan-list', views.cbtPlanViewSet.as_view({'post': 'planList'})),
    path('fetch-plan-data', views.cbtPlanViewSet.as_view({'post': 'fetchPlanData'})),
    
    path('navbars', views.cbtApiViewSet.as_view({'post': 'fetchNavData'})),


]