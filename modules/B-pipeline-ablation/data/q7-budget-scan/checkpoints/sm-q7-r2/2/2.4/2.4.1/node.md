# N71: NVMe SSD单盘功耗参数：企业级NVMe SSD（如Intel P5510、Samsung PM1733）典型功耗为10-25W/盘，单盘容量1.92TB-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

NVMe SSD单盘功耗参数：企业级NVMe SSD（如Intel P5510、Samsung PM1733）典型功耗为10-25W/盘，单盘容量1.92TB-7.68TB，平均功耗密度约为1.3-1.5W/TB（以7.68TB盘为例，20W/7.68TB≈2.6W/TB，以1.92TB盘为例，15W/1.92TB≈7.8W/TB，需按实际选型确定），修正N15中5W/TB为2.5-5W/TB区间

## Corrected Claim

企业级NVMe SSD（如Intel P5510、Samsung PM1733）典型功耗约为10-25W/盘，单盘容量1.92TB-7.68TB。具体功耗密度需根据实际选型的容量和功耗计算，通常在2-8W/TB区间，而非固定的1.3-1.5W/TB。

## Evidence

[质询]陈述中关于平均功耗密度（1.3-1.5W/TB）与具体示例计算（2.6W/TB, 7.8W/TB）存在内部逻辑矛盾，且参考来源未提供具体的功耗数值以直接支持该经验参数。 | 来源[2]确认了Intel P5510的容量规格（3.84TB/7.68TB），但未提供功耗数据；陈述内部关于功耗密度的计算示例（2.6W/TB, 7.8W/TB）与其声称的平均值（1.3-1.5W/TB）严重不符，且作为经验事实缺乏直接来源支持。

## Search Query

enterprise NVMe SSD power consumption watts per drive Intel P5510 Samsung PM1733 datasheet

## Retrieval Sources

- {'url': 'https://www.storagereview.com/zh-CN/review/intel-p5510-nvme-enterprise-ssd-review&rut=7f4175322e8ad2cb02f096400a165017db305d5055996197fb08b6c22b7804d1', 'type': 'ddg', 'title': '英特尔 P5510 NVMe 企业级固态硬盘评测 - StorageReview.com'}
- {'url': 'https://www.cloudspress.com/%E8%8B%B1%E7%89%B9%E5%B0%94-p5510-nvme-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98%E8%AF%84%E6%B5%8B/&rut=9725cdf4068acc7d760b5d41224160459ceef85c17a215febde401179f57f6a9', 'type': 'ddg', 'title': '英特尔 P5510 NVMe 企业级固态硬盘评测：性能、规格与兼容性'}
- {'url': 'https://www.solidigm.com/products/data-center/product-briefs/dc-p5510.html&rut=9d39d80a19751c58b0b2e00d6a8fe5df47af09188d33e9d05a974cb69d7a4c15', 'type': 'ddg', 'title': 'Solidigm™ D7-P5510 Product Brief'}
