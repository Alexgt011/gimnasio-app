# 🏋️ Sistema de Gestión de Gimnasio

Aplicación web desarrollada con Python y Flask para la gestión de instructores, turnos, autenticación y reportes.

## 🔁 Solicitudes gestionadas

### 📝 Solicitud por Cambio del Cliente

- **N° de Solicitud:** CR-GYM-001
- **Fecha:** 2025-06-01
- **Originador:** Alexander (Cliente)
- **Sistema:** Sistema de Gestión de Gimnasio – Versión 1.0
- **Elementos Afectados:** `app.py`, `templates/dashboard_admin.html`, `reportes_module.py`
- **Descripción del Cambio:** Agregar funcionalidad para exportar lista de instructores y sus horarios a Excel (.xlsx) desde el dashboard.
- **Justificación:** El cliente necesita los datos en Excel para planificación mensual.
- **Impacto Esperado:**
  - Modificaciones en backend (`reportes_module.py`) y frontend.
  - Nuevo botón de exportación.
  - Actualización en documentación de usuario y pruebas.
- **Fecha Requerida de Implementación:** 2025-06-05
- **Aprobación:** ✅ Aprobado por el CCB el 2025-06-02
- **Prioridad:** Alta
- **Asignado a:** Equipo Backend & UI
- **Estado:** En desarrollo (Sprint 4)

### 🐞 Solicitud por Corrección de Error

- **N° de Solicitud:** CR-GYM-002
- **Fecha:** 2025-06-01
- **Originador:** Marcelo Vargas (QA)
- **Sistema:** Sistema de Gestión de Gimnasio – Versión 1.0
- **Elementos Afectados:** `registro_module.py`, `templates/form_instructor.html`
- **Descripción del Error:** Permite registrar instructores sin turnos asignados.
- **Justificación:** Rompe la lógica del calendario y programación.
- **Impacto Esperado:**
  - Validación obligatoria de turnos en frontend.
  - Backend no insertará instructores incompletos.
  - Nuevas pruebas unitarias.
- **Fecha Requerida de Implementación:** 2025-06-03
- **Aprobación:** ✅ Aprobado por el CCB el 2025-06-01
- **Prioridad:** Crítica
- **Asignado a:** Backend Developer – Daniel
- **Estado:** En espera de pruebas

---

## 🔎 Revisión

> Toda solicitud debe ser revisada por el Comité de Control de Cambios (CCB).  
> Ninguna modificación se aplica sin la validación formal del comité.

---

## 📌 Registro de versiones salientes

| Versión  | Fecha de liberación | Descripción                                                            |
|----------|---------------------|------------------------------------------------------------------------|
| v1.0     | 2025-05-28          | Versión inicial funcional del sistema. Registro, login, gestión de instructores. |
| v1.0.1   | 2025-06-03 (estimado) | Corrección crítica: validación de turnos vacíos en instructores.     |
| v1.1     | 2025-06-05 (estimado) | Mejora: exportación de reportes a Excel desde el panel del administrador. |

---

## 🔧 Gestión de versiones

![Gestión de versiones](static/images/gestion_versiones.png)

Este diagrama muestra cómo se gestionan solicitudes por cambio y por error, con su revisión respectiva antes de fusionarse a `main`.

---

## ✨ Autor

**Alexander** – [GitHub](https://github.com/Alexgt011)

