# N365: Intel Gaudi 2 的 5 年 TCO 量化估算：硬件 CapEx 约为 $10,000 [待核验]，功耗 TDP 约为 650W（整卡），5 年电力成

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N124

## Claim

Intel Gaudi 2 的 5 年 TCO 量化估算：硬件 CapEx 约为 $10,000 [待核验]，功耗 TDP 约为 650W（整卡），5 年电力成本 = 650W * 1.1 * 24h * 365d * 5y * $0.10/kWh ≈ $1,555；总 TCO ≈ $11,555，显著高于 RTX 4090 方案（~$4,000-5,000）但低于 H100 方案（~$12,000+）。

## Corrected Claim

Intel Gaudi 2 的 5 年 TCO 量化估算：硬件 CapEx 具体数值需依据实际采购价格确定（通常高于 $10,000），功耗 TDP 约为 650W（整卡），5 年电力成本 ≈ $1,555；总 TCO 取决于硬件成本，通常显著高于 RTX 4090 方案，与 H100 方案相比需结合具体硬件价格判断。

## Evidence

[质询]硬件 CapEx 约为 $10,000 这一数值缺乏来源支持，且 Gaudi 2 作为数据中心加速卡，其实际市场采购价格通常远高于 $10,000（通常在 $15,000-$20,000+ 区间），该数值可能严重低估了硬件成本，导致总 TCO 估算偏低。 | 经验事实，逻辑自洽但缺来源支持；电力成本计算逻辑正确（650W * 1.1 * 24 * 365 * 5 * 0.1 ≈ $1,555），但硬件 CapEx 为经验参数，无外部来源验证，且 $10,000 的估值可能不符合市场实际，故降级。

## Search Query

Intel Gaudi 2 TDP power consumption watts
