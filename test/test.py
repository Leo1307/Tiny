import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_reg(dut):

    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    # ---------- Caso 1 ----------
    dut.ui_in.value = 0b10101010
    dut.uio_in.value = 0b00000001  # en = 1

    await RisingEdge(dut.clk)   # aquí se captura
    await Timer(1, units="ns")  # deja que se estabilice

    assert dut.uo_out.value.integer == 0b10101010, "No cargó con enable"

    # ---------- Caso 2 ----------
    dut.ui_in.value = 0b11111111
    dut.uio_in.value = 0b00000000  # en = 0

    await RisingEdge(dut.clk)
    await Timer(1, units="ns")

    assert dut.uo_out.value.integer == 0b10101010, "No mantuvo valor"