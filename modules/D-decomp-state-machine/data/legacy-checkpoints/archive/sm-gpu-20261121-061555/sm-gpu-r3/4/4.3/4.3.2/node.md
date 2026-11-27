# N96: Dequantize开销的量化估算公式：额外延迟 T_dequant = (Model_Size_Bytes * (1/Precision_Ratio - 1)

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Dequantize开销的量化估算公式：额外延迟 T_dequant = (Model_Size_Bytes * (1/Precision_Ratio - 1)) / Memory_Bandwidth_Effective；对于RTX 4090 (1008 GB/s) 运行 Qwen3-27B INT4 (13.5GB)，理论计算延迟约为 13.5/1008 ≈ 0.0134s/token，但Dequantize路径通常导致有效带宽降至 800-900 GB/s，实际延迟增加约 10-20%。

## Corrected Claim

Dequantize开销主要源于计算单元执行反量化指令（如位运算、LUT查找）的延迟，而非单纯由内存带宽降低导致。对于RTX 4090运行Qwen3-27B INT4，实际推理延迟的增加取决于GPU计算单元对INT4反量化指令的优化程度及内存访问模式，通常比FP16推理增加10-30%不等，具体数值需实测，不能简单通过带宽公式估算。

## Evidence

[质询]公式逻辑存在严重缺陷：Dequantize（反量化）的额外开销通常源于计算单元（ALU）执行位操作或查表（LUT）的指令延迟，而非单纯由内存带宽降低导致。将额外延迟完全归因于带宽从1008降至800-900 GB/s（仅约10-20%的带宽损失）在物理上是不充分的，因为INT4反量化涉及大量的非内存密集型计算指令，其瓶颈往往在计算吞吐而非内存带宽。此外，'13.5GB'是模型总大小，而非单token处理的数据量，直接用总大小除以带宽得到'每token延迟'在量纲和逻辑上均不成立（除非隐含假设每token需读取整个模型，但这与推理机制不符，且未明确说明）。 | 先验知识/题面给定，逻辑校验未通过：公式混淆了计算开销与带宽开销，且量纲推导（总模型大小/带宽=单token延迟）缺乏前提支撑，存在内部逻辑矛盾。
