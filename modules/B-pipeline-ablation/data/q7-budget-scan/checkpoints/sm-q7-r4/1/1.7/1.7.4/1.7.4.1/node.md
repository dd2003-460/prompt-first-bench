# N185: NVMe SSD Random Write 功耗分解：P_write_total = P_flash_program + P_dram_refresh + P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61, N62, N63

## Claim

NVMe SSD Random Write 功耗分解：P_write_total = P_flash_program + P_dram_refresh + P_ctrl_logic，其中 P_flash_program 受 NAND 类型（TLC/QLC）和 Page Program Latency 主导，7.68TB TLC 典型值约 15-18W，DRAM 刷新和控制器逻辑合计约 3-5W。

## Corrected Claim

NVMe SSD Random Write 功耗分解：P_write_total = P_flash_program + P_dram_refresh + P_ctrl_logic，其中 P_flash_program 受 NAND 类型（TLC/QLC）和 Page Program Latency 主导，7.68TB TLC 典型值约 15-18W，DRAM 刷新和控制器逻辑合计约 3-5W。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

enterprise NVMe SSD random write power consumption breakdown TLC QLC
