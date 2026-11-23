# N65: 加权平均对象大小 s_avg = (N_img * s_img + N_vid * s_vid) / (N_img + N_vid)，其中 N_img 和 N_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

加权平均对象大小 s_avg = (N_img * s_img + N_vid * s_vid) / (N_img + N_vid)，其中 N_img 和 N_vid 为图片与短视频的请求次数比，需根据业务数据确定（例如若图片请求占 80%，视频占 20%，则 s_avg ≈ 0.8*0.5MB + 0.2*10MB = 2.4MB）

## Corrected Claim

加权平均对象大小 s_avg = (N_img * s_img + N_vid * s_vid) / (N_img + N_vid)，其中 N_img 和 N_vid 为图片与短视频的请求次数比，需根据业务数据确定（例如若图片请求占 80%，视频占 20%，则 s_avg ≈ 0.8*0.5MB + 0.2*10MB = 2.4MB）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别聚焦于计算实例、对存储容量（对象数量/命中率）的影响、以及对带宽成本的影响，三个维度互不重叠且逻辑独立。父节点核心是定义s_avg及其业务依赖，子节点涵盖了其计算方法和主要下游影响，覆盖完整。虽然子节点1提供了具体数值，但这属于计算示例而非参数冗余，有助于理解，不构成压缩为单一变量的冗余。）
