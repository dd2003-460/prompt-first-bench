# N139: AMD Radeon Pro W7900 (48GB) 在 ROCm 环境下运行 Qwen3-27B (FP8) 的实测吞吐约为 60-80 tokens/se

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50

## Claim

AMD Radeon Pro W7900 (48GB) 在 ROCm 环境下运行 Qwen3-27B (FP8) 的实测吞吐约为 60-80 tokens/sec，基于 A100 基准吞吐 (100-120 t/s) 的 60-80% 性能比率估算。

## Corrected Claim

AMD Radeon Pro W7900 (48GB) 在 ROCm 环境下运行 Qwen3-27B (FP8) 的预估吞吐约为 60-80 tokens/sec，该数值基于 A100 基准吞吐 (100-120 t/s) 的 60-80% 性能比率估算得出，非实测数据。

## Evidence

[质询]该陈述将基于A100基准的估算值（60-80%性能比率）直接表述为“实测吞吐”，混淆了“估算”与“实测”的概念；且W7900与A100在显存带宽、计算架构及ROCm优化程度上的差异巨大，简单套用60-80%比率缺乏严谨依据，属于经验事实的粗略推测。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且陈述本身承认是基于估算而非直接实测数据，无法验证具体数值准确性）

## Search Query

AMD Radeon Pro W7900 Qwen3-27B FP8 ROCm throughput tokens per second
