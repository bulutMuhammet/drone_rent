from django import forms
from drones.models import RentedDrone

# drone kiralama formu
class RentedDroneForm(forms.ModelForm):
    class Meta:
        model = RentedDrone
        fields = ['drone', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        drone = cleaned_data.get('drone')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # eğer drone o tarihler arasında başka biri tarafından kiralandıysa hata ver
        if drone and start_date and end_date:
            conflicts = RentedDrone.objects.filter(drone=drone, start_date__lt=end_date, end_date__gt=start_date)
            if conflicts.exists():
                raise forms.ValidationError('Seçilen İHA o saatler arasında başka biri tarafından kiralanmıştır.')

            if end_date <= start_date:
                raise forms.ValidationError("Bitiş tarihi başlangıç tarihinden ileride olmalıdır")

        return cleaned_data