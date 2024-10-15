DATA SEGMENT USE16
BLANKLINE DB 13, 10, '$' ;ascii chara 13 and 10 carriage return and line feed respectively
MESG DB'Hello world!', '$'
MESG2 DB'should be line 2', '$'
MESG3 DB'should be line 3', '$'
DATA ENDS

CODE SEGMENT USE16
    ASSUME CS:CODE,DS:DATA
BEG: ;start begging the pc to work
    MOV AX,DATA ;loads up AX value for data segment
    MOV DS,AX ;moves ax into segement reg DS allows access to variables

    MOV AH,9 ;calls dos function 9 to print to screen
    MOV DX, OFFSET MESG ;loads address of MESG tp register
    INT 21H ;execute dos interupt 21H executing function 9

    MOV AH,9
    MOV DX, OFFSET BLANKLINE ; printing blank line
    INT 21H

    MOV AH,9
    MOV DX, OFFSET MESG2
    INT 21H

    MOV AH,9
    MOV DX, OFFSET BLANKLINE
    INT 21H

    MOV AH,9
    MOV DX, OFFSET MESG3
    INT 21H

    MOV AH,4CH ;DOS FUNCTION 4C exiting programme
    INT 21H ;EXECUTE the execute
CODE ENDS ;end of code segemnt
END BEG ; we can stop begging the pc to work now