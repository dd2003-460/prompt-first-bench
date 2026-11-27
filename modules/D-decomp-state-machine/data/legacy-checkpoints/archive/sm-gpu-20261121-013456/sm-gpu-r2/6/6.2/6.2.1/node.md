# N97: 失效场景(1)吞吐量突破：当需求吞吐量 > 20 tokens/s 时，单卡 4090 失效。升级路径对比：2×4090 (总吞吐~28 tokens/s, T

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

失效场景(1)吞吐量突破：当需求吞吐量 > 20 tokens/s 时，单卡 4090 失效。升级路径对比：2×4090 (总吞吐~28 tokens/s, TCO_3y=$4213) vs 1×A100 80GB (吞吐~45 tokens/s, TCO_3y=$4650)。单位 token 成本：2×4090 = $4213/(28*3600*3) ≈ $0.014/token；A100 = $4650/(45*3600*3) ≈ $0.0095/token。当吞吐量需求在 20-30 tokens/s 区间时，2×4090 单位成本更低；当 > 35 tokens/s 时，A100 单位成本更低。临界吞吐量 ≈ 32 tokens/s [待核验：需实测 A100 27B BF16 吞吐量]。

## Corrected Claim

失效场景(1)吞吐量突破：当需求吞吐量 > 20 tokens/s 时，单卡 4090 可能失效。升级路径对比（基于估算值）：2×4090 (总吞吐~28 tokens/s, TCO_3y≈$4213) vs 1×A100 80GB (吞吐~45 tokens/s, TCO_3y≈$4650)。单位 token 成本估算：2×4090 ≈ $0.014/token；A100 ≈ $0.0095/token。估算显示当吞吐量需求在 20-30 tokens/s 区间时，2×4090 单位成本可能更低；当 > 35 tokens/s 时，A100 单位成本可能更低。临界吞吐量估算 ≈ 32 tokens/s [注：吞吐量与TCO为估算值，需实测 A100 27B BF16 吞吐量及实际采购成本以确认]。

## Evidence

[质询]吞吐量数值（2×4090 ~28 tokens/s, A100 ~45 tokens/s）及TCO具体金额属于经验事实，缺乏实测数据或权威基准测试支持，且27B模型在BF16下的实际推理速度受硬件架构、软件栈优化影响极大，存在量级偏差风险。 | 经验事实，逻辑自洽但缺来源支持；数学推导部分（单位成本计算、临界点求解）逻辑正确，但基础参数（吞吐量、TCO）无法通过第一性原理推导，且无外部来源验证。

## Search Query

NVIDIA A100 80GB Qwen3-27B inference throughput tokens per second benchmark
