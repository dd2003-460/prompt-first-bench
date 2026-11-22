# N178: H200 运行 BF16 Qwen3-27B 时，Decode 阶段每 token 需从 HBM 读取的总数据量 = 权重大小 (54GB) + KV Cach

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

H200 运行 BF16 Qwen3-27B 时，Decode 阶段每 token 需从 HBM 读取的总数据量 = 权重大小 (54GB) + KV Cache 读取量 (12.58GB) = 66.58GB，修正父节点 N58 仅用权重大小 (54GB) 计算带宽瓶颈的错误，导致理论上限从 88.89 tokens/s 修正为 4800 / 66.58 ≈ 72.1 tokens/s。

## Corrected Claim

H200 运行 BF16 Qwen3-27B 时，Decode 阶段每 token 需从 HBM 读取的总数据量 = 权重大小 (54GB) + KV Cache 读取量 (12.58GB) = 66.58GB，修正父节点 N58 仅用权重大小 (54GB) 计算带宽瓶颈的错误，导致理论上限从 88.89 tokens/s 修正为 4800 / 66.58 ≈ 72.1 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H200 HBM带宽约4.8TB/s，Decode阶段带宽瓶颈计算逻辑正确（总读取量=权重+KV Cache），数值量级合理（54GB+12.58GB=66.58GB，4800/66.58≈72.1 tokens/s），符合大模型推理带宽瓶颈的基本原理。
