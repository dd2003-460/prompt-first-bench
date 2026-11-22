# N213: 若强制对 Embedding 层进行 INT8 量化，其显存占用降至 151,936 × 4096 × 1 byte ≈ 0.58 GB，相比 BF16 节省 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

若强制对 Embedding 层进行 INT8 量化，其显存占用降至 151,936 × 4096 × 1 byte ≈ 0.58 GB，相比 BF16 节省 0.58 GB 显存，但需验证 vLLM/TensorRT-LLM 是否支持对 Embedding 层单独量化及由此带来的查表精度损失（通常 MMLU 下降 >2% 即视为不可接受）。

## Corrected Claim

若强制对 Embedding 层进行 INT8 量化，其显存占用降至 151,936 × 4096 × 1 byte ≈ 0.58 GB，相比 BF16 节省 0.58 GB 显存。需验证 vLLM/TensorRT-LLM 是否支持对 Embedding 层单独量化及由此带来的查表精度损失（具体可接受的精度下降阈值需根据具体模型和评估基准确定，通常需通过实验验证）。

## Evidence

[质询]经验事实（MMLU下降阈值>2%）缺乏来源支持，且不同模型/任务下精度损失差异巨大，该阈值并非通用标准；此外，Embedding层量化在vLLM/TensorRT-LLM中的具体支持情况属于动态变化的工程细节，无来源佐证。 | 数值计算逻辑自洽（151936*4096*1/1024^3 ≈ 0.58GB），但source=search且无可用外部来源，经验事实（精度阈值、框架支持状态）无法验证，依据经验事实排除条款降级。

## Search Query

vLLM quantize embedding layer INT8 Qwen3-27B precision loss
