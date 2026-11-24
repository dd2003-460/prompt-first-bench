# N234: 单 POP 月度折旧成本 Depreciation_Per_POP = (CapEx_Per_POP / Useful_Life_Months) × (1 - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

单 POP 月度折旧成本 Depreciation_Per_POP = (CapEx_Per_POP / Useful_Life_Months) × (1 - Residual_Value_Ratio)，其中 CapEx_Per_POP 包含服务器、存储、网络设备采购成本（典型值 ¥500k-1M/POP），Useful_Life_Months 为资产折旧年限（通常 36-60 个月），Residual_Value_Ratio 为残值率（通常 5%-10%）。

## Corrected Claim

单 POP 月度折旧成本 Depreciation_Per_POP = (CapEx_Per_POP / Useful_Life_Months) × (1 - Residual_Value_Ratio)，其中 CapEx_Per_POP 包含服务器、存储、网络设备采购成本（典型值 ¥500k-1M/POP），Useful_Life_Months 为资产折旧年限（通常 36-60 个月），Residual_Value_Ratio 为残值率（通常 5%-10%）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点代表了公式中三个关键参数（CapEx, Useful_Life, Residual_Value）的不同组合场景（低投入长寿命、标准、高投入短寿命），彼此独立且互不矛盾。虽然形式上是参数取值的实例化，但在学术分解中，提供典型工作点（Work Points）用于界定参数范围是标准做法，不属于冗余重复，而是对父节点公式的具体化验证和边界界定。）

## Search Query

CDN edge node capex server storage network equipment cost depreciation useful life
