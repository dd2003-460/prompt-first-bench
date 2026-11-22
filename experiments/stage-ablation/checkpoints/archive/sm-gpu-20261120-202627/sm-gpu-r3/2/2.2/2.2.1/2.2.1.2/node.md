# N212: FP8 量化误差在 32K 长上下文下的累积效应量化：对比 1K 上下文与 32K 上下文下 FP8 相对 BF16 的 PPL 增加幅度差异（假设 1K 增加

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

FP8 量化误差在 32K 长上下文下的累积效应量化：对比 1K 上下文与 32K 上下文下 FP8 相对 BF16 的 PPL 增加幅度差异（假设 1K 增加 0.1%，32K 增加 X%），以验证 N52 中 1%-2% 的工程经验值在长序列下的有效性，需引用支持长上下文 KV Cache 量化的基准测试数据

## Corrected Claim

FP8 量化误差在长上下文（如 32K）下通常比短上下文（如 1K）有更显著的累积效应，导致 PPL 增加幅度扩大；具体增加幅度（如从 0.1% 升至 X%）及 1%-2% 的工程经验值在长序列下的有效性需依赖具体的长上下文 KV Cache 量化基准测试数据验证。

## Evidence

[质询]该陈述包含具体的经验数值假设（1K上下文PPL增加0.1%）和待验证的工程经验值（1%-2%），属于硬件/算法性能的经验事实，无法从第一性原理严格推导，且缺乏外部基准测试数据支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值及长上下文累积效应的具体量级）。

## Search Query

FP8 quantization perplexity degradation long context 32k tokens LLM inference
