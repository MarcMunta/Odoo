# Odoo - Modulo RRSS clientes

Repositorio de addon Odoo para ampliar la ficha de clientes/contactos con dos URLs de redes sociales:

- LinkedIn: `x_linkedin_url`
- Instagram: `x_instagram_url`

## Base tecnica

Odoo agrupa funcionalidad en modulos/addons. Un modulo declara modelos Python, vistas XML y datos. Este addon hereda `res.partner` y extiende la vista `base.view_partner_form`.

Referencia: https://www.odoo.com/documentation/15.0/developer/tutorials/getting_started/01_architecture.html

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
```

## Instalacion

1. Copiar `addons/partner_social_media` dentro de un directorio incluido en `addons_path`.
2. Reiniciar Odoo.
3. Activar modo desarrollador.
4. Apps -> Actualizar lista de aplicaciones.
5. Instalar o actualizar `Partner Social Media`.

En Docker, montar el directorio `addons` en `/mnt/extra-addons`.

## Prueba hecha

Se validaron los campos en `res.partner`, la vista heredada del formulario de contacto y un cliente de prueba con URLs de LinkedIn e Instagram. Las capturas y la justificacion visual estan en:

- `docs/Act2-Justificacion-RRSS-Odoo.pdf`
