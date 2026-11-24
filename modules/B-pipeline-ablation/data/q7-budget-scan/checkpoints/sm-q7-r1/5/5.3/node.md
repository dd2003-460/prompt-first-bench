# N28: NVMe SSD 方案的代表性工作点（高性低成/中性价比）：假设 500TB 有效容量需 500*1.805=902.5TB 物理容量，采用 1.92TB NV

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

NVMe SSD 方案的代表性工作点（高性低成/中性价比）：假设 500TB 有效容量需 500*1.805=902.5TB 物理容量，采用 1.92TB NVMe SSD，需 471 块；总硬件成本 ≈ 471 * ¥3,000/TB * 1.92TB ≈ ¥2.7M，年折旧（5 年直线）≈ ¥540k/年 [待核验]

## Corrected Claim

NVMe SSD 方案的代表性工作点：假设 500TB 有效容量需 902.5TB 物理容量，采用 1.92TB NVMe SSD，需约 471 块；若单 TB 成本约为 ¥3,000，则总硬件成本约 ¥2.7M，年折旧（5 年直线）约 ¥540k/年。（注：单价为假设值，需根据实际采购价格调整）

## Evidence

[质询]核心成本参数（¥3,000/TB）缺乏来源支持，且该单价对于企业级1.92TB NVMe SSD而言可能偏高或偏低（取决于具体型号和市场波动），属于经验事实，无法仅凭逻辑推导确定。 | 参考来源[1][2]仅涉及NVMe性能调优与影响因素，未提供价格或成本数据，无法支持或反驳具体的硬件成本估算；逻辑计算过程（500*1.805=902.5, 902.5/1.92≈470.05取整471, 471*1.92*3000=2,714,160≈2.7M, 2.7M/5=540k）自洽，但关键输入参数（单价）为经验事实且无来源佐证。

## Search Query

NVMe SSD 1.92TB price per TB 2024 enterprise datacenter

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/13966839866&rut=6b3dfb121d0f697923144e1615177c3f5e7ba04585679b0bea61746b2b8bf1cf', 'type': 'ddg', 'title': '服务器NVMe调优指南：4900万IOPS、340GB/s带宽 (24x SSD)'}
- {'url': 'https://zhuanlan.zhihu.com/p/705334634&rut=7fa348fcd13fb93ba3cfaf73e63c35e690770af739e2d6f5b6e40bbbece54522', 'type': 'ddg', 'title': '详解NVMe SSD存储性能影响因素 - 知乎'}
