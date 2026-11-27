# N91: 实际并发瓶颈转移分析：由于 max-num-seqs=8 远小于理论上限 105，显存 Preemption 不会触发。真正的瓶颈在于 8 个序列同时处于 De

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

实际并发瓶颈转移分析：由于 max-num-seqs=8 远小于理论上限 105，显存 Preemption 不会触发。真正的瓶颈在于 8 个序列同时处于 Decode 阶段时的 KV Cache 带宽压力或 Prefill 阶段的激活内存峰值（参考 N73 估算的 536 MB/card/seq）。

## Corrected Claim

实际并发瓶颈转移分析：由于 max-num-seqs=8 远小于理论上限 105，显存 Preemption 不会触发。真正的瓶颈在于 8 个序列同时处于 Decode 阶段时的 KV Cache 带宽压力或 Prefill 阶段的激活内存峰值（参考 N73 估算的 536 MB/card/seq）。

## Evidence

先验知识/题面给定，逻辑校验通过：max-num-seqs=8 远小于理论上限 105，显存 Preemption 确实不会触发；瓶颈转移至 KV Cache 带宽或 Prefill 激活内存峰值符合大模型推理系统的基本原理。
