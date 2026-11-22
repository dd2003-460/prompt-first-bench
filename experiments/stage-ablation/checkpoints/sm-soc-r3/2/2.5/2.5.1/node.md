# N53: 平台算法中‘近期成交速度’权重 w_speed 的动态调整机制：w_speed 并非固定 20%-30%，而是随市场流动性 L 动态变化：w_speed = 0

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

平台算法中‘近期成交速度’权重 w_speed 的动态调整机制：w_speed 并非固定 20%-30%，而是随市场流动性 L 动态变化：w_speed = 0.2 + 0.1 * (1 - L/L_max)，其中 L 为当前市场活跃买家数，L_max 为历史峰值；在市场冷清时（L < 0.5*L_max），w_speed 提升至 0.35，导致高价快速成交商品获得超额曝光，形成‘赢家通吃’效应，加剧均衡锁定。

## Corrected Claim

平台算法中‘近期成交速度’权重 w_speed 的动态调整机制：w_speed 随市场流动性 L 动态变化，公式为 w_speed = 0.2 + 0.1 * (1 - L/L_max)。在市场冷清时（L 趋近于 0），w_speed 最高可达 0.3，导致高价快速成交商品获得超额曝光，形成‘赢家通吃’效应。

## Evidence

[质询]该陈述包含具体的算法公式（w_speed = 0.2 + 0.1 * (1 - L/L_max)）和特定阈值（L < 0.5*L_max 时 w_speed 提升至 0.35），这属于特定平台（如电商或交易平台）的内部工程实现细节或经验性参数，并非通用的第一性原理或数学公理。虽然逻辑上自洽（公式计算结果与描述一致），但缺乏外部来源验证其是否为真实存在的通用机制或特定平台的准确描述，存在‘幻觉’或‘过度具体化’的风险。 | 逻辑校验通过：公式 w_speed = 0.2 + 0.1 * (1 - L/L_max) 在 L < 0.5*L_max 时，(1 - L/L_max) > 0.5，故 w_speed > 0.25。若 L 接近 0，w_speed 接近 0.3。陈述中称‘提升至 0.35’与公式最大值 0.3 存在轻微数值矛盾（0.3 < 0.35），或者暗示了额外的非线性调整未写入公式。但鉴于 source 为 knowledge，且无外部来源，主要问题在于具体参数（0.35）与公式推导（max 0.3）的不一致，以及缺乏来源支持具体实现细节。根据规则，knowledge 节点逻辑自洽即 verified，但此处存在内部数值矛盾（公式最大0.3 vs 描述0.35），故逻辑校验应视为存在瑕疵或需降级。重新检查：若 L=0, w=0.3。若 L=0.5Lmax, w=0.25。陈述说 L<0.5Lmax 时提升至 0.35。公式最大值为 0.3（当 L=0）。因此‘提升至 0.35’与公式矛盾。这是一个内部逻辑/数值错误。

## Search Query

recommendation algorithm dynamic weighting transaction speed market liquidity
