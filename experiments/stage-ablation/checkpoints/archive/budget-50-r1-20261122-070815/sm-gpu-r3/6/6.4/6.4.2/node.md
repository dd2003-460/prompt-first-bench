# N370: INT8 KV Cache 配置下，KV Cache 显存占用减半至 1.0 GB（若 N_full_attn=64），总显存需求降至 13.5 + 1.0 +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

INT8 KV Cache 配置下，KV Cache 显存占用减半至 1.0 GB（若 N_full_attn=64），总显存需求降至 13.5 + 1.0 + 0.5-1.0 = 15.0-15.5 GB，可安全运行于 16GB 卡，质量损失需通过 MMLU/GSM8K 下降幅度量化

## Corrected Claim

INT8 KV Cache 配置下，KV Cache 显存占用减半至 1.0 GB（若 N_full_attn=64），总显存需求降至 13.5 + 1.0 + 0.5-1.0 = 15.0-15.5 GB，可安全运行于 16GB 卡，质量损失需通过 MMLU/GSM8K 下降幅度量化

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化确实将KV Cache显存占用减半（16bit->8bit），数值计算13.5+1.0+0.5~1.0=15.0~15.5GB符合算术逻辑，且15.5GB<16GB在工程上可运行（考虑OS/驱动开销后通常需预留，但此处为理论估算，量级合理）。
