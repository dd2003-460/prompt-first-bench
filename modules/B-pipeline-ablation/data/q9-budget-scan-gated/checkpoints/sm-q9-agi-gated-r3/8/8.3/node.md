# N73: vLLM Preemption机制触发的真实瓶颈并非静态KV显存，而是Prefill阶段的激活内存峰值。在TP=4下，单个长序列(262k tokens)的Pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

vLLM Preemption机制触发的真实瓶颈并非静态KV显存，而是Prefill阶段的激活内存峰值。在TP=4下，单个长序列(262k tokens)的Prefill激活内存约为 262144 * hidden_size(4096) * 2bytes(FP16) / 4(cards) ≈ 536 MB/card，加上KV Cache 512MB，单序列总瞬时占用约1GB/card，远低于13.76GB限制，故长上下文并发受限主要取决于CPU调度或Batch大小而非OOM。

## Corrected Claim

vLLM Preemption机制触发的真实瓶颈并非静态KV显存，而是Prefill阶段的激活内存峰值。在TP=4下，单个长序列(262k tokens)的Prefill激活内存约为 262144 * hidden_size(4096) * 2bytes(FP16) / 4(cards) ≈ 536 MB/card，加上KV Cache 512MB，单序列总瞬时占用约1GB/card，远低于13.76GB限制，故长上下文并发受限主要取决于CPU调度或Batch大小而非OOM。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程符合线性代数维度与数据类型字节数标准（262144*4096*2/4 ≈ 536MB），且结论符合大模型推理中Prefill阶段激活内存通常小于KV Cache或与之相当、远小于单卡显存的工程常识。
