# N82: BF16 精度下的总内存需求计算：Weights = 27B * 2 bytes = 54 GB；KV Cache (32K, 16 full-attn lay

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

BF16 精度下的总内存需求计算：Weights = 27B * 2 bytes = 54 GB；KV Cache (32K, 16 full-attn layers) = 2 * 16 * 8 heads * 128 dim * 32768 * 2 bytes ≈ 5.37 GB；Overhead (vLLM, B=1) ≈ 3 GB；Total ≈ 62.37 GB。此数值超过 RTX 4090 (24GB) 和 A6000 (48GB)，需 A100 80GB 或 H100 80GB 或 Apple M3 Ultra (192GB) [待核验]，需确认 Qwen3-27B 的 n_kv_heads 是否为 8（GQA 配置）。

## Corrected Claim

BF16 精度下的总内存需求估算：Weights ≈ 54 GB；KV Cache 取决于 n_kv_heads（若为 8 则 ≈ 5.37 GB，若为其他值需重新计算）；Overhead ≈ 3 GB。总内存需求约 62 GB 以上（基于 n_kv_heads=8 假设），需 A100 80GB 或更高显存设备。需确认 Qwen3-27B 实际 n_kv_heads 配置以精确计算 KV Cache。

## Evidence

[质询]KV Cache 计算中假设 n_kv_heads=8，但 Qwen3-27B 的具体架构参数（如 GQA 配置）未在来源中证实，且 27B 模型通常可能采用不同的头数配置（如 32 或 40），若 n_kv_heads 不同，KV Cache 大小将显著变化，导致总内存需求估算偏差。 | 来源 [1] 仅介绍 BF16 基本概念，未提供 Qwen3-27B 的具体架构参数或内存计算数据，属于无关来源；逻辑上公式自洽，但关键参数 n_kv_heads 缺乏外部证据支持，且为经验事实，故降级。

## Search Query

Qwen3-27B GQA config n_kv_heads head_dim BF16 memory footprint 32k context

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2016088957016896902&rut=f2f4dfb75249d236f0f481be9b0f93a205c07766ceffeb2a2a8ab0bcaa98951c', 'type': 'ddg', 'title': 'bf16混合精度训练总结 - 知乎'}
