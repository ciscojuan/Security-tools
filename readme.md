# 🛡️ SOC & Pentesting Toolkit

Repositorio personal con scripts y herramientas orientadas a **análisis de seguridad web**, **hardening** y apoyo a tareas de **SOC (Security Operations Center)**.

Este repositorio está diseñado para crecer progresivamente con utilidades prácticas para:

* Pentesting web
* Análisis de cabeceras HTTP
* Evaluación de configuraciones SSL/TLS
* Automatización de tareas de seguridad

---

# 📂 Estructura del repositorio

```
.
├── http_headers_checker/
│   ├── headers_check.py
│   └── README.md
├── ssl_analysis/ (futuro)
├── tools/ (scripts adicionales)
└── README.md
```

---

# 🚀 Herramientas incluidas

## 🔍 HTTP Headers Checker (Python)

Script en Python para analizar cabeceras de seguridad HTTP de una web y generar un resultado tipo auditoría SOC.

### ✅ Características

* Validación de cabeceras críticas:

  * HSTS
  * CSP
  * X-Frame-Options
  * X-Content-Type-Options
  * Referrer-Policy
  * Permissions-Policy
* Detección de fingerprinting:

  * Server
  * X-Powered-By
* Score de seguridad automático
* Salida en consola con colores (tipo SOC)

---

# ⚙️ Requisitos

* Python 3.8+
* pip

Inst
