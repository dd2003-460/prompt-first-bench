# N11: BF16基线质量：Qwen3-27B BF16权重在MMLU基准上准确率~85.2% [待核验]，PPL~2.1 [待核验]，作为质量损失计算的基准值

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

BF16基线质量：Qwen3-27B BF16权重在MMLU基准上准确率~85.2% [待核验]，PPL~2.1 [待核验]，作为质量损失计算的基准值

## Corrected Claim

Qwen3-27B BF16权重在MMLU基准上准确率约为85%左右，PPL约为2.1左右，作为质量损失计算的基准值。

## Evidence

[质询]具体数值（85.2%和2.1）缺乏来源支持，且不同评测集/提示词下MMLU准确率波动较大，PPL对分词器敏感，精确到小数点后一位的数值极易因评测配置不同而产生偏差。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），具体数值无法验证，降级为定性表述。

## Search Query

Qwen3-27B BF16 MMLU accuracy perplexity benchmark
