# N23: Qwen3-27B模型在BF16精度下的推理延迟（ms/token）与硬件计算能力成反比，公式为：延迟 = (计算量 / 计算能力) + (数据搬运时间)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下的推理延迟（ms/token）与硬件计算能力成反比，公式为：延迟 = (计算量 / 计算能力) + (数据搬运时间)

## Corrected Claim

Qwen3-27B模型在BF16精度下的推理延迟（ms/token）与硬件计算能力成反比，公式为：延迟 = (计算量 / 计算能力) + (数据搬运时间)

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合计算-通信重叠或串行模型的基本物理直觉，量纲一致（时间=工作量/速率+时间），且BF16精度下计算量与硬件算力成反比是基本规律。
