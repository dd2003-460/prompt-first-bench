# N386: 工作点2（中性价比最优）：A100 40GB @ INT8量化，显存占用29.15GB，理论峰值吞吐35.0 tokens/s（基于2039 GB/s带宽），质

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

工作点2（中性价比最优）：A100 40GB @ INT8量化，显存占用29.15GB，理论峰值吞吐35.0 tokens/s（基于2039 GB/s带宽），质量系数Q_norm≈0.98（INT8质量损失极小），Normalized Throughput = 35.0 / max_tokens_s。此工作点平衡了质量与成本，适用于对精度要求较高且预算中等的场景。

## Corrected Claim

工作点2（中性价比最优）：A100 40GB @ INT8量化，显存占用29.15GB，理论峰值吞吐35.0 tokens/s（基于2039 GB/s带宽），质量系数Q_norm≈0.98（INT8质量损失极小），Normalized Throughput = 35.0 / max_tokens_s。此工作点平衡了质量与成本，适用于对精度要求较高且预算中等的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 40GB显存占用29.15GB在合理范围内，INT8量化质量系数0.98符合常规认知，吞吐计算基于给定带宽逻辑自洽。

## Search Query

A100 40GB INT8 quantization throughput tokens/s memory bandwidth 2039 GB/s
