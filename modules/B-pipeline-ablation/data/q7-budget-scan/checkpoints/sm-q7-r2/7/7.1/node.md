# N90: NVMe SSD 有效容量与物理容量的换算细节：企业级 NVMe SSD 标称容量通常为 1.92TB 或 3.84TB，但格式化后可用容量（Usable Ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

NVMe SSD 有效容量与物理容量的换算细节：企业级 NVMe SSD 标称容量通常为 1.92TB 或 3.84TB，但格式化后可用容量（Usable Capacity）约为标称值的 90%-95%（受文件系统元数据、保留空间影响）；因此 550TB 物理标称容量对应的有效可用容量约为 $550 \times 0.92 \approx 506TB$，需确保覆盖 500TB 业务数据 + 元数据开销（N10: 1-3%），故实际采购需向上取整至 576TB 或 640TB 物理容量

## Corrected Claim

NVMe SSD 有效容量与物理容量的换算细节：企业级 NVMe SSD 标称容量通常为 1.92TB 或 3.84TB，但格式化后可用容量（Usable Capacity）约为标称值的 90%-95%（受文件系统元数据、保留空间影响）；因此 550TB 物理标称容量对应的有效可用容量约为 $550 \times 0.92 \approx 506TB$，需确保覆盖 500TB 业务数据 + 元数据开销（N10: 1-3%），故实际采购需向上取整至 576TB 或 640TB 物理容量

## Evidence

先验知识/题面给定，逻辑校验通过：企业级NVMe SSD的Overhead（含FTL、元数据、预留空间）通常在5%-10%之间，90%-95%的可用率符合工程常识；550TB * 0.92 ≈ 506TB 的数学计算正确，且506TB > 500TB + 元数据开销，逻辑自洽。

## Search Query

enterprise NVMe SSD usable capacity vs nominal capacity overhead percentage
