# N337: 平台降权阈值 $X$ 的统计定义：$X = \arg\max_{x} \left[ \frac{\partial^2 \text{Exposure}(P)}{\

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117, N118, N119

## Claim

平台降权阈值 $X$ 的统计定义：$X = \arg\max_{x} \left[ \frac{\partial^2 \text{Exposure}(P)}{\partial P^2} \right]$，即曝光量对价格二阶导数的拐点位置，通常位于 $X \in [20\%, 30\%]$ 区间，需通过历史数据拟合曝光-价格曲线确定

## Corrected Claim

平台降权阈值 $X$ 通常需通过历史数据拟合曝光-价格曲线确定，其具体数值取决于平台策略，常见区间可能在 [20%, 30%] 附近，但并非严格定义为二阶导数拐点。

## Evidence

[质询]该陈述将‘平台降权阈值’这一通常由业务规则或算法策略决定的经验性参数，强行定义为曝光-价格曲线的二阶导数拐点（数学极值点），且给出了具体的数值区间 [20%, 30%]。这种将特定业务阈值与特定数学特征（拐点）直接等同的逻辑缺乏普遍性，且数值区间属于经验事实，无来源支持其普适性。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，无法验证该特定数学定义及数值区间的准确性。

## Search Query

platform downweighting threshold price deviation inflection point exposure curve
