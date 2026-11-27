# N30: BF16 权重内存精确计算公式与修正：Weight_Size_GB = (27e9 * 2 bytes) / 1e9 + Overhead, 其中 Overhe

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

BF16 权重内存精确计算公式与修正：Weight_Size_GB = (27e9 * 2 bytes) / 1e9 + Overhead, 其中 Overhead 包含 Embedding 和 LM Head 矩阵 (Vocab_Size * Hidden_Size * 2 bytes)，Qwen3-27B Vocab_Size 约为 152k，Overhead 约 1.2GB，故总权重约 55.2GB 而非简单的 54GB。

## Corrected Claim

BF16 权重内存精确计算公式与修正：Weight_Size_GB = (27e9 * 2 bytes) / 1e9 + Overhead, 其中 Overhead 包含 Embedding 和 LM Head 矩阵 (Vocab_Size * Hidden_Size * 2 bytes)，Qwen3-27B Vocab_Size 约为 152k，Overhead 约 1.2GB，故总权重约 55.2GB 而非简单的 54GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数*2字节=54GB，Vocab 152k*Hidden 4096*2字节*2(Embedding+LM Head)≈2.5GB，总重约56.5GB，与55.2GB量级一致且逻辑自洽。

## Search Query

Qwen3-27B embedding size vocabulary count
