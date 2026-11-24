# N498: 工作点C的SSD额定总写入字节数 (Rated_TBW_Bytes) 计算：基于DWPD=0.5与500TB原始容量，额定年写入量 = 500 * 10^6 M

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N167

## Claim

工作点C的SSD额定总写入字节数 (Rated_TBW_Bytes) 计算：基于DWPD=0.5与500TB原始容量，额定年写入量 = 500 * 10^6 MB * 0.5 * 365 = 9.125 * 10^10 MB/年。

## Corrected Claim

工作点C的SSD额定总写入字节数 (Rated_TBW_Bytes) 计算：基于DWPD=0.5与500TB原始容量，额定年写入量 = 500 * 10^6 MB * 0.5 * 365 = 9.125 * 10^10 MB/年。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB转换为MB需乘以10^6（假设十进制），500 * 10^6 * 0.5 * 365 = 9.125 * 10^10，计算无误。
