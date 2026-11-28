# N43: 在TP=4推理阶段，All-Reduce主要发生在Attention Head Split和FFN Output阶段。对于Qwen-27B（假设hidden=5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

在TP=4推理阶段，All-Reduce主要发生在Attention Head Split和FFN Output阶段。对于Qwen-27B（假设hidden=5120, batch=1, seq_len=1），单次All-Reduce数据量为 5120 * 2 (Q/O) * 4 (bytes/fp32) ≈ 40KB，传输延迟 = 40KB / 240GB/s ≈ 0.17 μs，加上启动延迟~5μs，总延迟<10μs，相对于单token生成时间(~100ms)占比<0.01%，证实通信非瓶颈。

## Corrected Claim

在TP=4推理阶段，All-Reduce主要发生在Attention Head Split和FFN Output阶段。对于Qwen-27B（假设hidden=5120, batch=1, seq_len=1），单次All-Reduce数据量为 5120 * 2 (Q/O) * 4 (bytes/fp32) ≈ 40KB，传输延迟 = 40KB / 240GB/s ≈ 0.17 μs，加上启动延迟~5μs，总延迟<10μs，相对于单token生成时间(~100ms)占比<0.01%，证实通信非瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程自洽（5120*2*4=40960 bytes≈40KB，40KB/240GB/s≈0.17μs，总延迟远小于100ms），符合TP推理通信开销极小的常识。
