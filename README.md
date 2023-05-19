# Exámen Final Taller de Matemática 1 🥇 🔢 🔤
## Estuardo Sebastián Valle Bances - 202001954 
El presente repositorio alberga algunos de los programas utilizados para el exámen final de Taller de Matemática 1. En su mayoría problemas de "Combinatoria". Así fue la ayuda de algunas herramientas de programación para la verificación de incisos. etc

## Problema 2: Calcular $10 \overline{C} 6$ utilizando moldes 🔤
En primera instancia, sería útil listar algunas de las variables que pueden cambiar. 
Prácticamente tenemos 6 espacios en los cuales pueden existir moldes. Para esto, utilizaremos las variables $x,y,z,w,v,h$

_ _ _ _ _ _

$$
\underline{x} \hspace{0.2cm} \underline{x} \hspace{0.2cm}  \underline{x} \hspace{0.2cm} \underline{x} \hspace{0.2cm} \underline{x}
$$

Mientras que algunos métodos fueron explicados en las hojas del exámen. En esta pequeña sección trataremos de averiguar el valor final con algunos métodos computacionales con el propósito de a) Probar que el poder computacional es demasiado y b) Tratar de comparar los valores finales. 

### Método 1: Fuerza Bruta 💥
Cómo lo dice el título de este método, iteraremos sobre todas las posibles palabras que pueden ser formadas. Éste constará de los siguientes pasos: 
- *Método*
1. Creamos un conjunto 
$$ 
A = \{ a, b, c, d, e, f, g, h, i, j \} 
$$ 
```python
# Conjunto
    A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    palabras = []
    palabra = ""
```
3. Crear una palabra 
```python
#Generamos una palabra al azar
        for i in range(6):
            palabra += A[random.randint(0, 6)]
```

