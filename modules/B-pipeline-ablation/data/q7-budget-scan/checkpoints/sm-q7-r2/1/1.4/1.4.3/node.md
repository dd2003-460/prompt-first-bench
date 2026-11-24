# N52: 元数据开销对有效可用容量的修正因子 F_meta = 1 - M_meta：本地方案 F_meta = 1 - 0.015 = 0.985；云方案 F_meta

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

元数据开销对有效可用容量的修正因子 F_meta = 1 - M_meta：本地方案 F_meta = 1 - 0.015 = 0.985；云方案 F_meta = 1 - 0.005 = 0.995（假设M_meta_cloud=0.5%为索引/标签开销）；该因子直接乘入分母，影响每TB年成本计算

## Corrected Claim

元数据开销对有效可用容量的修正因子 F_meta = 1 - M_meta：本地方案 F_meta = 1 - 0.015 = 0.985；云方案 F_meta = 1 - 0.005 = 0.995（假设M_meta_cloud=0.5%为索引/标签开销）；该因子直接乘入分母，影响每TB年成本计算

## Evidence

先验知识/题面给定，逻辑校验通过
