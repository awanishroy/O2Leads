from django.db import models
from django.utils.text import slugify  # For slug generation


# ================== MODELS FOR PORTFOLIO ==================
class CbtWebsiteData(models.Model):
  PR_WEBSITE_ID = models.AutoField(primary_key=True)
# PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE)
  PR_NAME = models.CharField(max_length=255)
  PR_LOGO = models.CharField(max_length=255, null=True, blank=True, default='/media/default-img.png')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_website_data'

# ===================== Industry Model ======================

class CbtIndustry(models.Model):
    PR_INDUSTRY_ID = models.AutoField(primary_key=True)

    PR_NAME = models.CharField(max_length=255, null=True, blank=True)
    PR_SLUG = models.SlugField(max_length=255, unique=True, blank=True)  # Allow blank slugs
    PR_DESCRIPTION = models.TextField(blank=True, null=True)
    PR_CONTENT_1 = models.TextField(blank=True, null=True)
    PR_BANNER_IMAGE = models.CharField(max_length=255, blank=True, null=True)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_WEBSITE = models.ForeignKey(CbtWebsiteData, null=True, blank=True, on_delete=models.CASCADE)

    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_industry'

    def save(self, *args, **kwargs):
        if not self.PR_SLUG and self.PR_NAME:
            self.PR_SLUG = slugify(self.PR_NAME)
        super().save(*args, **kwargs)


# ===================== Product Model =======================

class CbtProduct(models.Model):
    PR_PRODUCT_ID = models.AutoField(primary_key=True)

    PR_NAME = models.CharField(max_length=255, null=True, blank=True)
    PR_SLUG = models.SlugField(max_length=255, unique=True, blank=True)  # Allow blank slugs
    PR_DESCRIPTION = models.TextField(blank=True, null=True)
    PR_CONTENT_1 = models.TextField(blank=True, null=True)
    PR_BANNER_IMAGE = models.CharField(max_length=255, blank=True, null=True)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_WEBSITE = models.ForeignKey(CbtWebsiteData, null=True, blank=True, on_delete=models.CASCADE)

    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_product'

    def save(self, *args, **kwargs):
        if not self.PR_SLUG and self.PR_NAME:
            self.PR_SLUG = slugify(self.PR_NAME)
        super().save(*args, **kwargs)


# ===================== Pricing Model =======================

class CbtPricing(models.Model):
    PR_PRICING_ID = models.AutoField(primary_key=True)

    PR_NAME = models.CharField(max_length=255, null=True, blank=True)
    PR_SLUG = models.SlugField(max_length=255, unique=True, blank=True)  # Allow blank slugs
    PR_DESCRIPTION = models.TextField(blank=True, null=True)
    PR_CONTENT_1 = models.TextField(blank=True, null=True)
    PR_BANNER_IMAGE = models.CharField(max_length=255, blank=True, null=True)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_WEBSITE = models.ForeignKey(CbtWebsiteData, null=True, blank=True, on_delete=models.CASCADE)

    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_pricing'

    def save(self, *args, **kwargs):
        if not self.PR_SLUG and self.PR_NAME:
            self.PR_SLUG = slugify(self.PR_NAME)
        super().save(*args, **kwargs)


class CbtPricingPlan(models.Model):
    PR_PLAN_ID = models.AutoField(primary_key=True)
    PR_PRICING = models.ForeignKey(CbtPricing, on_delete=models.SET_NULL, null=True, blank=True)
    PR_NAME = models.CharField(max_length=255)
    PR_PRICE = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field for pricing
    PR_FEATURES = models.TextField(blank=True, null=True)  # List of features (can be stored as text or JSON)
    PR_STATUS = models.IntegerField(default=1)  # 1 for active, 0 for inactive````

    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_pricing_plan'