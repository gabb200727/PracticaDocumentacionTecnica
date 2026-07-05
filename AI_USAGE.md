# AI_USAGE.md

## Uso de Inteligencia Artificial

### Herramienta utilizada

* **Herramienta:** ChatGPT
* **Modelo:** GPT-5.5
* **Proveedor:** OpenAI

---

## Prompt utilizado

> "Mejora el siguiente código. Hazlo más robusto y completo."

Código proporcionado:

```python
# Programa sencillo para sumar dos números

# Pedir los números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar la suma
suma = num1 + num2

# Mostrar el resultado
print("La suma es:", suma)
```

---

## Cambios realizados

Se realizaron las siguientes mejoras sobre el código original:

* Se organizó el programa utilizando funciones para mejorar la estructura y facilitar el mantenimiento.
* Se implementó una función específica para solicitar y validar números ingresados por el usuario.
* Se agregó manejo de errores mediante `try-except` para evitar que el programa finalice si el usuario introduce un dato inválido.
* Se creó una función dedicada a realizar la operación de suma.
* Se añadió una función principal (`main`) para organizar el flujo de ejecución del programa.
* Se incorporó la estructura `if __name__ == "__main__":`, siguiendo las buenas prácticas de desarrollo en Python.
* Se mejoraron los mensajes mostrados al usuario para hacer la interacción más clara y amigable.
* Se añadió la posibilidad de realizar varias sumas consecutivas sin necesidad de reiniciar el programa.
* Se documentó el código mediante comentarios y cadenas de documentación (*docstrings*).

---

## Justificación de los cambios

Las mejoras se realizaron con el objetivo de:

* Incrementar la robustez del programa evitando errores por entradas incorrectas.
* Mejorar la legibilidad y organización del código mediante la modularización.
* Facilitar futuras modificaciones o ampliaciones del programa.
* Aplicar buenas prácticas de programación recomendadas en Python.
* Ofrecer una mejor experiencia al usuario mediante mensajes claros y validaciones.
* Obtener un código más profesional, reutilizable y fácil de mantener.

---

## Conclusión

La inteligencia artificial se utilizó como herramienta de apoyo para optimizar el código original, aplicando buenas prácticas de programación, validación de entradas, manejo de excepciones y una estructura modular. El resultado es un programa más seguro, organizado y fácil de comprender, manteniendo la misma funcionalidad solicitada inicialmente.
