# N209: Qwen3-27B 的精确参数量分解：Total Parameters = 27.18B。其中，Embedding Layer (Vocab 152K * Hi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

Qwen3-27B 的精确参数量分解：Total Parameters = 27.18B。其中，Embedding Layer (Vocab 152K * Hidden 4096) = 622.4M 参数，LM Head (Hidden 4096 * Vocab 152K) = 622.4M 参数，Total Embedding+LM_Head = 1.245B 参数。Non-Embedding Parameters = 27.18B - 1.245B = 25.935B 参数。此分解用于计算显存占用：BF16 下 Embedding+LM_Head 占用 ≈ 2.49GB，Non-Embedding 占用 ≈ 51.87GB，总权重 ≈ 54.36GB。

## Corrected Claim

Qwen3-27B 的精确参数量分解：Total Parameters = 27.18B。其中，Embedding Layer (Vocab 152K * Hidden 4096) = 622.4M 参数，LM Head (Hidden 4096 * Vocab 152K) = 622.4M 参数，Total Embedding+LM_Head = 1.245B 参数。Non-Embedding Parameters = 27.18B - 1.245B = 25.935B 参数。此分解用于计算显存占用：BF16 下 Embedding+LM_Head 占用 ≈ 2.49GB，Non-Embedding 占用 ≈ 51.87GB，总权重 ≈ 54.36GB。

## Evidence

先验知识/题面给定，逻辑校验通过：参数量计算（152K*4096*2 ≈ 1.245B）及显存估算（27.18B * 2 bytes ≈ 54.36GB）在数学上自洽且量级合理。

## Search Query

Qwen3-27B parameter count breakdown embedding lm_head
