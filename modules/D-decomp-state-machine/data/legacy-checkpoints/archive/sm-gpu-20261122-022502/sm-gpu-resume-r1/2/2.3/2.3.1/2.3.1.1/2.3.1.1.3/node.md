# N615: 基于修正后的有效带宽（假设 400 GB/s）和 Qwen3-27B 的 FLOPs 估算，M2 Ultra 运行 INT4 的 Decode 吞吐理论上限约为

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N188, N189, N190

## Claim

基于修正后的有效带宽（假设 400 GB/s）和 Qwen3-27B 的 FLOPs 估算，M2 Ultra 运行 INT4 的 Decode 吞吐理论上限约为 400 GB/s / 14.5 GB * 60% (ALU overhead) ≈ 16-18 tokens/s，这与 N188 中提到的 20-30 tokens/s 实测区间下沿相符，确认其性能远低于 GPU 专用硬件。

## Corrected Claim

基于修正后的有效带宽（假设 400 GB/s）和 Qwen3-27B 的 FLOPs 估算，M2 Ultra 运行 INT4 的 Decode 吞吐理论上限约为 400 GB/s / 14.5 GB * 60% ≈ 16.5 tokens/s，该值低于 N188 中提到的 20-30 tokens/s 实测区间，表明理论估算较为保守或实际硬件效率高于此假设，但仍确认其性能远低于 GPU 专用硬件。

## Evidence

[质询]计算逻辑存在内部矛盾：400 GB/s / 14.5 GB ≈ 27.6 tokens/s，乘以 60% 后约为 16.5 tokens/s，这与陈述中给出的 '16-18 tokens/s' 区间基本吻合，但陈述声称该结果与 '20-30 tokens/s 实测区间下沿相符' 存在逻辑瑕疵。16.5 低于 20，严格来说不属于 20-30 区间的下沿，而是低于该区间。此外，'ALU overhead' 在 Decode 阶段（通常受内存带宽限制）的表述不够准确，Decode 主要瓶颈是内存带宽而非 ALU 计算，除非特指某些特定操作，但通常 Decode 吞吐估算主要依赖带宽除以模型大小，60% 的效率因子可能过于保守或定义模糊。 | 逻辑校验发现计算结果 16.5 tokens/s 低于声称相符的 20-30 tokens/s 区间下沿，存在内部矛盾；且 source 为 knowledge，但逻辑不自洽导致无法直接 verified。
