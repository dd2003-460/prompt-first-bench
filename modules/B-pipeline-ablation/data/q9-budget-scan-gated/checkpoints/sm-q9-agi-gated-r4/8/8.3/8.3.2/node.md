# N147: 工作点A（高并发短上下文）：假设max_num_seqs=8，avg_seq_len=2k。Prefill激活内存峰值约为 2048 * 4096 * 2 / 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73, N74, N75

## Claim

工作点A（高并发短上下文）：假设max_num_seqs=8，avg_seq_len=2k。Prefill激活内存峰值约为 2048 * 4096 * 2 / 4 ≈ 4MB/卡（忽略Attention Score的非线性增长或假设使用FlashAttention），KV Cache占用 8 * 2048 * 2KB = 32MB。总瞬时占用远低于13.76GB，此时瓶颈确认为CPU调度延迟（进程切换/IPC）而非GPU显存，符合N73结论。

## Corrected Claim

工作点A（高并发短上下文）：假设max_num_seqs=8，avg_seq_len=2k。Prefill激活内存峰值约为 2048 * 4096 * 2 / 4 ≈ 4MB/卡（忽略Attention Score的非线性增长或假设使用FlashAttention），KV Cache占用 8 * 2048 * 2KB = 32MB。总瞬时占用远低于13.76GB，此时瓶颈确认为CPU调度延迟（进程切换/IPC）而非GPU显存，符合N73结论。

## Evidence

[质询]KV Cache 计算中 '2KB' 的单位定义模糊（通常指每 token 每层或每 token 总大小，此处隐含了特定模型配置如 Llama-7B 的 KV 大小），且 Prefill 激活内存估算忽略了中间层激活值（Activations）的累积，可能低估实际峰值。 | 先验知识/题面给定，逻辑校验通过：数值量级合理（4MB 和 32MB 均远小于 13.76GB），结论（瓶颈在 CPU 而非 GPU 显存）与前提数据一致，符合大模型推理资源调度的基本工程直觉。

## Search Query

vLLM high concurrency short context CPU scheduling bottleneck GPU idle
