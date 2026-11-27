# N339: Qwen3-27B 的层数 num_layers 实际为 64 层，但 All-Reduce 通信发生在每层的 Attention 输出和 FFN 输出后，总通

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110

## Claim

Qwen3-27B 的层数 num_layers 实际为 64 层，但 All-Reduce 通信发生在每层的 Attention 输出和 FFN 输出后，总通信次数为 2 * num_layers = 128 次/序列，需修正 T_comm 公式中的层数系数

## Corrected Claim

Qwen3-27B 的层数 num_layers 需根据具体模型配置文件确认（通常大模型层数在 32-80 之间，64 层是合理推测但非绝对事实）；在采用张量并行（TP）策略时，每层 Attention 和 FFN 各需一次 All-Reduce，总通信次数为 2 * num_layers，需据此修正 T_comm 公式。

## Evidence

[质询]Qwen3-27B 的具体架构参数（如层数是否为 64）属于经验事实，且不同版本或配置可能存在差异，仅凭逻辑无法确定具体数值；此外，'All-Reduce 通信发生在每层的 Attention 输出和 FFN 输出后'这一描述依赖于特定的并行策略（如张量并行 TP），并非所有分布式训练场景的通用默认行为，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体层数及通信模式细节）

## Search Query

Qwen3-27B architecture number of layers transformer
