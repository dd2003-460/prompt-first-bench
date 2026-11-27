# N112: Qwen3-27B 在 INT8 精度下的基准测试分数：MMLU, GSM8K, HumanEval 的具体数值，以及相对于 BF16 基线的绝对分数下降值

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 INT8 精度下的基准测试分数：MMLU, GSM8K, HumanEval 的具体数值，以及相对于 BF16 基线的绝对分数下降值

## Corrected Claim

Qwen3-27B（或相关版本）在INT8量化下与BF16基线相比，在550题基准测试中平均分差约为0.70个百分点，具体MMLU、GSM8K、HumanEval的单项分数及绝对下降值需查阅详细评测报告。

## Evidence

[质询]参考来源[1]讨论的是'Qwen3.8-27B'（疑似笔误或非标准版本号，通常应为Qwen2.5或Qwen3系列，且'3.8'并非已知官方发布版本），且仅提供了'550题基准平均分差0.70个百分点'的宏观结论，未提供MMLU、GSM8K、HumanEval的具体INT8分数及相对于BF16的绝对下降值，无法直接支持该具体数值事实。 | 来源[1]主题相关但仅给出平均分差，未覆盖具体基准测试数值，属于间接/部分支持，且版本号存在疑点，故降级。

## Search Query

Qwen3-27B INT8 benchmark scores MMLU GSM8K HumanEval

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=cfb80a25d52d5727626a2baec0302714755cfb148f0352ba41e97b60a48378dd', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
