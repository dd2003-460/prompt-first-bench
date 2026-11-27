# N30: Decode 阶段每 token 生成延迟受限于 HBM 带宽：加载 13.5 GB 权重需 13.5 / 900 = 15 ms/token，500 toke

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Decode 阶段每 token 生成延迟受限于 HBM 带宽：加载 13.5 GB 权重需 13.5 / 900 = 15 ms/token，500 tokens 生成耗时约 7.5 s，加上 prefill 120 ms 和 TP 通信开销（~15-25%），总耗时 8.7-9.4 s，低于题面给出的 15-20 s 范围，表明实际瓶颈可能在调度或批处理效率

## Corrected Claim

Decode 阶段每 token 生成延迟受限于 HBM 带宽：加载 13.5 GB 权重需 13.5 / 900 = 15 ms/token，500 tokens 生成耗时约 7.5 s，加上 prefill 120 ms 和 TP 通信开销（~15-25%），总耗时 8.7-9.4 s，低于题面给出的 15-20 s 范围，表明实际瓶颈可能在调度或批处理效率

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（13.5GB/900GB/s=15ms, 500*15ms=7.5s, 7.5+0.12=7.62s, 7.62*1.15~1.25≈8.76~9.53s），量级符合LLM推理常识，结论逻辑自洽。
