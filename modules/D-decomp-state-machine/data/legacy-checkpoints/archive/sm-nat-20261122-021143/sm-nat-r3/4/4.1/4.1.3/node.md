# N44: 线性折扣模型的有效性边界：当 u × T_avg < 0.1 时线性近似误差 < 5%；若 u × T_avg > 0.1，需使用指数模型 N16 [待核验]

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

线性折扣模型的有效性边界：当 u × T_avg < 0.1 时线性近似误差 < 5%；若 u × T_avg > 0.1，需使用指数模型 N16 [待核验]

## Corrected Claim

线性折扣模型在 u × T_avg 较小时（如 < 0.1）近似误差较小，具体阈值需依据特定模型参数或实验数据确定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于理论误差公式及临界点验证（通用性），子节点2聚焦于具体参数下的适用性判断（实例化），两者逻辑互补且无重叠；父节点中的条件判断（<0.1 vs >0.1）在子节点2中通过具体计算结果（0.012 < 0.1）得到了完整覆盖，且隐含了另一分支（若>0.1则需切换）的逻辑必要性，符合完备性要求。）

## Search Query

linear vs exponential decay approximation error cache hit rate update rate
