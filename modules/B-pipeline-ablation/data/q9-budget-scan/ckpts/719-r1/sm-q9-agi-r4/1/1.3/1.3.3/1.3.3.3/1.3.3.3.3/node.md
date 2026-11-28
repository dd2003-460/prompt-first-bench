# N416: Roofline 分析结论：由于实际 AI (4) << Roofline 拐点 (139)，FP4 推理处于内存带宽受限区 (Memory-Bound)。反量

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

Roofline 分析结论：由于实际 AI (4) << Roofline 拐点 (139)，FP4 推理处于内存带宽受限区 (Memory-Bound)。反量化 kernel 的额外计算开销可忽略，瓶颈在于 HBM 读取速率。理论最大吞吐 T_max = Bandwidth / Weight_Size = 900e9 / 13.5e9 = 66.7 tokens/s (理论上限，未计 GEMM 效率)。

## Corrected Claim

Roofline 分析结论：由于实际 AI (4) << Roofline 拐点 (139)，FP4 推理处于内存带宽受限区 (Memory-Bound)。反量化 kernel 的额外计算开销可忽略，瓶颈在于 HBM 读取速率。理论最大吞吐 T_max = Bandwidth / Weight_Size = 900e9 / 13.5e9 = 66.7 tokens/s (理论上限，未计 GEMM 效率)。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（900/13.5=66.7），Roofline模型逻辑自洽（AI<拐点即为Memory-Bound），符合计算机体系结构基本原理。
