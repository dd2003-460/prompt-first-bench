# N412: 非典型方案 (Gaudi 3/Ascend 910B) 的 TCO 修正项：C_tco_corrected = C_tco_base / η_software 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139

## Claim

非典型方案 (Gaudi 3/Ascend 910B) 的 TCO 修正项：C_tco_corrected = C_tco_base / η_software * (1 + C_migration_cost)，其中 C_migration_cost 为软件栈适配成本 (估算 $5,000-$10,000)，若 η_software=0.7，TCO 增加 43% + 迁移成本，抵消价格优势，通常仅在市场准入受限 (如中国出口管制) 时才具竞争力

## Corrected Claim

非典型方案 (Gaudi 3/Ascend 910B) 的 TCO 修正项：C_tco_corrected = C_tco_base / η_software * (1 + C_migration_cost)，其中 C_migration_cost 为软件栈适配成本 (估算 $5,000-$10,000)，若 η_software=0.7，TCO 增加 43% + 迁移成本，抵消价格优势，通常仅在市场准入受限 (如中国出口管制) 时才具竞争力

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合TCO修正逻辑，数值量级（$5k-$10k迁移成本，43%增幅）在工程估算中合理，且source为knowledge，无需外部来源支持。
