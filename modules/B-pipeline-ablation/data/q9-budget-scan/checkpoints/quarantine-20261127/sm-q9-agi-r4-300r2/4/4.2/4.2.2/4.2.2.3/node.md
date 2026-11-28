# N172: 科研任务类型对 η 的异质性影响：代码生成类子任务 η_code ≈ 0.85-0.90，纯逻辑推理类子任务 η_logic ≈ 0.50-0.60，文献综述类

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

科研任务类型对 η 的异质性影响：代码生成类子任务 η_code ≈ 0.85-0.90，纯逻辑推理类子任务 η_logic ≈ 0.50-0.60，文献综述类子任务 η_survey ≈ 0.65-0.75；混合科研循环中加权平均 η_mix = Σ(w_i * η_i)，其中 w_i 为各子任务 token 占比，直接影响整体 MTP 加速比 S_max = 1 + K * η_mix

## Corrected Claim

科研任务类型对 η 的异质性影响：代码生成类子任务 η_code ≈ 0.85-0.90，纯逻辑推理类子任务 η_logic ≈ 0.50-0.60，文献综述类子任务 η_survey ≈ 0.65-0.75；混合科研循环中加权平均 η_mix = Σ(w_i * η_i)，其中 w_i 为各子任务 token 占比，直接影响整体 MTP 加速比 S_max = 1 + K * η_mix

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

speculative decoding acceptance rate by task type code vs reasoning vs summarization
