# N141: KV Cache量化（如INT8/FP8）在vLLM/TensorRT-LLM中的支持状态与质量损失：INT8 KV Cache通常导致长文本生成质量下降0.5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

KV Cache量化（如INT8/FP8）在vLLM/TensorRT-LLM中的支持状态与质量损失：INT8 KV Cache通常导致长文本生成质量下降0.5-2%（需核验具体基准），但可将显存占用减半至~2.15GB，从而提升B_max

## Corrected Claim

KV Cache量化（如INT8/FP8）在vLLM/TensorRT-LLM中已获支持。INT8 KV Cache通常能显著降低显存占用（理论上减半），从而提升最大批处理大小（B_max），但可能在长文本生成中引入轻微的质量损失（具体幅度取决于模型与任务，通常较小）。

## Evidence

[质询]具体数值（0.5-2%质量下降、2.15GB显存占用）缺乏通用基准支持，且高度依赖具体模型规模、序列长度及硬件配置，属于特定实验结果而非通用规律；此外，'减半至~2.15GB'暗示原始FP16占用为4.3GB，这一特定数值缺乏上下文支撑，易产生误导。 | 经验事实，逻辑自洽（INT8量化确实能减少显存并可能引入轻微精度损失），但缺来源支持具体数值基准。

## Search Query

vLLM KV cache quantization INT8 quality degradation benchmark
