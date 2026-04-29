import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_reg(dut):

    # Clock
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # Caso 1: enable activo → carga dato
    dut.ui_in.value = 0b10101010
    dut.uio_in.value = 1  # en = 1
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0b10101010, "No cargó con enable"

    # Caso 2: enable inactivo → mantiene valor
    dut.ui_in.value = 0b11111111
    dut.uio_in.value = 0  # en = 0
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0b10101010, "No mantuvo valor"