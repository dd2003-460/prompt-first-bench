# N188: RTX 4090在W4精度下运行Qwen3-27B的实测OOM概率：在vLLM框架下，由于CUDA Context和KV Cache Manager的动态内存分

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

RTX 4090在W4精度下运行Qwen3-27B的实测OOM概率：在vLLM框架下，由于CUDA Context和KV Cache Manager的动态内存分配不可预测，22.85GB理论需求在24GB物理显存上导致OOM的概率约为15-25% [待核验]，需通过设置`--max-model-len`限制最大上下文长度至28K以预留2GB安全边际。

## Corrected Claim

RTX 4090在W4精度下运行Qwen3-27B时，由于动态内存分配的不确定性，存在OOM风险。建议通过设置`--max-model-len`限制最大上下文长度以预留安全边际，具体数值需根据实际负载测试确定。

## Evidence

[质询]该陈述包含具体的经验性数值（OOM概率15-25%、22.85GB理论需求、28K上下文限制），这些属于硬件与软件交互的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM RTX 4090 24GB OOM W4 quantization Qwen 27B memory leak
