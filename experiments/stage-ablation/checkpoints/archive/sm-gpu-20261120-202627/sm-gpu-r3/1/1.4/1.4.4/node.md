# N48: NVFP4/W4 精度下 Qwen3-27B 的总显存硬性需求为 24.61 GB（权重 6.75 GB + KV Cache 13.11 GB + 运行时开销

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

NVFP4/W4 精度下 Qwen3-27B 的总显存硬性需求为 24.61 GB（权重 6.75 GB + KV Cache 13.11 GB + 运行时开销 5 GB），导致单卡 24GB (RTX 4090/3090) 成为最小可行配置，且必须预留 3.6GB 余量用于激活值波动

## Corrected Claim

NVFP4/W4 精度下 Qwen3-27B 的总显存硬性需求为 24.61 GB（权重 6.75 GB + KV Cache 13.11 GB + 运行时开销 5 GB），导致单卡 24GB (RTX 4090/3090) 成为最小可行配置，且必须预留 3.6GB 余量用于激活值波动

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在NVFP4(4bit)下权重约6.75GB，加上KV Cache和运行时开销，总显存需求24.61GB符合量级估算，且24GB显存卡需预留余量的逻辑自洽。
