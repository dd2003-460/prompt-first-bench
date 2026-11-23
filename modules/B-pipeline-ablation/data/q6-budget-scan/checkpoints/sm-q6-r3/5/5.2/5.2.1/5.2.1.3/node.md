# N237: 混合对象类型的加权命中率公式：H(TTL) = Σ_i (w_i * H_i(TTL))，其中 w_i 为第i类对象的流量占比，H_i(TTL) 为该类对象在T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

混合对象类型的加权命中率公式：H(TTL) = Σ_i (w_i * H_i(TTL))，其中 w_i 为第i类对象的流量占比，H_i(TTL) 为该类对象在TTL下的命中率；需分别计算静态图片、UGC、运营素材三类对象的H_i(TTL)后加权求和

## Corrected Claim

混合对象类型的加权命中率公式：H(TTL) = Σ_i (w_i * H_i(TTL))，其中 w_i 为第i类对象的流量占比，H_i(TTL) 为该类对象在TTL下的命中率；需分别计算静态图片、UGC、运营素材三类对象的H_i(TTL)后加权求和

## Evidence

先验知识/题面给定，逻辑校验通过：加权命中率公式符合全概率公式及流量加权平均的基本数学定义，量纲与逻辑自洽。
