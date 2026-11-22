# N27: 条件性推荐框架需定义三个关键阈值：1) 预算上限 B (如 <$3000 仅限消费卡或 Mac, >$10000 可考虑数据中心卡)；2) 延迟容忍度 T_ma

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

条件性推荐框架需定义三个关键阈值：1) 预算上限 B (如 <$3000 仅限消费卡或 Mac, >$10000 可考虑数据中心卡)；2) 延迟容忍度 T_max (如 >5s/token 可用 4090, <1s/token 需 H100 或多卡)；3) 质量损失阈值 ΔQ (如 perplexity 增加 <0.1 可接受 FP8, <0.05 需 BF16)。

## Corrected Claim

条件性推荐框架需定义三个关键阈值：1) 预算上限 B (如 <$3000 仅限消费卡或 Mac, >$10000 可考虑数据中心卡)；2) 延迟容忍度 T_max (如 >5s/token 可用 4090, <1s/token 需 H100 或多卡)；3) 质量损失阈值 ΔQ (如 perplexity 增加 <0.1 可接受 FP8, <0.05 需 BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM quantization quality loss perplexity threshold FP8 BF16
