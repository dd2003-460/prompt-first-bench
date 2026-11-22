# N645: H100 SXM FP8 算力峰值 1979 TFLOPS，HBM3 带宽 3.35 TB/s；27B 模型 Decode 带宽瓶颈理论上限 = 3350 GB

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N198

## Claim

H100 SXM FP8 算力峰值 1979 TFLOPS，HBM3 带宽 3.35 TB/s；27B 模型 Decode 带宽瓶颈理论上限 = 3350 GB/s / 27 GB ≈ 124 tokens/s (单卡)；TP=2 时若权重分片，每卡读取 13.5 GB，理论上限 ≈ 3350 / 13.5 ≈ 248 tokens/s，但受限于 All-Reduce 同步和驱动开销，实测通常为 150-180 tokens/s [待核验]

## Corrected Claim

H100 SXM FP8 算力峰值约 1979 TFLOPS，HBM3 带宽约 3.35 TB/s；27B 模型 Decode 带宽瓶颈理论上限单卡约 124 tokens/s，TP=2 理论上限约 248 tokens/s，实测性能受同步开销影响通常低于理论值。

## Evidence

[质询]该陈述包含具体的硬件规格（H100 SXM FP8算力、HBM3带宽）及实测性能范围（150-180 tokens/s），属于经验事实。由于检索失败无外部来源支持，且实测数据受具体软件栈、序列长度、Batch Size等影响极大，无法仅凭逻辑推导确认具体数值区间。 | 经验事实，逻辑自洽但缺来源支持。理论带宽瓶颈计算（3350/27≈124, 3350/13.5≈248）在数学上成立，但H100具体规格及实测性能范围缺乏外部证据验证。

## Search Query

H100 SXM FP8 27B model decode throughput tokens per second vLLM
