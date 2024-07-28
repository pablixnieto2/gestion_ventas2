# ventas/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from ventas.models import Venta

@receiver(post_save, sender=apps.get_model('pagos', 'Pago'))
def actualizar_estado_venta(sender, instance, **kwargs):
    venta = instance.venta
    total_pagado = sum(pago.importe for pago in venta.pagos_ventas.all())
    
    if total_pagado == 0:
        venta.estado_pago = "Incluir Pago"
    elif total_pagado < 0:
        venta.estado_pago = "Revisar Venta"
    elif total_pagado < venta.total_a_pagar:
        venta.estado_pago = "Pagado Parcialmente"
    elif total_pagado == venta.total_a_pagar:
        venta.estado_pago = "Pagado"
    else:
        venta.estado_pago = "Devolver al Cliente"

    if "Cancel" in venta.comentarios:
        venta.estado_venta = "Cancelada"
    elif venta.estado_deposito == "Pendiente de Entrega" or venta.estado_pago == "Pagado Parcialmente" or (venta.tipo == "Alquiler" and venta.estado_entrega == "Entregado o Enviado"):
        venta.estado_venta = "En Proceso"
    elif venta.tipo == "Venta" and venta.estado_entrega == "Entregado o Enviado" and venta.estado_pago == "Pagado":
        venta.estado_venta = "Completa"
    elif venta.tipo == "Alquiler" and venta.estado_entrega == "Vestido Devuelto" and venta.estado_pago == "Pagado":
        venta.estado_venta = "Completa"
    else:
        venta.estado_venta = "En Proceso"
    
    venta.total_pagado = total_pagado
    venta.pendiente_de_pago = venta.total_a_pagar - total_pagado
    venta.save()
