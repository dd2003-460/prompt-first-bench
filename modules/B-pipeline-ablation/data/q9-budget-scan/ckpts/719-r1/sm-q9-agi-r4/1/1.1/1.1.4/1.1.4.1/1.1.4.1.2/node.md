# N368: SWE-bench Verified 数据集中，依赖库数量 (unique packages in requirements.txt or environmen

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

SWE-bench Verified 数据集中，依赖库数量 (unique packages in requirements.txt or environment.yaml) ≤ 3 的题目总数为 380 道，占全集 76% [待核验]

## Corrected Claim

SWE-bench Verified 数据集中，依赖库数量较少的题目占比约为 76%（具体数值需依据最新数据集版本及依赖解析标准确认）。

## Evidence

[质询]SWE-bench Verified 数据集通常包含约 500 道题（具体数量随版本更新略有波动，常见为 497-500 左右）。若总数为 500，380 道题占比应为 76%，数值上看似自洽。然而，'依赖库数量 ≤ 3' 这一具体统计指标并非 SWE-bench 官方文档中广泛引用的核心基准数据，且不同环境配置（requirements.txt vs environment.yaml）的解析方式可能导致计数差异，缺乏权威来源直接证实该精确数值（380 和 76%）。 | 经验事实，逻辑自洽（380/500=76%）但缺来源支持，且无可用外部证据验证具体统计值。

## Search Query

SWE-bench Verified dependency count distribution unique packages per instance
