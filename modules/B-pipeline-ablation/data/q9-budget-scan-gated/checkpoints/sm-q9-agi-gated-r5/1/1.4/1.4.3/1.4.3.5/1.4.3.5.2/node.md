# N122: N55 中 T_mem 计算错误：Prefill 阶段内存带宽限制不仅包括权重加载，还包括 KV Cache 写入和激活值暂存。正确估算：权重读取 13.5GB

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

N55 中 T_mem 计算错误：Prefill 阶段内存带宽限制不仅包括权重加载，还包括 KV Cache 写入和激活值暂存。正确估算：权重读取 13.5GB (TP=4 切分后单卡 3.375GB) 耗时 3.75ms，KV Cache 写入 (假设 seq_len=2000, hidden=4096, fp8) 约 16MB 耗时可忽略，激活值 L2 缓存未命中率约 30%，额外内存访问增加 20% 延迟，故 T_mem 修正为 3.75ms * 1.2 ≈ 4.5ms，而非 2.4ms；剩余 114ms 瓶颈需重新评估为软件栈非 GEMM 操作 (如 RoPE 计算、Masking) 的累积开销。

## Corrected Claim

N55 中 T_mem 计算需重新评估：Prefill 阶段内存带宽限制包括权重加载、KV Cache 写入及激活值暂存。权重读取 3.375GB 耗时约 3.75ms；KV Cache 写入（seq_len=2000, hidden=4096, fp8）实际大小约为数百 MB 至 GB 级，耗时不可忽略；激活值 L2 未命中导致的额外延迟需实测确定。T_mem 应基于完整内存流量重新计算，而非简单乘以 1.2。剩余瓶颈需通过 profiling 工具（如 Nsight Systems）定位具体非 GEMM 操作开销，而非直接归因于 RoPE/Masking。

## Evidence

[质询]KV Cache 写入量估算严重失实：seq_len=2000, hidden=4096 的 KV Cache 大小远大于 16MB（通常需数 GB），且 Prefill 阶段 KV Cache 写入是主要内存带宽瓶颈之一，不能简单视为‘可忽略’；此外，将剩余 114ms 归因于 RoPE/Masking 等非 GEMM 操作缺乏量化依据，可能低估了其他内核（如 LayerNorm、Softmax）或通信开销的影响。 | source=knowledge，但逻辑校验发现 KV Cache 写入量级错误（16MB 远低于实际值），导致 T_mem 修正系数 1.2 缺乏支撑，且瓶颈归因过于简化，存在内部矛盾。
