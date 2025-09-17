import tkinter as tk
from tkinter import messagebox

# --- configuración del icono ---
RUTA_DEL_LOGO = "Ropa.ico"

# --- funciones ---
def calcular_total():
    """
    Calcula subtotal, descuento, IVA y total
    """
    try:
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
        descuento = float(entry_descuento.get())

        if precio < 0 or cantidad < 0 or descuento < 0:
            messagebox.showerror("Error", "Los valores no pueden ser negativos.")
            return

        subtotal = precio * cantidad
        monto_descuento = subtotal * (descuento / 100) 
        subtotal_desc = subtotal - monto_descuento
        iva = subtotal_desc * 0.19
        total = subtotal_desc + iva

        etiqueta_resultado.config(
            text=f"Subtotal: {subtotal:.2f}\n"
                 f"Descuento ({descuento}): {monto_descuento:.2f}\n"
                 f"IVA (19%): {iva:.2f}\n"
                 f"Total: ${total:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos")

def salir():
    ventana.destroy()

def mostrar_info():
    messagebox.showinfo("Ayuda", "Esta es una calculadora de ventas con descuentos e IVA (19%).")

def mostrar_acerca():
    messagebox.showinfo("Acerca de", "Calculadora de Ventas\nCreado por: Samuel Torres\nVersión 1.0 - 2025")

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Calculadora de Ventas")
ventana.geometry("500x350")

# configurar icono
try:
    ventana.iconbitmap(RUTA_DEL_LOGO)
except tk.TclError:
    print(f"Advertencia: No se pudo cargar el icono desde: {RUTA_DEL_LOGO}")

# -- menú --
barra_menu = tk.Menu(ventana)

menu_inicio = tk.Menu(barra_menu, tearoff=0)
menu_inicio.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Mostrar ayuda", command=mostrar_info)
menu_ayuda.add_command(label="Acerca de", command=mostrar_acerca)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)

# -- widgets --
etiqueta_instruccion = tk.Label(ventana, text="Ingrese datos de la compra:")
etiqueta_instruccion.pack(pady=10)

tk.Label(ventana, text="Precio unitario:").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Cantidad:").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Label(ventana, text="Descuento (%):").pack()
entry_descuento = tk.Entry(ventana)
entry_descuento.pack()

# botón calcular
button_calcular = tk.Button(ventana, text="Calcular total", command=calcular_total)
button_calcular.pack(pady=10)

# etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack(pady=10)

# -- ejecutar --
ventana.mainloop()