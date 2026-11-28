# N610: 单次实验的随机种子控制：在vLLM中设置random_seed固定初始状态，但需记录每次运行前的CUDA device state hash以确保可复现性；若无

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

单次实验的随机种子控制：在vLLM中设置random_seed固定初始状态，但需记录每次运行前的CUDA device state hash以确保可复现性；若无法完全复现，则增加独立实验次数至N=20以抵消随机波动

## Corrected Claim

单次实验的随机种子控制：在vLLM中设置random_seed固定初始状态，但需记录每次运行前的CUDA device state hash以确保可复现性；若无法完全复现，则增加独立实验次数至N=20以抵消随机波动

## Evidence

先验知识/题面给定，逻辑校验通过
