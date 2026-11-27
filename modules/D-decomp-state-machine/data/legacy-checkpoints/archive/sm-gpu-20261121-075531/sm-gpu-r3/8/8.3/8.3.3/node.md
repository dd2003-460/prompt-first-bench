# N346: AMD 替代工作点 (RX 7900 XTX + INT8): 24GB 显存限制同 4090，需 W4 或双卡；在 ROCm 环境下，W4 量化 TPS 预计

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

AMD 替代工作点 (RX 7900 XTX + INT8): 24GB 显存限制同 4090，需 W4 或双卡；在 ROCm 环境下，W4 量化 TPS 预计为 35-45 tokens/s，比同配置 NVIDIA 卡低 10-20% 因软件栈优化滞后 [待核验]；此工作点主要作为价格更低 ($800 vs $1600) 时的性价比备选，而非纯性能备选。

## Corrected Claim

AMD 替代工作点 (RX 7900 XTX + INT8): 24GB 显存限制同 4090，需 W4 或双卡；在 ROCm 环境下，W4 量化性能预计略低于同配置 NVIDIA 卡（因软件栈优化滞后）；此工作点主要作为价格更低 ($800 vs $1600) 时的性价比备选，而非纯性能备选。

## Evidence

[质询]具体性能数值（35-45 tokens/s）及性能差距比例（10-20%）属于经验事实，缺乏来源支持，且受模型大小、序列长度等变量影响极大，无法仅凭逻辑推导确定。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

RX 7900 XTX ROCm LLM inference throughput Qwen 27B W4
