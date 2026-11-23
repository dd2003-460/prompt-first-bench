# N236: TTL敏感性指数 β 的取值与对象类型强相关：对于T_update=∞的对象，β→0（命中率不随TTL变化）；对于T_update=0的对象，β→∞（TTL>0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

TTL敏感性指数 β 的取值与对象类型强相关：对于T_update=∞的对象，β→0（命中率不随TTL变化）；对于T_update=0的对象，β→∞（TTL>0即导致无效缓存，命中率趋近0）；对于T_update=1-7天的运营素材，β≈1.0-1.5

## Corrected Claim

TTL敏感性指数 β 的取值与对象类型强相关：对于T_update=∞的对象，β→0（命中率不随TTL变化）；对于T_update=0的对象，β→∞（TTL>0即导致无效缓存，命中率趋近0）；对于T_update=1-7天的运营素材，β≈1.0-1.5

## Evidence

先验知识/题面给定，逻辑校验通过
