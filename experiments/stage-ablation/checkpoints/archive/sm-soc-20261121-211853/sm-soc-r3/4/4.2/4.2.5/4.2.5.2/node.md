# N101: $QualityScore$ 对高溢价卖家的惩罚机制量化：若某商品 $N_{views}=1000$（log项=6.9）但好评率仅 80%（0.8），其 Sco

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

$QualityScore$ 对高溢价卖家的惩罚机制量化：若某商品 $N_{views}=1000$（log项=6.9）但好评率仅 80%（0.8），其 Score=5.52；若另一商品 $N_{views}=100$（log项=4.6）但好评率 95%（0.95），其 Score=4.37。算法需设置阈值 $T_{score}$，使得低分商品在排序中权重 $W_{final} = W_{base} \times e^{-\lambda (T_{score} - Score)}$ 显著降低。

## Corrected Claim

$QualityScore$ 对高溢价卖家的惩罚机制量化：若某商品 $N_{views}=1000$（log项=6.9）但好评率仅 80%（0.8），其 Score=5.52；若另一商品 $N_{views}=100$（log项=4.6）但好评率 95%（0.95），其 Score=4.37。算法需设置阈值 $T_{score}$，使得低分商品在排序中权重 $W_{final} = W_{base} \times e^{-\lambda (T_{score} - Score)}$ 显著降低。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（1000*0.8*6.9=5520/1000=5.52, 100*0.95*4.6=4370/1000=4.37），公式逻辑自洽，符合排序惩罚机制设计原理。

## Search Query

ranking algorithm penalty low rating high view count exponential decay
