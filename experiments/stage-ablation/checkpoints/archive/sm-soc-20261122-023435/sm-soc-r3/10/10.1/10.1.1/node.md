# N248: 成交周期 T 对 DAU 的边际贡献系数：ΔDAU/ΔT = -0.05 * DAU_base / T_base，其中 DAU_base 为平台日活用户数，T_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N80

## Claim

成交周期 T 对 DAU 的边际贡献系数：ΔDAU/ΔT = -0.05 * DAU_base / T_base，其中 DAU_base 为平台日活用户数，T_base 为平均成交周期（天）；该系数假设 DAU 与 T 呈反比关系，需通过 A/B 测试验证。

## Corrected Claim

成交周期 T 对 DAU 的潜在影响需通过 A/B 测试量化，当前假设的边际贡献系数（-0.05 * DAU_base / T_base）仅为待验证的初始假设，缺乏理论或数据支持。

## Evidence

[质询]该系数公式（ΔDAU/ΔT = -0.05 * DAU_base / T_base）缺乏经济学或行为学理论支撑，属于任意设定的经验参数；且将成交周期（T）与日活用户数（DAU）直接建立反比线性关系违背基本直觉（DAU通常由获客和留存驱动，而非直接由成交速度决定），存在严重的因果混淆和量纲/逻辑风险。 | 无可用外部证据；逻辑校验发现该公式缺乏理论依据且因果关系存疑，属于未经验证的假设性经验参数，无法通过第一性原理推导，故降级。

## Search Query

impact of transaction speed on daily active users in e-commerce
