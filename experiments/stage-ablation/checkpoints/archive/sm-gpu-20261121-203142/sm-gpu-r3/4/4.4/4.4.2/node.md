# N88: RTX 4090 (24GB, 1.0 TB/s带宽, 82 TFLOPS BF16) 在32K上下文下的TTFT估算：Prefill计算量约为 2 * 27B

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

RTX 4090 (24GB, 1.0 TB/s带宽, 82 TFLOPS BF16) 在32K上下文下的TTFT估算：Prefill计算量约为 2 * 27B * 32K FLOPs，理论时间 = 1.7e12 FLOPs / 82e12 FLOPS ≈ 20.7秒；实际因优化（FlashAttention等）可能降至5-10秒 [待核验]。

## Corrected Claim

RTX 4090 (24GB, 1.0 TB/s带宽, 82 TFLOPS BF16) 在32K上下文下的TTFT估算：Prefill计算量约为 2 * 27B * 32K FLOPs，理论时间 = 1.7e12 FLOPs / 82e12 FLOPS ≈ 20.7秒；实际因优化（FlashAttention等）可能降至5-10秒 [待核验]。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交，分别聚焦于计算量修正、硬件有效算力修正和算法加速修正，无重复或矛盾。但存在完备性缺失：父节点明确指出 RTX 4090 为 24GB 显存，而 Qwen3-27B 模型在 BF16 精度下权重约占 54GB，远超显存容量。子节点均未涉及‘模型无法完整加载到显存’这一核心物理约束，也未讨论由此引发的 Offloading（权重卸载）对 TTFT 的巨大影响（通常会导致时间从秒级跃升至分钟级），这使得基于纯计算和 FlashAttention 的估算在 24GB 显存硬件上可能完全不成立。）

## Search Query

RTX 4090 Qwen 27B 32k context time to first token
