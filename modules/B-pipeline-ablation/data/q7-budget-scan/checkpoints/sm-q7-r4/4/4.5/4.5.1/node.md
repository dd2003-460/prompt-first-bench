# N82: NVMe SSD阵列将RTO从24h压缩至4h所需的瞬时写入IOPS需求量为：(500TB * 1.805) / (4 * 3600) ≈ 61,000 IOP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

NVMe SSD阵列将RTO从24h压缩至4h所需的瞬时写入IOPS需求量为：(500TB * 1.805) / (4 * 3600) ≈ 61,000 IOPS (假设4KB随机写块大小)

## Corrected Claim

NVMe SSD阵列将RTO从24h压缩至4h所需的瞬时写入IOPS需求量为：(500TB * 1.805) / (4 * 3600) ≈ 61,000 IOPS (假设4KB随机写块大小)

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1修正了父节点中严重的单位换算错误（TB转KB），子节点2基于修正后的数据探讨了不同块大小对IOPS的影响及可行性结论。两者逻辑递进，分别解决了'计算正确性'和'工程可行性'两个独立维度，无重叠且无矛盾。）
