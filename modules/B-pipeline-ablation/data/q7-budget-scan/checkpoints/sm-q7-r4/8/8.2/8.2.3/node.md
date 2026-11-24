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

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且正交：第一个子节点负责修正基础物理参数（扫描耗时），第二个子节点基于该修正参数推导最终指标（活跃率）及业务影响（成本）。两者无重叠或矛盾，共同完整覆盖了父节点中关于‘修正’和‘对比N128假设’的核心内容。虽然第二个子节点引用了第一个的结果，但这属于正常的因果推导关系，不构成冗余。）

## Search Query

cold data lake access frequency annual scan rate storage tiering
