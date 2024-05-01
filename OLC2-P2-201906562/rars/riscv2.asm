.data
msg_null: .asciz "null"
msg_false: .asciz "false"
msg_true: .asciz "true"
str_1: .string "----------------------" 
str_1.typeof: .string "String" 
str_2: .string "----ARCHIVO BASICO----" 
str_2.typeof: .string "String" 
str_3: .string "--------16 pts--------" 
str_3.typeof: .string "String" 
str_4: .string "----------------------" 
str_4.typeof: .string "String" 
bol: .word 1 
bol.typeof: .string "boolean" 
bol2: .word 1 
bol2.typeof: .string "boolean" 
str_5: .string "imprimir" 
str_5.typeof: .string "String" 
cad1: .space 70 
cad1.typeof: .string "string" 
str_6: .string "cadena valida" 
str_6.typeof: .string "String" 
cad2: .space 70 
cad2.typeof: .string "string" 
val1: .word 0 
val1.typeof: .string "number" 
val2: .word 0 
val2.typeof: .string "number" 
val3: .word 0 
val3.typeof: .string "number" 
str_7: .string "El valor de val1 es:" 
str_7.typeof: .string "String" 
str_8: .string "El valor de val2 es:" 
str_8.typeof: .string "String" 
str_9: .string "El valor de val3 es:" 
str_9.typeof: .string "String" 
str_10: .string "El resultado de la operación es:" 
str_10.typeof: .string "String" 
str_11: .string "El valor de bol es:" 
str_11.typeof: .string "String" 
str_12: .string "El valor de cad1 es:" 
str_12.typeof: .string "String" 
str_13: .string "El valor de cad2 es:" 
str_13.typeof: .string "String" 
str_14: .string "El valor de bol2:" 
str_14.typeof: .string "String" 
a: .word 0 
a.typeof: .string "number" 
b: .word 0 
b.typeof: .string "number" 
c: .word 0 
c.typeof: .string "number" 
f: .word 1 
f.typeof: .string "boolean" 
j: .word 0 
j.typeof: .string "number" 
k: .word 0 
k.typeof: .string "number" 
val: .word 0 
val.typeof: .string "number" 
resp: .word 0 
resp.typeof: .string "number" 
valorVerdadero: .word 0 
valorVerdadero.typeof: .string "number" 
cop1: .word 0 
cop1.typeof: .string "number" 

flot: .float 6.3
flott: .float 3.1

.text
.globl _start

_start:
### Agregando un primitivo numerico 
### Impriendo el valor 

	flw f0, flot, t0
	flw f1, flott, t0
	
	fdiv.s f3, f0, f1
	
	fmv.s fa0, f3
	li a7, 2
	ecall 
	
	fcvt.s.w f3, t0
	
	
	li a0, 10
	li a7, 11
	ecall
	
	lw t0, 0(t0)
	
	mv a0, t0
	li a7, 1
	ecall 
	
	fcvt.w.s t0, f4
	
	fmul.s f4, f4, f1
	
	fsub.s f1, f3, f4
	
	
	

	
	li a0, 10
	li a7, 11
	ecall

	li a0, 0
	li a7, 93
	ecall
