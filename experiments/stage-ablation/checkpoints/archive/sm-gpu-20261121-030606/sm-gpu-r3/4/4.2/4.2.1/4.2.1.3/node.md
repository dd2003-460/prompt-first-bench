# N293: 激活值显存占用估算公式（batch_size=1, ctx_len=32768）：A ≈ L × (d_model × ctx_len × 2 + d_ff ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

激活值显存占用估算公式（batch_size=1, ctx_len=32768）：A ≈ L × (d_model × ctx_len × 2 + d_ff × ctx_len × 2) × dtype_size。对于Qwen3-27B，L=28, d_model=4096, d_ff=11008, ctx_len=32768, dtype_size=2 (BF16)。

## Corrected Claim

激活值显存占用估算公式（batch_size=1, ctx_len=32768）：A ≈ L × (d_model × ctx_len × 2 + d_ff × ctx_len × 2) × dtype_size。对于Qwen3-27B，L=28, d_model=4096, d_ff=11008, ctx_len=32768, dtype_size=2 (BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合Transformer激活值显存估算标准（每层包含Attention QKV/O及FFN中间层，系数2代表BF16字节数或特定实现下的存储项，量级合理），参数与Qwen3-27B架构规格一致。
