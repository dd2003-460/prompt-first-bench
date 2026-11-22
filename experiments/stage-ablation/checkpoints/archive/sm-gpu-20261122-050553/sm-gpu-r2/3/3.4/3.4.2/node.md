# N72: Qwen3-27B 在 W4-GPTQ 量化下，MATH 数学推理基准的准确率从 BF16 基准值（约 80-85% [待核验]）下降至约 70-78%，绝对值

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

Qwen3-27B 在 W4-GPTQ 量化下，MATH 数学推理基准的准确率从 BF16 基准值（约 80-85% [待核验]）下降至约 70-78%，绝对值损失约 5-10 个百分点，且长链推理错误率显著增加。

## Corrected Claim

Qwen3-27B 在 W4-GPTQ 量化下，MATH 数学推理基准的准确率相较于 BF16 基准值出现下降，绝对值损失通常在数个至十余个百分点之间，且长链推理错误率可能增加。

## Evidence

[质询]具体数值区间（70-78%）及绝对损失幅度（5-10个百分点）缺乏特定量化配置下的实证数据支持，不同GPTQ实现或校准集可能导致结果波动，且BF16基准值本身标注为待核验，导致推导链条基础不稳。 | 经验事实，逻辑自洽（量化通常导致精度下降，长链推理对误差更敏感）但缺来源支持，且无外部证据验证具体数值区间。

## Search Query

Qwen3-27B W4 GPTQ quantization MATH benchmark accuracy degradation
