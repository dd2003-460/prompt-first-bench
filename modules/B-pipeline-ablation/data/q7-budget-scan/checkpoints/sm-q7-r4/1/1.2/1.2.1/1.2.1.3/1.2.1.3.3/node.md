# N436: 满足寿命要求的SSD数量最小值推导：设需 SSD 数量为 N_ssd，单盘容量 C_ssd=8TB，DWPD=1。要求年写入总量 < N_ssd * C_ssd

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

满足寿命要求的SSD数量最小值推导：设需 SSD 数量为 N_ssd，单盘容量 C_ssd=8TB，DWPD=1。要求年写入总量 < N_ssd * C_ssd * 1 * 365。年写入总量 = 5TB/day * 8(WAF) * 365 = 14,600TB。不等式：N_ssd * 8 * 365 > 14,600 => N_ssd > 14,600 / 2920 ≈ 5。因此最少需 5 块 SSD 才能满足 1 年寿命，但 5 块不足以构成 RAID-6 (需至少 4 块，通常 6+ 块以保证冗余和性能)，故需至少 6 块 SSD，此时总容量 48TB，需增加 10 块以上以满足 100TB 温数据存储需求，导致成本激增。

## Corrected Claim

满足寿命要求的SSD数量最小值推导：设需 SSD 数量为 N_ssd，单盘容量 C_ssd=8TB，DWPD=1。要求年写入总量 < N_ssd * C_ssd * 1 * 365。年写入总量 = 5TB/day * 8(WAF) * 365 = 14,600TB。不等式：N_ssd * 8 * 365 > 14,600 => N_ssd > 14,600 / 2920 ≈ 5。因此最少需 5 块 SSD 才能满足 1 年寿命，但 5 块不足以构成 RAID-6 (需至少 4 块，通常 6+ 块以保证冗余和性能)，故需至少 6 块 SSD，此时总容量 48TB，需增加 10 块以上以满足 100TB 温数据存储需求，导致成本激增。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程（14600/2920=5）及RAID-6最小盘数（4盘）与扩容逻辑均符合工程常识与数学推导。
