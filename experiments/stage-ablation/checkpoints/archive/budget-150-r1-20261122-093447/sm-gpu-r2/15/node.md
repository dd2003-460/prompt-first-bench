# N136: AMD Radeon PRO W7900 (48GB GDDR6, 1.9TB/s bandwidth, ~$5000) 作为专业工作站卡，其显存容量 (48G

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD Radeon PRO W7900 (48GB GDDR6, 1.9TB/s bandwidth, ~$5000) 作为专业工作站卡，其显存容量 (48GB) 和带宽 (1.9TB/s) 组合在 FP8 精度下提供单卡可行性，且价格低于 L40S；ROCm 软件栈在 Linux 下对 PyTorch 支持成熟，是评估'AMD 专业卡'性价比的必要候选，填补了消费级 AMD 卡 (RX 7900 XTX) 与数据中心 AMD 卡 (MI300X) 之间的价格/性能空白。

## Corrected Claim

AMD Radeon PRO W7900 拥有 48GB GDDR6 显存和 1.9TB/s 带宽，其硬件规格在 FP8 精度下具备单卡运行大模型的潜力；作为专业卡，其定位介于消费级与数据中心卡之间，但 ROCm 软件栈成熟度及具体价格优势需结合最新市场数据进一步评估。

## Evidence

[质询]陈述中关于 ROCm 软件栈成熟度、FP8 单卡可行性以及具体价格（~$5000）和与 L40S 的价格对比属于经验性市场/软件生态事实，参考来源仅提供了硬件规格（显存、带宽），未提供软件支持度或价格数据，无法通过现有来源直接验证这些非硬件属性。 | 来源 [1][2][3] 直接支持硬件规格（48GB GDDR6, 1.9TB/s 带宽由 384-bit * 18Gbps 计算得出），但 ROCm 成熟度、FP8 可行性及价格对比缺乏来源支持，属经验事实，逻辑自洽但缺来源直接支持。

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html&rut=3e2bb66ec9d359b525aaa9d2923594370a6770a1c282e7c898fdddb942fd2890', 'type': 'ddg', 'title': 'AMD Radeon™ PRO W7900 Professional Graphics'}
- {'url': 'https://www.amd.com/content/dam/amd/en/documents/products/graphics/workstation/radeon-pro-w7900-datasheet.pdf&rut=0dd197f08b4ec648a2ed44ac19397d06e7146fd38516ac204d11ed74046c155a', 'type': 'ddg', 'title': 'PDF 232010504-B_Radeon-PRO_W7900_Datasheet_PDF - AMD'}
- {'url': 'https://www.techpowerup.com/gpu-specs/radeon-pro-w7900.c4147&rut=c9e29e2794737cb68f765be57350edfdc1d0af4030a640638ad6f71c19e3ad7b', 'type': 'ddg', 'title': 'AMD Radeon PRO W7900 Specs | TechPowerUp GPU Database'}
