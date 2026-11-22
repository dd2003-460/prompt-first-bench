# N728: H100 SXM 的年折旧率（Depreciation Rate）按 3 年直线折旧法计算为 33.3%，若采用 5 年折旧则为 20%，具体取值需匹配企业会计

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N297

## Claim

H100 SXM 的年折旧率（Depreciation Rate）按 3 年直线折旧法计算为 33.3%，若采用 5 年折旧则为 20%，具体取值需匹配企业会计政策，数据来源为 IRS 固定资产折旧表 [待核验]。

## Corrected Claim

H100 SXM 若按 3 年直线折旧法计算，年折旧率为 33.3%；若按 5 年直线折旧法计算，年折旧率为 20%。具体取值需匹配企业会计政策。注意：IRS MACRS 通常采用加速折旧法，直线折旧率为企业会计政策选择，非 IRS 表格直接默认值。

## Evidence

[质询]该陈述将具体的会计折旧率（33.3%和20%）与IRS固定资产折旧表直接关联，但IRS MACRS（修改加速成本回收系统）通常采用加速折旧法（如3年财产通常为34.75%/31.75%/17.49%），而非直线折旧法；直线折旧是GAAP或企业特定会计政策下的选择，并非IRS表格的直接默认值，存在口径混淆风险。 | 经验事实，逻辑自洽（直线折旧计算正确：1/3≈33.3%，1/5=20%），但缺来源支持且存在会计政策与税务法规口径混淆的可能。

## Search Query

H100 SXM depreciation rate 3-year 5-year IRS MACRS
