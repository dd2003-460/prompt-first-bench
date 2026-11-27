# N116: N60 中 '15k tokens Prefill 理论耗时 6.5ms' 的计算公式 (2*27e9*15000)/125e12 存在数量级错误：2*27e9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

N60 中 '15k tokens Prefill 理论耗时 6.5ms' 的计算公式 (2*27e9*15000)/125e12 存在数量级错误：2*27e9*15000 = 8.1e14 FLOPs，除以 125e12 应为 6.48 秒 (s) 而非 6.5 毫秒 (ms)；且该公式未考虑 TP=4 并行，单卡实际承担 FLOPs 为 8.1e14/4 = 2.025e14，在 50 TFLOPS (40% 利用率) 下理论时间为 4.05s。

## Corrected Claim

N60 中 '15k tokens Prefill 理论耗时 6.5ms' 的计算公式 (2*27e9*15000)/125e12 存在数量级错误：2*27e9*15000 = 8.1e14 FLOPs，除以 125e12 应为 6.48 秒 (s) 而非 6.5 毫秒 (ms)；且该公式未考虑 TP=4 并行，单卡实际承担 FLOPs 为 8.1e14/4 = 2.025e14，在 50 TFLOPS (40% 利用率) 下理论时间为 4.05s。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 2*27e9*15000 = 8.1e14，除以 125e12 确为 6.48 秒，原陈述指出的单位错误（ms vs s）及 TP 并行修正逻辑均正确。
