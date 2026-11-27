# N48: 48小时无咨询率的统计检验：观测值 60% 与假设值 P(consult|price_drop) 的差异需通过二项分布检验；若样本量 n=200，标准误 SE=

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

48小时无咨询率的统计检验：观测值 60% 与假设值 P(consult|price_drop) 的差异需通过二项分布检验；若样本量 n=200，标准误 SE=√(0.6×0.4/200)=0.035，95%置信区间为 [0.53, 0.67]；若理论模型预测值 P(consult|price_drop)=0.4，则 z=(0.6-0.4)/0.035=5.7，p<0.001，支持柠檬市场效应 [待核验]：需实际样本量和理论预测值

## Corrected Claim

48小时无咨询率的统计检验：观测值 60% 与假设值 P(consult|price_drop) 的差异需通过二项分布检验；若样本量 n=200，标准误 SE=√(0.6×0.4/200)=0.035，95%置信区间为 [0.53, 0.67]；若理论模型预测值 P(consult|price_drop)=0.4，则 z=(0.6-0.4)/0.035=5.7，p<0.001，支持柠檬市场效应 [待核验]：需实际样本量和理论预测值

## Evidence

逻辑推导成立，来源未直接覆盖（来源[2][3]确认假设检验方法论，但具体数值计算基于二项分布正态近似公式，经逻辑校验无误）

## Search Query

lemon market effect price drop consultation probability statistical test

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2015903531488538850&rut=6f421a25b0e99140761adf55db95763bebc690bbe59441ca0b9cfe16d74792d3', 'type': 'ddg', 'title': '新版SPC判异准则大更新!8条Nelson准则实操，拒绝无效干预#SPC#SPC 手册#2026 版 SPC#AIAG#统计过程控制#过程能力 ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/695769863&rut=0e341b2cb9d71438791609ef70bb23a365fe997eeb121b65eff5a1fb2260c315', 'type': 'ddg', 'title': '假设检验的临界值法与p值法 - 知乎 - 知乎专栏'}
- {'url': 'https://math.pku.edu.cn/teachers/mwfy/Teaching/ProbabilityStatistics/slide6.pdf&rut=797702df0a4017299fead5ca87f5682dc3e5230d4880fbb3d621d5aa67c219f6', 'type': 'ddg', 'title': 'PDF 概率统计 B 第六章假设检验'}
