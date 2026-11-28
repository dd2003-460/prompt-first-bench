# N101: 针对 4×V100-16GB 集群，构建 Needle-in-a-Haystack 测试集的上下文长度阶梯为 [8192, 32768, 65536, 1310

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

针对 4×V100-16GB 集群，构建 Needle-in-a-Haystack 测试集的上下文长度阶梯为 [8192, 32768, 65536, 131072, 262144] tokens，以覆盖从安全区到 max_model_len 极限的全谱系

## Corrected Claim

针对 4×V100-16GB 集群，构建 Needle-in-a-Haystack 测试集的上下文长度阶梯为 [8192, 32768, 65536, 131072, 262144] tokens，以覆盖从安全区到 max_model_len 极限的全谱系

## Evidence

父节点级核验未通过：不完备（正交性满足（仅一个子节点无冲突）。但完备性严重不足：父节点要求构建包含5个上下文长度的完整测试集阶梯，而子节点仅分析了其中一个极端值（262144）的可行性，未涵盖其余四个长度（8192, 32768, 65536, 131072）的显存计算与可行性评估，也未涉及集群调度或测试策略的具体构建细节。）

## Search Query

Needle in a haystack context length ladder benchmark design
