# N156: inode表内存缓存压力：5亿inode × 256B = 128GB元数据，若全部常驻内存，占256GB RAM的50%；剩余128GB用于页缓存，导致数据页

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

inode表内存缓存压力：5亿inode × 256B = 128GB元数据，若全部常驻内存，占256GB RAM的50%；剩余128GB用于页缓存，导致数据页命中率下降，增加SSD随机读次数，间接增加功耗和IOPS消耗，估算额外功耗增量约5-10W。

## Corrected Claim

inode表内存缓存压力：5亿inode × 256B = 128GB元数据，若全部常驻内存，占256GB RAM的50%；剩余128GB用于页缓存，导致数据页命中率下降，增加SSD随机读次数，间接增加功耗和IOPS消耗，估算额外功耗增量约5-10W。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别处理了内存占比修正、命中率计算和功耗推导三个独立环节。但存在严重的不完备性：子节点2中关于命中率的计算示例存在逻辑错误（230.4GB缓存覆盖200GB热数据，命中率应为100%而非下降，且未展示真正导致命中率下降的场景），未能有效分解‘命中率下降’这一核心因果链；此外，父节点提到的‘5-10W’估算缺乏具体的数据规模前提（如总扫描量、对象分布），子节点3仅给出了公式而未结合前两个子节点的结论进行闭环验证，导致最终功耗估算缺乏支撑。）

## Search Query

Linux page cache vs inode cache memory pressure storage performance
