# N87: Qwen3-27B 在 W4 量化下，MATH 任务相对于 MMLU 任务的准确率下降幅度比值（Sensitivity_Ratio = ΔMATH / ΔMML

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

Qwen3-27B 在 W4 量化下，MATH 任务相对于 MMLU 任务的准确率下降幅度比值（Sensitivity_Ratio = ΔMATH / ΔMMLU），量化数学推理任务对量化的敏感度系数

## Corrected Claim

Qwen3-27B在W4量化下，数学推理任务（MATH）通常比知识检索任务（MMLU）对量化更敏感，但具体敏感度系数（Sensitivity_Ratio）需基于具体基准测试数据计算，现有来源未提供确切数值。

## Evidence

[质询]参考来源仅提供了Qwen3-27B量化后的整体平均分差或定性描述，未提供MATH和MMLU两个具体任务在W4量化下的独立准确率数据，无法计算或验证具体的Sensitivity_Ratio数值。 | 来源[1]和[2]涉及Qwen3-27B量化性能，但缺乏MATH与MMLU任务的具体量化前后对比数据，无法直接支持该特定比值结论，属于经验事实且缺来源直接支持。

## Search Query

Qwen3-27B W4 quantization sensitivity math vs general QA

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=b4516df8992fdf7a3c7e8f94308cbb87f96dc4ab542bf2ddc1a5f6aa5bec2829', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1904196249697101553&rut=d839ffe9950b2a267e46796011c6380a31f26a29f2576f2456d77d6a8e647b8b', 'type': 'ddg', 'title': 'Qwen3量化技术深度解析：性能极限与挑战 - 知乎'}
