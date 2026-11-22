# N163: Qwen3-27B 处理 32K tokens 的 Prefill 计算量约为 `2 * 27e9 * 32768` FLOPs，即约 1.76 PFLOPs。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Qwen3-27B 处理 32K tokens 的 Prefill 计算量约为 `2 * 27e9 * 32768` FLOPs，即约 1.76 PFLOPs。RTX 4090 理论 Prefill 时间约为 `1.76e15 / 82.6e12` ≈ 21.3 秒，但考虑到并行度和算子效率，实际实测时间通常在 1.5-2.5 秒区间 [待核验]，需区分理论峰值与实际 MFU (Model FLOPs Utilization)。

## Corrected Claim

Qwen3-27B 处理 32K tokens 的 Prefill 理论计算量约为 1.76 PFLOPs，基于 RTX 4090 峰值算力（82.6 TFLOPS）的理论时间约为 21.3 秒。实际实测时间受 MFU、量化精度及并行策略影响极大，通常在数秒至数十秒区间，具体数值需依赖特定基准测试数据，不宜直接断定为 1.5-2.5 秒。

## Evidence

[质询]实际实测时间 1.5-2.5 秒与理论计算时间 21.3 秒存在约 10 倍差距，这隐含了极高的 MFU（约 85-90%）或使用了未提及的量化/优化技术（如 FP8/INT8），在标准 FP16/BF16 推理下，RTX 4090 处理 27B 模型 32K 上下文 Prefill 达到此速度极不寻常，且缺乏具体硬件配置和软件栈说明，属于经验事实且数值存疑。 | 逻辑推导部分（理论 FLOPs 和理论时间）自洽，但实际实测时间属于经验事实，无来源支持且与常规 MFU 预期存在较大偏差，无法排除特定优化场景，故降级。

## Search Query

Qwen3-27B prefill latency 32k tokens RTX 4090 benchmark
