`timescale 1ns/1ps
module Counter_tb();
    reg clk, reset;
    wire [3:0] count;

    Counter uut(clk, reset, count);

    initial begin
        clk = 0;
        forever #5 clk = ~clk; // 10ns clock
    end

    initial begin
        reset = 1; #10;
        reset = 0; #100;
        $finish;
    end
endmodule
