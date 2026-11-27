# N156: RTX 4090 Founders Edition 物理厚度为 2.7 槽 (约 60mm)，但第三方品牌 (如 ASUS ROG Strix, MSI Sup

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

RTX 4090 Founders Edition 物理厚度为 2.7 槽 (约 60mm)，但第三方品牌 (如 ASUS ROG Strix, MSI Suprim) 通常为 3.0-3.5 槽 (65-75mm)；若机箱插槽间距为 3 槽 (75mm)，3.5 槽 GPU 安装会导致第二张卡风扇被遮挡或无法安装，需选择间距 ≥ 4 槽的机箱或选用薄版 (2.7 槽) GPU 型号。

## Corrected Claim

RTX 4090系列GPU物理厚度通常较大，第三方品牌（如ASUS ROG Strix, MSI Suprim）多为3.0-3.5槽（65-75mm）；若机箱插槽间距仅为3槽（75mm），3.5槽GPU安装会导致第二张卡风扇被遮挡或无法安装，需选择间距≥4槽的机箱或选用较薄版本的GPU型号。

## Evidence

[质询]陈述中关于RTX 4090 Founders Edition厚度为2.7槽（约60mm）的具体数值缺乏来源直接支持，且不同来源对4090系列厚度的描述存在差异（来源[2]称3-4槽，来源[3]称3.5槽），未明确区分FE版与第三方版的精确物理尺寸差异，存在将特定型号规格泛化或数值不精确的风险。 | 来源[2]和[3]支持RTX 4090系列GPU物理厚度较大（3-3.5槽），逻辑上3.5槽GPU在3槽间距机箱中确实会遮挡下一张卡，但来源未直接证实FE版仅为2.7槽这一具体经验参数，故降级。

## Search Query

RTX 4090 third party GPU thickness slot count 3.5 slot 4 slot

## Retrieval Sources

- {'url': 'https://willitrunai.com/blog/qwen-3-5-quantization-speed-comparison&rut=3fb2c1e4801f1dd9174df6498445cd31de44d01b58c2a80daeedd6b09d7b280f', 'type': 'ddg', 'title': 'Qwen 3.5 Speed by Quant (2026): Q2 vs Q4 vs Q8 on RTX 4090'}
- {'url': 'https://minibull.net/collection/slots-games/rtx-4090-how-many-slots-45829.html&rut=e4d4ff81b6300e897083268d2d4f3cc530647096b4b3b33641da7de13afd81bc', 'type': 'ddg', 'title': 'RTX 4090 How Many Slots: PCIe, Memory & Expansion Guide'}
- {'url': 'https://www.amazon.com/GeForce-GDDR6X-3-5-Slot-Gaming-Graphics/dp/B0FBSB611Q&rut=65cbac913d230e466013c566127014624fdc47465dc2340712c50ee585799245', 'type': 'ddg', 'title': 'NVD GeForce RTX 4090 24GB GDDR6X 3.5-Slot Gaming Graphics Card - amazon.com'}
