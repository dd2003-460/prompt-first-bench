# N291: 2x RTX 4090 方案中，PCIe 4.0 x16 双向带宽为 64 GB/s，在 TP=2 推理中，每层 All-Reduce 通信量为 2 * n_k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

2x RTX 4090 方案中，PCIe 4.0 x16 双向带宽为 64 GB/s，在 TP=2 推理中，每层 All-Reduce 通信量为 2 * n_kv_heads * head_dim * seq_len * dtype_size；在 32K 上下文、BF16 下，每层通信量为 134.2 MB，16 层总通信量为 2.15 GB，理论传输时间为 2.15GB / 64GB/s ≈ 33.6 ms，占单 token Decode 时间 (假设 100ms) 的 33.6%，显著抵消 TCO 优势。

## Corrected Claim

2x RTX 4090 方案中，PCIe 4.0 x16 双向带宽为 64 GB/s，在 TP=2 推理中，每层 All-Reduce 通信量为 2 * n_kv_heads * head_dim * seq_len * dtype_size；在 32K 上下文、BF16 下，每层通信量为 134.2 MB，16 层总通信量为 2.15 GB，理论传输时间为 2.15GB / 64GB/s ≈ 33.6 ms，占单 token Decode 时间 (假设 100ms) 的 33.6%，显著抵消 TCO 优势。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 双向带宽 64GB/s 符合标准；通信量计算 2 * 8 * 128 * 32768 * 2 ≈ 134.2MB 及总耗时 33.6ms 推导正确，符合 TP=2 推理通信瓶颈的工程常识。

## Search Query

PCIe tensor parallel all-reduce overhead LLM inference 32k
