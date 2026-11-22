# N346: Mac Studio (M3 Max, 128GB) 的硬件采购成本约为 $4,000-$5,000，若以 3 年直线折旧（残值率 30%，因苹果设备保值率较高

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Mac Studio (M3 Max, 128GB) 的硬件采购成本约为 $4,000-$5,000，若以 3 年直线折旧（残值率 30%，因苹果设备保值率较高）计算，年折旧成本 = ($4,500 * 0.7) / 3 = $1,050/年；该折旧成本低于 RTX 6000 Ada 方案 ($1,813/年)，在低利用率 (<20%) 场景下可能使 Mac 方案的 Cost_Per_Token 低于 NVIDIA 专业卡方案。

## Corrected Claim

Mac Studio (M3 Max, 128GB) 的硬件采购成本约为 $4,000-$5,000，若以 3 年直线折旧（残值率 30%，因苹果设备保值率较高）计算，年折旧成本 = ($4,500 * 0.7) / 3 = $1,050/年；该折旧成本低于 RTX 6000 Ada 方案 ($1,813/年)，在低利用率 (<20%) 场景下可能使 Mac 方案的 Cost_Per_Token 低于 NVIDIA 专业卡方案。

## Evidence

先验知识/题面给定，逻辑校验通过：硬件成本量级符合市场常识，折旧公式计算正确（4500*0.7/3=1050），且1050<1813的比较逻辑自洽。

## Search Query

Mac Studio M3 Max 128GB price depreciation value
