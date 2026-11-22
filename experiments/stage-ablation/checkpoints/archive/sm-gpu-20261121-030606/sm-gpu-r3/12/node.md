# N184: 硬件候选集必须包含NVIDIA RTX 5090 (32GB GDDR7, ~$2000-$2500), RTX 4090 (24GB GDDR6X, ~$16

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

硬件候选集必须包含NVIDIA RTX 5090 (32GB GDDR7, ~$2000-$2500), RTX 4090 (24GB GDDR6X, ~$1600-$2000), 以及非典型的高性价比替代方案：AMD Radeon RX 7900 XTX (24GB GDDR6, ~$900-$1100) 和 Intel Arc B580 (12GB, 需双卡或排除因容量不足)。筛选标准基于：(1) 显存容量≥21GB (W4精度下限), (2) 显存带宽≥1000GB/s (吞吐量下限), (3) 价格≤$2500 (消费级上限)。

## Corrected Claim

硬件候选集包含NVIDIA RTX 5090 (32GB GDDR7) [来源支持]，以及RTX 4090、AMD RX 7900 XTX和Intel Arc B580等替代方案（具体价格与带宽参数需进一步核实）。筛选标准基于显存容量≥21GB、带宽≥1000GB/s及价格≤$2500（标准依据未提供）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对显存容量修正、带宽阈值验证、特定GPU精度约束及特定GPU排除逻辑进行了独立分析，彼此之间无逻辑矛盾或重复，且共同覆盖了父节点中列出的所有硬件候选（RTX 5090, RTX 4090, RX 7900 XTX, Intel Arc B580）及筛选标准（容量、带宽、价格/可行性）的细化与验证。）

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/&rut=a11ece31eb6c4de74732c323577b537d8cfb33cfb24e0f367ee8c99420a152bf', 'type': 'ddg', 'title': 'GeForce RTX 5090 Graphics Cards | NVIDIA'}
