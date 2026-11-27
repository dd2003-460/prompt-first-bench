# N25: INT4 量化导致困惑度增加 0.5-1.2 (相对增加 6-15%)，在复杂推理任务（如数学、代码）上准确率下降 5-10% [待核验]，需要具体任务评估。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

INT4 量化导致困惑度增加 0.5-1.2 (相对增加 6-15%)，在复杂推理任务（如数学、代码）上准确率下降 5-10% [待核验]，需要具体任务评估。

## Corrected Claim

INT4 量化通常导致困惑度相对增加约 6-15%（如来源[1]实测为 11.3%），在复杂推理任务上可能引起准确率下降，具体幅度需视模型与任务而定，建议进行具体任务评估。

## Evidence

[质询]来源[1]仅提供了单一实验配置（group_size=32）下困惑度增加11.3%的数据，无法直接支撑“0.5-1.2绝对值”及“6-15%相对增加”的宽泛范围；且所有来源均未提供“复杂推理任务准确率下降5-10%”的具体实证数据，该部分属于缺乏直接来源支持的定性推断。 | 来源[1]直接支持困惑度相对增加约11.3%（落在6-15%区间内），逻辑自洽；但关于复杂推理任务准确率下降的具体数值（5-10%）在参考来源中无直接证据支持，属于经验事实且缺来源直接覆盖，故降级。

## Search Query

INT4 quantization accuracy degradation Qwen benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00860/article/details/152591028&rut=28d2cf8a468981fd4eb47e12ac237a540573055b1909c0ab37969b53f9356dae', 'type': 'ddg', 'title': 'GPTFast中的量化误差分析：INT4模型的困惑度变化实验-CSDN博客'}
- {'url': 'https://blog.csdn.net/SimCompile/article/details/160054448&rut=3dc4c656cba619b382d571cdf26a8fa8abd14420204d4d93afc7bdda4f74af8c', 'type': 'ddg', 'title': '为什么你的INT4模型崩了？：SITS2026实测17个开源大模型量化表现，独家发布「量化鲁棒性评分卡」（含Qwen2、'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162357960&rut=40b082bc7cf3e80ea78fcb5bbb09a7f68d9f48e96433b104571b7f55cb6dcfc4', 'type': 'ddg', 'title': '模型量化实战：从 Fp16 到 Int4 的精度与性能平衡_人工智能_继续商行-ai硬件创业社区'}
