# N126: BF16 精度下 Qwen3-27B 推理所需的总显存为 Weight (54 GB) + KV Cache (4 GB) + Runtime Overhead

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

BF16 精度下 Qwen3-27B 推理所需的总显存为 Weight (54 GB) + KV Cache (4 GB) + Runtime Overhead (2 GB) = 60 GB

## Corrected Claim

BF16 精度下 Qwen3-27B 推理所需的总显存为 Weight (54 GB) + KV Cache (4 GB) + Runtime Overhead (2 GB) = 60 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16下权重约54GB，KV Cache与Runtime Overhead估算合理，总显存60GB符合工程常识。
