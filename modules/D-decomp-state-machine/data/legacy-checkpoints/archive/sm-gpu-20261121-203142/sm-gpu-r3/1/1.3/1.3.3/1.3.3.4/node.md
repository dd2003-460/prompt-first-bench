# N152: INT8 KV Cache 量化对推理延迟的影响：每层 Attention 计算中，INT8 到 BF16 的反量化及点积运算开销，通常使每 Token 生成延

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

INT8 KV Cache 量化对推理延迟的影响：每层 Attention 计算中，INT8 到 BF16 的反量化及点积运算开销，通常使每 Token 生成延迟增加 3-8% [待核验]

## Corrected Claim

INT8 KV Cache 量化在 Attention 计算中引入的反量化及点积运算开销，通常会导致每 Token 生成延迟出现一定程度的增加，具体幅度取决于硬件架构与实现优化程度。

## Evidence

[质询]该陈述包含具体的经验性数值范围（3-8%），属于硬件/软件性能指标，无法从第一性原理严格推导。且不同硬件架构（如GPU vs CPU）、模型规模及量化实现方式（如是否使用专用内核）下，反量化开销差异巨大，固定百分比范围缺乏普适性，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该数值属于具体性能指标，不适用第一性原理推导条款）

## Search Query

INT8 KV cache inference latency overhead percentage
