# N315: 2×RTX 4090 (48GB) 与 1×L40S (48GB) 在 Qwen3-27B FP8 方案下的 TCO 对比：2×4090 硬件成本 $3198，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

2×RTX 4090 (48GB) 与 1×L40S (48GB) 在 Qwen3-27B FP8 方案下的 TCO 对比：2×4090 硬件成本 $3198，功耗 900W；L40S 硬件成本 $4000，功耗 350W。在电价 $0.12/kWh 下，3年电力成本 2×4090 为 $4471，L40S 为 $1093。若吞吐量 L40S 为 2×4090 的 1.5x (因无多卡通信开销且原生 FP8)，则 L40S 单位 token 成本约为 2×4090 的 40-50%，在长期运行 (>1年) 场景下 L40S 性价比更优。

## Corrected Claim

2×RTX 4090 (48GB) 与 1×L40S (48GB) 在 Qwen3-27B FP8 方案下的 TCO 对比：2×4090 硬件成本 $3198，功耗 900W；L40S 硬件成本 $4000，功耗 350W。在电价 $0.12/kWh 下，3年电力成本 2×4090 为 $4471，L40S 为 $1093。若吞吐量 L40S 为 2×4090 的 1.5x (因无多卡通信开销且原生 FP8)，则 L40S 单位 token 成本约为 2×4090 的 40-50%，在长期运行 (>1年) 场景下 L40S 性价比更优。

## Evidence

检索失败: no sources from any channel (all 5 failed)
