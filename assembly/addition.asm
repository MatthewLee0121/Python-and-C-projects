DATA SEGMENT USE16
NEXTLINE DB 13, 10, '$'
NUM1 DB 5
NUM2 DB 6 ;changed to 6 so answer is 11
RESULT DB 0
OUTPUT DB 'result of num1 + num2 = $'
DATA ENDS

CODE SEGMENT USE16
    ASSUME CS:CODE,DS:DATA

BEG: ;start to beg this pc to work
    MOV AX, DATA ;move registery ax to data stream
    MOV DS, AX

    MOV AL, NUM1 ;moves num1 into al registery
    ADD AL, NUM2 ;adds value of num2 to the al registery value
    ADD AL, '0' ;adds a 0 to al registery
    MOV RESULT, AH ;moves al value onto the end of result value

    MOV AH, 9
    LEA DX, OUTPUT
    INT 21H

    MOV DL, RESULT
    MOV AH, 2
    INT 21H

    MOV AH, 9
    LEA DX, NEXTLINE
    INT 21H

    MOV AH, 4CH
    INT 21H
CODE ENDS
END BEG