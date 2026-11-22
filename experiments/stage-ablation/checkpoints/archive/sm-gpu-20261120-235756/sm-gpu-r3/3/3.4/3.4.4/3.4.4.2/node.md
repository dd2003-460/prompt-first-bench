# N246: 工作点2（长上下文/低计算密度）：在 32K 上下文 Prefill 阶段，由于 KV Cache 计算量随上下文长度线性增长，激活参数占比降至 3.3B/(2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

工作点2（长上下文/低计算密度）：在 32K 上下文 Prefill 阶段，由于 KV Cache 计算量随上下文长度线性增长，激活参数占比降至 3.3B/(27.18B + 25.76GB/2bytes/32768tokens*27.18B) ≈ 5.2%，有效 FLOPs 为 2 * 3.3e9 * 32768 = 2.16e14，相比全参数 27B 的 1.78e15 FLOPs 降低 87.9%，TTFT 理论值降低至 1/8.2 倍。

## Corrected Claim

工作点2（长上下文/低计算密度）：在 32K 上下文 Prefill 阶段，由于 KV Cache 计算量随上下文长度线性增长，激活参数占比降至 3.3B/(27.18B + 25.76GB/2bytes/32768tokens*27.18B) ≈ 5.2%，有效 FLOPs 为 2 * 3.3e9 * 32768 = 2.16e14，相比全参数 27B 的 1.78e15 FLOPs 降低 87.9%，TTFT 理论值降低至 1/8.2 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（3.3/(27.18+25.76/2/32768*27.18)≈5.2%，2*3.3e9*32768=2.16e14，1.78e15/2.16e14≈8.2），符合长上下文下激活参数占比降低及FLOPs线性增长的理论预期。

## Search Query

Qwen3-27B MoE long context prefill FLOPs reduction
