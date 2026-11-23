# N39: 全公有云策略的 P99 延迟成本函数 $C_{pub}(T, s)$：$C_{pub} = C_{bandwidth}^{pub} + C_{req}^{pub

- **status**: verified
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

先验知识/题面给定，逻辑校验通过
