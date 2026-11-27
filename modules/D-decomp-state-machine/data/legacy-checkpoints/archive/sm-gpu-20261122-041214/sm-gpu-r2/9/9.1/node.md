# N162: RTX 4090 (24GB) 运行 Qwen3-27B (FP8) 在 vLLM 引擎下的实测解码吞吐量 (Decode Throughput) 具体数值 (

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

RTX 4090 (24GB) 运行 Qwen3-27B (FP8) 在 vLLM 引擎下的实测解码吞吐量 (Decode Throughput) 具体数值 (tokens/s, batch=1)，需排除 Prefill 阶段，仅统计自回归生成阶段的平均速度，并标注使用的量化方法（如 GPTQ, AWQ, or FP8 native）。

## Corrected Claim

RTX 4090 (48GB) 运行 Qwen3.8-27B (FP8) 在 vLLM 引擎下的实测解码吞吐量约为 66-73 tokens/s (batch=1)。

## Evidence

[质询]参考来源[1]明确标注硬件为 'RTX 4090 48GB'，而事实节点要求的是 'RTX 4090 (24GB)'。虽然两者在计算核心（SM数量、频率）上可能相似，但显存带宽和容量不同，且48GB版本可能是特定OEM或超频版，直接引用48GB的数据作为24GB版本的实测值存在硬件规格不匹配的风险。此外，来源中提到的模型是 'Qwen3.8-27B'，而节点要求 'Qwen3-27B'，版本号细微差异可能导致性能波动。 | 来源[1]提供了vLLM引擎下Qwen3.8-27B-FP8在RTX 4090 48GB上的解码吞吐量（66-73 tok/s），逻辑量级合理（27B模型在单卡4090上FP8量化，batch=1时60-70 tok/s符合预期），但硬件显存规格（48GB vs 24GB）和模型版本号（3.8 vs 3）与节点要求不完全一致，属于间接支持且存在硬件差异，故降级。

## Search Query

RTX 4090 Qwen3-27B FP8 vLLM decode throughput tokens per second benchmark

## Retrieval Sources

- {'url': 'https://github.com/vllm-project/vllm/issues/68877&rut=d526e2571e9354a0facb45f748360fa0b843b71437906969d2f6e51e61d83e85', 'type': 'ddg', 'title': '[Benchmark] Qwen3.8-27B-FP8 at 256K on one RTX 4090 48GB: 18 ... - GitHub'}
