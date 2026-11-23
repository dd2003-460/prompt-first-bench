# N39: 全公有云策略的 P99 延迟成本函数 $C_{pub}(T, s)$：$C_{pub} = C_{bandwidth}^{pub} + C_{req}^{pub

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

全公有云策略的 P99 延迟成本函数 $C_{pub}(T, s)$：$C_{pub} = C_{bandwidth}^{pub} + C_{req}^{pub} + C_{infra}^{pub}$，其中 $C_{bandwidth}^{pub} = \text{Traffic}_{daily} \times P_{99}^{pub}$（按 95th 峰值计费），$P_{99}^{pub} \approx 0.2-0.5 \text{ ¥/GB}$，$C_{req}^{pub} \approx 0.0001-0.0005 \text{ ¥/req}$，无固定基础设施成本。

## Corrected Claim

全公有云策略的 P99 延迟成本函数 $C_{pub}(T, s)$：$C_{pub} = C_{bandwidth}^{pub} + C_{req}^{pub} + C_{infra}^{pub}$，其中 $C_{bandwidth}^{pub} = \text{Traffic}_{daily} \times P_{99}^{pub}$（按 95th 峰值计费），$P_{99}^{pub} \approx 0.2-0.5 \text{ ¥/GB}$，$C_{req}^{pub} \approx 0.0001-0.0005 \text{ ¥/req}$，无固定基础设施成本。

## Evidence

父节点级核验未通过：非正交（子节点3（基础设施成本）与子节点1（带宽成本）存在概念重叠和逻辑矛盾。父节点定义中明确指出'无固定基础设施成本'且$C_{infra}^{pub}$应为0或忽略不计，但子节点3将其定义为带宽成本的折扣部分，这既违反了父节点的定义（导致正交性破坏，因为折扣应体现在单价或总成本中，而非作为独立的基础设施CAPEX/OPEX项），又与子节点1的计费模型（按95th峰值计费）产生逻辑冲突（95th计费通常已是最终结算价，不再单独扣除折扣，或者折扣已包含在$p_{95}$中）。此外，子节点3试图将'带宽折扣'归类为'基础设施成本'，混淆了成本类别。）
