# N656: RTX 5090 32GB 显存优势量化：32GB 显存允许 BF16 下运行 27B 模型 (27e9 * 2 bytes = 54GB > 32GB，仍不可

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N202

## Claim

RTX 5090 32GB 显存优势量化：32GB 显存允许 BF16 下运行 27B 模型 (27e9 * 2 bytes = 54GB > 32GB，仍不可行，需 FP8 或 INT8)。FP8 权重 = 27GB，KV Cache (32K, FP8) = 4.25GB，总 31.25GB，刚好装入 32GB。相比 4090 的 W4 量化，FP8 质量损失更小 (PERPLEXITY 增加 <0.5 vs W4 的 1.5-2.0)。

## Corrected Claim

RTX 5090 32GB 显存允许在 BF16 下运行 27B 模型（27e9 * 2 bytes = 54GB > 32GB，不可行，需 FP8 或 INT8）。以 FP8 为例，权重约 27GB，若 KV Cache（32K 上下文，FP8）约为 4.25GB，总占用约 31.25GB，可装入 32GB 显存。相比 4090 常见的 W4 量化，FP8 通常具有更小的质量损失（具体 Perplexity 增加幅度依模型和基准而定，通常 FP8 优于 W4）。

## Evidence

[质询]KV Cache 4.25GB 的数值缺乏具体模型架构参数（如层数、头数、头维度）支持，属于经验估算值，且不同模型（如 Llama 3 27B 与 Mistral 27B）的 KV Cache 大小差异显著，直接断言为 4.25GB 存在精度风险；此外，FP8 与 W4 的 Perplexity 对比数据（<0.5 vs 1.5-2.0）也是特定基准下的经验值，非绝对真理。 | 先验知识/题面给定，逻辑校验通过：BF16 54GB > 32GB 不可行，FP8 权重 27GB + KV Cache 4.25GB = 31.25GB < 32GB 可行，数学逻辑自洽；但 KV Cache 具体数值及 PPL 对比为经验事实，无外部来源直接支持，故降级。
