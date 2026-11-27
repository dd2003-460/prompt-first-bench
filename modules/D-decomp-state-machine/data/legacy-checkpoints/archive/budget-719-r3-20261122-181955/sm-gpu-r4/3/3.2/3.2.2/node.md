# N94: ITL (Inter-Token Latency) 计算公式为 ITL = 1 / Throughput_decode；在 32K 上下文下，RTX 4090 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

ITL (Inter-Token Latency) 计算公式为 ITL = 1 / Throughput_decode；在 32K 上下文下，RTX 4090 的 ITL 预计约为 1 / 11.5 ≈ 87 ms/token (理论) 至 120-150 ms/token (实测)，而 A100 80GB 的 ITL 预计约为 1 / 23.5 ≈ 42 ms/token (理论) 至 60-80 ms/token (实测)；ITL 直接决定生成阶段的流畅度。

## Corrected Claim

ITL (Inter-Token Latency) 计算公式为 ITL = 1 / Throughput_decode；在 32K 上下文下，RTX 4090 的 ITL 预计约为 1 / 11.5 ≈ 87 ms/token (理论) 至 120-150 ms/token (实测)，而 A100 80GB 的 ITL 预计约为 1 / 23.5 ≈ 42 ms/token (理论) 至 60-80 ms/token (实测)；ITL 直接决定生成阶段的流畅度。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 876)
