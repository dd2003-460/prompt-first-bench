# N62: 买家被动性的量化指标：定义买家主动搜索率 S_active = N_active_searches / N_total_views，若 S_active < 0

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

买家被动性的量化指标：定义买家主动搜索率 S_active = N_active_searches / N_total_views，若 S_active < 0.2 且降价后48小时咨询量变化率 ΔQ < 5%（p>0.05），则证实买家主要依赖算法推送而非主动搜索，支持平台驱动论。

## Corrected Claim

买家被动性的量化指标：定义买家主动搜索率 S_active = N_active_searches / N_total_views。若 S_active 显著低于行业基准（例如 < 0.2）且降价后48小时咨询量变化率 ΔQ 不显著（p>0.05），则提示买家可能主要依赖算法推送而非主动搜索，需结合其他行为数据进一步验证平台驱动论。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了核心指标S_active的计算口径、辅助指标ΔQ的统计检验方法，以及综合判定逻辑（引入了父节点未提及但逻辑上必要的R_rec指标）。三者分别对应“输入定义”、“统计方法”和“决策规则”，维度清晰，无重复或矛盾。虽然子节点3引入了新变量R_rec，但这属于对“平台驱动论”证据链的合理补全，而非冗余。）

## Search Query

buyer active search rate vs algorithmic recommendation dependency online marketplace behavior study
