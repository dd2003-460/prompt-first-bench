# N366: 在 Tensor Parallelism (TP=2) 推理中，每张 GPU 仅存储 1/2 的模型权重和 1/2 的 KV Cache，因此单卡显存占用减半；

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N151, N152, N153

## Claim

在 Tensor Parallelism (TP=2) 推理中，每张 GPU 仅存储 1/2 的模型权重和 1/2 的 KV Cache，因此单卡显存占用减半；若第二张卡通过 PCIe 4.0 x4 连接，其瓶颈在于 All-Reduce 通信延迟而非显存带宽；对于 27B 模型，TP=2 的通信量约为 (Batch * Seq_Len * Hidden_Dim * Bytes) / 2，在 8 GB/s 带宽下，每次 All-Reduce 的延迟约为 (32768 * 4096 * 2) / 8e9 ≈ 33ms (假设 Hidden=4096)，这将显著增加 T_decode，导致整体吞吐量远低于双 x16 方案，但并非 '0.14 tokens/s' 这种极端值，需重新计算通信开销对 T_decode 的具体贡献。

## Corrected Claim

在 Tensor Parallelism (TP=2) 推理中，每张 GPU 存储 1/2 的模型权重和 KV Cache。若通过 PCIe 4.0 x4 连接，瓶颈在于通信延迟。对于 27B 模型，假设 Hidden=4096，单次 All-Reduce 传输数据量约为 268MB (基于 32768*4096*2 估算)，在 8 GB/s 带宽下理论延迟约为 0.033ms (33微秒)，实际受协议开销影响会更高，但远小于 33ms。需重新评估通信开销对 T_decode 的具体贡献，原陈述中的 33ms 延迟计算错误。

## Evidence

[质询]数值计算存在严重量级错误：32768 * 4096 * 2 的结果约为 2.68e8 (268,435,456)，除以 8e9 得到的延迟约为 0.033ms (33微秒)，而非陈述中的 33ms。陈述将结果夸大了1000倍，导致对通信瓶颈的定性判断（'显著增加T_decode'）缺乏该具体数值支撑，且33ms的延迟在PCIe 4.0 x4 (理论带宽约4GB/s，实际更低) 下传输268MB数据是不合理的（实际应约为67ms以上，若按8GB/s理论峰值则更低，但绝非33ms这种基于错误算术得出的值）。此外，All-Reduce通信量公式通常涉及2倍数据量（Ring All-Reduce），此处公式简化且未明确Batch/Seq_Len具体值，直接代入32768和4096作为常数进行计算缺乏上下文支撑，属于经验事实且计算错误。 | 逻辑校验发现算术错误：(32768 * 4096 * 2) / 8e9 ≈ 0.033ms，而非33ms。来源不可用，无法外部核验，但内部数值矛盾导致无法验证。

## Search Query

Tensor Parallelism communication overhead PCIe x4 latency LLM inference
