# N69: 单卡 BF16 方案的维护成本 C_maint 估算：消费级 GPU 无 ECC，故障率约为 1-2%/年，维护成本约为 $100-$200/年（含驱动更新和潜

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

单卡 BF16 方案的维护成本 C_maint 估算：消费级 GPU 无 ECC，故障率约为 1-2%/年，维护成本约为 $100-$200/年（含驱动更新和潜在硬件更换）；数据中心级 GPU 有 ECC 和冗余设计，故障率约为 0.5-1%/年，维护成本约为 $50-$100/年（主要为人力巡检成本）。

## Corrected Claim

单卡 BF16 方案的维护成本 C_maint 估算：消费级 GPU 无 ECC，故障率约为 1-2%/年，维护成本约为 $100-$200/年（含驱动更新和潜在硬件更换）；数据中心级 GPU 有 ECC 和冗余设计，故障率约为 0.5-1%/年，维护成本约为 $50-$100/年（主要为人力巡检成本）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU failure rate per year consumer vs datacenter ECC impact
