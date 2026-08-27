# Formulario Kobo Collect — Inventario Fotográfico de Bodega

Archivo: `inventario_fotografico_bodega.xlsx` (XLSForm, listo para subir a KoboToolbox: Proyectos > Nuevo > Subir un archivo XLSForm).

## Contenido del formulario

- **Tipo de Registro** (select_one): "Registro inicial de Bodega" o "Registro cierre día Bodega".
- **Encargado de la información** (texto)
- **Fecha de la información** (fecha, por defecto hoy)
- **Hora** (hora)
- **Ubicación de la bodega** (geopoint / GPS)
- **Comentario General** (texto libre)
- **6 fotos de referencia** (foto_1 a foto_6), todas obligatorias.

## Sobre la ubicación KMZ

KoboCollect no genera un archivo `.kmz` directamente en el celular; el campo `geopoint`
guarda latitud/longitud/altitud/precisión con cada envío. Para obtener el KML/KMZ:

1. En KoboToolbox, entra al proyecto > pestaña **Data** > **Downloads**.
2. Elige el formato **GeoJSON** o usa el mapa integrado y expórtalo como **KML**.
3. El KML se puede abrir en Google Earth y, si se necesita, comprimir a `.kmz`
   (zip con extensión `.kmz`) desde Google Earth ("Guardar lugar como... .kmz").

Si en cambio se necesita exportar directamente en `.kmz` desde el propio formulario, se
requeriría un flujo externo (script/Zapier/Google Earth) ya que XLSForm no soporta ese
formato de salida de forma nativa.

## Cómo editar

Editar `build_form.py` y volver a ejecutar `python3 build_form.py` para regenerar el
archivo `.xlsx` con cambios (agregar preguntas, cambiar textos, etc.).
