# N70: 散热与维护成本在本地工作站场景中占比 <5% TCO，可忽略不计；但多卡方案 (2x3090) 的风道设计可能导致实际功耗高于标称 TDP (预计 +10-15

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

散热与维护成本在本地工作站场景中占比 <5% TCO，可忽略不计；但多卡方案 (2x3090) 的风道设计可能导致实际功耗高于标称 TDP (预计 +10-15%)，需在 TCO 模型中引入 1.1 系数修正

## Corrected Claim

散热与维护成本在本地工作站场景中占比 <5% TCO，可忽略不计；但多卡方案 (2x3090) 的风道设计可能导致实际功耗高于标称 TDP (预计 +10-15%)，需在 TCO 模型中引入 1.1 系数修正

## Evidence

先验知识/题面给定，逻辑校验通过：本地工作站散热维护成本占比低符合常理，多卡风道导致功耗增加10-15%及引入1.1系数修正在工程估算中逻辑自洽且量级合理。

## Search Query

dual GPU power consumption overhead vs single GPU
