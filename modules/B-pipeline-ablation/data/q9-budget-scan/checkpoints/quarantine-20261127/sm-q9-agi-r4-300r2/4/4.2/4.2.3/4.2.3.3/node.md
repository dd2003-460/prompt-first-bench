# N175: 通信瓶颈临界序列长度 L_critical：当 C_comm > 20% 时，需满足 L > (0.2 * T_compute * bandwidth_effe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

通信瓶颈临界序列长度 L_critical：当 C_comm > 20% 时，需满足 L > (0.2 * T_compute * bandwidth_effective) / (2 * hidden_dim * batch_size * dtype_bytes)；代入典型参数（T_compute=5ms, bandwidth=250GB/s, hidden=4096, batch=8, dtype=2bytes），L_critical ≈ 78k tokens；超过此长度应启用 Sequence Parallelism 或减小 batch_size 以规避通信瓶颈

## Corrected Claim

通信瓶颈临界序列长度 L_critical：当 C_comm > 20% 时，需满足 L > (0.2 * T_compute * bandwidth_effective) / (2 * hidden_dim * batch_size * dtype_bytes)；代入典型参数（T_compute=5ms, bandwidth=250GB/s, hidden=4096, batch=8, dtype=2bytes），L_critical ≈ 78k tokens；超过此长度应启用 Sequence Parallelism 或减小 batch_size 以规避通信瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合通信量与计算时间平衡的基本原理，数值代入计算准确（0.2*5ms*250GB/s / (2*4096*8*2B) ≈ 78125 tokens），量级合理。

## Search Query

tensor parallelism communication bottleneck critical sequence length threshold
