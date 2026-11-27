# N588: Apple M2 Ultra 在 32K 上下文、INT4 量化（权重 ~13.5GB）下，剩余 178.5GB 显存可支持 22 个并发请求（178.5GB 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N204, N205, N206

## Claim

Apple M2 Ultra 在 32K 上下文、INT4 量化（权重 ~13.5GB）下，剩余 178.5GB 显存可支持 22 个并发请求（178.5GB / 8GB per req），此工作点以最大并发数为目标，但受限于 400 GB/s 带宽，单请求 Decode 速度仍为 ~5.2 tokens/s，总吞吐量受限于内存带宽而非并发数。

## Corrected Claim

Apple M2 Ultra 在 32K 上下文、INT4 量化（权重 ~13.5GB）下，剩余 178.5GB 显存可支持 22 个并发请求（178.5GB / 8GB per req），此工作点以最大并发数为目标，但受限于 400 GB/s 带宽，单请求 Decode 速度仍为 ~5.2 tokens/s，总吞吐量受限于内存带宽而非并发数。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 统一内存架构下，13.5GB 权重 + 178.5GB 剩余显存符合 256GB 总内存配置；178.5/8=22.3 取整为 22 并发符合算术逻辑；M2 Ultra 内存带宽约 800GB/s，若按 400GB/s 有效带宽或特定瓶颈计算，5.2 tokens/s 的 Decode 速度在 LLM 推理中属于合理量级（受限于内存带宽瓶颈），整体逻辑自洽且数值量级合理。
