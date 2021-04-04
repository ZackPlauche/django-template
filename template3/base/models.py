from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class BusinessInfo(BaseSetting):
    phone_number = PhoneNumberField(help_text="Enter the phone number you want your customers to contact you or your business through.")
    phone_number_display = models.CharField(max_length=50, blank=True, help_text="Enter the phone number in the format you'd like your customers to see it (e.g., +1 (303) 261-8653)")
    email = models.EmailField(help_text="Enter the email you'd like customers to contact you / your business through.")
    email_display = models.CharField(max_length=50, blank=True, help_text="Enter the email or text you'd like people to see & click on. (defaults to Email set above if none).")

    class Meta:
        verbose_name = 'business information'

class HomePage(Page):
    hero_title = models.CharField(max_length=260, blank=True)
    hero_subtitle = models.CharField(max_length=260, blank=True)
    hero_cta_text = models.CharField('Hero CTA text', max_length=50, blank=True)
    hero_cta_link = models.CharField('Hero CTA link', max_length=260, blank=True)
    hero_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True)
    body_2 = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragragh', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            (
                FieldPanel('hero_title'),
                FieldPanel('hero_subtitle'),
                FieldPanel('hero_cta_text'),
                FieldPanel('hero_cta_link'),
                ImageChooserPanel('hero_background_image'),
            ),
            heading='Hero Section'
        ),
        FieldPanel('body'),
    ]




class AboutPage(Page):
    pass


class ContactPage(Page):
    pass