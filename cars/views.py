from django.shortcuts import render, redirect, get_object_or_404
from cars.models import Car, CarImage
from cars.forms import CarModelForm, CarImageFormSet
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all()
        search = request.GET.get('search')
        
        if search:
            cars = Car.objects.filter(name__icontains=search)

        context = {'cars': cars}
        return render(request, 'cars.html', context)
    

@method_decorator(login_required(login_url='login_view'), name='dispatch')
class NewCarView(View):
    def get(self,request):
        form = CarModelForm()

        context = {'form': form}
        return render(request, 'new_car.html', context)
    
    def post(self, request):
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            messages.success(request, "Car added successfully")
            return redirect("cars")

        context = {'form': form}
        return render(request, 'new_car.html', context)
    

@method_decorator(login_required(login_url='login_view'), name='dispatch')   
class DeleteCarView(View):
    def get(self, request, id):
        car = get_object_or_404(Car, id=id)
        if car.user != request.user:
            messages.error(request, "You are not authorized to delete this car")
            return redirect("cars")
        car.delete()
        messages.error(request, "Car deleted successfully")
        return redirect("cars")


@method_decorator(login_required(login_url='login_view'), name='dispatch')   
class UpdateCarView(View):
    def get(self, request, id):
        car = get_object_or_404(Car, id=id)
        if car.user != request.user:
            messages.error(request, "You are not authorized to update this car")
            return redirect("cars")
        
        form = CarModelForm(instance=car)
        formset = CarImageFormSet(instance=car)

        context = {'form': form, 'formset': formset}
        return render(request, 'update_car.html', context)
    
    def post(self, request, id):
        car = get_object_or_404(Car, id=id)
        if car.user != request.user:
            messages.error(request, "You are not authorized to update this car")
            return redirect("cars")
        
        form = CarModelForm(request.POST, request.FILES, instance=car)
        formset = CarImageFormSet(request.POST, request.FILES, instance=car)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Car updated successfully")
            return redirect("cars")

        context = {'form': form, 'formset': formset}
        return render(request, 'update_car.html', context)
    

class CarDetailView(View):
    def get(self, request, id):
        car = get_object_or_404(Car, id=id)
        images = car.car_images.all()

        if not images.exists():
            images = CarImage.objects.filter(car=car).first()

        context = {'car': car, 'images': images, 'user': request.user}
        return render(request, 'car_detail.html', context)
    