# N367: L2 容量 C_L2 与成本的关系：在公有云场景下，L2 通常由中心节点提供，不计入额外带宽成本但增加延迟；在自建场景下，C_L2 对应中心机房的存储成本，每 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N113

## Claim

L2 容量 C_L2 与成本的关系：在公有云场景下，L2 通常由中心节点提供，不计入额外带宽成本但增加延迟；在自建场景下，C_L2 对应中心机房的存储成本，每 TB SSD 月租金约为 ¥200-500，若 C_L2 = 5TB，则 C_infra_L2 ≈ ¥1000-2500/月，分摊到每千请求成本约为 ¥0.0005-0.0012/1000req。

## Corrected Claim

在自建场景下，C_L2 对应中心机房的存储成本，具体金额取决于所选存储类型（SSD/HDD）及供应商，若 C_L2 = 5TB，需根据实际采购价格计算 C_infra_L2。

## Evidence

[质询]具体价格数值（¥200-500/TB/月）及分摊成本属于经验事实，缺乏来源支持，且不同云厂商/地区价格差异较大，该区间可能不准确或过时。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

CDN L2 center node storage cost per TB SSD monthly
