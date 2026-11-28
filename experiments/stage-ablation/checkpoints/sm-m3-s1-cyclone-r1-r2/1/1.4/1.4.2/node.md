# N37: 地表拖曳系数 C_d 与粗糙度长度 z0 及中性层结湍流参数 K 的关系式：C_d ≈ (κ²/ln(z/z0))²，其中 κ≈0.4 为冯·卡门常数；当 z0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

地表拖曳系数 C_d 与粗糙度长度 z0 及中性层结湍流参数 K 的关系式：C_d ≈ (κ²/ln(z/z0))²，其中 κ≈0.4 为冯·卡门常数；当 z0 从 0.01m 增至 0.5m 时，ln(10/0.01)≈6.9 变为 ln(10/0.5)≈3.0，C_d 理论增幅约 (6.9/3.0)² ≈ 5.3 倍。

## Corrected Claim

地表拖曳系数 C_d 与粗糙度长度 z0 及中性层结湍流参数 K 的关系式：C_d ≈ (κ²/ln(z/z0))²，其中 κ≈0.4 为冯·卡门常数；当 z0 从 0.01m 增至 0.5m 时，ln(10/0.01)≈6.9 变为 ln(10/0.5)≈3.0，C_d 理论增幅约 (6.9/3.0)² ≈ 5.3 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合中性层结下莫根滕斯特伦关系（Momentum Balance），数值计算 ln(1000)≈6.9, ln(20)≈3.0, (6.9/3.0)^2≈5.29，量级与逻辑均正确。

## Search Query

drag coefficient formula roughness length logarithmic wind profile von karman constant
