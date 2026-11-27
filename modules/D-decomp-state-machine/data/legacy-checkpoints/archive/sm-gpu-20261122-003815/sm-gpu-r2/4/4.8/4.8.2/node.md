# N144: Apple M3 Ultra 统一内存带宽参数：M3 Ultra (Mac Studio) 统一内存带宽为 819 GB/s，与 RTX 4090 (1008 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

Apple M3 Ultra 统一内存带宽参数：M3 Ultra (Mac Studio) 统一内存带宽为 819 GB/s，与 RTX 4090 (1008 GB/s) 相当，但受限于 CPU-GPU 共享带宽，实际 LLM 推理有效带宽可能降至 60-70% (约 500-570 GB/s) [待核验]。

## Corrected Claim

Apple M3 Ultra 统一内存带宽参数：M3 Ultra (Mac Studio) 统一内存带宽为 819 GB/s，与 RTX 4090 (1008 GB/s) 相当，但受限于 CPU-GPU 共享带宽，实际 LLM 推理有效带宽通常低于峰值，具体数值取决于负载特征。

## Evidence

[质询]「实际 LLM 推理有效带宽可能降至 60-70%」这一具体数值范围缺乏通用物理定律或第一性原理支持，属于高度依赖具体负载、内存访问模式及系统调度的经验性估计，且不同场景下波动极大，该具体百分比区间可能不准确或过于绝对。 | 先验知识/题面给定，逻辑校验通过：M3 Ultra 819 GB/s 带宽及与 RTX 4090 对比符合已知硬件规格；但 60-70% 有效带宽为经验估计，非严格推导，故降级。

## Search Query

Apple M3 Ultra memory bandwidth effective LLM inference throughput
