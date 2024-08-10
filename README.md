
# DNS Enumeration Tool

## Descripción

Esta herramienta realiza la enumeración de registros DNS para un dominio objetivo. Permite obtener y mostrar los registros DNS más comunes, como `A`, `AAAA`, `CNAME`, `MX`, `NS`, `SOA` y `TXT` para un dominio especificado.

## Cómo funciona

La herramienta se compone de dos scripts principales:

1. **`dns_enumeration.py`**: Este script define una clase `DnsEnumeration` que se encarga de realizar la resolución de los registros DNS para el dominio objetivo.

2. **`dns_main.py`**: Este script actúa como la entrada principal de la herramienta. Utiliza el módulo `argparse` para aceptar un dominio objetivo desde la línea de comandos y luego llama a la clase `DnsEnumeration` para realizar la enumeración de DNS.

## Uso

### Requisitos

Antes de ejecutar la herramienta, asegúrate de tener los requisitos necesarios instalados:

```bash
pip install -r requirements.txt
```

### Ejecución

Para utilizar la herramienta, ejecuta el siguiente comando desde la línea de comandos:

```bash
python dns_main.py --target dominio.com
```

Reemplaza `dominio.com` con el dominio que deseas analizar.

### Ejemplo

```bash
python dns_main.py --target ejemplo.com
```

Este comando ejecutará la enumeración DNS para `ejemplo.com` y mostrará los registros encontrados en la salida de la consola.

---
