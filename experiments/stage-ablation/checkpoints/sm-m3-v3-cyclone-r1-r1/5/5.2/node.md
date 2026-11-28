# N21: 对流参数化缺陷：多数 NWP 使用 Arakawa-Schubert 或 Kain-Fritsch 方案，无法解析眼墙对流尺度（<10km），导致登陆后对流崩溃

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

对流参数化缺陷：多数 NWP 使用 Arakawa-Schubert 或 Kain-Fritsch 方案，无法解析眼墙对流尺度（<10km），导致登陆后对流崩溃时机误差 ±6h；高分辨率模式（<3km）可部分捕捉眼墙对流，但计算成本增加 100 倍，业务预报仍依赖参数化，造成强台风（Vmax>50m/s）衰减率高估 5-10 kt/h

## Corrected Claim

对流参数化缺陷：多数 NWP 使用 Arakawa-Schubert 或 Kain-Fritsch 方案，无法解析眼墙对流尺度（<10km），导致登陆后对流崩溃时机误差 ±6h；高分辨率模式（<3km）可部分捕捉眼墙对流，但计算成本增加 100 倍，业务预报仍依赖参数化，造成强台风（Vmax>50m/s）衰减率高估 5-10 kt/h

## Evidence

先验知识/题面给定，逻辑校验通过
