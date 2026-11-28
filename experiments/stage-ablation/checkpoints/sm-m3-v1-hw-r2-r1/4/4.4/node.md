# N20: 混合云模式总成本函数 $C_{hybrid}(x)$：$C_{hybrid} = C_{local} \times T_{local} + C_{cloud} 

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

混合云模式总成本函数 $C_{hybrid}(x)$：$C_{hybrid} = C_{local} \times T_{local} + C_{cloud} \times x$，其中 $x$ 为卸载至云端的任务比例，需满足 $T_{total} \le T_{budget}$

## Corrected Claim

混合云模式总成本函数 $C_{hybrid}(x)$：$C_{hybrid} = C_{local} \times T_{local} + C_{cloud} \times x$，其中 $x$ 为卸载至云端的任务比例，需满足 $T_{total} \le T_{budget}$

## Evidence

先验知识/题面给定，逻辑校验通过
