
`default_nettype none
module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
  
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, 1'b0};

  assign uio_oe[0] = 1'b0;


  reg_pp_8b_en_ar U0(
    .clk_i    (clk),
    .rst_n_i  (rst_n),
    .d_i      (ui_in[7:0]),
    .en_i     (1'b1),
    .q_o      (uo_out[7:0])
  );


endmodule
