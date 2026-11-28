# N100: 消费级 GPU (GDDR6X/7) 的不可纠正比特错误率 (UBER) 在 7x24 高负载下显著高于 ECC HBM 内存，行业估计 HBM ECC 的 U

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

消费级 GPU (GDDR6X/7) 的不可纠正比特错误率 (UBER) 在 7x24 高负载下显著高于 ECC HBM 内存，行业估计 HBM ECC 的 UBER 约为 10^-16 to 10^-17 bits/bit/hour，而无 ECC GDDR 可能高达 10^-14 至 10^-15 [待核验]，这导致长期运行下出现 Silent Data Corruption (静默数据损坏) 的概率增加。

## Corrected Claim

消费级 GPU (GDDR6X/7) 由于缺乏 ECC 保护，其不可纠正比特错误率 (UBER) 在长期高负载下显著高于配备 ECC 的 HBM 内存，这导致长期运行下出现 Silent Data Corruption (静默数据损坏) 的风险增加。

## Evidence

[质询]参考来源均聚焦于SSD/NAND闪存的UBER定义与指标，完全未涉及GPU显存（GDDR/HBM）的可靠性数据，无法验证具体的数值量级（10^-16 vs 10^-14）及HBM ECC的具体性能表现。 | 逻辑上，非ECC显存缺乏纠错机制，其有效UBER确实远高于具备强纠错能力的HBM ECC，且高负载高温会加剧错误率，定性结论符合物理直觉；但具体数值属于经验事实，现有来源（[1][2][3]）均为SSD领域，与GPU显存主题无关，无法提供直接支持。

## Search Query

GDDR vs HBM ECC uncorrectable bit error rate UBER comparison

## Retrieval Sources

- {'url': 'https://blog.csdn.net/QiuShan226/article/details/156428423&rut=258e639a14c5e847049551aecf9c17249910897aa978e682b0e593ccd1106db6', 'type': 'ddg', 'title': 'UBER 低意味着什么？一文看懂 SSD 不可恢复位错误率的真实意义_ssd uber-CSDN博客'}
- {'url': 'https://blog.csdn.net/qq_34254642/article/details/105452627&rut=0e4f505cf5020afbd2f3bc61e5ecbd4256951729e4bfcc13973951a5b021ec56', 'type': 'ddg', 'title': 'Uber、Rber和mtbf的概念 - Csdn博客'}
- {'url': 'https://www.ssstc.com/tw/knowledge-detail/ssd-uncorrectable-bit-error-rate/&rut=5d4365a3d25f5e8516d01f26f298df55c9ce27fcf37f17d66748b7e8a0b21903', 'type': 'ddg', 'title': 'UBER（Uncorrectable Bit Error Rate，不可修正位元錯誤率）｜SSSTC建興儲存科技'}
