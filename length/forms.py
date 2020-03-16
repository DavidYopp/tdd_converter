from django import forms


class LengthConverterForms(form.Forms):
    MEASUREMENTS = (
        ('Centimetre', 'Centimetre'),
        ('metre', 'Metre'),
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    input_value = forms.DecimalField(decimal_places=3)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_value = forms.DecimalField(decimal_places=3, required=False)
