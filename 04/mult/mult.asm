// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	@R0
	D=M
	@ZERO
	D;JEQ		// if R0 is 0 jump to ZERO label

	@R1
	D=M
	@ZERO
	D;JEQ		// if R1 is 0 jump to ZERO label

	@R2
	M=0			// Ensure output is initialized to zero

	@cnt
	M=1			// set cnt=1

(LOOP)
	@cnt
	D=M 		// D=cnt

	@R1
	D=D-M		// D=cnt-R1
	
	@END
	D;JGT		// if (cnt-R1 > 0) jump to END

    @R0
    D=M 		// set D=R0

    @R2
    M=D+M 		// Actually multiply by R2=R0+R2

    @cnt
    M=M+1

	@LOOP
	0;JMP

(ZERO)
	@R2
	M=0			// set the result to zero. program came here because one of its operand is 0
	@END
	0;JMP

(END)
    @END
    0;JMP
