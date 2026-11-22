# N166: H100 SXM5 在 BF16 精度下运行 Qwen3-27B (32K ctx) 的吞吐量理论上限：显存带宽 3350 GB/s，BF16 权重 54GB，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43, N44, N45

## Claim

H100 SXM5 在 BF16 精度下运行 Qwen3-27B (32K ctx) 的吞吐量理论上限：显存带宽 3350 GB/s，BF16 权重 54GB，单 token 生成需读取 54GB 数据，理论最小时间 16ms，对应最大吞吐量 62.5 tokens/s；实测 45-55 tokens/s 对应有效带宽利用率 72-88%。

## Corrected Claim

H100 SXM5 在 BF16 精度下运行 Qwen3-27B (32K ctx) 的吞吐量理论上限：显存带宽 3350 GB/s，BF16 权重 54GB，单 token 生成需读取 54GB 数据，理论最小时间 16ms，对应最大吞吐量 62.5 tokens/s；实测 45-55 tokens/s 对应有效带宽利用率 72-88%。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 显存带宽 3.35TB/s 与 BF16 下 27B 模型权重约 54GB 符合工程常识，计算 54GB/3350GB/s ≈ 16.1ms，对应理论上限 ~62.5 tokens/s 数学自洽；实测 45-55 tokens/s 对应 72-88% 带宽利用率符合大模型推理实际表现。
