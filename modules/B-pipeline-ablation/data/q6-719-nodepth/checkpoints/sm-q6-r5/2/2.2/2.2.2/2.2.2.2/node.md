# N170: C_self_storage 的量化基准：自建单个 POP 节点通常配置 4-8 台服务器，每台 20-40TB NVMe 存储。单 POP 有效缓存容量 C_

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

C_self_storage 的量化基准：自建单个 POP 节点通常配置 4-8 台服务器，每台 20-40TB NVMe 存储。单 POP 有效缓存容量 C_self_storage ≈ 100-200TB（扣除系统开销和元数据）。若 10 个 POP 分布全国，单 POP 容量受限于本地磁盘，通常 C_self_storage ≈ 50-100TB。取基准值 C_self_storage = 80TB。

## Corrected Claim

C_self_storage 的量化基准：自建单个 POP 节点通常配置 4-8 台服务器，每台 20-40TB NVMe 存储。单 POP 有效缓存容量 C_self_storage ≈ 100-200TB（扣除系统开销和元数据）。若 10 个 POP 分布全国，单 POP 容量受限于本地磁盘，通常 C_self_storage ≈ 50-100TB。取基准值 C_self_storage = 80TB。

## Evidence

父节点级核验未通过：不完备（子节点1计算得出的基准值（104.4TB）与父节点最终采用的基准值（80TB）存在数值矛盾，且未解释差异来源（如是否扣除更多开销或采用保守估计）；子节点2引入了命中率H_self这一新变量，超出了父节点仅定义存储容量C_self_storage的范围，导致主题发散；父节点中关于'10个POP分布'的宏观背景未在子节点中体现。）
