

# PyTorch HRR: El Motor Lógico

**Un módulo de IA Neurosimbólica independiente que realiza álgebra con conceptos.**

Este repositorio implementa **Representaciones Reducidas Holográficas (HRR)**, un tipo de Arquitectura Simbólica Vectorial (VSA). A diferencia de las redes neuronales estándar que utilizan asociaciones "difusas", este motor te permite vincular vectores matemáticamente para formar estructuras de datos complejas y luego consultarlos con alta precisión.

### La Teoría
En la IA estándar:
* `King` y `Queen` son simplemente vectores similares.

En este Motor Lógico:
* `Queen` se define matemáticamente como `King - Man + Woman`.
* `Apple` se define como `(Color * Red) + (Shape * Round) + (Taste * Sweet)`.

Utilizamos **Convolución Circular** (vía FFT) para vincular vectores y **Correlación Circular** para desvincularlos.

### Inicio Rápido

**1. Instalar Dependencias**
```bash
pip install torch numpy


### Cómo Usarlo

Ejecuta el script: python interactive_logic.py

¡Prueba esta secuencia para recrear manualmente la demostración "Apple" y luego prueba con tus propios ejemplos!

1. Crea los Ingredientes

bash
new Color Shape Taste
new Red Round Sweet


2. Crea las Propiedades "Vinculadas" (El Pegamento)

bash
bind P1 Color Red
bind P2 Shape Round
bind P3 Taste Sweet


(Nota: P1, P2, P3 son solo nombres temporales para "Propiedad 1", etc.)

3. Construye el Objeto

bash
add Apple P1 P2 P3


4. El Gran Finale (Haz la pregunta)

bash
query Apple Color

Debería responder: RED


5. Prueba otra consulta para ver si funciona:

bash
query Apple Shape

Debería responder: ROUND

Puedes probar la ecuación clásica de PLN
new King Man Woman Queen
# En HRR, la resta es más difícil de visualizar, pero podemos probar la Vinculación
bind K King Man
query K King
# Esto es un poco abstracto para este script en particular, ¡mantente en la receta de Apple primero!

Hechos
1. "¿Funciona como una AGI?" Sí y No. Sí: Resuelve la parte más difícil de la AGI: el Razonamiento. Las Redes Neuronales normales (como GPT) se basan en la probabilidad (adivinar). Este motor se basa en el Álgebra (matemáticas). Si le enseñas que A > B y B > C, sabrá que A > C. No adivina; calcula. No: No es un cerebro completo. No tiene "Conciencia" ni "Agencia". Es simplemente una calculadora lógica muy avanzada. Piensa en ella como el Hemisferio Izquierdo del cerebro (Lógica/Matemáticas), mientras que ChatGPT es el Hemisferio Derecho (Creatividad/Lenguaje).
2. "¿No puede chatear?".
El Motor Lógico es mudo.
No genera oraciones como "La manzana es roja".
Genera un Vector (una lista de 2048 números).
Debes escribir código para traducir ese vector de vuelta a una palabra ("RED").
No puede escribir un poema, contar un chiste o mantener una conversación. Solo responde consultas lógicas específicas.
3. "¿Olvido Catastrófico?
"Esta es la mejor parte:
NO sufre de Olvido Catastrófico de la manera en que lo hace la IA normal.
La analogía "Pizarra vs. Mochila":
IA Normal (Red Neuronal): Funciona como una Pizarra. Para aprender algo nuevo, a menudo tienes que borrar (sobregrabar) un poco de lo viejo. Si aprendes demasiado, borras tu propio nombre. Esto es el Olvido Catastrófico.
Motor Lógico (HRR): Funciona como una Mochila. Para aprender algo nuevo, solo lo Agregas a la pila ($Knowledge = Fact1 + Fact2$).
Agregar Fact3 no borra Fact1. Coexisten en superposición.
El Límite: No "olvida", pero puede llenarse. Si metes 1,000 elementos en la mochila, se vuelve un lío y no puedes encontrar nada (esto se llama "Ruido" o "Saturación").

Característica,Red Neuronal (IA Estándar),Motor Lógico (Artefacto #3)
Razonamiento,❌ Débil (Alucinaciones),✅ Perfecto (Algebraico)
Chateo,✅ Excelente (Fluido),❌ Imposible (Solo vectores)
Memoria,❌ Se sobrescribe a sí misma (Olvida),✅ Apila (No olvida)
