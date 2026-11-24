# N424: DRAM 静态刷新功耗修正：基于 JEDEC DDR4 规范，单 rank 刷新电流典型值为 20-40mA @ 1.2V，而非 50-100mA。对于 NVM

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N186

## Claim

DRAM 静态刷新功耗修正：基于 JEDEC DDR4 规范，单 rank 刷新电流典型值为 20-40mA @ 1.2V，而非 50-100mA。对于 NVMe 控制器内置的 8GB DRAM 缓存（通常 4 个 rank），静态刷新功耗 P_static_refresh = 4 ranks * 0.03A * 1.2V ≈ 0.144W。此值应替换 N186 中 0.06-0.12W 的低估区间，作为基础底噪。

## Corrected Claim

DRAM 静态刷新功耗修正：基于 JEDEC DDR4 规范，单 rank 刷新电流典型值约为 10-20mA @ 1.2V。对于 NVMe 控制器内置的 8GB DRAM 缓存（假设 4 个 rank），静态刷新功耗 P_static_refresh 估算范围约为 0.048W - 0.096W。此值可作为基础底噪参考，具体数值需依据实际 DRAM 颗粒规格调整。

## Evidence

[质询]数值量级存疑：JEDEC DDR4 规范中 I_RR (Refresh Current) 的典型值通常在 10-20mA 左右（取决于密度和速度），20-40mA 的上限偏高；此外，NVMe 控制器内置 DRAM 通常采用 LPDDR 或嵌入式封装，其刷新机制和功耗特性与标准 DDR4 DIMM 存在差异，直接套用 DDR4 规范可能不准确。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值处于 JEDEC 典型范围边缘，无法确证）

## Search Query

JEDEC DDR4 refresh current per rank mA typical value
