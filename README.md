# Parcial-1
Parcial 1 trabajo de Calculadora Ventas de Ropa 

# Calculadora de Ventas con Tkinter

Este proyecto es una **aplicación de escritorio en Python** desarrollada con la librería **Tkinter**, que funciona como una calculadora de ventas. Permite ingresar datos básicos de una compra y obtener el **subtotal, descuento aplicado, IVA (19%) y el total final a pagar**.  

El programa está diseñado para ser **sencillo, práctico y visualmente claro**, ideal como ejercicio de aprendizaje en programación con interfaces gráficas.

---

## Autor

- **Creado por:** Samuel Torres  
- **Versión:** 1.0 – 2025  

---

## Características principales

- **Interfaz gráfica (GUI)** creada con **Tkinter**.
- Ingreso de datos mediante **campos de texto (`Entry`)**:
  - Precio unitario.
  - Cantidad de productos.
  - Porcentaje de descuento.
- Cálculo automático de:
  - Subtotal (precio × cantidad).
  - Descuento aplicado.
  - IVA (19% fijo).
  - Total final.
- **Validación de errores**: evita valores negativos o no numéricos mostrando mensajes de error con `messagebox`.
- **Menú de opciones**:
  - **Inicio → Salir**: cerrar la aplicación.
  - **Ayuda → Mostrar ayuda**: explica el funcionamiento.
  - **Ayuda → Acerca de**: muestra la información del autor y versión.
- Personalización de ventana:
  - Título, tamaño fijo y carga de icono (`Ropa.ico`).
- **Mensajes emergentes (`messagebox`)** para ayuda, errores y créditos.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3  
- **Biblioteca GUI:** Tkinter (módulos `Tk`, `Label`, `Entry`, `Button`, `Menu`, `messagebox`)  

---

## Flujo de uso

1. El usuario abre la aplicación.  
2. Ingresa el **precio unitario**, la **cantidad** de productos y el **descuento (%)**.  
3. Presiona el botón **"Calcular total"**.  
4. El programa muestra en pantalla el detalle de la operación: subtotal, monto de descuento, IVA y total a pagar.  
5. El menú permite acceder a ayuda o salir de la aplicación fácilmente.  



