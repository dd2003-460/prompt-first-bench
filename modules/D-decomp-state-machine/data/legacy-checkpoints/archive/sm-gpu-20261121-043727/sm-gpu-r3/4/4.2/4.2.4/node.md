# N68: 量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_decode 具体数值：基于修正后的内存带宽公式，代入 RTX 4090 的 GDDR6

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_decode 具体数值：基于修正后的内存带宽公式，代入 RTX 4090 的 GDDR6X 带宽 (1.0 TB/s) 和权重/缓存大小，计算每生成 1 个 token 的理论时间下限（注意：若模型无法完整装入显存，此值无意义，需结合 N25 的量化方案）

## Corrected Claim

量化 Qwen3-27B 在 RTX 4090 (BF16) 上的 T_decode 具体数值：基于修正后的内存带宽公式，代入 RTX 4090 的 GDDR6X 带宽 (1.0 TB/s) 和权重/缓存大小，计算每生成 1 个 token 的理论时间下限（注意：若模型无法完整装入显存，此值无意义，需结合 N25 的量化方案）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1处理了BF16下的显存可行性（前提验证），子节点2处理了量化（W4）下的具体计算（核心任务）。两者在逻辑上互斥且互补，共同覆盖了父节点中‘若无法装入则无意义，需结合量化方案’的两个分支。不存在重复或矛盾。）

## Search Query

RTX 4090 memory bandwidth GDDR6X LLM decode tokens per second
