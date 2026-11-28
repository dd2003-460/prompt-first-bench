# N62: 针对 Qwen3.8-27B 的幻觉率基线，需在相同提示模板下，对比 Temperature=0.7 与 Temperature=0.1 两种设置下的 FCR 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

针对 Qwen3.8-27B 的幻觉率基线，需在相同提示模板下，对比 Temperature=0.7 与 Temperature=0.1 两种设置下的 FCR 差异，通常低温设置可降低幻觉率 20%-40%，但可能降低多样性，需记录具体的 ΔFCR 数值。

## Corrected Claim

针对 Qwen3.8-27B 的幻觉率基线，需在相同提示模板下，对比 Temperature=0.7 与 Temperature=0.1 两种设置下的 FCR 差异。理论上低温设置倾向于降低幻觉率但可能降低多样性，需记录具体的 ΔFCR 数值以评估实际影响。

## Evidence

[质询]「通常低温设置可降低幻觉率 20%-40%」是一个具体的经验量化范围，缺乏普遍适用的科学共识或权威基准数据支持，不同模型、任务和数据集下的实际降幅差异极大，该具体百分比区间可能不准确或过度概括。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值范围无法从第一性原理推出）

## Search Query

Qwen3-27B hallucination rate temperature sensitivity benchmark
