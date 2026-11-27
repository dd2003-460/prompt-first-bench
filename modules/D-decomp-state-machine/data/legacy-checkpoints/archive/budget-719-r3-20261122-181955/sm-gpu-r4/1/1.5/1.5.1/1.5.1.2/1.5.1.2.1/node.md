# N570: Qwen3-27B 在 BF16 精度下的权重文件大小为 54 GB (27B params * 2 bytes/param)，这是 Decode 阶段内存带宽

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N198

## Claim

Qwen3-27B 在 BF16 精度下的权重文件大小为 54 GB (27B params * 2 bytes/param)，这是 Decode 阶段内存带宽消耗的基础项。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重文件大小为 54 GB (27B params * 2 bytes/param)，这是 Decode 阶段内存带宽消耗的基础项。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 2字节/BF16 = 54GB，计算正确且符合大模型显存占用常识。
