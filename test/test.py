import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_reg(dut):
    # Iniciar reloj
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Aplicar reset y asegurarse que ena esté activo
    dut.rst_n.value  = 0
    dut.ena.value    = 1    # ← activar alimentación del diseño
    dut.ui_in.value  = 0
    dut.uio_in.value = 0

    for _ in range(5):
        await RisingEdge(dut.clk)

    # Liberar reset
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # Aplicar dato y habilitación
    dut.ui_in.value  = 0b10101010
    dut.uio_in.value = 0b00000001   # uio[0] = en = 1

    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")

    assert dut.uo_out.value.to_unsigned() == 0b10101010, \
        f"Se esperaba 0xAA, se obtuvo {dut.uo_out.value}"
        