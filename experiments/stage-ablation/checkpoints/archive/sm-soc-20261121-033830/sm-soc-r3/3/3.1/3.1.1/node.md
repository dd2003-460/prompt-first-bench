# N58: 二手市场中时间成本系数 λ 的估计值需通过离散选择模型（Mixed Logit）回归得出，其数值通常显著高于普通商品市场（例如 λ_used > λ_new *

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

二手市场中时间成本系数 λ 的估计值需通过离散选择模型（Mixed Logit）回归得出，其数值通常显著高于普通商品市场（例如 λ_used > λ_new * 2），具体倍数需依据平台用户行为数据标定。

## Corrected Claim

二手市场中时间成本系数 λ 的估计值需通过离散选择模型（Mixed Logit）回归得出，其数值通常高于普通商品市场，具体倍数需依据平台用户行为数据标定。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（λ）在不同市场细分下的具体取值实例，属于参数枚举而非独立维度的分解，存在严重冗余；同时父节点强调的‘显著高于普通商品市场（>2倍）’这一核心约束在子节点中缺乏明确的对比基准（未提供普通商品市场的λ基准值），导致无法验证是否满足‘显著高于’的条件，完备性不足。）

## Search Query

used goods market time preference coefficient estimation mixed logit
