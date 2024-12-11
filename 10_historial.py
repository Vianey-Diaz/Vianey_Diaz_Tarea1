class HistorialNavegador:
    def __init__(self):
        self.historial = []  # Pila para guardar las páginas visitadas

    def visitar(self, pagina):
        """Agrega una nueva página al historial."""
        self.historial.append(pagina)
        print(f"Visitando: {pagina}")

    def ir_atras(self):
        """Va hacia atrás en el historial si es posible."""
        if len(self.historial) > 1:  # Debe haber al menos dos páginas
            pagina_actual = self.historial.pop()  # Quitamos la página actual
            pagina_anterior = self.historial[-1]  # La nueva página actual es la anterior
            print(f"Regresando de {pagina_actual} a {pagina_anterior}")
        elif len(self.historial) == 1:
            print(f"Estás en la primera página: {self.historial[-1]}")
        else:
            print("El historial está vacío. No hay a dónde ir.")

    def mostrar_historial(self):
        """Muestra el historial completo."""
        if self.historial:
            print("Historial de navegación:")
            for pagina in reversed(self.historial):  # Mostrar de la más reciente a la más antigua
                print(f"  {pagina}")
        else:
            print("El historial está vacío.")


# Ejemplo de uso
navegador = HistorialNavegador()

# Simular navegación
navegador.visitar("pagina1.com")
navegador.visitar("pagina2.com")
navegador.visitar("pagina3.com")

# Mostrar historial
navegador.mostrar_historial()

# Ir hacia atrás
navegador.ir_atras()
navegador.ir_atras()

# Intentar ir atrás más allá del historial
navegador.ir_atras()

# Mostrar historial después de ir atrás
navegador.mostrar_historial()
