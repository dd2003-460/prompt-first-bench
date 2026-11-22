# N9: 消费级显卡（如 RTX 4090 24GB, RTX 3090 24GB）在 BF16/FP8 下无法单卡承载 Qwen3-27B + 32K KV Cache

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

消费级显卡（如 RTX 4090 24GB, RTX 3090 24GB）在 BF16/FP8 下无法单卡承载 Qwen3-27B + 32K KV Cache，需评估双卡或量化方案可行性

## Corrected Claim

消费级显卡（如 RTX 4090 24GB, RTX 3090 24GB）在 BF16/FP8 下无法单卡承载 Qwen3-27B + 32K KV Cache，需评估双卡或量化方案可行性

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点1、2、3在逻辑结构上高度重复，均遵循'权重+KV+开销=总需求 vs 单卡显存'的同一评估范式，仅精度参数不同，属于典型的参数化冗余而非正交维度。此外，父节点要求评估'双卡或量化方案可行性'，但子节点5讨论的是带宽/速度，未直接回答双卡方案在量化下的可行性（如双卡INT4是否可行），且未涵盖双卡通信架构（如PCIe vs NVLink）对可行性的具体约束分析，导致完备性缺失。）
