from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import AssetType
from django.urls import reverse_lazy
from .forms import AssettypeCreateForm
# Create your views here.

class AssettypeListView(ListView):
    model = AssetType
    template_name = 'asset_type/list.html'


class AssettypeAddView(CreateView):
    model = AssetType
    template_name = 'asset_type/add.html'
    success_url = reverse_lazy('list')
    form_class = AssettypeCreateForm

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class
    #     print(form)
    #     typename = request.POST.get('type_name')
    #     description = request.POST.get('description')

    #     if typename and description == "":
    #         print("typename")
    #         asset_type = form.save(self,commit=False) 
    #         asset_type.type_name = typename# Create the model instance without saving to the database
    #         asset_type.description = description  # Assign the value of description field
    #         asset_type.save()  # Save the model instance to the database
    #         data = {'success': True}
    #         return JsonResponse(data)

    #     elif typename and description:
    #         form.save()
    #         data = {'success': True}
    #         return JsonResponse(data)

    #     else:
    #         form.add_error("type_name", "Invalid details")
    #         return JsonResponse({'success': False, 'message': 'Invalid data'})

    
    def form_valid(self, form) :
        # form = self.form_class
        description = self.request.POST.get('description')
        #description = form.cleaned_data['description']
        if description == '':
            print("inside form valid")
            form.instance.description = None
        data = {'success':True , 'id' : self.object.id}
        return JsonResponse(data)
        
    
    def form_invalid(self, form) :
        # form = self.form_class
        # description = self.request.POST.get('description')
        #description = form.cleaned_data['description']
        # if description == '':
        #     super().form_valid(form)
        print("Inside form invalid")
        return JsonResponse(form.errors.as_json(), safe=False)
    



        

class AssettypeUpdateView(UpdateView):
    model = AssetType
    fields =['type_name','description']
    template_name = 'asset_type/update.html'
    success_url = reverse_lazy('list')

    # def form_valid(self, form) :
    #     form = self.get_form
    #     if form:
    #         data = {'success':True , 'id' : self.object.id}
    #     return JsonResponse(data)
    
    # def form_invalid(self, form) :
    #     return JsonResponse(form.errors.as_json(), safe=False)

    
class AssettypeDetailView(DetailView):
    model= AssetType
    template_name = 'asset_type/detail.html'
    context_object_name = 'asset'

class AssettypeDeleteView(DeleteView):
    model = AssetType
    template_name = 'asset_type/delete.html'
    context_object_name = 'asset'
    success_url = reverse_lazy('list')