# N387: 工作点3（高成本低性）：H100 80GB @ BF16，显存占用58.29GB，理论峰值吞吐57.4 tokens/s（基于3350 GB/s带宽），质量系数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

工作点3（高成本低性）：H100 80GB @ BF16，显存占用58.29GB，理论峰值吞吐57.4 tokens/s（基于3350 GB/s带宽），质量系数Q_norm=1.0（无量化损失），Normalized Throughput = 57.4 / max_tokens_s。此工作点提供最高质量和最大上下文窗口，但单位吞吐成本最高，适用于对精度和稳定性要求极高的生产环境。

## Corrected Claim

工作点3（高成本低性）：H100 80GB @ BF16，显存占用58.29GB，理论峰值吞吐57.4 tokens/s（基于3350 GB/s带宽），质量系数Q_norm=1.0（无量化损失），Normalized Throughput = 57.4 / max_tokens_s。此工作点提供最高质量和最大上下文窗口，但单位吞吐成本最高，适用于对精度和稳定性要求极高的生产环境。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB 显存占用 58.29GB 在 80GB 限制内，BF16 无量化损失 Q_norm=1.0 符合定义，吞吐与带宽关系逻辑自洽。

## Search Query

H100 80GB BF16 throughput tokens/s memory bandwidth 3350 GB/s
