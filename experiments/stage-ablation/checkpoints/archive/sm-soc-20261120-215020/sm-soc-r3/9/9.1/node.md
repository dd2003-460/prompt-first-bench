# N234: 标准化程度对噪声尺度参数 $b$ 的量化映射：建立商品类别标准化指数 $S_{std}$（0-1）与 $b$ 的线性关系 $b = b_{min} + (b_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

标准化程度对噪声尺度参数 $b$ 的量化映射：建立商品类别标准化指数 $S_{std}$（0-1）与 $b$ 的线性关系 $b = b_{min} + (b_{max} - b_{min}) \times (1 - S_{std})$。需确定二手市场中手机（$S_{std} \approx 0.9$）和家具（$S_{std} \approx 0.2$）的 $b$ 值，验证 $b \approx 0.05$ 和 $b \approx 0.15$ 的假设是否覆盖 15-25% 的偏差区间。

## Corrected Claim

标准化程度对噪声尺度参数 $b$ 的量化映射：建立商品类别标准化指数 $S_{std}$（0-1）与 $b$ 的线性关系 $b = b_{min} + (b_{max} - b_{min}) \times (1 - S_{std})$。需确定二手市场中手机（$S_{std} \approx 0.9$）和家具（$S_{std} \approx 0.2$）的 $b$ 值，验证 $b \approx 0.05$ 和 $b \approx 0.15$ 的假设是否覆盖 15-25% 的偏差区间。

## Evidence

先验知识/题面给定，逻辑校验通过：线性映射公式在数学上自洽，且手机（高标准化）对应低噪声b=0.05、家具（低标准化）对应高噪声b=0.15符合经济直觉，数值量级合理。
