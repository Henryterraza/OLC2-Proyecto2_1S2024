
## Conversion de entero a float
```
.data
    float1: .float 1.2
    float2: .float 2.5
    result: .float 0.0
    integer: .word 5  # Valor entero a sumar

.text
.global start

start:
    # Cargar el primer valor de punto flotante en f0
    flw f0, float1, t0   # Cargar de la memoria
    flw f1, float2, t0   # Cargar de la memoria
    
    # Sumar los dos valores flotantes
    fadd.s f2, f0, f1
    
    # Guardar el resultado en memoria
    fsw f2, result, t0   
    
    # Cargar el resultado de punto flotante en f0
    flw f0, result, t0   # Cargar de la memoria
    
    # Cargar el valor entero en un registro
   # Cargar de la memoria
    lw t1, integer

    
    # Convertir el valor entero a punto flotante
    fcvt.s.w f4, t1          # Convertir el valor entero a flotante
    

    # Sumar el valor entero al resultado de la suma de los valores flotantes
    fadd.s f2, f0, f4
    
    # Guardar el resultado en memoria
    fsw f2, result, t0   
    
    # Imprimir el resultado de punto flotante
    flw fa0, result, t0
    li a7, 2            # Imprimir un número de punto flotante en stdout
    ecall
    
    # Salir del programa
    li a0, 0            # Salir del programa con código de estado 0 (éxito)
    li a7, 93
    ecall

```




## Leet caracter por caracter 
```
.data
hola: .string "Hola"  # Include a newline character (\n) at the end

.text
.globl _start
_start:
    # Load the address of the "hola" string into register a0
    la t0, hola
    
print_loop:
    lb t1, 0(t0)    # Load the byte at the address pointed by t0
    beqz t1, exit   # If t1 is 0 (end of string), exit the loop
    
    mv a0, t1       # Move the character to be printed to a0
    li a7, 11       # Set system call number for printing character
    ecall  
    
    
    li a0, 10
    li a7, 11
    ecall
             
                      
                               
                                                 # Print the character
    addi t0, t0, 1  # Move to the next character
    j print_loop    # Repeat the loop
    
exit:
    # Terminate the program
    li a0, 0    # Set system call number for exit
    li a7, 10   # Set system call number for exit
    ecall       # Exit the program

```





## Combinacion de dos strings
```
.data
msg_true: .asciz "true"
msg_false: .asciz "false"
msg_combined: .asciz 12   # Espacio para contener los dos mensajes

.text
.global main

main:
    # Cargar la dirección de inicio de msg_true en a0
    la a0, msg_true
    # Cargar la dirección de inicio de msg_false en a1
    la a1, msg_false
    # Cargar la dirección de inicio de msg_combined en a2
    la a2, msg_combined

copy_loop:
    # Cargar un byte de msg_true y almacenarlo en msg_combined
    lb t0, 0(a0)
    sb t0, 0(a2)
    # Comprobar si se ha llegado al final de msg_true
    beqz t0, check_false
    # Incrementar los punteros de origen y destino
    addi a0, a0, 1
    addi a2, a2, 1
    # Repetir el bucle si no se ha llegado al final de msg_true
    j copy_loop

check_false:
    # Cargar un byte de msg_false y almacenarlo en msg_combined
    lb t0, 0(a1)
    sb t0, 0(a2)
    # Incrementar los punteros de origen y destino
    addi a1, a1, 1
    addi a2, a2, 1
    # Comprobar si se ha llegado al final de msg_false
    beqz t0, end_copy
    # Repetir el bucle si no se ha llegado al final de msg_false
    j check_false

end_copy:
    # Añadir un carácter nulo al final de msg_combined
    li t0, 0
    sb t0, 0(a2)
    

    # Fin del programa
    la a0, msg_combined      # Exit status
    li a7, 4
    ecall          # Realizar la llamada al sistema para salir del programa
    

    # Fin del programa
    li a0, 0       # Exit status
    li a7, 93
    ecall          # Realizar la llamada al sistema para salir del programa


```




## Imprimir true o false

```
.data
msg_true: .asciz "true"
msg_false: .asciz "false"

.text
.global main

main:
    
    
    
    li a0, 1      # Carga 1 en el registro a0
    beqz a0, L1  # Salta a print_false si a0 es igual a 0
    la a0, msg_true   # Carga la dirección de msg_true en a0
    li a7, 4        # Carga el número del sistema de llamada para imprimir en a7 (4 para imprimir cadena)
    ecall
    j L2
              # Llama al sistema# Si no se ha saltado, entonces a0 es 1:

L1:
    la a0, msg_false  # Carga la dirección de msg_false en a0
    li a7, 4        # Carga el número del sistema de llamada para imprimir en a7 (4 para imprimir cadena)
    ecall           # Llama al sistema
L2:



end_program:
    li a7, 10       # Carga el número del sistema de llamada para salir en a7 (10 para salir del programa)
    ecall           # Llama al sistema 
     
```


## guardar exp a variable
```
.data
i1: .word 0
i2: .word 1
f1: .word 0x0
flo2: .word 0x40200000
sp1: .asciz ""
s2: .asciz "Hola mundo"
c: .byte 99
b1: .word 0
b2: .word 1

.text
.globl _start
_start:
	li t0, 4
	li t3, 268435460
	sw t0, 0(t3)
	
	
	li t3, 268435460
	lw t1, 0(t3)
	
	la t0, i1
    #se guarda en variable
	sw t1, 0(t0)



    li t1, 2
	sw t1, 0(t0)
	la t0, b1
	li t1, 0
	sw t1, 0(t0)
	la t0, sp1
	sb t1, 0(t0)
	addi t0, t0, 1
	li t1, 108
	sb t1, 0(t0)
	addi t0, t0, 1
	li t1, 97
	sb t1, 0(t0)
	addi t0, t0, 1
	li t1, 0
	sb t1, 0(t0)

	lw a0, i1
	li a7, 1
	ecall
	li a0, 10
	li a7, 11
	ecall

	lw a0, flo2
	li a7, 34
	ecall
	li a0, 10
	li a7, 11
	ecall

	lw a0, b1
	li a7, 1
	ecall
	li a0, 10
	li a7, 11
	ecall

	la a0, sp1
	li a7, 4
	ecall
	li a0, 10
	li a7, 11
	ecall

```

## Guardar en variable un valor flotante
```
.data
i1: .word 0
i2: .word 1
f1: .word 0x0
flo2: .word 0x40200000
sp1: .asciz ""
s2: .asciz "Hola mundo"
c: .byte 99
b1: .word 0
b2: .word 1

.text
.globl _start
_start:
	li t0, 4
	li t3, 268435460
	sw t0, 0(t3)
	
	
	li t3, 268435460
	lw t1, 0(t3)
	
	la t0, i1
    #se guarda en variable
	sw t1, 0(t0)



    li t1, 2
	sw t1, 0(t0)
	la t0, b1
	li t1, 0
	sw t1, 0(t0)
	la t0, sp1
	sb t1, 0(t0)
	addi t0, t0, 1
	li t1, 108
	sb t1, 0(t0)
	addi t0, t0, 1
	li t1, 97
	sb t1, 0(t0)
	addi t0, t0, 1
	li t1, 0
	sb t1, 0(t0)

	lw a0, i1
	li a7, 1
	ecall
	li a0, 10
	li a7, 11
	ecall

	lw a0, flo2
	li a7, 34
	ecall
	li a0, 10
	li a7, 11
	ecall

	lw a0, b1
	li a7, 1
	ecall
	li a0, 10
	li a7, 11
	ecall

	la a0, sp1
	li a7, 4
	ecall
	li a0, 10
	li a7, 11
	ecall

```
## Asignar nuevos valores a variables 
```
.data
msg_null: .asciz "null"
msg_false: .asciz "falsedsaf"
msg_true: .asciz "true"
numero: .word 0 

numeros: .word 4 
float: .float 1.8

floatt: .float 1.3

.text
.globl _start

_start:

### Agregando un primitivo numerico 
	li t0, 2
	la t1, numero
	sw t0, 0(t1)
	
	lw a0, numero
	li a7, 1
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
	
	
	flw f0, float, t0
	
	fsw f0, floatt, t0
	
	flw fa0, floatt, t0
	li a7, 2
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall


### Agregando un primitivo numerico 
	la t0, msg_null
	la t1, msg_false
	sw t1, 0(t0)
	
	lw a0, msg_null
	li a7, 4
	ecall
	
	li a0, 10
	li a7, 11
	ecall


### Agregando un primitivo numerico 
	la t0, numero
	lw t1, numeros
	sw t1, 0(t0)
	
	lw a0, numero
	li a7, 1
	ecall





	li a0, 0
	li a7, 93
	ecall
```