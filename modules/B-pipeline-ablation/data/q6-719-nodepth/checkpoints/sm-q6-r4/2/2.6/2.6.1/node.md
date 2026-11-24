# N84: 混合策略下自建部分回源带宽成本 (C_bw_self, ¥/1000 req) 计算为 (C_bw_self_month / Q_day_total) * 10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

混合策略下自建部分回源带宽成本 (C_bw_self, ¥/1000 req) 计算为 (C_bw_self_month / Q_day_total) * 1000，其中 C_bw_self_month 为自建 POP 部分产生的回源带宽月成本，Q_day_total 为日均总请求量。

## Corrected Claim

混合策略下自建部分回源带宽成本 (C_bw_self, ¥/1000 req) 计算为 (C_bw_self_month / Q_day_total) * 1000，其中 C_bw_self_month 为自建 POP 部分产生的回源带宽月成本，Q_day_total 为日均总请求量。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了流量变量 V_origin_self，子节点2基于该流量定义了成本变量 C_bw_self_month。两者分别对应计算链中的不同层级（流量 vs 成本），逻辑上互为前置依赖而非重复或矛盾，符合正交性。父节点公式仅包含 C_bw_self_month 和 Q_day_total，Q_day_total 作为外部输入参数通常不在此层级分解，因此子节点覆盖了父节点公式中需要推导的内部关键变量。）
