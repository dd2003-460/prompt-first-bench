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

父节点级核验通过：正交+完备+无冗余（父节点的核心任务是计算收敛时间常数，但隐含了错误的公式前提。唯一的子节点指出了该前提错误（混淆了更新率与请求率），并提供了修正后的公式及基于正确参数的计算结果。由于只有一个子节点，不存在正交性冲突或冗余问题；该子节点覆盖了父节点中“公式修正”和“重新计算”两个关键方面，因此是完备的。）

## Search Query

LFU frequency counter convergence time constant update rate
