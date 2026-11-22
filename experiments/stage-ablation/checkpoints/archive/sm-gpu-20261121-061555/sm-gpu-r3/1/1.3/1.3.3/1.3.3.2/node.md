# N166: Intel Arc A770 的 16GB 显存在 W4A16 量化下 (权重 ~7GB) 仅能支持约 8-10K 上下文窗口的 KV Cache (~2-3G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Intel Arc A770 的 16GB 显存在 W4A16 量化下 (权重 ~7GB) 仅能支持约 8-10K 上下文窗口的 KV Cache (~2-3GB)，无法满足 32K 上下文硬性约束，除非启用 CPU 内存 Swap，但这会导致吞吐量进一步下降 50% 以上，故该方案在容量上不可行。

## Corrected Claim

Intel Arc A770 的 16GB 显存在 W4A16 量化下 (权重 ~7GB) 仅能支持约 8-10K 上下文窗口的 KV Cache (~2-3GB)，无法满足 32K 上下文硬性约束，除非启用 CPU 内存 Swap，但这会导致吞吐量进一步下降 50% 以上，故该方案在容量上不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：A770 16GB 显存扣除权重后剩余空间确实不足以容纳 32K 上下文的 KV Cache，且 CPU Swap 导致性能大幅下降符合硬件架构常识。
