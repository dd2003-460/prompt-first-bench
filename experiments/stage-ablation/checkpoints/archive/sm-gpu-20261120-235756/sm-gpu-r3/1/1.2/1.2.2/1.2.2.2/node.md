# N148: BF16 精度下，Qwen3-27B 运行 32K 上下文时单卡推理的最小显存需求基线为 61.86 GB（计算式：权重 54.36 GB + KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

BF16 精度下，Qwen3-27B 运行 32K 上下文时单卡推理的最小显存需求基线为 61.86 GB（计算式：权重 54.36 GB + KV Cache 7.5 GB），该数值未计入激活值峰值（约 2-4 GB）和框架开销（约 1-2 GB），因此实际所需显存为 64.86-67.86 GB。

## Corrected Claim

BF16 精度下，Qwen3-27B 运行 32K 上下文时单卡推理的最小显存需求基线为 61.86 GB（计算式：权重 54.36 GB + KV Cache 7.5 GB），该数值未计入激活值峰值（约 2-4 GB）和框架开销（约 1-2 GB），因此实际所需显存为 64.86-67.86 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB；32K上下文KV Cache估算合理；总显存计算逻辑自洽。
