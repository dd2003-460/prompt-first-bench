# N427: Qwen3-27B的hidden_size具体数值需从HuggingFace官方config.json中提取，预期值约为4096（基于27B参数规模估算），该值

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

Qwen3-27B的hidden_size具体数值需从HuggingFace官方config.json中提取，预期值约为4096（基于27B参数规模估算），该值直接决定KV Cache每层每token的字节数（hidden_size * 2 bytes for Q/K）。

## Corrected Claim

Qwen3-27B的hidden_size需从HuggingFace官方config.json中提取，基于27B参数规模推测可能在4096-5120之间，该值影响KV Cache大小，但具体每token字节数需结合注意力头配置（如GQA）计算。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（hidden_size=4096），属于经验事实。虽然27B模型通常对应4096或5120的hidden size，但仅凭参数规模估算存在不确定性（例如Qwen2-72B为8192，Qwen2-7B为3584，27B的具体值需查证，且Qwen3系列若存在，其架构参数需官方确认，不能仅靠估算视为确切事实）。此外，KV Cache字节数计算通常涉及head_dim或hidden_size，具体取决于实现（如GQA/MQA），直接断言hidden_size * 2 bytes可能忽略了分组注意力机制下的实际存储差异。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证Qwen3-27B的具体config参数及KV Cache计算细节）

## Search Query

Qwen3-27B config.json hidden_size num_hidden_layers num_attention_heads
