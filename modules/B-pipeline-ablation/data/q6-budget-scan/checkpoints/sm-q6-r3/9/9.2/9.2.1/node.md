# N363: 对象总数 N 的估算：基于日均上传 200GB 和平台生命周期（假设 90 天数据保留），若平均对象大小 $s_{avg}=1.5$MB，则累计对象数 $N \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

对象总数 N 的估算：基于日均上传 200GB 和平台生命周期（假设 90 天数据保留），若平均对象大小 $s_{avg}=1.5$MB，则累计对象数 $N \approx \frac{200 \times 1024 \text{ MB} \times 90}{1.5 \text{ MB}} \approx 12.3 \text{ million}$；此 N 值用于 Zipf 分母归一化。

## Corrected Claim

对象总数 N 的估算：基于日均上传 200GB 和平台生命周期（假设 90 天数据保留），若平均对象大小 $s_{avg}=1.5$MB，则累计对象数 $N \approx \frac{200 \times 1024 \text{ MB} \times 90}{1.5 \text{ MB}} \approx 12.3 \text{ million}$；此 N 值用于 Zipf 分母归一化。

## Evidence

先验知识/题面给定，逻辑校验通过：200GB/天 * 90天 = 18000GB = 18432000MB，除以1.5MB/对象 = 12288000 ≈ 12.3 million，计算无误且量级合理。
