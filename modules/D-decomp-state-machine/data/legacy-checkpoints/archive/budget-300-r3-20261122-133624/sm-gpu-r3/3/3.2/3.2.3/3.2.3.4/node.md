# N268: 短文本 PPL（Perplexity）对长程 KV Cache 精度损失不敏感：在 WikiText-103（平均序列长度 ~512 tokens）上，INT8

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83, N84, N85

## Claim

短文本 PPL（Perplexity）对长程 KV Cache 精度损失不敏感：在 WikiText-103（平均序列长度 ~512 tokens）上，INT8 KV Cache 的 PPL 增量仅为 0.05±0.02，而 32K 长上下文下的 PPL 增量高达 0.8±0.3，表明 PPL 是短程指标，无法捕捉长程依赖退化

## Corrected Claim

短文本 PPL 对长程 KV Cache 精度损失不敏感：在 WikiText-103 等短文本基准上，INT8 KV Cache 的 PPL 增量通常较小，而在 32K 长上下文基准下 PPL 增量显著增大，表明 PPL 在短文本上难以捕捉长程依赖退化。

## Evidence

[质询]具体数值（0.05±0.02 和 0.8±0.3）属于特定实验条件下的经验数据，缺乏通用性，且不同模型、量化算法（如SmoothQuant, KVQuant）及硬件平台下结果差异巨大，直接引用具体数值作为普遍事实存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理推导，属于特定实验结果）

## Search Query

perplexity sensitivity to KV cache quantization short vs long context length
