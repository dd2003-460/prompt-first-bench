# N244: 公式中 d_model 的具体数值代入：Qwen3.8-27B 的 hidden_size (d_model) 为 4096，代入 T_verify 公式得 T

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

公式中 d_model 的具体数值代入：Qwen3.8-27B 的 hidden_size (d_model) 为 4096，代入 T_verify 公式得 T_memory(L) = L * 4096 * 2 * 4 / BW_eff，其中 *2 代表 K 和 V 两个缓存，*4 代表 FP16 字节数（假设 KV Cache 虽为 FP8 存储但计算时转为 FP16 或 BF16 进行点积），若 KV 保持 FP8 计算则系数调整为 *2。

## Corrected Claim

以某典型大语言模型为例，若其 hidden_size (d_model) 为 4096，代入 T_verify 公式得 T_memory(L) = L * 4096 * 2 * 4 / BW_eff，其中 *2 代表 K 和 V 两个缓存，*4 代表 FP16 字节数（假设 KV Cache 虽为 FP8 存储但计算时转为 FP16 或 BF16 进行点积），若 KV 保持 FP8 计算则系数调整为 *2。

## Evidence

[质询]Qwen3.8-27B 并非公开存在的标准模型版本（Qwen 系列常见为 7B/14B/72B 等，或 Qwen2.5 系列），其 hidden_size 为 4096 属于未经证实的经验参数，且不同规模模型的 hidden_size 差异较大，该具体数值缺乏权威来源支持。 | 经验事实，逻辑自洽但缺来源支持
