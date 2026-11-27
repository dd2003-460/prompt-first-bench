# N71: LFU在Pareto(β=0.9)分布下的频率老化滞后损失ε_LFU，定义为因频率计数器未收敛或历史权重过高导致的误驱逐率，其量级与更新率λ_update和平均

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20, N21, N22

## Claim

LFU在Pareto(β=0.9)分布下的频率老化滞后损失ε_LFU，定义为因频率计数器未收敛或历史权重过高导致的误驱逐率，其量级与更新率λ_update和平均驻留时间T_resident的乘积λ*T_resident成正比，当λ*T_resident<0.1时ε_LFU≈0。

## Corrected Claim

LFU在Pareto(β=0.9)分布下的频率老化滞后损失ε_LFU通常与更新率λ_update和平均驻留时间T_resident的乘积λ*T_resident正相关，当该乘积较小时（如<0.1），ε_LFU显著降低，但具体数值关系需依赖实验或特定模型验证。

## Evidence

[质询]该陈述将LFU的误驱逐率（经验性能指标）与特定参数乘积（λ*T_resident）建立严格的线性正比关系，并给出精确阈值（<0.1时≈0），这属于具体的经验事实/工程参数，无法从第一性原理严格推导，且缺乏通用理论支持该特定量级关系。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值关系非第一性原理可推导）

## Search Query

LFU frequency aging lag loss Pareto distribution update rate lambda T_resident convergence
