# N288: 长尾区域日均请求数 R_req_tail = 80,000 次/日，计算过程：Traffic_TB_tail (0.4TB) / s_avg (5MB) = 4

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

长尾区域日均请求数 R_req_tail = 80,000 次/日，计算过程：Traffic_TB_tail (0.4TB) / s_avg (5MB) = 400GB / 5MB = 80,000 次

## Corrected Claim

长尾区域日均请求数 R_req_tail = 80,000 次/日，计算过程：Traffic_TB_tail (0.4TB) / s_avg (5MB) = 400GB / 5MB = 80,000 次

## Evidence

先验知识/题面给定，逻辑校验通过：0.4TB = 400GB，400GB / 5MB = 400,000MB / 5MB = 80,000次，计算无误。
