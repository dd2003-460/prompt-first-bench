# N20: Qwen3-27B模型在BF16精度下激活值峰值显存占用约为2.5GB（基于32K上下文长度和batch_size=1估算），FP8/INT8/NVFP4/W4

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下激活值峰值显存占用约为2.5GB（基于32K上下文长度和batch_size=1估算），FP8/INT8/NVFP4/W4精度下激活值占用与BF16基本一致或略低

## Corrected Claim

Qwen3-27B模型在BF16精度下激活值峰值显存占用约为2.5GB（基于32K上下文长度和batch_size=1估算），FP8/INT8/NVFP4/W4精度下激活值占用与BF16基本一致或略低

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义通用公式与参数假设，节点2修正定性认知（澄清精度关系），节点3和节点4分别独立计算注意力（Attention）和MLP两个主要组件的显存占用。虽然节点3和节点4都是具体计算，但它们针对的是模型中不同的结构模块，不构成冗余。完备性方面，覆盖了父节点中提到的'精度一致性'解释以及'2.5GB估算'的来源分解（注意力+MLP+潜在KV Cache）。）
