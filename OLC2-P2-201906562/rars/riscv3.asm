.data
msg_null: .asciz "null"
msg_false: .asciz "false"
msg_true: .asciz "true"
str_1: .string "Negacion unaria" 
str_1.typeof: .string "String" 
str_2: .string "Igualdad" 
str_2.typeof: .string "String" 
str_3: .string "Desigualdad" 
str_3.typeof: .string "String" 
str_4: .string "Mayorque" 
str_4.typeof: .string "String" 
str_5: .string "Menorque" 
str_5.typeof: .string "String" 
str_6: .string "Mayor igual que" 
str_6.typeof: .string "String" 
str_7: .string "Menor igual que" 
str_7.typeof: .string "String" 
str_8: .string "Negacion logica" 
str_8.typeof: .string "String" 
str_9: .string "AND" 
str_9.typeof: .string "String" 

.text
.globl _start

_start:
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_1
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435460
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435464
	sw t0, 0(t3)

### Realizando operacion 
	li t3, 268435460
	lw t1, 0(t3)
	li t3, 268435464
	lw t2, 0(t3)
### Impriendo el valor 

	la a0, msg_null
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_2
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435472
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435476
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435472
	lw t1, 0(t3)
	li t3, 268435476
	lw t2, 0(t3)

### Se verifica si es igual 
	beq t1, t2, L0
	li t0, 0
	li t3, 268435480
	sw t0, 0(t3)
	j L1
L0:
	li t0, 1
	li t3, 268435480
	sw t0, 0(t3)
L1:
### Impriendo el valor 

	li t3, 268435480
	lw a0, 0(t3)
	beqz a0, L2
	la a0, msg_true
	li a7, 4
	ecall
	j L3
L2:
	la a0, msg_false
	li a7, 4
	ecall
L3:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_3
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435484
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435488
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435484
	lw t1, 0(t3)
	li t3, 268435488
	lw t2, 0(t3)

### Se verifica si no es igual 
	bne t1, t2, L4
	li t0, 0
	li t3, 268435492
	sw t0, 0(t3)
	j L5
L4:
	li t0, 1
	li t3, 268435492
	sw t0, 0(t3)
L5:
### Impriendo el valor 

	li t3, 268435492
	lw a0, 0(t3)
	beqz a0, L6
	la a0, msg_true
	li a7, 4
	ecall
	j L7
L6:
	la a0, msg_false
	li a7, 4
	ecall
L7:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_4
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435496
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 20
	li t3, 268435500
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435496
	lw t1, 0(t3)
	li t3, 268435500
	lw t2, 0(t3)

### Se verifica si es mayor 
	bgt t1, t2, L8
	li t0, 0
	li t3, 268435504
	sw t0, 0(t3)
	j L9
L8:
	li t0, 1
	li t3, 268435504
	sw t0, 0(t3)
L9:
### Impriendo el valor 

	li t3, 268435504
	lw a0, 0(t3)
	beqz a0, L10
	la a0, msg_true
	li a7, 4
	ecall
	j L11
L10:
	la a0, msg_false
	li a7, 4
	ecall
L11:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_5
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435508
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 20
	li t3, 268435512
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435508
	lw t1, 0(t3)
	li t3, 268435512
	lw t2, 0(t3)

### Se verifica si es menor 
	blt t1, t2, L12
	li t0, 0
	li t3, 268435516
	sw t0, 0(t3)
	j L13
L12:
	li t0, 1
	li t3, 268435516
	sw t0, 0(t3)
L13:
### Impriendo el valor 

	li t3, 268435516
	lw a0, 0(t3)
	beqz a0, L14
	la a0, msg_true
	li a7, 4
	ecall
	j L15
L14:
	la a0, msg_false
	li a7, 4
	ecall
L15:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_6
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435520
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 9
	li t3, 268435524
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435520
	lw t1, 0(t3)
	li t3, 268435524
	lw t2, 0(t3)

### Se verifica si es mayor o igual 
	bge t1, t2, L16
	li t0, 0
	li t3, 268435528
	sw t0, 0(t3)
	j L17
L16:
	li t0, 1
	li t3, 268435528
	sw t0, 0(t3)
L17:
### Impriendo el valor 

	li t3, 268435528
	lw a0, 0(t3)
	beqz a0, L18
	la a0, msg_true
	li a7, 4
	ecall
	j L19
L18:
	la a0, msg_false
	li a7, 4
	ecall
L19:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_7
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435532
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 9
	li t3, 268435536
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435532
	lw t1, 0(t3)
	li t3, 268435536
	lw t2, 0(t3)

### Se verifica si es menoro igual 
	ble t1, t2, L20
	li t0, 0
	li t3, 268435540
	sw t0, 0(t3)
	j L21
L20:
	li t0, 1
	li t3, 268435540
	sw t0, 0(t3)
L21:
### Impriendo el valor 

	li t3, 268435540
	lw a0, 0(t3)
	beqz a0, L22
	la a0, msg_true
	li a7, 4
	ecall
	j L23
L22:
	la a0, msg_false
	li a7, 4
	ecall
L23:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_8
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435548
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435552
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435548
	lw t1, 0(t3)
	li t3, 268435552
	lw t2, 0(t3)

### Se verifica si es igual 
	beq t1, t2, L24
	li t0, 0
	li t3, 268435556
	sw t0, 0(t3)
	j L25
L24:
	li t0, 1
	li t3, 268435556
	sw t0, 0(t3)
L25:
	li t0, 268435556
	lw t1, 0(t0)
### Operacion condicional 
	seqz t0, t1
	li t3, 268435544
	sw t0, 0(t3)
### Impriendo el valor 

	li t3, 268435544
	lw a0, 0(t3)
	beqz a0, L26
	la a0, msg_true
	li a7, 4
	ecall
	j L27
L26:
	la a0, msg_false
	li a7, 4
	ecall
L27:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall
### Agregando un primitivo numerico 
### Impriendo el valor 

	la a0, str_9
	li a7, 4
	ecall
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435560
	sw t0, 0(t3)

### Agregando un primitivo numerico 
	li t0, 10
	li t3, 268435564
	sw t0, 0(t3)
### Agregando valor booleano 
	li t3, 268435560
	lw t1, 0(t3)
	li t3, 268435564
	lw t2, 0(t3)

### Se verifica si es igual 
	beq t1, t2, L28
	li t0, 0
	li t3, 268435568
	sw t0, 0(t3)
	j L29
L28:
	li t0, 1
	li t3, 268435568
	sw t0, 0(t3)
L29:
### Impriendo el valor 

	li t3, 268435568
	lw a0, 0(t3)
	beqz a0, L30
	la a0, msg_true
	li a7, 4
	ecall
	j L.final
L30:
	la a0, msg_false
	li a7, 4
	ecall
L.final:
### Salto de linea 

	li a0, 10
	li a7, 11
	ecall

	li a0, 0
	li a7, 93
	ecall
