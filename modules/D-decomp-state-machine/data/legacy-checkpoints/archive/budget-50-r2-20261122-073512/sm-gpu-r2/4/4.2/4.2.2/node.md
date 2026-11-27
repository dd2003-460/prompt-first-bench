# N149: P_auxiliary（辅助功耗）的量化计算：P_auxiliary = P_gpu × N_gpus × 0.15（15% 经验系数，涵盖 CPU、内存、风扇

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

P_auxiliary（辅助功耗）的量化计算：P_auxiliary = P_gpu × N_gpus × 0.15（15% 经验系数，涵盖 CPU、内存、风扇、主板）；例如 2× RTX 4090 方案：P_auxiliary = 450W × 2 × 0.15 = 135W；数据中心方案：P_auxiliary = 700W × 1 × 0.20 = 140W（20% 系数，因冗余电源和更多风扇）。

## Corrected Claim

P_auxiliary（辅助功耗）的量化计算：P_auxiliary = P_gpu × N_gpus × 0.15（15% 经验系数，涵盖 CPU、内存、风扇、主板）；例如 2× RTX 4090 方案：P_auxiliary = 450W × 2 × 0.15 = 135W；数据中心方案：P_auxiliary = 700W × 1 × 0.20 = 140W（20% 系数，因冗余电源和更多风扇）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU server auxiliary power consumption ratio CPU memory fans percentage
