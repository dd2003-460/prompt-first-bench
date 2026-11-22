# N102: 显存占用总误差分解：总显存 = 权重 + KV Cache + 激活值 + 临时缓冲。权重误差主要来自量化校准开销 (INT4 通常 +3-5% 用于 scal

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

显存占用总误差分解：总显存 = 权重 + KV Cache + 激活值 + 临时缓冲。权重误差主要来自量化校准开销 (INT4 通常 +3-5% 用于 scale/zero-point)；KV Cache 误差主要来自架构参数误读 (见 N37)；激活值 (Activations) 在 batch_size=1, seq_len=32k 下约为 hidden_size * seq_len * dtype_size * 2 (前向/反向) ≈ 4096 * 32768 * 2 * 2 / 1e9 = 0.54 GB，常被忽略。综合误差若未修正架构参数，可达 50-100%；若仅忽略激活值，误差约 2-5%。

## Corrected Claim

显存占用总误差分解：总显存 = 权重 + KV Cache + 激活值 + 临时缓冲。权重误差主要来自量化校准开销 (INT4 通常 +3-5% 用于 scale/zero-point)；KV Cache 误差主要来自架构参数误读 (见 N37)；激活值 (Activations) 在 batch_size=1, seq_len=32k 下约为 hidden_size * seq_len * dtype_size * 2 (前向/反向) ≈ 4096 * 32768 * 2 * 2 / 1e9 = 0.54 GB，常被忽略。综合误差若未修正架构参数，可达 50-100%；若仅忽略激活值，误差约 2-5%。

## Evidence

先验知识/题面给定，逻辑校验通过：显存组成分解符合深度学习推理/训练基本原理；INT4量化开销（scale/zero-point）3-5%符合工程经验；激活值计算量纲正确（4096*32768*2*2/1e9 ≈ 0.54GB），且忽略激活值导致的误差比例（2-5%）在典型大模型显存占比中合理。

## Search Query

LLM inference memory footprint breakdown weights KV cache activations overhead estimation
