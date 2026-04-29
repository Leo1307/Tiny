/*
* Instituto Tecnológico de Costa Rica
* Prof. Dr.-ing. Pablo Mendoza Ponce
* Rev. 1 28 July 2024
*/

`timescale 1ns/1ps
module reg_pp_8b_en_ar(
  input logic         clk_i,
  input logic         rst_n_i,
  input logic [7:0]   d_i,
  input logic         en_i,
  output logic [7:0]  q_o);
  
  // Registro de 8 bits con habilitación y reset asíncrono activo bajo
  always_ff @(posedge clk_i) begin
    if (!rst_n_i) begin
      q_o <= '0;          // Reset síncrono
    end else if (en_i) begin
      q_o <= d_i;
  end
end
  
endmodule