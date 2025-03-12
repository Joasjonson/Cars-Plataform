from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from cars.models import CarInventory, Car
from openai_api.client import get_car_ai_description


# Signal to send a welcome email to the user after registration
@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created and instance.email:
        send_mail(
            'Welcome to PyCar!',
            f"Hello {instance.username},\n\n"
            "Welcome to CarHub, your go-to platform for buying and selling cars. "
            "We're excited to have you on board! With your account, you can easily browse through "
            "exclusive car offers, post your own vehicles for sale, and connect with other car enthusiasts.\n\n"
            "Get started by adding your car listings or checking out the amazing offers available!\n\n"
            "If you have any questions or need assistance, feel free to reach out to us.\n\n"
            "Happy car shopping!\n\nBest regards,\nThe PyCar Team",
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )

# Signal to update inventory after car is added
@receiver(post_save, sender=Car)
def update_inventory(sender, instance, **kwargs):
    print("Inventory updated")
    cars = Car.objects.all()

    cars_count = cars.count()
    cars_value = sum([car.value for car in cars])
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


# Signal to update inventory after car is deleted
@receiver(post_delete, sender=Car)
def update_inventory(sender, instance, **kwargs):
    print("Inventory updated")
    cars = Car.objects.all()

    cars_count = cars.count()
    cars_value = sum([car.value for car in cars])
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


# Generate AI description for car if description is empty
#@receiver(pre_save, sender=Car)
#def check_description(sender, instance, **kwargs):
#    if not instance.description:
#        ai_description = get_car_ai_description(instance.name, 
#                                                instance.brand, 
#                                                instance.model_year)
#        
#        instance.description = ai_description
