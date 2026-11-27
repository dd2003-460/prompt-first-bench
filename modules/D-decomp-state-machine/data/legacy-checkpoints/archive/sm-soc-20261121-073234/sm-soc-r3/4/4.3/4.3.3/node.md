# N88: 高估值买家子集（估值 > 挂价）的占比比例 p_high，即 P(v_buyer > P_listing)，该比例直接决定在 15-25% 高溢价下成交周期缩短

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

高估值买家子集（估值 > 挂价）的占比比例 p_high，即 P(v_buyer > P_listing)，该比例直接决定在 15-25% 高溢价下成交周期缩短的幅度，需计算 p_high 与成交周期 T 的关系 T = 1/(λ * p_high)。

## Corrected Claim

在简化匹配模型假设下，若成交事件服从泊松分布且仅受买家估值高于挂价这一条件约束，则成交周期 T 可近似表示为 T = 1/(λ * p_high)；但在实际市场中，该关系需引入流动性折扣及多因素修正。

## Evidence

[质询]公式 T = 1/(λ * p_high) 隐含假设成交率仅由买家估值高于挂价这一单一因素决定，且忽略市场流动性、搜索摩擦及卖家接受度等关键变量，属于过度简化的理论模型而非经验事实；此外，参考来源完全无关，无法验证该特定公式在15-25%溢价场景下的适用性。 | 逻辑上该公式符合泊松过程或简单匹配模型的基本直觉（成交率=基础到达率*匹配概率），量纲合理；但参考来源[1]讨论股票估值方法，与二手房/商品交易成交周期模型无关，无外部证据支持该具体公式，且作为经验性模型参数关系，缺乏来源直接支持，故降级。

## Search Query

high valuation buyer proportion impact on transaction speed second-hand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/20520536584&rut=670f1ec69317d340bd368f1802a9af7018a58dae802978ba250ae6b88fc51226', 'type': 'ddg', 'title': '手把手教你看懂一只股票数据（估值分析篇PE、PB、PS、PEG等）'}
