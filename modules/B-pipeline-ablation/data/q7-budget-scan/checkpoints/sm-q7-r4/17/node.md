# N303: 云对象存储的初始迁移成本（Ingestion Cost）量化：将 500TB 本地数据上传至云对象存储（如阿里云 OSS/AWS S3）产生的公网流入流量费（I

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

云对象存储的初始迁移成本（Ingestion Cost）量化：将 500TB 本地数据上传至云对象存储（如阿里云 OSS/AWS S3）产生的公网流入流量费（Ingress Traffic）通常免费，但数据传输过程中的带宽占用及潜在的专线租赁前置费用（若使用 Express Connect/Direct Connect 进行初始批量传输以避免公网拥塞）约为 ¥5,000 - ¥20,000（一次性），若仅走公网则无直接费用但耗时极长（按 1Gbps 专线约需 6 天，按 10Gbps 约需 0.6 天），此隐性时间成本需折算。

## Corrected Claim

云对象存储的初始迁移成本（Ingestion Cost）量化：将 500TB 本地数据上传至云对象存储（如阿里云 OSS/AWS S3）产生的公网流入流量费（Ingress Traffic）通常免费，但数据传输过程中的带宽占用及潜在的专线租赁前置费用（若使用 Express Connect/Direct Connect 进行初始批量传输以避免公网拥塞）约为 ¥5,000 - ¥20,000（一次性），若仅走公网则无直接费用但耗时极长（按 1Gbps 专线约需 6 天，按 10Gbps 约需 0.6 天），此隐性时间成本需折算。

## Evidence

检索失败: no sources from any channel (all 5 failed)
