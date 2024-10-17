from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from websiteApp.helpers import *
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.decorators.clickjacking import xframe_options_exempt


# ======================================== HOME PAGE START =====================================

def index(request):
    seo = {
        'title': 'o2 Infosystems - Design, Development, and Telecom Services for Business Growth',
        'description': 'Welcome to o2 Infosystems, offering expert design & development, telecom services, hosted IVR solutions, and more to enhance your business growth.',
        'keywords': 'Design & Development, Telecom Services, Hosted IVR, Promotional Services, Cloud Solutions, Hosting, Leads generation'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/index.html', data)


# ======================================== HOME PAGE END =======================================


# ======================================== ABOUT PAGE START ====================================

def about(request):
    seo = {
        'title': 'About Us - o2 Infosystems: Business Solutions Across Multiple Industries',
        'description': 'Learn about o2 Infosystems and our mission to deliver top-tier design, development, telecom, and cloud solutions to businesses worldwide.',
        'keywords': 'about o2 Infosystems, design services, development services, telecom solutions, cloud hosting, IVR solutions'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/about.html', data)


# ======================================== ABOUT PAGE END ======================================


# ======================================== SOLUTIONS PAGE START =================================
def products(request):
    seo = {
        'title': 'o2 Infosystems Solutions - Design, Telecom, Cloud, and IVR Solutions for Every Industry',
        'description': 'Explore the innovative design, development, telecom, IVR, and cloud hosting solutions o2 Infosystems offers to optimize business operations.',
        'keywords': 'Design services, Telecom services, IVR solutions, Cloud solutions, hosting services, business tools'
    }

    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/product.html', data)



def single_products(request, PR_CATEGORY):
    product = get_object_or_404(CbtProduct, PR_SLUG=PR_CATEGORY)
    
    seo = {
        'title': f'{product.PR_NAME} - o2 Infosystems SaaS Solutions for Business',
        'description': f'{product.PR_NAME} helps businesses streamline operations with advanced SaaS tools, tailored for your specific industry needs.',
        'keywords': f'{product.PR_NAME}, SaaS solutions, business optimization, {product.PR_NAME} tools'
    }

    data = {
        'Seo': seo,
        'Product': product.PR_NAME,
        'Description': product.PR_DESCRIPTION,
        'Content': product.PR_CONTENT_1,
        'Slug': product.PR_SLUG,
        'BackgroundImage': product.PR_BANNER_IMAGE,
    }

    return render(request, 'websiteApp/company/product_single.html', data)


# ======================================== SOLUTIONS PAGE END ===================================


# ======================================== INDUSTRY PAGE START =================================
def industry(request):
    seo = {
        'title': 'Industry Solutions by o2 Infosystems - SaaS, Telecom, and Cloud Solutions for Every Sector',
        'description': 'Discover how o2 Infosystems tailors telecom, IVR, and cloud solutions to suit a wide variety of industries for optimized business growth.',
        'keywords': 'industry solutions, telecom services, hosted IVR, cloud solutions, business software'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/industry.html', data)


def single_industry(request, PR_INDUSTRY):
    industry = get_object_or_404(CbtIndustry, PR_SLUG=PR_INDUSTRY)
    
    seo = {
        'title': f'{industry.PR_NAME} Solutions by o2 Infosystems - SaaS and Telecom Services',
        'description': f'{industry.PR_NAME} solutions by o2 Infosystems provide tailored software, cloud, and telecom tools to streamline industry-specific business processes.',
        'keywords': f'{industry.PR_NAME}, telecom solutions, cloud hosting, IVR services'
    }

    data = {
        'Seo': seo,
        'Industry': industry.PR_NAME,
        'Description': industry.PR_DESCRIPTION,
        'Content': industry.PR_CONTENT_1,
        'Slug': industry.PR_SLUG,
        'BackgroundImage': industry.PR_BANNER_IMAGE,
    }

    return render(request, 'websiteApp/company/industry_single.html', data)


# ======================================== SOLUTIONS PAGE END ===================================


# ======================================== CONSULTATION PAGE START =============================
def booking(request):
    seo = {
        'title': 'Book a Demo - o2 Infosystems SaaS Solutions',
        'description': 'Schedule a live demo with o2 Infosystems experts and discover how our SaaS, telecom, and cloud solutions can enhance your business efficiency.',
        'keywords': 'book demo, SaaS demo, telecom services, IVR solutions, business solutions'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/booking.html', data)

# ======================================== CONSULTATION PAGE END ===============================


# ======================================== FAQ PAGE START ======================================
def faq(request):
    seo = {
        'title': 'Frequently Asked Questions - o2 Infosystems',
        'description': 'Find answers to common questions about o2 Infosystems’ SaaS products, design services, telecom solutions, and more.',
        'keywords': 'FAQ, SaaS support, design services, telecom solutions, IVR hosting'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/faq.html', data)

# ======================================== FAQ PAGE END ========================================


# ======================================== COOKIES PAGE START ======================================
def cookies(request):
    seo = {
        'title': 'Cookies Policy - o2 Infosystems',
        'description': 'Read our cookies policy to learn how we use cookies to enhance your experience on our SaaS, telecom, and design services platform.',
        'keywords': 'cookies policy, privacy policy, data usage, SaaS solutions'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/cookies.html', data)

# ======================================== FAQ PAGE END ========================================


# ======================================== SUPPORT PAGE START ======================================
def support(request):
    seo = {
        'title': 'Support - o2 Infosystems Telecom, SaaS, and Cloud Solutions',
        'description': 'Contact o2 Infosystems for support regarding our telecom, IVR, cloud hosting, and design services. Our team is ready to assist you.',
        'keywords': 'support, SaaS support, telecom solutions, cloud hosting, design services'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/contact_support.html', data)


# ======================================== SUPPORT PAGE END ========================================


# ======================================== SALES PAGE START ======================================
def sales(request):
    seo = {
        'title': 'Sales Inquiries - o2 Infosystems Solutions',
        'description': 'Get in touch with our sales team for more information on our design, telecom services, hosted IVR, and cloud hosting solutions.',
        'keywords': 'sales support, design services, telecom solutions, cloud hosting, IVR solutions'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/contact_sales.html', data)


# ======================================== SALES PAGE END ==========================================


# ======================================== HELP PAGE START ======================================
def help(request):
    seo = {
        'title': 'Help Center - o2 Infosystems SaaS Solutions',
        'description': 'Find quick answers to your questions about o2 Infosystems products and services, including SaaS solutions, design, telecom, and cloud services.',
        'keywords': 'help, SaaS support, telecom services, cloud hosting, design services'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/contact_help.html', data)

# ======================================== Help PAGE END ========================================


# ======================================== CONTACT PAGE START ==================================
def contact(request):
    seo = {
        'title': 'Contact Us - o2 Infosystems Business Solutions',
        'description': 'Reach out to o2 Infosystems for inquiries or support on our SaaS, telecom, and cloud hosting services. We’re here to assist you.',
        'keywords': 'contact, SaaS support, telecom services, cloud hosting, business inquiries'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/contact_us.html', data)


def contact_us(request):
    seo = {
        'title': 'Contact Us - o2 Infosystems Business Solutions',
        'description': 'Reach out to o2 Infosystems for inquiries or support on our SaaS, telecom, and cloud hosting services. We’re here to assist you.',
        'keywords': 'contact, SaaS support, telecom services, cloud hosting, business inquiries'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/contact_us_single.html', data)


@csrf_protect
@require_http_methods(["POST"])
def contact_post(request):
    if request.method == 'POST':
        # handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Logic to send email
        send_mail(
            f'Message from {name}',
            message,
            email,
            ['support@o2 Infosystems.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('workobserver.contact')

    return redirect('workobserver.contact')
# ======================================== CONTACT PAGE END ====================================


# ======================================== POLICY PAGE START ===================================
def policy(request):
    seo = {
        'title': 'Privacy Policy - o2 Infosystems',
        'description': 'Read our privacy policy to understand how o2 Infosystems handles your personal data and ensures your privacy across our services.',
        'keywords': 'privacy policy, data protection, SaaS data security, telecom solutions'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/policy.html', data)

# ======================================== POLICY PAGE END =====================================


# ======================================== TERMS PAGE START =====================================
def terms(request):
    seo = {
        'title': 'Terms and Conditions - o2 Infosystems Solutions',
        'description': 'Read the terms and conditions for using o2 Infosystems’ SaaS, telecom, IVR, and cloud hosting services.',
        'keywords': 'terms and conditions, SaaS user agreement, telecom service terms, cloud hosting terms'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/terms.html', data)

# ======================================== TERMS PAGE END =======================================


# ======================================== PRICING PAGE START ===================================

def single_pricing(request, PR_PRICING_TYPE):
    pricing = get_object_or_404(CbtPricing, PR_SLUG=PR_PRICING_TYPE)
    plans = CbtPricingPlan.objects.filter(PR_PRICING=pricing, PR_STATUS=1)
    
    seo = {
        'title': f'Pricing for {pricing.PR_NAME} - o2 Infosystems Solutions',
        'description': f'Discover the pricing options for {pricing.PR_NAME} offered by o2 Infosystems, including SaaS, telecom, and cloud solutions.',
        'keywords': f'{pricing.PR_NAME}, SaaS pricing, telecom service pricing, cloud hosting prices'
    }

    data = {
        'Seo': seo,
        'Pricing': pricing.PR_NAME,
        'Plans': plans,
        'Description': pricing.PR_DESCRIPTION,
        'Content': pricing.PR_CONTENT_1,
        'Slug': pricing.PR_SLUG,
        'BackgroundImage': pricing.PR_BANNER_IMAGE,
    }

    return render(request, 'websiteApp/company/pricing_single.html', data)


# ======================================== PRICING PAGE END ======================================


# ======================================== CLIENT PAGE START =====================================

def client(request):
    seo = {
        'title': 'Our Clients - o2 Infosystems Business Solutions',
        'description': 'Explore the clients who trust o2 Infosystems for their SaaS, telecom, and cloud hosting needs.',
        'keywords': 'clients, SaaS clients, telecom clients, cloud hosting clients, business solutions'
    }
    data = {
        'Seo': seo
    }
    return render(request, 'websiteApp/company/our_client.html', data)


# ======================================== CLIENT PAGE END ======================================


# ======================================== BLOG PAGE START ======================================
def blog(request):
    seo = {
        'title': 'Our Blog - o2 Infosystems Insights and Trends',
        'description': 'Stay updated with the latest posts on SaaS, telecom, and cloud solutions from the o2 Infosystems team.',
        'keywords': 'SaaS blog, business trends, telecom services, cloud hosting trends, business solutions'
    }
    data = {
        'Seo': seo,
    }
    return render(request, 'websiteApp/company/blog.html', data)



def blog_single(request, PR_SLUG):
    seo = {
        'title': f'{PR_SLUG} - Blog Post from o2 Infosystems',
        'description': f'Read {PR_SLUG} and discover insights into SaaS, telecom, and cloud hosting trends and how they can benefit your business.',
        'keywords': f'{PR_SLUG}, SaaS trends, telecom blog, cloud hosting blog, business solutions blog'
    }
    data = {
        'Seo': seo,
    }
    return render(request, 'websiteApp/company/blog_single.html', data)

# ======================================== BLOG PAGE END ========================================

# =========================================================================================== PAGE FUNCTION ====================================================================

# USER FORM FUNCTION HERE 
@xframe_options_exempt
def industryForm(request, user_token, data_id=None):
    user_data, isValid = userPermission(user_token)
    if isValid:
        cat_objs = CbtIndustry.objects.filter()
        if data_id is not None:
            data = CbtIndustry.objects.get(PR_INDUSTRY_ID=data_id)
            context = {'action': 'update', 'data': data}

        else:
            context = {'action': 'add', 'data': ''}
            
        return render(request, 'websiteApp/form/industry/industry-form.html', context)

    return render(request, 'invalid.html', {'msg': user_data})


# USER FORM FUNCTION HERE 
@xframe_options_exempt
def productForm(request, user_token, data_id=None):

    user_data, isValid = userPermission(user_token)
    if isValid:
        cat_objs = CbtProduct.objects.filter() # To be change on category added
        if data_id is not None:
            data = CbtProduct.objects.get(PR_PRODUCT_ID=data_id)
            context = {'action': 'update', 'data': data}

        else:
            context = {'action': 'add', 'data': ''}
            
        return render(request, 'websiteApp/form/product/product-form.html', context)
    
    return render(request, 'YourApp/invalid.html', {'msg': user_data})


# USER FORM FUNCTION HERE 
@xframe_options_exempt
def pricingForm(request, user_token, data_id=None):

    user_data, isValid = userPermission(user_token)
    if isValid:
        cat_objs = CbtPricing.objects.filter()
        if data_id is not None:
            data = CbtPricing.objects.get(PR_PRICING_ID=data_id)
            context = {'action': 'update', 'data': data}

        else:
            context = {'action': 'add', 'data': ''}
            
        return render(request, 'websiteApp/form/pricing/pricing-form.html', context)
    
    return render(request, 'YourApp/invalid.html', {'msg': user_data})


def pricingPlanForm(request, user_token, data_id=None):

    user_data, isValid = userPermission(user_token)
    if isValid:
        cat_objs = CbtPricingPlan.objects.filter()
        if data_id is not None:
            data = CbtPricingPlan.objects.get(PR_PLAN_ID=data_id)
            context = {'action': 'update', 'data': data}

        else:
            context = {'action': 'add', 'data': ''}
            
        return render(request, 'websiteApp/form/pricing/pricing-plan-form.html', context)
    
    return render(request, 'YourApp/invalid.html', {'msg': user_data})
