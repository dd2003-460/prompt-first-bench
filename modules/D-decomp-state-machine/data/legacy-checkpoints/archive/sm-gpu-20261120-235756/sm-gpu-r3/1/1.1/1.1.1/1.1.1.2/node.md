# N142: Qwen3-27B 的激活专家参数（Active Experts）在 BF16 下的显存占用为 6.6 GB（计算式：3.3B * 2 bytes），该部分决定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Qwen3-27B 的激活专家参数（Active Experts）在 BF16 下的显存占用为 6.6 GB（计算式：3.3B * 2 bytes），该部分决定实际计算吞吐，其显存占比 12.2% 与计算负载占比不成正比，导致显存利用率与计算效率解耦。

## Corrected Claim

Qwen3-27B 的激活专家参数（Active Experts）在 BF16 下的显存占用为 6.6 GB（计算式：3.3B * 2 bytes），该部分决定实际计算吞吐，其显存占比 12.2% 与计算负载占比不成正比，导致显存利用率与计算效率解耦。

## Evidence

先验知识/题面给定，逻辑校验通过：3.3B参数在BF16下占用6.6GB显存符合基本计算逻辑（3.3 * 2 = 6.6），且MoE模型中激活参数显存占比与计算负载解耦是已知架构特性。
