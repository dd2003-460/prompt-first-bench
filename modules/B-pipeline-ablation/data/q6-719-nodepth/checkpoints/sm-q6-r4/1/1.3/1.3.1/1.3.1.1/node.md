# N162: T_queue（排队延迟）遵循 M/M/c 模型，其期望值 T_queue = (1/(μ×c - λ))，其中 c 为边缘节点并发处理核心数，μ 为单核服务速

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

T_queue（排队延迟）遵循 M/M/c 模型，其期望值 T_queue = (1/(μ×c - λ))，其中 c 为边缘节点并发处理核心数，μ 为单核服务速率，λ 为到达请求率；在日均 2TB 下载且峰值 4 小时承载的情况下，λ ≈ 2TB/4h/ReqSize，需代入具体并发数 c 计算 1-5ms 的区间边界

## Corrected Claim

T_queue（排队延迟）遵循 M/M/c 模型，其期望值需通过 Erlang C 公式计算，而非简单的 1/(μ×c - λ)；在日均 2TB 下载且峰值 4 小时承载的情况下，λ ≈ 2TB/4h/ReqSize，需代入具体并发数 c 及 Erlang C 公式计算 1-5ms 的区间边界

## Evidence

[质询]公式错误：M/M/c 模型的排队延迟期望值并非简单的 1/(μc - λ)，该公式是 M/M/1 模型在特定条件下的近似或 M/M/∞ 的某种变体，M/M/c 需要利用 Erlang C 公式计算，且 1/(μc - λ) 量纲虽为时间，但数值通常远大于毫秒级（除非 μ 极大），直接使用该简化公式会导致量级严重偏差。 | 先验知识/题面给定，逻辑校验发现公式与标准 M/M/c 模型定义不符，存在硬逻辑错误（公式误用），故降级。
