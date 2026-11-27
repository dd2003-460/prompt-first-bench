# N185: Qwen3-27B 在 W4 (INT4) 权重 + FP8 KV Cache 配置下的总显存占用：权重 13.5 GB + KV Cache 4 GB = 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

Qwen3-27B 在 W4 (INT4) 权重 + FP8 KV Cache 配置下的总显存占用：权重 13.5 GB + KV Cache 4 GB = 17.5 GB。加上激活值、CUDA 上下文及框架开销（通常 2-4 GB），总占用约为 19.5-21.5 GB。该数值低于 RTX 4090 的 24 GB 显存容量，因此单卡 RTX 4090 在理论上可容纳该配置，无需多卡或 CPU Offload。

## Corrected Claim

Qwen3-27B 在 W4 (INT4) 权重 + FP8 KV Cache 配置下的总显存占用：权重 13.5 GB + KV Cache 4 GB = 17.5 GB。加上激活值、CUDA 上下文及框架开销（通常 2-4 GB），总占用约为 19.5-21.5 GB。该数值低于 RTX 4090 的 24 GB 显存容量，因此单卡 RTX 4090 在理论上可容纳该配置，无需多卡或 CPU Offload。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对权重量化开销、框架/上下文固定开销、以及动态激活值与OOM风险进行了独立且互补的细化。三者分别对应显存占用的不同组成部分（静态权重、静态开销、动态激活），逻辑上正交。父节点中的'2-4 GB'模糊区间被合理拆解为更精确的'1-1.5 GB固定开销'和'1-2 GB动态激活'，覆盖了父节点的所有关键假设和结论，且指出了原估算中未明确区分的风险点，无冗余。）
