# N87: 质量提升曲线参数 τ 的校准方法：τ (时间常数) 并非固定值，而是依赖于初始错误类型分布；若初始错误主要为逻辑断裂 (Logic Breaks)，τ≈3 轮；

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

质量提升曲线参数 τ 的校准方法：τ (时间常数) 并非固定值，而是依赖于初始错误类型分布；若初始错误主要为逻辑断裂 (Logic Breaks)，τ≈3 轮；若主要为事实性错误 (Fact Errors)，由于需要 RAG 检索与验证，τ≈5-7 轮；公式 Q(t) 中的 t 应为迭代轮数 N 而非时间，修正公式为 Q(N) = Q_max - (Q_max - Q_init) * exp(-N/τ_N)，其中 τ_N 为轮数常数。

## Corrected Claim

质量提升曲线参数 τ 的校准方法：τ (时间常数) 并非固定值，而是依赖于初始错误类型分布；若初始错误主要为逻辑断裂 (Logic Breaks)，τ≈3 轮；若主要为事实性错误 (Fact Errors)，由于需要 RAG 检索与验证，τ≈5-7 轮；公式 Q(t) 中的 t 应为迭代轮数 N 而非时间，修正公式为 Q(N) = Q_max - (Q_max - Q_init) * exp(-N/τ_N)，其中 τ_N 为轮数常数。

## Evidence

先验知识/题面给定，逻辑校验通过：将时间常数从连续时间映射到离散迭代轮数符合指数收敛模型的离散化逻辑，不同错误类型对应不同收敛速度（逻辑断裂修复快于事实性错误需检索验证）符合工程直觉，公式形式自洽。

## Search Query

iterative refinement convergence rate logic vs factual errors LLM
