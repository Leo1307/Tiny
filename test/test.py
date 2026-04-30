import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_reg(dut):
    # Iniciar reloj de 10ns (100 MHz)
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Aplicar reset asíncrono por VARIOS ciclos para limpiar los X
    dut.rst_n.value  = 0
    dut.ui_in.value  = 0
    dut.uio_in.value = 0

    for _ in range(5):                  # ← mantener reset 5 ciclos
        await RisingEdge(dut.clk)

    # Liberar reset
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)          # esperar que el reset se propague

    # Aplicar dato y habilitación
    dut.ui_in.value  = 0b10101010
    dut.uio_in.value = 0b00000001      # uio[0] = en = 1

    await RisingEdge(dut.clk)          # el registro captura d_i en este flanco
    await Timer(1, unit="ns")          # pequeño delta para estabilizar

    assert dut.uo_out.value.to_unsigned() == 0b10101010, \
        f"Se esperaba 0xAA, se obtuvo {dut.uo_out.value}"