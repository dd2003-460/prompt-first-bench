# N30: 上传路径成本结构：C_upload = V_upload * p_upload + C_processing_upload，其中V_upload为日均上传流量（

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

上传路径成本结构：C_upload = V_upload * p_upload + C_processing_upload，其中V_upload为日均上传流量（200GB/天），p_upload为上传带宽价格（通常低于下载，约¥0.1-0.3/GB），C_processing_upload为转码/处理成本（约¥0.5-2/GB）

## Corrected Claim

上传路径成本结构：C_upload = V_upload * p_upload + C_processing_upload，其中V_upload为日均上传流量（200GB/天），p_upload为上传带宽价格（通常低于下载，约¥0.1-0.3/GB），C_processing_upload为转码/处理成本（约¥0.5-2/GB）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个独立变量（p_upload 和 C_processing_upload），内容互不重叠且无矛盾，覆盖了成本结构的两个主要组成部分。）

## Search Query

CDN upload bandwidth pricing and processing cost
