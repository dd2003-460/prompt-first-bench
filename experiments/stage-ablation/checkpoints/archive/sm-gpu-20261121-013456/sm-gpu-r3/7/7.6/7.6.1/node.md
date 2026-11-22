# N280: Mac Studio M3 Ultra 运行 Qwen3-27B 在 Q4_K_M 量化下的实测吞吐量为 12.46 tokens/s，在 BF16 下受限于内

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

Mac Studio M3 Ultra 运行 Qwen3-27B 在 Q4_K_M 量化下的实测吞吐量为 12.46 tokens/s，在 BF16 下受限于内存带宽（800GB/s），理论上限约为 14.4 tokens/s (800GB/s / 54GB)，实际约为 10-12 tokens/s，而非 5-7 tokens/s。

## Corrected Claim

Mac Studio M3 Ultra 运行 Qwen3-27B 在 Q4_K_M 量化下的实测吞吐量约为 24-26 tokens/s。

## Evidence

[质询]数值量级严重错误：参考来源显示 Qwen3-27B 在 Mac Studio M3 Ultra 上 Q4_K_M 量化下的实测吞吐量约为 21-26 tokens/s，而陈述中声称的 12.46 tokens/s 与实测数据相差近一倍，且陈述中关于 BF16 理论上限 14.4 tokens/s 的计算（800GB/s / 54GB）也忽略了模型权重在 BF16 下实际占用约 54GB 但推理时还需考虑 KV Cache 及内存访问效率，更重要的是该数值远低于 Q4_K_M 的实测值，逻辑上 BF16 速度不应显著低于 Q4_K_M 的实测值（通常量化加速比在 1.5-2x 左右，若 Q4 为 24 tok/s，BF16 理论上限应更高或接近，但陈述称 BF16 上限仅 14.4 且实际 10-12，这与 Q4 实测 24 tok/s 形成矛盾，因为 Q4 数据量减半，速度应更快，而非 BF16 更慢或两者都远低于实测）。 | 来源 [1] 和 [2] 直接显示 Q4_K_M 下速度约为 24-26 tokens/s，与陈述中的 12.46 tokens/s 矛盾；且陈述中 BF16 速度低于 Q4 实测速度违背基本量化加速原理。

## Search Query

Mac Studio M3 Ultra Qwen3-27B inference speed tokens/s benchmark

## Retrieval Sources

- {'url': 'https://willitrunai.com/can-run/qwen-3.8-27b-on-m3-ultra-256gb&rut=5f355ca23e9c176dea3174d465663a2c17498f611510a67f4ac2a9c0d56c1edf', 'type': 'ddg', 'title': 'Qwen3.8 27B on Mac Studio M3 Ultra 256GB: YES, ~24 tok/s'}
- {'url': 'https://llmspeed.dev/qwen3.6-27b-on-mac-studio-m3-ultra-512gb/&rut=05ead1a9fe90b45c607b9bc76963fde5dbd7e21cb4a6a6b139efc1691a9eb903', 'type': 'ddg', 'title': 'Qwen 3.6/3.8 27B on Mac Studio M3 Ultra 512GB: ~26 tok/s | llmspeed'}
- {'url': 'https://aicanrun.com/run/qwen3-8-27b-on-mac-studio-m3-ultra-256gb&rut=e67c36f3468a414d203eea057122c7f44944bf2335336cfad85508b2c1287993', 'type': 'ddg', 'title': 'Qwen3.8 27B on Mac Studio M3 Ultra · 256GB? YES - AICanRun'}
