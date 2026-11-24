# N93: HDD 物理容量与有效容量的换算：企业级 HDD 标称容量通常为 16TB/18TB/20TB，格式化后有效容量约为标称值的 95%-97%（RAID6 开销较

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

HDD 物理容量与有效容量的换算：企业级 HDD 标称容量通常为 16TB/18TB/20TB，格式化后有效容量约为标称值的 95%-97%（RAID6 开销较小）；400TB 有效数据需 $400 / 0.96 \approx 417TB$ 物理容量，考虑 RAID6 冗余系数 1.2，需 $417 \times 1.2 \approx 500TB$ 物理容量，即需 25-32 块 16-20TB HDD

## Corrected Claim

HDD 物理容量与有效容量的换算：企业级 HDD 标称容量通常为 16TB/18TB/20TB，格式化后有效容量约为标称值的 95%-97%（RAID6 开销较小）；400TB 有效数据需 $400 / 0.96 \approx 417TB$ 物理容量，考虑 RAID6 冗余系数 1.2，需 $417 \times 1.2 \approx 500TB$ 物理容量，即需 25-32 块 16-20TB HDD

## Evidence

[质询]RAID6 冗余系数 1.2 的假设较为理想化，实际 RAID6 通常需至少 2 块盘做校验，若使用 16TB 盘，2 块校验盘占比约为 2/25=8%，系数为 1.08 而非 1.2；若系数 1.2 成立，则隐含了更多的校验盘或更小的盘数，这与“25-32 块”的范围在边界上可能存在轻微张力，但整体量级和逻辑链条自洽。 | 先验知识/题面给定，逻辑校验通过：1. 格式化损耗 3-5% 符合 HDD 实际表现；2. 400/0.96≈417 计算正确；3. 417*1.2≈500 计算正确；4. 500TB / 16TB ≈ 31.25 块，500TB / 20TB = 25 块，落在 25-32 块区间内，逻辑自洽。

## Search Query

enterprise HDD usable capacity overhead RAID6 physical to logical conversion
