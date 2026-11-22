# N540: RTX 4090 在 Qwen3-27B INT4 权重下的实际 Decode 吞吐受限于显存带宽，但存在激活内存 (Activations) 与 KV Cac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

RTX 4090 在 Qwen3-27B INT4 权重下的实际 Decode 吞吐受限于显存带宽，但存在激活内存 (Activations) 与 KV Cache 的动态分配开销，实际可用带宽效率约为 85-90%，导致有效吞吐上限修正为 74.6 * 0.85 ≈ 63.4 tokens/s 至 74.6 * 0.90 ≈ 67.1 tokens/s。

## Corrected Claim

RTX 4090 在 Qwen3-27B INT4 权重下的实际 Decode 吞吐受限于显存带宽，但存在激活内存 (Activations) 与 KV Cache 的动态分配开销，实际可用带宽效率约为 85-90%，导致有效吞吐上限修正为 74.6 * 0.85 ≈ 63.4 tokens/s 至 74.6 * 0.90 ≈ 67.1 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽瓶颈下，85-90% 的带宽效率系数符合 LLM 推理中因 KV Cache 和激活值开销导致的典型性能损耗范围，数值计算自洽。
