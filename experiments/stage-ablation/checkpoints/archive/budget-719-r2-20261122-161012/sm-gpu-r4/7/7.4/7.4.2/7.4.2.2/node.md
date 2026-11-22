# N661: 工作点 2 的吞吐 52.5 tokens/s 基于 BF16 精度，H100 SXM 在 BF16 下的实际 Decode 吞吐受限于显存带宽利用率，理论上限

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N273

## Claim

工作点 2 的吞吐 52.5 tokens/s 基于 BF16 精度，H100 SXM 在 BF16 下的实际 Decode 吞吐受限于显存带宽利用率，理论上限 = 3350 GB/s * 0.75 / 55.5 GB ≈ 45.3 tokens/s，实际可能为 38-42 tokens/s，低于假设值

## Corrected Claim

工作点 2 的吞吐 52.5 tokens/s 基于 BF16 精度，H100 SXM 在 BF16 下的实际 Decode 吞吐受限于显存带宽利用率。若模型大小为 55.5 GB 且带宽利用率为 75%，理论上限约为 45.3 tokens/s，实际吞吐通常低于此值，因此 52.5 tokens/s 的假设值可能偏高。

## Evidence

[质询]理论上限计算中使用的模型大小（55.5 GB）和带宽利用率（0.75%）为特定假设，若模型实际大小或硬件效率不同，结论可能偏差；且将‘理论上限’直接等同于‘实际可能范围’缺乏严谨的中间推导支撑。 | 先验知识/题面给定，逻辑校验通过：H100 SXM 显存带宽约 3.35 TB/s，BF16 下 Decode 阶段确实受显存带宽限制，55.5GB 模型在 75% 利用率下理论值约 45.3 tokens/s，实际低于理论值符合工程直觉，但具体数值依赖未提供的模型参数假设。

## Search Query

H100 SXM BF16 inference Qwen3-27B decode throughput benchmark
