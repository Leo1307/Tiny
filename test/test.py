import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_reg(dut):
    # Iniciar reloj de 10ns (100 MHz)
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Aplicar reset asíncrono
    dut.rst_n.value   = 0
    dut.ui_in.value   = 0
    dut.uio_in.value  = 0
    await RisingEdge(dut.clk)   # dejar que el reset se estabilice

    # Liberar reset, colocar dato y habilitación
    dut.rst_n.value   = 1
    dut.ui_in.value   = 0b10101010
    dut.uio_in.value  = 0b00000001  # uio[0] = en = 1

    await RisingEdge(dut.clk)   # ✅ el registro captura d_i en este flanco
    await Timer(1, units="ns")  # pequeño delta para que se estabilice

    assert dut.uo_out.value.to_unsigned() == 0b10101010, \
        f"Se esperaba 0xAA, se obtuvo {dut.uo_out.value.to_unsigned():#04x}"