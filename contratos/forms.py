from django import forms
from .models import Vehiculo_contratos
from .models import Factura
from .models import usuario, user, estado, documentos, presupuesto, contrato_venta_cupo, contrato_compra_cupo, contrato_compra, contrato_venta,Checklist
from vehiculos.models import Usuario
import difflib

class VehiculoForm(forms.ModelForm):
    valor_presupuesto = forms.FloatField(required=False, label="Presupuesto")

    class Meta:
        model = Vehiculo_contratos
        fields = [
            'placa', 'marca', 'linea', 'modelo', 'color', 'cilindraje', 'puertas',
            'capacidad', 'clase', 'tipo_carroceria', 'tipo_servicio', 'valor', 'n_motor',
            'n_chasis', 'n_vin', 'n_serie', 'sitio_matricula', 'n_acta_matricula',
            'fecha_matricula', 'ciudad_vehiculo', 'valor_presupuesto', 'imagen'
        ]
        

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['n_factura', 'nit', 'nombre_local', 'fecha', 'descripcion', 'cantidad', 'valor', 'iva', 'imagen']
        widgets = {
            'iva': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        self.vehiculo = kwargs.pop('vehiculo', None)
        super(FacturaForm, self).__init__(*args, **kwargs)

    def clean_n_factura(self):
        n_factura = self.cleaned_data.get('n_factura')
        if Factura.objects.filter(n_factura=n_factura).exists():
            raise forms.ValidationError("Ya existe una factura con este número.")
        return n_factura

    def clean(self):
        cleaned_data = super().clean()
        valor = cleaned_data.get("valor")
        cantidad = cleaned_data.get("cantidad")
        descripcion = cleaned_data.get("descripcion")

        if valor is not None and cantidad is not None and valor < 0:
            self.add_error('valor', 'El valor no puede ser negativo.')
        if cantidad < 0:
            self.add_error('cantidad', 'La cantidad no puede ser negativa.')

        if descripcion and self.vehiculo:
            facturas = Factura.objects.filter(id_placa=self.vehiculo).exclude(id=self.instance.id)
            for factura in facturas:
                similarity = difflib.SequenceMatcher(None, descripcion, factura.descripcion).ratio()
                if similarity > 0.7:
                    self.add_error('descripcion', f'La descripción es similar a la de la factura {factura.n_factura} del vehículo {self.vehiculo.placa}.')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'nombre', 'p_apellido', 's_apellido', 'cedula', 'telefono', 
            'direccion', 'correo', 'ciudad', 'barrio', 'ciudad_exp', 'tipo_doc'
        ]

# Formulario para el modelo user
class UserForm(forms.ModelForm):
    ROL_CHOICES = [
        ('administrador', 'administrador'),
        ('Logistica', 'Logística'),
        ('Asesor', 'Asesor'),
    ]
    SEDE_CHOICES = [
        ('Green Wash', 'Green Wash'),
        ('Taxi Cupos', 'Taxi Cupos'),
    ]

    rol = forms.ChoiceField(choices=ROL_CHOICES)
    sede = forms.ChoiceField(choices=SEDE_CHOICES)

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'first_name', 'last_name', 'rol', 'sede']
        widgets = {
            'password': forms.PasswordInput(),  # Para ocultar el texto al ingresar la contraseña
        }

# Formulario para el modelo estado
class EstadoForm(forms.ModelForm):
    ESTADO_CHOICES = [
        ('Vitrina', 'Vitrina'),
        ('Taller', 'Taller'),
        ('Vendido', 'Vendido'),
        ('Chatarrizado', 'Chatarrizado'),
    ]
    
    estado = forms.ChoiceField(choices=ESTADO_CHOICES)

    class Meta:
        model = estado
        fields = ['id_placa', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_placa'].queryset = Vehiculo_contratos.objects.all()
        self.fields['id_placa'].label_from_instance = lambda obj: obj.placa

# Formulario para el modelo documentos
class DocumentosForm(forms.ModelForm):
    class Meta:
        model = documentos
        fields = [
            'id_placa', 'n_orden', 'emp_afiliadora', 'n_tarjeta_operacion', 
            'tarjeta_operacion', 'fecha_inicial_to', 'fecha_final_to', 'fecha_inicio_soat', 
            'fecha_final_soat', 'soat', 'fecha_inicio_tecno', 'fecha_final_tecno', 
            'tecnomecanica', 'fecha_inicio_sRC', 'fecha_final_sRc', 'seguros_rc'
        ]

# Formulario para el modelo presupuesto
class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = presupuesto
        fields = ['id_placa', 'valor_p']

# Formulario para el modelo contrato_venta_cupo
class ContratoVentaCupoForm(forms.ModelForm):
    class Meta:
        model = contrato_venta_cupo
        fields = ['id_placa', 'cc_comprador', 'cc_vendedor', 'valor_vCupo', 'primer_abono', 'archivos']

# Formulario para el modelo contrato_compra_cupo
class ContratoCompraCupoForm(forms.ModelForm):
    class Meta:
        model = contrato_compra_cupo
        fields = ['id_placa', 'cc_comprador', 'cc_vendedor', 'valor_cCupo', 'primer_abono', 'archivos']

# Formulario para el modelo contrato_compra
class ContratoCompraForm(forms.ModelForm):
    class Meta:
        model = contrato_compra
        fields = ['id_placa', 'cc_comprador', 'cc_vendedor', 'valor_c', 'primer_abono', 'archivos']

# Formulario para el modelo contrato_venta
class ContratoVentaForm(forms.ModelForm):
    class Meta:
        model = contrato_venta
        fields = ['id_placa', 'cc_comprador', 'cc_vendedor', 'valor_v', 'primer_abono', 'archivos']
        

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['traspaso', 'documentos_al_dia', 'entrega_comercial', 'desembolso', 'saldo']