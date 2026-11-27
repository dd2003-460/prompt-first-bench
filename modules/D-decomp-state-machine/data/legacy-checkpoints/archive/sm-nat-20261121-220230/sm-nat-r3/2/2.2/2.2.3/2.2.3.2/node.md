# N151: 决策错误率 P_error 与滞后误差 Δ_f 的阈值关系：当 Δ_f > f_threshold 时，LFU 误驱逐概率 P_error ≈ 1 - exp(

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

决策错误率 P_error 与滞后误差 Δ_f 的阈值关系：当 Δ_f > f_threshold 时，LFU 误驱逐概率 P_error ≈ 1 - exp(-Δ_f / f_threshold)。若 f_threshold 设为当前缓存中最低驻留对象的热度 h_th（由 N68 计算得出），则 P_error 直接决定 LFU 相对于理想 LFU 的命中率损失 ΔH_loss = P_error * (H_ideal - H_LRU)。

## Corrected Claim

在特定理论模型假设下，决策错误率 P_error 与滞后误差 Δ_f 呈负相关，且 LFU 相对于理想 LFU 的命中率损失 ΔH_loss 与 P_error 及理想与 LRU 命中率之差成正比。

## Evidence

[质询]该陈述中的公式 P_error ≈ 1 - exp(-Δ_f / f_threshold) 以及 ΔH_loss = P_error * (H_ideal - H_LRU) 属于特定的理论模型假设或经验拟合公式，并非缓存替换算法（如LFU）的通用第一性原理或数学恒等式。在缺乏具体模型定义或来源支持的情况下，直接断言这种精确的指数关系和线性损失关系缺乏普适性依据，且 'f_threshold' 的定义依赖于前序节点 N68，存在逻辑链条上的依赖风险。 | source=knowledge，逻辑上量纲自洽（概率无量纲，热度差与阈值同量纲），但具体函数形式（指数衰减）和损失计算公式属于特定模型假设，非通用真理，且无外部来源验证其普适性，故降级为定性表述。

## Search Query

LFU decision error rate threshold frequency mismatch probability
