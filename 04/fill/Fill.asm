// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

        @8192   // (512 * 32) / 16
        D=A
        @count
        M=D     // count = 8192 (no. of bytes)
(LOOP)
        @index
        M=0     // index = 0
(INNER)
        @KBD
        D=M
        @BLACK
        D;JNE   // goto BLACK if KBD value is not 0
(WHITE)
        @index
        D=M
        @SCREEN
        A=A+D   // Calculate byte address
        M=0     // White fill
        @END
        0;JMP   // goto END
(BLACK)
        @index
        D=M
        @SCREEN
        A=A+D   // Calculate byte address
        M=-1    // Black fill
(END)   
        @index
        MD=M+1  // index++
        @count
        D=D-M
        @LOOP
        D;JEQ   // goto LOOP if count - index == 0
        @INNER
        0;JMP   // goto INNER


