# N278: RX 7900 XTX 的 BF16 软件模拟开销在长序列（seq_len>16K）场景下更为显著，由于 KV Cache 读取频率增加，实际 BF16 吞吐量

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

RX 7900 XTX 的 BF16 软件模拟开销在长序列（seq_len>16K）场景下更为显著，由于 KV Cache 读取频率增加，实际 BF16 吞吐量进一步下降至 FP16 峰值的 40%-50%，即 24.2-30.3 TFLOPS

## Corrected Claim

RX 7900 XTX 在长序列（seq_len>16K）场景下，由于 KV Cache 读取频率增加，BF16 软件模拟的实际吞吐量可能显著低于 FP16 峰值，具体数值需参考实测数据。

## Evidence

[质询]该陈述包含具体的经验性性能数据（40%-50% 吞吐量、24.2-30.3 TFLOPS），属于特定硬件在特定场景下的实测或估算结果，无法从第一性原理或数学公理直接推导得出，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RX 7900 XTX BF16 software emulation long sequence KV cache overhead throughput
