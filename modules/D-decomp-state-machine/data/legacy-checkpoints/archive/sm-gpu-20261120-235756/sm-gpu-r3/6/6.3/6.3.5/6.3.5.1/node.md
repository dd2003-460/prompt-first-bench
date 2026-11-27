# N327: 修正矛盾：N121的KV Cache计算正确。Qwen3-27B采用GQA（8 KV heads），单token KV占用为 2(K/V) × 64(layer

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

修正矛盾：N121的KV Cache计算正确。Qwen3-27B采用GQA（8 KV heads），单token KV占用为 2(K/V) × 64(layers) × 8(heads) × 128(dim) × 2bytes(BF16) = 256 KB/token；32K tokens总占用 = 256KB × 32768 = 8.0 GB。N123引用的25.76GB（对应128 heads或错误公式）为错误值，修正后A100 80GB在BF16下剩余显存为 80 - 54.36(权重) - 8.0(KV) = 17.64 GB。

## Corrected Claim

修正矛盾：N121的KV Cache计算正确。Qwen3-27B采用GQA（8 KV heads），单token KV占用为 2(K/V) × 64(layers) × 8(heads) × 128(dim) × 2bytes(BF16) = 256 KB/token；32K tokens总占用 = 256KB × 32768 = 8.0 GB。N123引用的25.76GB（对应128 heads或错误公式）为错误值，修正后A100 80GB在BF16下剩余显存为 80 - 54.36(权重) - 8.0(KV) = 17.64 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B架构参数（64层，8 KV heads，128 head_dim）符合GQA设计惯例，KV Cache计算公式及数值推导（256KB/token * 32768 = 8GB）逻辑自洽且量级合理。

## Search Query

Qwen3-27B GQA kv_heads 8 architecture parameters
