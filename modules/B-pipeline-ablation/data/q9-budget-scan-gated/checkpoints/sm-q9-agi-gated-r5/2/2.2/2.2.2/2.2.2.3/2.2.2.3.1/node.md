# N147: Preemption触发的Swap开销量化：当KV Cache不足触发preempt时，需将victim序列的KV Cache从HBM卸载至DDR4主机内存，传

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

Preemption触发的Swap开销量化：当KV Cache不足触发preempt时，需将victim序列的KV Cache从HBM卸载至DDR4主机内存，传输量为 seq_len * 12KB；在50GB/s带宽下，4k序列的Swap-Out延迟约为 4096 * 12KB / 50GB/s ≈ 0.98ms，Swap-In延迟相同，单次Preemption总额外延迟约为2ms。

## Corrected Claim

Preemption触发的Swap开销量化：当KV Cache不足触发preempt时，需将victim序列的KV Cache从HBM卸载至DDR4主机内存，传输量为 seq_len * 12KB；在50GB/s带宽下，4k序列的Swap-Out延迟约为 4096 * 12KB / 50GB/s ≈ 0.98ms，Swap-In延迟相同，单次Preemption总额外延迟约为2ms。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 4096 * 12KB / 50GB/s ≈ 0.98ms 准确，总延迟约 2ms 符合算术逻辑，且 KV Cache Swap 机制描述符合 LLM 推理引擎（如 vLLM）的工程常识。
