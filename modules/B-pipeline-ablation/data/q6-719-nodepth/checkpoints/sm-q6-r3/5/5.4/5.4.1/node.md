# N113: 公有云CDN因地缘政策导致的服务中断/降级概率 P_cloud_outage 极低（<0.01%），且通常包含在SLA赔付条款内，无额外显性风险溢价成本

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

公有云CDN因地缘政策导致的服务中断/降级概率 P_cloud_outage 极低（<0.01%），且通常包含在SLA赔付条款内，无额外显性风险溢价成本

## Corrected Claim

公有云CDN因地缘政策导致的服务中断/降级概率通常极低，且此类风险通常包含在SLA赔付条款内，一般不产生额外的显性风险溢价成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于概率基准值的推导（风险频率），子节点2聚焦于赔付覆盖率及剩余成本计算（风险影响/成本）。两者分别对应风险量化中的‘概率’和‘损失/补偿’维度，逻辑上正交且互补。父节点声称‘无额外显性风险溢价成本’，子节点2通过公式 Residual_Risk_Cost = (1 - Coverage) * Loss 揭示了‘显性’与‘隐性/剩余’成本的界限，虽然父节点结论略显绝对（通常剩余成本被视为隐性风险而非显性溢价，但在此语境下可理解为无额外的保费支出），但子节点准确拆解了构成该结论的两个关键参数（概率和覆盖率），覆盖了父节点的核心逻辑。）

## Search Query

cloud CDN SLA geopolitical risk compensation clause
