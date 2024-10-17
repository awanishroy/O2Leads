from rest_framework import serializers
from rest_framework.validators import *
# from drf_writable_nested import WritableNestedModelSerializer
from websiteApp.models import *

class CbtIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtIndustry
        fields = '__all__'

class CbtProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtIndustry
        fields = '__all__'

class CbtPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtIndustry
        fields = '__all__'

class CbtPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtPricingPlan
        fields = '__all__'

        
# Serializer For Industries Navbar This is use for Only API Purpose

class CbtNavbarIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtIndustry
        fields = ['PR_INDUSTRY_ID', 'PR_NAME', 'PR_SLUG']  # Include fields relevant to the navigation

class CbtNavbarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtProduct
        fields = ['PR_PRODUCT_ID', 'PR_NAME', 'PR_SLUG']  # Include fields relevant to the navigation

class CbtNavbarPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtPricing
        fields = ['PR_PRICING_ID', 'PR_NAME', 'PR_SLUG']  # Include fields relevant to the navigation
