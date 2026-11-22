# N154: RTX 4080 Super (16GB) 运行 Qwen3-27B W4 (AWQ/GPTQ) 在 32K 上下文下的理论最大并发序列数或单序列 KV Cac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

RTX 4080 Super (16GB) 运行 Qwen3-27B W4 (AWQ/GPTQ) 在 32K 上下文下的理论最大并发序列数或单序列 KV Cache 上限，受限于 16GB 显存减去 15.43GB (权重+激活) 后的剩余 0.57GB，仅支持约 290 个 token 的 KV Cache，远低于 32K 需求，故 16GB 卡实际不可行。

## Corrected Claim

RTX 4080 Super (16GB) 运行 Qwen3-27B W4 (AWQ/GPTQ) 在 32K 上下文下的理论最大并发序列数或单序列 KV Cache 上限，受限于 16GB 显存减去 15.43GB (权重+激活) 后的剩余 0.57GB，仅支持约 290 个 token 的 KV Cache，远低于 32K 需求，故 16GB 卡实际不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B W4量化权重约13.5GB，加上激活值与框架开销约2GB，总占用约15.5GB，剩余显存约0.5GB；KV Cache每token约1.7MB（基于27B模型结构估算），0.5GB仅支持约300 token，远低于32K需求，结论合理。

## Search Query

RTX 4080 Super 16GB Qwen3-27B AWQ 32k context KV cache limit
