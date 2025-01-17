from django.forms import ModelForm, TextInput

from core.sh.models import Province

class ProvinceForm(ModelForm):

  class Meta:
    model = Province
    fields = '__all__'
    labels = {
      'number_id': 'N° de Provincia'
    }
    widgets = {
      'number_id': TextInput(
        attrs={
          'placeholder': 'Ingrese el numero identificatorio de la provincia',
        }
      ),

      'province': TextInput(
        attrs={
          'placeholder': 'Ingrese el nombre de la provincia a agregar',
        }
      )
    }