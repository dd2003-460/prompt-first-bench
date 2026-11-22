# N416: Apple M2 Ultra 运行 Qwen3-27B 的精度限制：MLX 框架目前主要支持 FP16/INT8/INT4 量化，缺乏对 FP8 (E4M3/E

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N150

## Claim

Apple M2 Ultra 运行 Qwen3-27B 的精度限制：MLX 框架目前主要支持 FP16/INT8/INT4 量化，缺乏对 FP8 (E4M3/E5M2) 的原生硬件加速支持，因此必须使用 INT8 或 INT4，这导致模型权重精度损失大于 NVIDIA FP8 方案。

## Corrected Claim

Apple M2 Ultra 在运行 Qwen3-27B 时，受限于硬件架构，缺乏 NVIDIA Hopper 架构级别的 FP8 原生硬件加速。MLX 框架主要提供 FP16 和 INT 系列量化支持，因此通常采用 INT8 或 INT4 量化方案，其精度损失特性与 NVIDIA FP8 方案存在差异。

## Evidence

[质询]该陈述包含具体的技术实现细节（MLX框架当前对FP8的支持状态、M2 Ultra硬件对FP8的原生加速缺失），属于快速变化的经验事实。虽然M2 Ultra确实缺乏像Hopper架构那样的原生FP8 Tensor Core，但MLX框架作为Apple官方维护的库，其量化支持范围（是否已引入FP8或等效低精度格式）是动态更新的，且'缺乏原生硬件加速'与'必须使用INT8/INT4'之间的因果链条在软件层面可能存在绕过或模拟支持，仅凭逻辑无法确证当前最新状态。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证MLX当前具体量化支持列表及M2 Ultra对FP8的硬件支持细节）

## Search Query

MLX framework Qwen3-27B quantization support FP8 INT8
