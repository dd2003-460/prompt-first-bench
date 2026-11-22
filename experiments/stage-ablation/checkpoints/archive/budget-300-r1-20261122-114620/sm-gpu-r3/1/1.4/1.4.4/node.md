# N53: 多卡张量并行 (TP) 框架支持：vLLM 支持 Qwen3-27B 的 TP=2 (2x RTX 4090) 且通信后端为 NCCL over PCIe Ge

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

多卡张量并行 (TP) 框架支持：vLLM 支持 Qwen3-27B 的 TP=2 (2x RTX 4090) 且通信后端为 NCCL over PCIe Gen4；llama.cpp 仅支持 pipeline parallel (PP) 不支持 TP，2x 4090 下 PP 切分点在第 32 层，通信延迟增加 12ms/token [待核验]

## Corrected Claim

vLLM 支持 Qwen3-27B 的 TP=2 (2x RTX 4090)，但受限于 PCIe Gen4 带宽，通信开销显著；llama.cpp 主要支持 pipeline parallel (PP)，在 2x 4090 下 PP 切分及具体延迟需实测验证，12ms/token 为估算值。

## Evidence

[质询]具体数值（如12ms/token延迟、第32层切分点）缺乏来源支持，且vLLM在PCIe Gen4下使用NCCL进行TP通信的效率及可行性存在技术争议（通常TP对带宽要求极高，PCIe可能成为瓶颈，导致性能远低于预期或不可用，而非简单支持）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM tensor parallel Qwen3-27B 2x RTX 4090 NCCL
