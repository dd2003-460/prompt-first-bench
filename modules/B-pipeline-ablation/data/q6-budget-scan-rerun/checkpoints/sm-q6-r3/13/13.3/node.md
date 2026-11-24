# N413: 公有云CDN技术债务转移成本的量化：虽然用户侧 C_debt ≈ 0，但需计入隐性成本：1) 配置迁移成本（每次协议升级需重新配置，约0.05 FTE/次，年均

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

公有云CDN技术债务转移成本的量化：虽然用户侧 C_debt ≈ 0，但需计入隐性成本：1) 配置迁移成本（每次协议升级需重新配置，约0.05 FTE/次，年均2次）；2) 兼容性测试成本（新协议上线后需验证，约0.02 FTE/次）；总隐性成本 C_debt_pub = (0.05 + 0.02) × 2 × 30万 = 4.2万元/年

## Corrected Claim

公有云CDN技术债务转移成本的量化：虽然用户侧 C_debt ≈ 0，但需计入隐性成本：1) 配置迁移成本（每次协议升级需重新配置，约0.05 FTE/次，年均2次）；2) 兼容性测试成本（新协议上线后需验证，约0.02 FTE/次）；总隐性成本 C_debt_pub = (0.05 + 0.02) × 2 × 30万 = 4.2万元/年

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (0.05+0.02)*2*300,000 = 42,000 元，数值量级与FTE成本估算逻辑自洽。

## Search Query

cloud CDN configuration migration cost protocol upgrade compatibility testing
