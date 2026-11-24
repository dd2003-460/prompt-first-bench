# N161: 40块NVMe SSD的聚合顺序读取吞吐与功耗：单盘7GB/s，40盘聚合理论值280GB/s，考虑RAID-6 parity计算开销（约10-15%），有效吞

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

40块NVMe SSD的聚合顺序读取吞吐与功耗：单盘7GB/s，40盘聚合理论值280GB/s，考虑RAID-6 parity计算开销（约10-15%），有效吞吐≈240-250GB/s；总静态功耗 = 40 × 8W = 320W，动态功耗（满负荷）= 40 × 12W = 480W，年电力成本（PUE 1.4，¥0.8/kWh）= 0.48kW × 1.4 × 0.8 × 8760 ≈ ¥4,700/年。

## Corrected Claim

40块NVMe SSD的聚合顺序读取吞吐与功耗：单盘7GB/s，40盘聚合理论值280GB/s，考虑RAID-6 parity计算开销（约10-15%），有效吞吐≈240-250GB/s；总静态功耗 = 40 × 8W = 320W，动态功耗（满负荷）= 40 × 12W = 480W，年电力成本（PUE 1.4，¥0.8/kWh）= 0.48kW × 1.4 × 0.8 × 8760 ≈ ¥4,700/年。

## Evidence

先验知识/题面给定，逻辑校验通过：吞吐量计算（7*40=280，扣除10-15%开销后约为240-250）及功耗成本计算（480W*1.4*0.8*8760h ≈ 4700元）均符合算术逻辑与工程常识。

## Search Query

NVMe SSD aggregate throughput RAID-6 power consumption enterprise
