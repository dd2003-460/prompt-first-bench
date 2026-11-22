# N87: INT4 (AWQ/GPTQ) 量化下的准确率损失：相比 BF16，INT4 在 MMLU 上的下降通常为 3-5% [待核验]，在 HumanEval 上的下

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

INT4 (AWQ/GPTQ) 量化下的准确率损失：相比 BF16，INT4 在 MMLU 上的下降通常为 3-5% [待核验]，在 HumanEval 上的下降为 5-8% [待核验]；需查阅 Qwen3 官方 AWQ 量化模型卡或第三方评测（如 OpenLLM Leaderboard）确认具体数值，判断是否满足 <5% 的可接受阈值（若应用对代码生成敏感，则需更严格标准）。

## Corrected Claim

INT4 (AWQ/GPTQ) 量化通常会导致模型性能轻微下降，具体损失幅度取决于模型规模与任务类型；在代码生成等敏感任务上，损失可能高于通用知识任务（如 MMLU）。需查阅具体模型（如 Qwen3）的官方评测数据以确认是否满足 <5% 的阈值。

## Evidence

[质询]具体数值范围（MMLU 3-5%, HumanEval 5-8%）属于经验事实，且高度依赖于模型规模（如7B vs 70B）、具体量化算法实现（AWQ vs GPTQ）以及基准测试的具体版本。参考来源仅提供了定性对比或通用原理，未提供针对 Qwen3 或特定模型在 MMLU/HumanEval 上的精确量化损失数值，无法直接证实该特定区间。 | 逻辑自洽（INT4量化通常导致轻微性能下降，代码生成任务对精度更敏感），但参考来源[1][2][3]仅涉及量化算法原理和通用对比，未提供具体的 MMLU/HumanEval 准确率损失数值，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B INT4 AWQ GPTQ accuracy loss MMLU HumanEval percentage drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/bumblebee16/article/details/167129055&rut=2431b040d4392d18dffb7a8f17b86a9576e628b80a92c5fbdef8bf28da193f87', 'type': 'ddg', 'title': '【模型量化⑤】Weight-Only INT4：AWQ与GPTQ两大算法深度解析-CSDN博客'}
- {'url': 'https://guijiagi.com/posts/model-quantization-2026-int4-int8-awq-gptq-comparison/&rut=acf560ae4b150e45982209726534866d0d46bcc0d2a7d8a603e6aa3f7440da4a', 'type': 'ddg', 'title': '模型量化技术 2026：Int4/Int8/Awq/Gptq 实测对比'}
- {'url': 'https://blog.csdn.net/weixin_37647148/article/details/161776271&rut=fe61a36c5f2f092fad5634128462803eb9671522aca5834aab3bda206586d57f', 'type': 'ddg', 'title': '量化压缩实战：Int8 / Int4 / Awq / Gptq 全面对比 - Csdn博客'}
