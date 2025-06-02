# 📌 CHANGELOG - Sistema de Gestión de Gimnasio

Este archivo documenta todos los cambios importantes realizados en el sistema de gimnasio, incluyendo mejoras, correcciones y versiones publicadas.

---

## [v1.1] - 2025-06-05 (estimado)
### ✨ Solicitud de Cambio por Nuevo Requisito (CR-GYM-001)
- **Agregado** botón para exportar la lista de instructores a Excel (.xlsx) desde el panel de administrador.
- **Integrado** módulo `reportes_module.py` con funcionalidad de exportación.
- **Actualizada** la interfaz `dashboard_admin.html` para incluir la nueva funcionalidad.
- **Revisión:** ✅ Aprobado por el CCB el 2025-06-02  
- **Asignado a:** Equipo Backend & UI  
- **Prioridad:** Alta

---

## [v1.0.1] - 2025-06-03 (estimado)
### 🐛 Solicitud de Cambio por Corrección de Error (CR-GYM-002)
- **Corregido** error que permitía registrar instructores sin turno asignado.
- **Agregada** validación en el backend (`registro_module.py`) y en el formulario HTML.
- **Implementadas** pruebas automatizadas para prevenir regresión.
- **Revisión:** ✅ Aprobado por el CCB el 2025-06-01  
- **Asignado a:** Backend Developer – Daniel  
- **Prioridad:** Crítica

---

## [v1.0] - 2025-05-28
### 🚀 Versión Inicial
- Registro y login de instructores.
- Gestión de turnos.
- Panel de administración funcional.
- Pruebas básicas con Selenium y Faker.
- Estructura de proyecto inicial completa.

---

🛡 Todas las solicitudes fueron revisadas y aprobadas por el Comité de Control de Cambios (CCB) antes de su implementación.
