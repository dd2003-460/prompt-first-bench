# N61: LFU 频率遗忘率模型（中性价比最优）：LFU 有效命中率 H_LFU = H_LRU + Δ_H * exp(-λ_forget * T)，其中 Δ_H 为理

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

LFU 频率遗忘率模型（中性价比最优）：LFU 有效命中率 H_LFU = H_LRU + Δ_H * exp(-λ_forget * T)，其中 Δ_H 为理论增益，λ_forget 为频率遗忘率，T 为时间窗口，源自 Cao et al. 1997 的 LFU 变体分析。

## Corrected Claim

LFU 算法通过记录访问频率来优化缓存替换，但存在‘频率老化’问题，即旧的高频对象可能长期占据缓存。Cao et al. (1997) 等研究指出，简单的 LFU 在动态工作负载下表现不佳，通常引入时间衰减因子（如 LRU-K 或 2Q）来缓解此问题，而非使用特定的指数增益公式。

## Evidence

[质询]该公式形式（H_LFU = H_LRU + Δ_H * exp(-λ_forget * T)）并非 Cao et al. 1997 论文中的标准结论或通用定义。Cao et al. 主要提出了 LRU-K 和 2Q 等算法，虽然讨论了 LFU 的局限性（如频率老化），但并未给出这样一个具体的、带有指数衰减项的命中率解析公式。这极有可能是对 LFU 频率老化机制（Frequency Aging）的某种简化或错误重构，将‘频率随时间衰减’的概念错误地映射到了‘命中率增益’上，且缺乏明确的理论推导支持该特定函数形式。 | 先验知识/题面给定，逻辑校验未通过：公式形式与经典 LFU 理论及 Cao et al. 1997 的核心贡献不符，存在概念混淆风险（将频率衰减机制误用为命中率增益模型），且无来源支持该特定解析式。
