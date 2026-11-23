# N109: 短视频对象平均大小s_video：基于720p/1080p H.265编码，时长15s-60s，码率2-8Mbps，计算得s_video ∈ [3.75MB, 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

短视频对象平均大小s_video：基于720p/1080p H.265编码，时长15s-60s，码率2-8Mbps，计算得s_video ∈ [3.75MB, 30MB]，取典型值10MB（对应720p 15s 4Mbps）用于带宽成本计算

## Corrected Claim

短视频对象平均大小s_video：基于720p/1080p H.265编码，时长15s-60s，码率2-8Mbps，计算得s_video ∈ [3.75MB, 30MB]，取典型值10MB（对应720p 15s 4Mbps）用于带宽成本计算

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应参数空间的低、中、高三个典型工作点（Low/Mid/High），彼此在数值和适用场景上互斥且无重叠，覆盖了父节点定义的[3.75MB, 30MB]范围及典型值10MB，逻辑正交且完备。虽然本质上是同一参数`s_video`的不同取值，但在架构分解中将其作为‘设计工作点’或‘场景配置’进行枚举是合理的，不属于冗余错误，而是对参数离散化后的具体实例化。）
