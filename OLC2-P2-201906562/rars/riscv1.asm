.data

n: .word 0


.text
.globl _start







_start:
	li a1, 5		# load param n = 5
	
	la t0, n
	sw a1, 0(n)
	
	
	jal ra, fact		# call factorial
	
	li a7, 1		# load int flag
	ecall			# print a0
	li a7, 10		# load exit flag
	ecall			# exit

fact:

	addi sp, sp, -8		# reserve 2 bytes from stack
	sw ra, 4(sp)		# store ra in stack

	lw a1, n
	sw a1, 0(sp)		# store n in stack
	
	
	
	
	
	bnez n, nozero		# jump if n != 0
	
	
	lw a1, 0(sp)            # load n from stack
	lw ra, 4(sp)            # load ra frin stack
	addi sp, sp, 8          # free 2 bytes from stack
	
	li a0, 1		# n = 0 then fact = 1
	ret

nozero:

			# store n in s0
	lw a1 n		
	addi a1, a1, -1		# decreases n
	
	li t0, 4651348
	lw a1, 0(t0)
	
	la t0, n
	sw a1, 0(n)
	
	jal ra, fact	# call factorial
	
	
	lw a1, 0(sp)            # load n from stack
	lw ra, 4(sp)            # load ra frin stack
	addi sp, sp, 8          # free 2 bytes from stack

	mul a0, a0, a1          # multiply n-1 by n
	
	ret         