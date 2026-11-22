# N359: 统一假设的自洽性验证公式：设高溢价带来的成交加速因子为 k_speed (k_speed > 1)，降价导致的信号污染因子为 k_signal (k_signa

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

统一假设的自洽性验证公式：设高溢价带来的成交加速因子为 k_speed (k_speed > 1)，降价导致的信号污染因子为 k_signal (k_signal < 1)。若 k_speed * (1 + Premium) > k_signal * (1 - Discount)，则两个现象共存。实证估算显示，在算法驱动下 k_speed ≈ 1.2-1.5，而 k_signal ≈ 0.6-0.8，满足不等式，证明二者可由同一算法机制解释。

## Corrected Claim

统一假设的自洽性验证公式：设高溢价带来的成交加速因子为 k_speed (k_speed > 1)，降价导致的信号污染因子为 k_signal (k_signal < 1)。若 k_speed * (1 + Premium) > k_signal * (1 - Discount)，则两个现象共存。理论上，只要加速因子与溢价率的乘积大于污染因子与折扣率的乘积，二者即可共存，但具体参数需依赖特定市场的实证数据。

## Evidence

[质询]该陈述中的具体数值（k_speed ≈ 1.2-1.5, k_signal ≈ 0.6-0.8）属于经验事实，缺乏公开权威来源的直接支持，且“实证估算”的具体出处不明，存在数据捏造或过度拟合的风险。 | 逻辑上不等式成立（1.2*1.1 > 0.8*0.9），但参考来源[1]为数学集合，[2]为量化策略通用方法论，均未提供该特定市场现象的实证数据支持，属于经验事实缺来源。

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Mandelbrot_set&rut=ab6ea1393657cf325b28fd8375d2d2a68e9c6f9d6ee0ae202f40fad20699d7cf', 'type': 'ddg', 'title': 'Mandelbrot set - Wikipedia'}
- {'url': 'https://zhuanlan.zhihu.com/p/2039647989845775942&rut=ac9f0a514a1abbf8dc0d716df712ab8e2bd3b44f40518a063c60670dbcf366a0', 'type': 'ddg', 'title': '量化策略构建5步法：假设提出、因子构造、组合优化、回测验证、实盘迭代 - 知乎'}
