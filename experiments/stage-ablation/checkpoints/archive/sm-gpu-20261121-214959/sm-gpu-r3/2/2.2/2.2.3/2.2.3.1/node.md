# N180: B200 运行 NVFP4 Qwen3-27B 时，Decode 阶段每 token 需从 HBM 读取的总数据量 = 权重大小 (13.5GB) + KV C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

B200 运行 NVFP4 Qwen3-27B 时，Decode 阶段每 token 需从 HBM 读取的总数据量 = 权重大小 (13.5GB) + KV Cache 读取量 (12.58GB) = 26.08GB，修正父节点 N59 仅用权重大小 (13.5GB) 计算带宽瓶颈的错误，导致理论上限从 592.6 tokens/s 修正为 8000 / 26.08 ≈ 306.7 tokens/s。

## Corrected Claim

B200 运行 NVFP4 Qwen3-27B 时，Decode 阶段每 token 需从 HBM 读取的总数据量 = 权重大小 (13.5GB) + KV Cache 读取量 (12.58GB) = 26.08GB，修正父节点 N59 仅用权重大小 (13.5GB) 计算带宽瓶颈的错误，导致理论上限从 592.6 tokens/s 修正为 8000 / 26.08 ≈ 306.7 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 13.5 + 12.58 = 26.08 正确，带宽换算 8000 / 26.08 ≈ 306.7 正确，且 Decode 阶段带宽瓶颈确实由权重与 KV Cache 共同决定，符合大模型推理基本物理直觉。
