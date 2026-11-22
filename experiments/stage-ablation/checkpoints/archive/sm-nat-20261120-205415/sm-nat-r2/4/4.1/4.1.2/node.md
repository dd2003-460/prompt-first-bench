# N57: 头部对象热度贡献率 H_head = ∑_{i=1}^K h_i / ∑_{i=1}^{N} h_i，在 Pareto(β=0.9) 分布下，该值随 K 的增大

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

头部对象热度贡献率 H_head = ∑_{i=1}^K h_i / ∑_{i=1}^{N} h_i，在 Pareto(β=0.9) 分布下，该值随 K 的增大而趋近于 1；H_base 的下界近似为 H_head 与大小加权因子的乘积

## Corrected Claim

头部对象热度贡献率 H_head = ∑_{i=1}^K h_i / ∑_{i=1}^{N} h_i，在 Pareto(β=0.9) 分布下，该值随 K 的增大而趋近于 1；H_base 的下界近似为 H_head 与大小加权因子的乘积

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布具有长尾特性，头部累积贡献率随K增大趋近于1符合数学定义；H_base作为基础热度，其下界由头部主导部分（H_head）与加权因子决定，逻辑自洽。
