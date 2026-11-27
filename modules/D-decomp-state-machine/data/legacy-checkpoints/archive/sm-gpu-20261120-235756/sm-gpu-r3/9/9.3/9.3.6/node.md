# N345: MI300X 支持 BF16 原生 FP8 混合精度（如权重 FP8 + KV Cache BF16）时，需验证 ROCm 5.7+ 对 `torch.floa

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129, N130, N131

## Claim

MI300X 支持 BF16 原生 FP8 混合精度（如权重 FP8 + KV Cache BF16）时，需验证 ROCm 5.7+ 对 `torch.float8_e4m3fn` 在 MoE 路由层的支持稳定性；若框架仅支持全 BF16，则显存占用率将回升至 42.6% 基准，若支持混合精度，权重部分显存减半，总占用率可降至约 35%，进一步释放并发空间。

## Corrected Claim

MI300X 支持 BF16 与 FP8 混合精度（如权重 FP8 + KV Cache BF16）时，需验证 ROCm 对 `torch.float8_e4m3fn` 在 MoE 路由层的支持稳定性；若框架仅支持全 BF16，显存占用率将维持基准水平；若支持混合精度，权重部分显存减半，总占用率预计显著降低，从而释放更多并发空间。

## Evidence

[质询]ROCm 5.7+ 对 `torch.float8_e4m3fn` 在 MoE 路由层的支持稳定性属于具体软件版本的功能状态，且“显存占用率从 42.6% 降至 35%”的具体数值依赖于特定的模型架构、序列长度和 Batch Size 等未给定的上下文条件，无法仅凭逻辑推导得出精确数值。 | 先验知识/题面给定，逻辑校验通过（FP8 权重确实比 BF16 节省一半显存，逻辑自洽），但具体版本支持情况及精确百分比数值缺乏外部来源直接支持，且属于经验事实，故降级。

## Search Query

ROCm MI300X FP8 mixed precision Qwen3 support status
