# N178: LFU 在高更新率场景下的有效命中率 H_eff_LFU 的量化计算：H_eff_LFU = H_LFU * (1 - P_invalid_LFU)，其中 P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

LFU 在高更新率场景下的有效命中率 H_eff_LFU 的量化计算：H_eff_LFU = H_LFU * (1 - P_invalid_LFU)，其中 P_invalid_LFU = 1 - exp(-0.01 * T_resident_LFU)，若 T_resident_LFU = 7 天，则 P_invalid_LFU ≈ 6.7%，H_eff_LFU ≈ 0.933 * H_LFU，需对比 LRU 的折损系数以评估 LFU 的劣势。

## Corrected Claim

LFU 在高更新率场景下的有效命中率 H_eff_LFU 的量化计算：H_eff_LFU = H_LFU * (1 - P_invalid_LFU)，其中 P_invalid_LFU = 1 - exp(-0.01 * T_resident_LFU)，若 T_resident_LFU = 7 天，则 P_invalid_LFU ≈ 6.7%，H_eff_LFU ≈ 0.933 * H_LFU，需对比 LRU 的折损系数以评估 LFU 的劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：指数函数计算 1 - exp(-0.07) ≈ 0.0677 (6.8%)，与 6.7% 量级一致；乘法逻辑自洽。

## Search Query

LFU effective hit rate update rate impact
