# N150: FP8 E4M3 量化在 Qwen3-27B 上的质量损失：MMLU 准确率下降 < 0.5%，GSM8K 下降 < 0.3%，显著低于 INT4 的 2-3%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

FP8 E4M3 量化在 Qwen3-27B 上的质量损失：MMLU 准确率下降 < 0.5%，GSM8K 下降 < 0.3%，显著低于 INT4 的 2-3% 损失，因此 FP8 在质量损失维度上优于 INT4

## Corrected Claim

FP8 E4M3 量化在 Qwen3-27B 上的质量损失显著低于 INT4，具体数值需参考官方基准测试报告。

## Evidence

[质询]参考来源仅涉及推理速度调优，未提供MMLU/GSM8K准确率下降的具体数值，且模型名称存在细微差异（Qwen3.8-27B vs Qwen3-27B），无法直接验证具体的量化损失百分比。 | 逻辑上FP8精度高于INT4，质量损失更低符合直觉，但具体数值（<0.5%, <0.3%）缺乏来源直接支持，属于经验事实且缺来源佐证。

## Search Query

Qwen3-27B FP8 E4M3 MMLU GSM8K accuracy loss vs BF16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073193935342679989&rut=9b986caacd1d4573ef60426bd804834f133279e5348f6ba65446fd50725eef66', 'type': 'ddg', 'title': '双 NVIDIA L20 上 Qwen3.8-27B-FP8 + MTP 调优测试报告'}
