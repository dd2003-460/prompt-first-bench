# N301: Qwen3-27B 的注意力头配置参数：总注意力头数 (num_heads) 和 KV 头数 (num_key_value_heads)，以计算 GQA 分组因

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

Qwen3-27B 的注意力头配置参数：总注意力头数 (num_heads) 和 KV 头数 (num_key_value_heads)，以计算 GQA 分组因子 G = num_heads / num_key_value_heads（例如 32/16=2），这是推导误差衰减比例的前提参数。

## Corrected Claim

Qwen3-27B 采用 GQA（分组查询注意力）机制，其 G 因子 G = num_heads / num_key_value_heads 大于 1，具体数值需参考官方模型配置。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（num_heads 和 num_key_value_heads 的具体数值或比例），属于经验事实。虽然 Qwen3-27B 确实采用 GQA 机制，但具体的头数配置（如是否为 32/16 或其他组合）需要查阅官方技术报告或模型配置文件才能确认，仅凭逻辑无法推导出确切的整数配置。 | 经验事实，逻辑自洽（GQA 机制存在且 G 因子定义正确）但缺来源支持（检索失败，无法验证具体头数数值）。

## Search Query

Qwen3-27B model config num_heads num_key_value_heads json
