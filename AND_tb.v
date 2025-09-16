`timescale 1ns/1ps
module AND_tb();
    reg A, B;
    wire Y;

    AND_gate uut(A, B, Y);

    initial begin
        $monitor("A=%b, B=%b, Y=%b", A, B, Y);
        A=0; B=0; #10;
        A=0; B=1; #10;
        A=1; B=0; #10;
        A=1; B=1; #10;
        $finish;
    end
endmodule
