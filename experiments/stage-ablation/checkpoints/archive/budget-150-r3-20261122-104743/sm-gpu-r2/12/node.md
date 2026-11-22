# N198: 候选硬件筛选的显存硬性下限：基于BF16精度下总显存需求约60-65GB（N53/N126），单卡方案显存必须≥80GB以容纳32K上下文KV Cache及运行

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件筛选的显存硬性下限：基于BF16精度下总显存需求约60-65GB（N53/N126），单卡方案显存必须≥80GB以容纳32K上下文KV Cache及运行时开销；多卡方案总显存必须≥65GB。此标准排除了RTX 4090 (24GB)、RTX 3090 (24GB)、A100 40GB等无法独立运行BF16 27B模型的选项，除非采用激进量化（如4-bit）且接受质量损失。

## Corrected Claim

基于BF16精度下27B模型权重（约54GB）及32K上下文KV Cache估算，总显存需求约60-65GB。因此，单卡方案需≥80GB显存，多卡方案总显存需≥65GB。此标准排除了RTX 4090 (24GB)、RTX 3090 (24GB)、A100 40GB等选项，除非采用激进量化。

## Evidence

[质询]来源仅提供了通用的显存估算公式和选型指南，未直接提供针对'BF16 27B模型+32K上下文'这一特定场景的60-65GB总显存需求数值，也未明确列出排除RTX 4090/3090/A100 40GB的具体结论，属于间接支持。 | 逻辑校验通过：27B参数BF16模型权重约54GB，加上32K上下文的KV Cache及运行时开销，总需求确实在60-65GB量级，因此24GB或40GB显卡无法独立运行，逻辑自洽；但参考来源[1]仅给出通用公式，未直接覆盖该具体数值结论，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072251777756443832&rut=b883069abeb0579b64860e52da9601eb529e464aee1427be3eb422bea3cddb30', 'type': 'ddg', 'title': '大模型显卡需求速查表：推理、训练、微调显存公式与选型指南'}
