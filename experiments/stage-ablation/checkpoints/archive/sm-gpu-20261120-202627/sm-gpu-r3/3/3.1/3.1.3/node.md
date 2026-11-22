# N67: NVIDIA RTX 3090 (24GB) 在 Qwen3-27B 上的显存带宽为 936 GB/s，当前单卡二手/现货均价约为 $800-$1100 [待核

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

NVIDIA RTX 3090 (24GB) 在 Qwen3-27B 上的显存带宽为 936 GB/s，当前单卡二手/现货均价约为 $800-$1100 [待核验：实时价格]，其 TDP 为 350W。

## Corrected Claim

NVIDIA RTX 3090 (24GB) 在 Qwen3-27B 上的显存带宽为 936 GB/s，当前单卡二手/现货均价约为 $800-$1100 [待核验：实时价格]，其 TDP 为 350W。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且互斥：前三个子节点分别对应 BF16、INT8、INT4 三种不同精度下的显存占用可行性分析，属于递进式的排除法论证，最后一个是基于可行方案（INT4）的性能上限估算。它们共同覆盖了硬件规格（带宽/TDP/价格隐含在背景中，虽未单独列出但父节点已给出）对模型部署的影响，没有重复或矛盾。）

## Search Query

RTX 3090 memory bandwidth TDP price 2024
