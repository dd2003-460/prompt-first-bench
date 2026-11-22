# N248: Qwen3-27B 在 Q4_K_M 量化下的模型权重文件大小约为 15.5 GB（基于 27B 参数 * 4.5 bits/param / 8），这是 App

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

Qwen3-27B 在 Q4_K_M 量化下的模型权重文件大小约为 15.5 GB（基于 27B 参数 * 4.5 bits/param / 8），这是 Apple Silicon 推理吞吐量的主要带宽消耗源，需从总内存带宽中扣除以计算有效 KV Cache 带宽。

## Corrected Claim

Qwen3-27B 在 Q4_K_M 量化下的模型权重文件大小约为 15.5 GB（基于 27B 参数 * 4.5 bits/param / 8），这是 Apple Silicon 推理吞吐量的主要带宽消耗源，需从总内存带宽中扣除以计算有效 KV Cache 带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 4.5 bits/param / 8 ≈ 15.18 GB，与15.5 GB量级一致（考虑量化开销/元数据），且Apple Silicon带宽瓶颈逻辑自洽。
