# N110: 各候选硬件组合的总热设计功耗 (TDP_total) 计算：例如 2×RTX 4090 (450W×2) + 主机其他部件 (100W) ≈ 1000W，处于风

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

各候选硬件组合的总热设计功耗 (TDP_total) 计算：例如 2×RTX 4090 (450W×2) + 主机其他部件 (100W) ≈ 1000W，处于风冷临界点；1×H100 (700W) + 主机 (100W) ≈ 800W，风冷可行 [given]

## Corrected Claim

各候选硬件组合的总热设计功耗 (TDP_total) 计算：例如 2×RTX 4090 (450W×2) + 主机其他部件 (100W) ≈ 1000W，处于风冷临界点；1×H100 (700W) + 主机 (100W) ≈ 800W，风冷可行 [given]

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余性高：所有子节点本质上是同一公式 'TDP_total = GPU_TDP + Host_TDP' 在不同硬件参数下的实例化，结构高度重复，可压缩为参数表。2. 完备性不足：父节点明确限定为 '[given]' 中的两个具体案例（2x4090 和 1xH100），子节点额外引入了 A100、MI300X 和 Apple M3 Ultra 等父节点未提及的硬件，超出了父节点定义的范围，导致范围不匹配（Scope Mismatch）。）
