# N186: KV Cache 量化对显存的节省量化：BF16 KV Cache (7.25GB) 量化为 INT8 后，占用降至 ~3.6GB (节省 50%)；量化为 F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

KV Cache 量化对显存的节省量化：BF16 KV Cache (7.25GB) 量化为 INT8 后，占用降至 ~3.6GB (节省 50%)；量化为 FP8 后，占用同样降至 ~3.6GB (节省 50%)。这使得在 24GB 显卡上，INT4 权重 + INT8 KV Cache 的总显存需求从 21.25GB (14+7.25) 降至 17.6GB (14+3.6)，释放了 3.65GB 显存用于更长上下文或更大 Batch Size。

## Corrected Claim

KV Cache 量化对显存的节省量化：BF16 KV Cache (7.25GB) 量化为 INT8 后，占用降至 ~3.6GB (节省 50%)；量化为 FP8 后，占用同样降至 ~3.6GB (节省 50%)。这使得在 24GB 显卡上，INT4 权重 + INT8 KV Cache 的总显存需求从 21.25GB (14+7.25) 降至 17.6GB (14+3.6)，释放了 3.65GB 显存用于更长上下文或更大 Batch Size。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16(16bit)转INT8/FP8(8bit)显存减半符合物理规律，数值计算(7.25/2≈3.6, 14+3.6=17.6)准确无误。
