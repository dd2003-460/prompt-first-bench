# N267: 冷数据盘活跃率 T_active_cold 修正：对于 80% 冷数据，若按“极少访问”定义为每月一次全量扫描，则年活跃时间占比 = (12次 * 24h/次)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

冷数据盘活跃率 T_active_cold 修正：对于 80% 冷数据，若按“极少访问”定义为每月一次全量扫描，则年活跃时间占比 = (12次 * 24h/次) / 8760h ≈ 3.3%，远低于 N128 假设的 10%（10% 更接近温数据特征）

## Corrected Claim

冷数据盘活跃率 T_active_cold 修正：对于 80% 冷数据，若按“极少访问”定义为每月一次全量扫描，则年活跃时间占比 = (12次 * 24h/次) / 8760h ≈ 3.3%，远低于 N128 假设的 10%（10% 更接近温数据特征）

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (12*24)/8760 ≈ 3.3% 准确，且 3.3% 确实远低于 10%，符合冷数据低活跃率的定义逻辑。

## Search Query

cold data lake access frequency annual scan rate storage tiering
