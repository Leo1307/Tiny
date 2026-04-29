<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

El diseño implementa un registro de 8 bits con señal de habilitación (`en`).
Las entradas `d0` a `d7` representan el dato de entrada.
Cuando la señal `en` está activa, el valor de las entradas se almacena en el registro interno.
Las salidas `q0` a `q7` reflejan el valor almacenado.

Si `en` está inactiva, el registro mantiene su valor previo.


## How to test

1. Colocar un valor binario en las entradas `d0–d7`.
2. Activar la señal `en`.
3. Verificar que las salidas `q0–q7` coinciden con las entradas.
4. Cambiar las entradas sin activar `en` y comprobar que la salida no cambia.
5. Volver a activar `en` y verificar que el nuevo valor se carga correctamente.


## External hardware

No se requiere hardware externo.
