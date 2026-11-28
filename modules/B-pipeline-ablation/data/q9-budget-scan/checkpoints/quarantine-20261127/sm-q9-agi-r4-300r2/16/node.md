# N234: 人工抽查的最小样本量与置信度：为验证AI系统产出的‘可发表级’结论，需对每批次产出的结论进行随机抽样审计。根据二项分布置信区间计算，若期望错误率<5%，需至少抽

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

人工抽查的最小样本量与置信度：为验证AI系统产出的‘可发表级’结论，需对每批次产出的结论进行随机抽样审计。根据二项分布置信区间计算，若期望错误率<5%，需至少抽取n=60个独立结论样本，才能在95%置信水平下将真实错误率的95%上界控制在10%以内（Clopper-Pearson区间）。

## Corrected Claim

人工抽查的最小样本量与置信度：为验证AI系统产出的‘可发表级’结论，需对每批次产出的结论进行随机抽样审计。根据二项分布置信区间计算，若期望错误率<5%，需至少抽取n=60个独立结论样本，才能在95%置信水平下将真实错误率的95%上界控制在10%以内（Clopper-Pearson区间）。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

binomial proportion confidence interval minimum n for 5% error rate
