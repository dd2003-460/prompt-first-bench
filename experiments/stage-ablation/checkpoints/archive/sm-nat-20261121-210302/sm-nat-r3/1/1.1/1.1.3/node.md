# N26: 最大对象大小 S_max 在 CDN 缓存中通常受限于单文件最大允许缓存大小，常见上限为 100MB 或 1GB，需结合 128GB 内存限制和实际对象分布尾部

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

最大对象大小 S_max 在 CDN 缓存中通常受限于单文件最大允许缓存大小，常见上限为 100MB 或 1GB，需结合 128GB 内存限制和实际对象分布尾部确定。

## Corrected Claim

最大对象大小 S_max 在 CDN 缓存中受限于具体服务商的单文件最大允许缓存大小（不同厂商限制从几MB到数百GB不等），需结合具体CDN策略、内存限制和实际对象分布尾部确定。

## Evidence

父节点级核验未通过：不完备, 有冗余（工作点A和工作点B本质上是同一参数（S_max）在不同约束下的两个具体取值，属于冗余分解而非正交维度；同时，父节点强调需结合'实际对象分布尾部'，但子节点中缺乏关于对象大小分布统计特性（如CDF、长尾特征）对S_max选择的直接分析，导致完备性不足。）

## Search Query

CDN cache maximum object size limit typical value
