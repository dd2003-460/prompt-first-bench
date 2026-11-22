# N39: 买家容忍度阈值 θ 的基准量化：基于买家搜索成本 C_search 与咨询成本 C_consult 的权衡，θ 通常等于 (C_search + C_consu

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N8

## Claim

买家容忍度阈值 θ 的基准量化：基于买家搜索成本 C_search 与咨询成本 C_consult 的权衡，θ 通常等于 (C_search + C_consult) / σ 的倒数形式简化，经验值为 0.5-0.8，显著小于卖家溢价系数 k (≈0.32-0.5)，导致 P_ask > V + θ·σ 的商品被过滤。

## Corrected Claim

买家容忍度阈值 θ 与卖家溢价系数 k 的具体数值关系及计算公式因市场模型而异，不能简单断言 θ 显著小于 k 或固定为 0.5-0.8。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点4（计算公式实例化）在逻辑上依赖于子节点2、3（成本量化）和子节点1（方差量化），且重复了父节点中已给出的公式结构，导致内容重叠；此外，子节点1关注的噪声方差与父节点核心主题（基于成本权衡的容忍度阈值θ）正交性较弱，属于边界条件而非θ的直接决定因素。）

## Search Query

buyer search cost consultation cost threshold used market
