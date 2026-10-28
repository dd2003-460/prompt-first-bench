# 编程用机械键盘选购 — 阶段 02 资料搜集（stage-gate: keyboard-selection-research）

> 创建：2026-10-28 · 阶段：02（信息调研）· 依据：阶段 01 空缺 R1–R4 · 实际观察时间：2026-10-28 · 执行通道：本地 agent 自执行（ralph web-llm 不可用，已改用公开网页检索，loop 不豁免）

---

## 一、来源索引（S1–S15）

每条来源记录：标题、URL、发布/更新时间、类型、置信度。所有“实际观察时间”统一为 2026-10-28（本次检索时间）。

| # | 标题 | URL | 发布/更新时间 | 类型 | conf |
|---|------|-----|---------------|------|------|
| S1 | Keychron Q1 Pro — Official Keychron Store | https://keychron-store.com/keychron-q1-pro/ | 2026-05-18（页面标注） | 官方商城 | 🟢 |
| S2 | Keychron Q1 Pro keyboard review: Simply unbeatable — PCWorld | https://www.pcworld.com/article/1502685/keychron-q1-pro-keyboard-review.html | 2025-04-28 | 专业评测 | 🟡 |
| S3 | Keychron Q1 Pro review: they actually pulled it off — The Verge | https://www.theverge.com/23633720/keychron-q1-pro-review-wireless-mechanical-keyboard | 2023-03-14 | 专业评测（时间久远，价格可能滞后） | 🟡 |
| S4 | Keychron Q1 Pro Wireless Mechanical Gaming Keyboard — GamingPCGuru | https://gamingpcguru.com/mechanical-gaming-keyboard-6/ | 2026-09-04 | 社区/聚合评测 | 🟡 |
| S5 | MonsGeek M1W Review: Best Budget Aluminum Wireless Mechanical Keyboard Under $150 — NicheVolt | https://nichevolt.com/keyboards/monsgeek-m1w.html | 未标注具体日期 | 社区评测 | 🟡 |
| S6 | Monsgeek M1W Review – Almost Great — SemiPro Tech+Gear | https://semiprotechgear.com/monsgeek-m1w-review-almost-great/ | 2023-09-05 | 社区评测 | 🟡 |
| S7 | Monsgeek M1W SP review: a near-perfect mechanical keyboard — PCGamesN | https://www.pcgamesn.com/monsgeek-m1w-sp-review | 2025-05-06 | 专业评测（M1W SP 型号，非标准 M1W） | 🟡 |
| S8 | NuPhy Air75 V2 — NuPhy 官方商城 | https://pay.nuphy.com/products/air75-v2 | 未标注具体日期 | 官方商城 | 🟢 |
| S9 | NuPhy Air75 V2 — NuPhy 官网 | https://nuphy.com/products/air75-v2 | 未标注具体日期 | 官网 | 🟢 |
| S10 | 【手慢无】NuPhy Air75 V2 机械键盘京东仅售 594 元 — 中关村在线 | https://diy.zol.com.cn/853/8535520.html | 2024-01-26 | 电商促销新闻（时间久远，价格可能滞后） | 🟡 |
| S11 | NuPhy Air75 V2 矮轴机械键盘 — Taobao/Tmall NuPhy 旗舰店 | https://www.taobao.com/list/item/742844466499.htm | 未标注 | 电商商城 | 🟡 |
| S12 | Leopold FC750R — AliExpress 聚合 | https://www.aliexpress.com/w/wholesale-leopold-fc750r.html | 未标注 | 电商聚合（第三方卖家，非 Leopoid 官方） | 🔴 |
| S13 | Leopold FC750R BT — GoodGamingShop（零售商） | https://www.goodgamingshop.com/product/87293af0-33c7-4ff2-b406-103037796fb5 | 未标注 | 零售商 | 🔴 |
| S14 | 2026 程序员办公机械键盘技术选购指南 — CSDN | https://blog.csdn.net/2501_92433281/article/details/160348077 | 2026-04-20 | 中文技术博客 | 🟡 |
| S15 | Best Mechanical Keyboard for Mac in 2026 — celmin.ca | https://celmin.ca/best-mechanical-keyboard-for-mac/ | 2026-07-02 | 专业评测 | 🟡 |

**说明**：S10 为 2024 年旧文，其价格仅作历史参考，不作为当前报价依据；S12/S13 为非官方零售商列表，数据弱，仅作参考。

---

## 二、各候选关键主张与证据

### C1: Keychron Q1 Pro（75%，热插拔，三模）

| 主张 | 观察内容（2026-10-28 检索） | 来源 | conf | 备注 |
|------|---------------------------|------|------|------|
| 布局/键数 | 75%，81 键（官方标称） | S1 | 🟢 | 与 S2/S4 的 84 键不一致 → 见 02.5 矛盾记录 |
| 连接方式 | Bluetooth 5.1 + 2.4 GHz + 有线 USB-C，三模；保存多达 3 个设备连接 | S1, S3 | 🟢/🟡 | S1 官方；S3 评测佐证 3 设备切换 |
| 电池/续航 | 4000 mAh；低亮度 RGB 下最多 100 小时，灯关闭最多 300 小时 | S1 | 🟢 | S4 声称 4500 mAh / 50–100+ 小时，与 S1 不一致 → 见 02.5 |
| 热插拔 | 支持热插拔，5 针 MX 兼容轴座 | S1, S3 | 🟢/🟡 | |
| 轴体选项 | Keychron K Pro 茶轴（段落）/香蕉轴（咔哒）/红轴（线性） | S3 | 🟡 | 2023 年评测，当前可选轴体可能已变 |
| 键帽/材质 | 双色注塑 PBT KSA 高度键帽；铝合金机身；双层垫片（gasket） | S1, S2 | 🟢/🟡 | |
| 编程/定制 | QMK/VIA 支持；1000 Hz 有线轮询率；全键无冲突 | S1 | 🟢 | |
| Mac/Windows 兼容 | 随盒附 Mac 与 Windows 两套键帽；Mac/Windows 布局可选 | S1, S3 | 🟢/🟡 | |
| 保修 | 2 年质保 | S1 | 🟢 | |
| 价格 | 官方 $189（组装版）；PCWorld $199；The Verge $199；GamingPCGuru $179–219 区间 | S1/S2/S3/S4 | 🟢/🟡 | 多源价格不一致，以结算页为准；美元→人民币换算未经核验（见“存在性断言-未核验”） |
| 交付 | 官方交付 7–14 天 | S1 | 🟢 | |

### C2: NuPhy Air75 V2（75%，低轮廓矮轴，热插拔，三模）

| 主张 | 观察内容（2026-10-28 检索） | 来源 | conf | 备注 |
|------|---------------------------|------|------|------|
| 布局/键数 | ANSI 75%，84 键 | S8, S9 | 🟢 | |
| 轴体 | Gateron 低轮廓机械轴（KS-33）；红轴 2.0（线性）/茔藓轴（段落，60gf）/芦荟轴（线性，37gf） | S8 | 🟢 | Taobao S11 标注“芦荟轴（线性轴/37gf）”与官方一致 |
| 连接方式 | 三模：2.4G + Bluetooth 5.1 + 有线 USB-C；2.4G 轮询率 1000 Hz，蓝牙 125 Hz，有线 1000 Hz | S8, S9 | 🟢 | |
| 热插拔 | 支持热插拔 | S8, S9 | 🟢 | |
| 键帽/材质 | 双色注塑 PBT 键帽；铝合金框架 + ABS 底壳；重 598 g | S8, S9 | 🟢 | |
| 续航 | 4000 mAh；灯全亮 35–57 小时（实验室），灯关闭最多 220 小时 | S8, S9 | 🟢 | 官方实验室数据，实际使用可能偏低 |
| Mac/Windows 兼容 | 兼容 macOS/Windows/Linux/Android/iOS；随盒附 Mac 与 Windows 修饰键键帽；功能行映射 macOS 快捷键 | S8, S9, S15 | 🟢/🟡 | S15 佐证“Mac-first 设计” |
| 保修 | 1 年质保 | S8 | 🟢 | |
| 价格 | 官方 $119.95–$129.95（随轴体/颜色）；京东 ¥594（S10，2024-01-26 旧文）；Taobao NuPhy 旗舰店 ¥699（S11） | S8/S9/S10/S11 | 🟢/🟡/🟡 | S10 价格已过期 2 年，仅作历史参考；S11 为商城列表，未标日期 |

### C3: MonsGeek M1W（75%，铝机身，三模，热插拔）

| 主张 | 观察内容（2026-10-28 检索） | 来源 | conf | 备注 |
|------|---------------------------|------|------|------|
| 布局/键数 | 75%，82 键（ANSI） | S5, S6 | 🟡 | |
| 连接方式 | 蓝牙 + 2.4G + USB-C 有线 | S5, S6, S7 | 🟡 | |
| 电池 | 6000 mAh | S5, S6 | 🟡 | |
| 轴体 | Akko V3 Cream（线性，S5）/Akko V3 Piano Pro（线性，S6/S7） | S5/S6/S7 | 🟡 | 不同评测标注的默认轴体不一致 |
| 热插拔 | 支持热插拔（MX 兼容） | S5, S6 | 🟡 | |
| 机身 | 全 CNC 铝合金机身；垫片结构；旋钮 | S5, S6 | 🟡 | |
| 定制软件 | **S5 声称支持 QMK/VIA；S6 声称使用专有软件、非 QMK/VIA** | S5/S6 | 🟡/🟡 | **直接矛盾，未解决 → 见 02.5** |
| Mac/Windows 兼容 | macOS/Windows 兼容；OS/连接切换键位于 Caps Lock 键帽下方 | S6 | 🟡 | “不频繁切换 Mac 与 Windows 的用户更合适”（S6 原文） |
| 价格 | S6：$109（散件）/ $139（组装）/ $149（组装 ISO）；S5：组装版低于 $150；S7（M1W SP 别型号）：$167 组装 | S5/S6/S7 | 🟡 | 型号版本多（M1W vs M1W SP），价格不可直接横向比较 |
| 质量问题 | S6 反馈 2.4G 连接不稳定（“从未在 2.4G 上获得稳定连接”） | S6 | 🟡 | 单个评测员体验，可能为个例 |

### C4: Leopold FC750R / FC750R BT（75%，Cherry MX，有线/蓝牙）

| 主张 | 观察内容（2026-10-28 检索） | 来源 | conf | 备注 |
|------|---------------------------|------|------|------|
| 布局/键数 | 75%（S12 表格与正文互有 TKL/75% 出入） | S12 | 🔴 | 来源本身不一致，数据弱 |
| 轴体 | Cherry MX（红/青/茶/黑可选，S12）；FC750R PD 使用 Alps RK8000（S12 聚合页） | S12 | 🔴 | |
| 连接方式 | FC750R 为有线 USB-C；FC750R BT 为蓝牙 + 有线双模 | S12, S13 | 🔴 | 非官方渠道 |
| 热插拔 | 不支持热插拔（S13） | S13 | 🔴 | |
| 键帽/材质 | PBT 双色注塑键帽；顶装结构；铝板 | S13 | 🔴 | |
| 兼容性 | Windows/Linux/Mac（S13 声称兼容） | S13 | 🔴 | 非官方来源 |
| 价格 | S12：$100–$130；S13：IDR 1,290,000（约等值未换算） | S12/S13 | 🔴 | 货币与渠道不明，不可作为预算判断依据 |

---

## 三、无法给出可核验来源的主张（显式降级）

以下主张属于**存在性断言-未核验**，不得作为已核验事实使用：

| 主张 | 降级理由 |
|------|----------|
| 各轴体的实际手感（段落/线性/咔哒的打字舒适度） | 手感为主观体验，公开来源无可复核的实测数据；需用户亲试或店内体验 |
| 长期耐用性与轴体晃动/QC 表现（半年以上使用） | 所有来源均为首发或短期评测，无长期跟踪数据 |
| 美元标价换算为人民币的到手价 | 未引用汇率来源，且未含关税/运费，仅为粗略估算 |
| Keychron Q1 Pro 当前官方库存与交付时效（官方标称 7–14 天） | 为官方页面陈述，未经独立验证，标记为“官方声明—未独立核验” |
| MonsGeek M1W 2.4G 连接在日常办公中的稳定性 | 仅单一评测员负面体验（S6），样本为 1 |

---

## 四、数据缺口（阶段 02 未解决，进入下一阶段仍明确保留）

1. 各型号人民币到手价与现货状态（官方站多为美元标价，且页面价格可能随时调整）；
2. MonsGeek M1W 是否支持 QMK/VIA（S5 与 S6 直接矛盾）；
3. Leopold FC750R 官方规格页（未找到官方来源，仅零售商/聚合页）；
4. 轴体手感与长期耐用性（主观，无法由文档核验，必须用户实测）。

---

## 五、阶段 02 Reviewer 门禁自检

- 阶段 01 关键空缺 R1–R4 是否逐项有证据或明确保留为未解决 ✅（R4 价格/现货部分有部分证据并标注滞后风险；R3 热插拔部分有官方证据）
- **证据来源完备**：每条关键主张均附来源（URL/路径 + 快照时间戳）；无来源主张已在 §三 显式降级为“存在性断言-未核验” ✅
- 关键主张独立来源：Q1 Pro 价格有 S1/S2/S3/S4 四源；Air75 V2 规格有官方 S8/S9 双源 ✅
- 易变事实时效性：价格类标注来源发布时间，S10（2024 年）已标注“可能滞后” ✅
- 未将网页检索摘要误写为事实：所有观察均标注来源与置信度 ✅
- 来源矛盾是否记录：Q1 Pro 键数/电池/价格；M1W QMK/VIA；Air75 V2 价格；Leopold 规格 — 已全部记录，交由 02.5 处理 ✅

**本阶段自判：证据已足够支撑进入 02.5 交叉核验；不强行收敛矛盾。**（ralph 运行时不可用，agent 自检，conf-0.2。）
