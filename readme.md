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
├── cabeceras-HTTP_SSL.py
│
└── README.md
```

---

# 🚀 Herramientas incluidas

## 🔍 HTTP Headers Checker (Python)

Script en Python para analizar cabeceras de seguridad HTTP y SSL de una web siguiendo la metodologia OWASP.

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

# ⚙️ Como usarlo:

* pip install requests
* python3 cabeceras-HTTP_SSL.py

