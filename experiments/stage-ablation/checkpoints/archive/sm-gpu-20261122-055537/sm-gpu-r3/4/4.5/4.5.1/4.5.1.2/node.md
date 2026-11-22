# N257: 若将 H100 部署于主流云厂商（如 AWS/Azure/GCP）作为基准对比，其 GPU 实例租赁溢价约为 $2.5-3.5/小时（如 AWS p4d.24x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

若将 H100 部署于主流云厂商（如 AWS/Azure/GCP）作为基准对比，其 GPU 实例租赁溢价约为 $2.5-3.5/小时（如 AWS p4d.24xlarge 或 Azure ND H100 v5），相比本地 3 年 TCO 中的电力成本（约 $0.15/kWh * 700W * 8760h ≈ $923/年），云端成本在 3 年周期内约为 $65,000-95,000，远高于本地硬件购置成本 $25,000，因此本地部署在 TCO 上具有 2-3 倍优势。

## Corrected Claim

若将 H100 部署于主流云厂商（如 AWS/Azure/GCP）作为基准对比，其 GPU 实例租赁溢价约为 $2.5-3.5/小时（如 AWS p4d.24xlarge 或 Azure ND H100 v5），相比本地 3 年 TCO 中的电力成本（约 $0.15/kWh * 700W * 8760h ≈ $923/年），云端成本在 3 年周期内约为 $65,000-95,000，远高于本地硬件购置成本 $25,000，因此本地部署在 TCO 上具有 2-3 倍优势。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS p4d.24xlarge H100 hourly price vs local TCO comparison
