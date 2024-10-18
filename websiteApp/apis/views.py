from rest_framework import viewsets
from websiteApp.response.cbt_api_response import *
from websiteApp.helpers import *
from . helpers import *
from . serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse



class cbtIndustryViewSet(viewsets.ModelViewSet):
    
    def addIndustry(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                serializer = CbtIndustrySerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()
                    return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
                
                return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()

    def UpdateIndustry(self, request, PR_INDUSTRY_ID=None):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid and PR_INDUSTRY_ID is not None:
                try:
                    instance = CbtIndustry.objects.get(PR_INDUSTRY_ID=PR_INDUSTRY_ID)
                    serializer = CbtIndustrySerializer(instance, data=data, partial=True)
                    
                    if serializer.is_valid():
                        serializer.save()
                        return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
                    return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                except ObjectDoesNotExist:
                    return CbtDataResponse([], ApiStatus.Failure, CbtMessage.DataNotFound).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def industryList(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                industry_objs = CbtIndustry.objects.all()
                serializer = CbtIndustrySerializer(industry_objs, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def fetchIndustryData(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                industry_data = CbtIndustry.objects.all()
                serializer = CbtIndustrySerializer(industry_data, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()

class cbtProductViewSet(viewsets.ModelViewSet):
    
    def addProduct(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                serializer = CbtProductSerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()
                    return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
                
                return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()

    def updateProduct(self, request, PR_PRODUCT_ID=None):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid and PR_PRODUCT_ID is not None:
                try:
                    instance = CbtProduct.objects.get(PR_PRODUCT_ID=PR_PRODUCT_ID)
                    serializer = CbtProductSerializer(instance, data=data, partial=True)
                    
                    if serializer.is_valid():
                        serializer.save()
                        return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
                    return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                except ObjectDoesNotExist:
                    return CbtDataResponse([], ApiStatus.Failure, CbtMessage.DataNotFound).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
    
    def productList(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                product_objs = CbtProduct.objects.all()
                serializer = CbtProductSerializer(product_objs, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def fetchProductData(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                product_data = CbtProduct.objects.all()
                serializer = CbtProductSerializer(product_data, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()

class cbtPricingViewSet(viewsets.ModelViewSet):
    
    def addPricing(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                serializer = CbtPricingSerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()
                    return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
                
                return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()

    def updatePricing(self, request, PR_PRICING_ID=None):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid and PR_PRICING_ID is not None:
                try:
                    instance = CbtPricing.objects.get(PR_PRICING_ID=PR_PRICING_ID)
                    serializer = CbtPricingSerializer(instance, data=data, partial=True)
                    
                    if serializer.is_valid():
                        serializer.save()
                        return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
                    return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                except ObjectDoesNotExist:
                    return CbtDataResponse([], ApiStatus.Failure, CbtMessage.DataNotFound).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def pricingList(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                pricing_objs = CbtPricing.objects.all()
                serializer = CbtPricingSerializer(pricing_objs, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def fetchPricingData(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                pricing_data = CbtPricing.objects.all()
                serializer = CbtPricingSerializer(pricing_data, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
        
class cbtPlanViewSet(viewsets.ModelViewSet):
    
    def addPlan(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                serializer = CbtPlanSerializer(data=data)
                
                if serializer.is_valid():
                    serializer.save()
                    return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
                
                return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()

    def updatePlan(self, request, PR_PLAN_ID=None):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid and PR_PLAN_ID is not None:
                try:
                    instance = CbtPricingPlan.objects.get(PR_PLAN_ID=PR_PLAN_ID)
                    serializer = CbtPlanSerializer(instance, data=data, partial=True)
                    
                    if serializer.is_valid():
                        serializer.save()
                        return CbtDataResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
                    return CbtDataResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                except ObjectDoesNotExist:
                    return CbtDataResponse([], ApiStatus.Failure, CbtMessage.DataNotFound).cbtResponse()

            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()

        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def pricingList(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                pricing_objs = CbtPricingPlan.objects.all()
                serializer = CbtPlanSerializer(pricing_objs, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    def fetchPricingData(self, request):
        try:
            data = request.data
            msg, isValid = userPermission(data.get('PR_TOKEN'))
            if isValid:
                pricing_data = CbtPricingPlan.objects.all()
                serializer = CbtPlanSerializer(pricing_data, many=True)
                return CbtDataResponse(serializer.data, ApiStatus.Success).cbtResponse()
            return CbtDataResponse([], ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
        except Exception as ex:
            return CbtDataResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
        
class cbtApiViewSet(viewsets.ModelViewSet):

    def fetchNavData(self, request):
            try:
                data = request.data
                msg, isValid = userPermission(data.get('PR_TOKEN'))

                if isValid:
                    industries = CbtIndustry.objects.filter(PR_STATUS=1)
                    industry_serializer = CbtNavbarIndustrySerializer(industries, many=True)

                    product = CbtProduct.objects.filter(PR_STATUS=1)
                    product_serializer = CbtNavbarProductSerializer(product, many=True)

                    pricing = CbtPricing.objects.filter(PR_STATUS=1)
                    pricing_serializer = CbtNavbarPricingSerializer(pricing, many=True)
                    
                    nav_data = {
                        "Industries": industry_serializer.data,
                        "Product": product_serializer.data,
                        "Pricing": pricing_serializer.data,
                    }

                    return CbtDataResponse(nav_data, ApiStatus.Success).cbtResponse()
                return CbtDataResponse({}, ApiStatus.Failure, CbtMessage.cbtMsg(msg)).cbtResponse()
            
            except Exception as ex:
                return CbtDataResponse({}, ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()