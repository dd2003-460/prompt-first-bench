# N311: 在二手交易平台的假设验证场景中，若错误接受错误假设（如误判买家驱动均衡）导致的策略失误成本（$C_{strategy}$）远高于错误拒绝正确假设的成本（$C_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

在二手交易平台的假设验证场景中，若错误接受错误假设（如误判买家驱动均衡）导致的策略失误成本（$C_{strategy}$）远高于错误拒绝正确假设的成本（$C_{wait}$），则决策阈值 $\theta_{MAP}$ 应设为 $\frac{C_{wait}}{C_{wait} + C_{strategy}}$。例如，若 $C_{strategy} = 5 \times C_{wait}$，则 $\theta_{MAP} = 0.167$，此时 $P(H|D) < 0.5$ 仍可能支持采取该假设行动。

## Corrected Claim

在二手交易平台的假设验证场景中，若错误接受错误假设（如误判买家驱动均衡）导致的策略失误成本（$C_{strategy}$）远高于错误拒绝正确假设的成本（$C_{wait}$），则决策阈值 $\theta_{MAP}$ 应设为 $\frac{C_{wait}}{C_{wait} + C_{strategy}}$。例如，若 $C_{strategy} = 5 \times C_{wait}$，则 $\theta_{MAP} = 0.167$，此时 $P(H|D) < 0.5$ 仍可能支持采取该假设行动。

## Evidence

先验知识/题面给定，逻辑校验通过：基于贝叶斯决策理论，最小化期望损失的最优阈值公式为 θ = C_wait / (C_wait + C_strategy)，代入 C_strategy = 5 * C_wait 计算得 1/6 ≈ 0.167，且该阈值低于 0.5 符合高风险行动需更低后验概率支持的直觉。
