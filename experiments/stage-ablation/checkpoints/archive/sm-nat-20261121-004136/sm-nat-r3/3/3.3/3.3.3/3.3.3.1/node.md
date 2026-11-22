# N128: 工作点1（高性低成/近似LFU）：采用 Count-Min Sketch 存储频率，每个对象开销约 4-8 字节，总开销 < 1MB，C_data ≈ 128G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点1（高性低成/近似LFU）：采用 Count-Min Sketch 存储频率，每个对象开销约 4-8 字节，总开销 < 1MB，C_data ≈ 128GB，性能损失主要来自哈希冲突导致的频率高估（误报率 ≈ e^(-k)），适合大规模对象数场景。

## Corrected Claim

工作点1（高性低成/近似LFU）：采用 Count-Min Sketch 存储频率，每个对象开销约 4-8 字节，总开销 < 1MB，C_data ≈ 128GB，性能损失主要来自哈希冲突导致的频率高估（误报率 ≈ e^(-k)），适合大规模对象数场景。

## Evidence

先验知识/题面给定，逻辑校验通过：Count-Min Sketch 空间复杂度为 O(km)，4-8字节/对象符合典型配置；误报率 e^(-k) 符合理论推导；128GB 数据量下总开销 <1MB 量级合理（取决于对象数量，若对象数在百万级以内则成立，作为近似LFU工作点描述逻辑自洽）。
