# N183: NVMe SSD Random Read 18-22W功耗的物理来源分解：NAND阵列随机寻址电流贡献约60-70%（因随机IO导致NAND页读取而非块读取，能

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

NVMe SSD Random Read 18-22W功耗的物理来源分解：NAND阵列随机寻址电流贡献约60-70%（因随机IO导致NAND页读取而非块读取，能耗激增），主控解码与纠错(ECC)贡献约20-30%，DRAM缓存命中/未命中的能耗差异较小。

## Corrected Claim

NVMe SSD Random Read 18-22W功耗的物理来源分解：NAND阵列随机寻址电流贡献约60-70%（因随机IO导致NAND页读取而非块读取，能耗激增），主控解码与纠错(ECC)贡献约20-30%，DRAM缓存命中/未命中的能耗差异较小。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD random read power consumption NAND ECC controller breakdown
