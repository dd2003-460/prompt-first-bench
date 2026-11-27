# N148: 工作点B（低并发长上下文）：假设max_num_seqs=1，seq_len=262k。若使用FlashAttention，Prefill激活内存峰值降低至 O

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73, N74, N75

## Claim

工作点B（低并发长上下文）：假设max_num_seqs=1，seq_len=262k。若使用FlashAttention，Prefill激活内存峰值降低至 O(N) 级别，约为 262144 * 4096 * 2 / 4 ≈ 536MB/卡（与N73一致）。KV Cache占用 512MB。总占用 ~1GB/卡。此时瓶颈转移至Decode阶段的显存带宽（Memory-Bound），吞吐降至 900GB/s / (27e9 params * 2bytes) ≈ 16.6 tok/s，远低于Prefill速度，Preemption机制在此工况下几乎不触发，因为显存有大量余量。

## Corrected Claim

工作点B（低并发长上下文）：假设max_num_seqs=1，seq_len=262k。若使用FlashAttention，Prefill激活内存峰值降低至 O(N) 级别，约为 262144 * 4096 * 2 / 4 ≈ 536MB/卡（与N73一致）。KV Cache占用 512MB。总占用 ~1GB/卡。此时瓶颈转移至Decode阶段的显存带宽（Memory-Bound），吞吐降至 900GB/s / (27e9 params * 2bytes) ≈ 16.6 tok/s，远低于Prefill速度，Preemption机制在此工况下几乎不触发，因为显存有大量余量。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention O(N) 内存估算量级正确（~536MB），Decode 阶段受限于显存带宽的计算符合 Roofline 模型直觉（900GB/s / 54GB ≈ 16.6 tok/s），且低并发长上下文场景下显存余量充足导致 Preemption 不触发的逻辑自洽。

## Search Query

vLLM long context single sequence decode throughput memory bound bandwidth
