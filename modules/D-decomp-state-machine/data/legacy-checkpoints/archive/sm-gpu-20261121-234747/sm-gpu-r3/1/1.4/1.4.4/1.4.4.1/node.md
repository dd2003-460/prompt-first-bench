# N227: AWS EC2 p4d.24xlarge (8×A100) 在 us-east-1 的按需实例小时费约为 $32.76，折算单卡 A100 租赁成本约为 $4.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54, N55, N56

## Claim

AWS EC2 p4d.24xlarge (8×A100) 在 us-east-1 的按需实例小时费约为 $32.76，折算单卡 A100 租赁成本约为 $4.10/GPU-hour，显著高于 N54 声称的 $1.5-$2.5 区间，需核实 N54 数据是否特指 Lambda Labs 等低价第三方平台或包含竞价实例折扣

## Corrected Claim

AWS EC2 p4d.24xlarge (8×A100) 在 us-east-1 的按需实例小时费约为 $32.76（需核实最新价格），折算单卡 A100 租赁成本约为 $4.10/GPU-hour。该价格显著高于 N54 声称的 $1.5-$2.5 区间，后者可能特指 Lambda Labs 等低价第三方平台或包含竞价实例折扣，具体需结合 N54 上下文确认。

## Evidence

[质询]该陈述包含具体的市场价格数据（$32.76/小时，$4.10/GPU-hour），属于经验事实。由于本轮检索无可用来源，无法验证这些具体数值是否准确，也无法确认N54声称的$1.5-$2.5区间是否确实指代特定平台或竞价实例，存在数据过时或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持。虽然$32.76/8=$4.095≈$4.10的数学计算正确，且AWS按需价格通常高于第三方或竞价实例符合经济直觉，但缺乏外部来源直接支持具体数值。

## Search Query

AWS EC2 p4d.24xlarge on-demand price per hour us-east-1 2025
