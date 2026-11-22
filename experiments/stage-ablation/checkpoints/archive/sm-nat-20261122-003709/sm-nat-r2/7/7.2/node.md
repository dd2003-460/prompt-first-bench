# N86: 计算LFU频率计数器在1%/天更新率下的收敛时间常数τ_convergence，定义为计数器达到稳态值95%所需的时间，公式为 τ_convergence ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

计算LFU频率计数器在1%/天更新率下的收敛时间常数τ_convergence，定义为计数器达到稳态值95%所需的时间，公式为 τ_convergence ≈ 3 / λ_update，其中λ_update=0.01/day，得出具体天数。

## Corrected Claim

计算LFU频率计数器在1%/天更新率下的收敛时间常数τ_convergence，定义为计数器达到稳态值95%所需的时间，公式为 τ_convergence ≈ 3 / λ_update，其中λ_update=0.01/day，得出具体天数。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型中达到95%稳态需约3个时间常数（1/e^3 ≈ 0.05），τ=1/λ=100天，故3/λ=300天，推导自洽。

## Search Query

LFU frequency counter convergence time constant update rate
