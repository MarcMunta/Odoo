# Odoo - Modulos OffiTec

Repositorio de addons Odoo para las actividades de ERP.

## Modulos incluidos

- `partner_social_media`: amplia la ficha de clientes/contactos con URLs de LinkedIn e Instagram.
- `offitec_request_management`: crea una pantalla de solicitudes de mobiliario para OffiTec.

## Base tecnica

Odoo agrupa funcionalidad en modulos/addons. Un modulo declara modelos, vistas XML, reglas de acceso y datos.

Referencias:

- https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/01_architecture.html
- https://www.odoo.com/documentation/19.0/developer/tutorials/importable_modules.html

## Estructura

```text
addons/
  partner_social_media/
    __init__.py
    __manifest__.py
    models/
      __init__.py
      res_partner.py
    views/
      res_partner_views.xml
  offitec_request_management/
    __init__.py
    __manifest__.py
    models/
      offitec_request_model.xml
    security/
      ir.model.access.csv
    views/
      offitec_request_views.xml
    data/
      offitec_request_data.xml
```

## Instalacion

1. Copiar el addon dentro de un directorio incluido en `addons_path`.
2. Reiniciar Odoo.
3. Activar modo desarrollador.
4. Apps -> Actualizar lista de aplicaciones.
5. Instalar o actualizar el modulo.

En Docker, montar el directorio `addons` en `/mnt/extra-addons`.

## Entregas PDF

- `docs/Act2-Justificacion-RRSS-Odoo.pdf`
- `docs/Act3-Justificacion-Nuevo-Modulo-OffiTec-Odoo.pdf`

Las capturas de prueba estan en `docs/screenshots` y `docs/screenshots_act3`.
