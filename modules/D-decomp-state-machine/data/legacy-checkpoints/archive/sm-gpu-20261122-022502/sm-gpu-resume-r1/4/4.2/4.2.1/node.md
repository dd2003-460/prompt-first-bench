# N90: 工作点 A1 (高性低成/前沿)：2x RTX 4090 运行 INT4 Qwen3-27B (13.5GB) + FP8 KV Cache (6.29GB) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点 A1 (高性低成/前沿)：2x RTX 4090 运行 INT4 Qwen3-27B (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB/卡。理论 Decode 上限 ≈ 1008 GB/s / 13.5 GB ≈ 74.6 tokens/s。CapEx ≈ $3198 + $2000 配套 = $5198。

## Corrected Claim

工作点 A1 (高性低成/前沿)：2x RTX 4090 运行 INT4 Qwen3-27B (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB/卡。理论 Decode 上限 ≈ 1008 GB/s / 13.5 GB ≈ 74.6 tokens/s。CapEx ≈ $3198 + $2000 配套 = $5198。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对性能（吞吐）、资源（显存）、成本（功耗/电费）三个独立维度进行修正和细化，内容互不重叠且无逻辑矛盾。父节点中的理论值、显存估算和成本估算均被更精确的实参覆盖，涵盖了工作点评估的关键方面。）
