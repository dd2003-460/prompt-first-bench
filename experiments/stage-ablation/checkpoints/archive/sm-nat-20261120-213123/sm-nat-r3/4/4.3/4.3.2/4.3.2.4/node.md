# N130: LFU 与 LRU 在热度漂移场景下的命中率对比公式 $\Delta_{drift} \approx 0.5 \cdot dP/dt \cdot T_{lag\

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57, N58, N59

## Claim

LFU 与 LRU 在热度漂移场景下的命中率对比公式 $\Delta_{drift} \approx 0.5 \cdot dP/dt \cdot T_{lag\_time}$ 中，$T_{lag\_time}$ 并非固定为 20s，而是取决于 LFU 计数器的响应时间常数 $\tau_{LFU} = T_{counter} / \ln(2)$；对于 $T_{counter}=1day$，$\tau_{LFU} \approx 1.44 days$，远大于 LRU 的 $\tau_{LRU} \approx 1/\lambda_{avg}$（秒级）；因此当 $dP/dt > 0.1\%/day$ 时，$\Delta_{drift} \approx 0.5 \cdot 0.001 \cdot 1.44 \cdot 86400s \approx 622$（无意义，单位错误），需修正为 $\Delta_{drift} \approx (dP/dt) \cdot \tau_{LFU} / \tau_{LRU}$，在 $dP/dt=0.1\%/day$ 下，$\Delta_{drift} \approx 0.001 \cdot (1.44 \cdot 86400) / (1/500000) \approx 62200$，表明公式失效，需采用仿真或基于 Markov 链的解析解。

## Corrected Claim

LFU 与 LRU 在热度漂移场景下的命中率差异取决于 LFU 的响应时间常数 τ_LFU 与 LRU 的响应时间常数 τ_LRU 的比值，以及热度漂移速率 dP/dt。由于 LFU 的 τ_LFU 通常远大于 LRU 的 τ_LRU，LFU 在快速变化的工作负载下表现较差。具体的命中率差值 Δ 需要通过仿真或基于 Markov 链的解析模型计算，简单的线性近似公式 Δ ≈ (dP/dt) * τ_LFU / τ_LRU 量纲错误，不可直接使用。

## Evidence

[质询]公式推导存在严重的量纲错误和逻辑跳跃：1. 原始公式 Δ ≈ 0.5 * (dP/dt) * T_lag 中，dP/dt 是概率变化率（1/时间），T_lag 是时间，乘积无量纲，但命中率差值 Δ 通常也是无量纲或百分比，量纲上看似可行但物理意义不明；2. 修正后的公式 Δ ≈ (dP/dt) * τ_LFU / τ_LRU 中，(dP/dt) 单位是 1/时间，τ_LFU/τ_LRU 无量纲，结果单位是 1/时间，这与命中率差值（无量纲）量纲不符；3. 数值计算中，dP/dt=0.1%/day = 0.001/86400s ≈ 1.16e-8 s^-1，τ_LFU ≈ 1.24e5 s，τ_LRU ≈ 2e-5 s（假设 λ=500000/s），则 Δ ≈ 1.16e-8 * 1.24e5 / 2e-5 ≈ 71.8，这是一个无量纲数，但原文计算过程混乱，且 62200 这个数值来源不明，量级巨大，不符合命中率差值应在 [0,1] 或 [0,100%] 的常识。 | 先验知识/题面给定，逻辑校验失败：公式量纲不一致，修正后的公式量纲仍错误，且数值计算过程存在明显错误，无法从第一性原理推出该具体公式及数值。
