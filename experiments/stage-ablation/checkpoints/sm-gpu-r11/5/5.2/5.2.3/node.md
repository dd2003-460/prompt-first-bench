# N259: Qwen3-27B 在 32K 上下文长度下的 Perplexity 增量公式：ΔPPL = PPL_W4_32K - PPL_INT8_32K，其中 PPL 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Qwen3-27B 在 32K 上下文长度下的 Perplexity 增量公式：ΔPPL = PPL_W4_32K - PPL_INT8_32K，其中 PPL 需在 WikiText-103 或 C4 数据集的长文本子集上计算，需对比 W4 与 INT8 在 4K/8K/16K/32K 四个长度点的 PPL 曲线斜率差异。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下的 Perplexity 增量公式：ΔPPL = PPL_W4_32K - PPL_INT8_32K，其中 PPL 需在 WikiText-103 或 C4 数据集的长文本子集上计算，需对比 W4 与 INT8 在 4K/8K/16K/32K 四个长度点的 PPL 曲线斜率差异。

## Evidence

先验知识/题面给定，逻辑校验通过
