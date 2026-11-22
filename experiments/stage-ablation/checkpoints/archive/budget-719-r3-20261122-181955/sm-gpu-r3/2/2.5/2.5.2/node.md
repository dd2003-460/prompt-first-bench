# N86: FP8 量化下的准确率损失：相比 BF16，FP8 (E4M3/E5M2) 在 MMLU 上的下降通常 < 1% [待核验]，在 HumanEval 上的下降 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

FP8 量化下的准确率损失：相比 BF16，FP8 (E4M3/E5M2) 在 MMLU 上的下降通常 < 1% [待核验]，在 HumanEval 上的下降 < 2% [待核验]；需引用 Qwen3 官方量化报告或第三方评测（如 LMSYS Chatbot Arena 数据）确认具体数值，判断是否满足 <2% 的可接受阈值。

## Corrected Claim

FP8 量化（E4M3/E5M2）相比 BF16 在多数前沿模型上能保持较高的精度一致性，训练收敛曲线几乎重合，但具体在 MMLU 和 HumanEval 上的准确率下降幅度需依据特定模型（如 Qwen3）的官方报告或第三方评测数据确认，通常认为在合理范围内（如 <2%），但具体数值因模型而异。

## Evidence

[质询]陈述中关于 MMLU 和 HumanEval 具体准确率下降数值（<1% 和 <2%）属于经验事实，且未提供具体模型版本（如 Qwen3 或 Llama 3）及评测基准的具体数据支撑，不同模型和任务下 FP8 的精度损失波动较大，直接断言通常小于该阈值缺乏普遍性证据。 | 来源 [1] 仅定性指出 FP8 训练收敛曲线与 BF16 几乎重合，未提供 MMLU/HumanEval 的具体准确率下降数值；来源 [2] 仅讨论量化原理，无评测数据。作为经验事实，缺乏直接来源支持具体数值阈值，故降级。

## Search Query

Qwen3-27B FP8 quantization accuracy loss MMLU HumanEval percentage drop

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2049244381027292133&rut=fee3d0aa8830cb2b3e399635c76d1a6a5c76f34b375dff285dc8d9ec2932d675', 'type': 'ddg', 'title': 'Nvfp4、Fp8、Bf16 大模型量化格式详解 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/574825662&rut=f191144fc4891f6c1f3bf6838e26898380539972ecea368c6b245ffd9df8d2f6', 'type': 'ddg', 'title': 'Fp8 量化-原理、实现与误差分析 - 知乎'}
