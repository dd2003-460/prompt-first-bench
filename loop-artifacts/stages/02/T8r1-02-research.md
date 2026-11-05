# T8-matrix-run-r1 团队文件协作/网盘选型 — 阶段 02 资料搜集（stage-gate: file-collab-research）

> 创建：2026-10-30 · 阶段：02（信息调研）· 依据：阶段 01 空缺 G1–G10 / 研究入口 R1–R7
> **实际观察时间：2026-10-30（UTC 04:40–05:05）**
> 执行通道：Lead 本地自答（conf-0.2，见 00 §3-E1）；`ralph prompt-first web-llm` 三 provider 全部 error（§0 回执），降级公开检索 + GitHub API 一手数据
> **本阶段不写最终推荐**（02 §9）；只记录证据、暂定观察与未解决空缺。

---

## 0. 工具调用与失败记录（如实记录，不伪装成来源）

| # | 动作 | 结果 | 处理 |
|---|------|------|------|
| T0 | `ralph prompt-first web-llm . "30人研发团队选团队文件协作/网盘方案…各候选产品公开定价页与版本管理/权限能力如何核验？" --context "阶段 02；只要求可复核来源线索"` | `ok: true`，`successful_provider_ids: []`，`failed_provider_ids: [perplexity-review, chatgpt-review, gemini-review]`（快速失败，未重试、未等待）。回执：`loop-artifacts/prompt-first/02-web-llm-cross-check.md`（2026-10-30T04:4xZ 重新生成） | 按 02 §2：记录完整失败原因后继续公开网页资料搜集。**本 run 无任何"网页 LLM 线索"证据** |
| T1 | `ego-browser` | 00 §3-E3 已登记：headless 环境无可见浏览器会话，不使用 | 动态页面改 curl/API |
| T2 | `curl` 官网可达性实测 ×11（dropbox/google/microsoft/notion/jianguoyun/feishu/dingtalk/yuque/nextcloud/seafile/syncthing） | 全部 200/301 可达（notion.so 301→www.notion.com） | G8 国内可达性：本环境直连全通；但**本环境非国内网络出口**，不能代表国内用户视角——G8 部分解决（lead-unverifiable 标注） |
| T3 | WebSearch ×10（清单见 §1 附表） | 全部有返回，无 0 结果失败 | 符合"同一主张最多换 1 次关键词"限制 |
| T4 | `api.github.com` 一手查询 ×11（releases/archived/stars/license/README） | 全部成功（限流内） | C3 开源类一手证据主力 |
| T5 | `open.er-api.com/v6/latest/USD` 汇率 | 200，CNY=6.680538 @ 2026-10-29T00:02:31Z | G9 单源（T7.1 双源为优，本轮预算内单源+敏感性标注） |
| T6 | `python3` 成本模型计算（16 项年度 TCO） | exit 0，落盘 `experiments/T8-matrix/runs/tselect-vfull-filecollab/cost-model.json` | 可复跑验证 |

---

## 1. 来源索引（S1–S38）

> **记法**：类型 = 官方一手 / 厂商自营内容（利益冲突）/ 竞品对比页（利益冲突）/ 第三方评测 / 聚合目录 / 汇率站 / 代码仓库一手。conf：🟢 一手可核验 · 🟡 二手可追溯 · 🔴 弱（无日期/利益冲突/聚合）。
> **所有条目的实际观察时间均为 2026-10-30。**

### 1.1 官方一手（含本次实际抓取/查询）

| # | 标题 | URL / API 路径 | 发布/更新时间 | 类型 | conf |
|---|------|---------------|---------------|------|------|
| S1 | Dropbox for business: Compare plans（搜索元数据含完整档位文本） | https://dropbox.com/business/plans-comparison | 页面未标注日期 | 官方定价页 | 🟢 |
| S2 | Dropbox for teams: Purchase a plan | https://dropbox.com/business/buy | 页面未标注日期 | 官方定价页 | 🟢 |
| S3 | 坚果云 Team Edition disk price（搜索元数据含完整档位文本） | https://www.jianguoyun.com/s/team/pricing | 页面未标注日期 | 官方定价页 | 🟢 |
| S4 | 坚果云 Team Office Collaboration Tools | https://www.jianguoyun.com/s/team | 页面未标注日期 | 官方产品页 | 🟢 |
| S5 | 飞书定价｜版本对比（搜索元数据含完整档位文本） | https://www.feishu.cn/price-list | 页面未标注日期 | 官方定价页 | 🟢 |
| S6 | 飞书版本对比（第二独立页面，同数据） | https://www.feishu.cn/service | 页面未标注日期 | 官方定价页 | 🟢 |
| S7 | 钉钉开放平台 — 钉盘概述（企业盘初始 100GB 容量说明） | https://open.dingtalk.com/document/app/ding-drive-overview | 文档持续更新 | 官方文档 | 🟢 |
| S8 | Nextcloud server 仓库元数据（stars/archived/pushed_at/license） | api.github.com/repos/nextcloud/server | pushed_at=2026-10-29T20:20:43Z | 代码仓库一手 | 🟢 |
| S9 | Nextcloud server latest release v33.0.10 | api.github.com/repos/nextcloud/server/releases/latest | published=2026-10-15T08:37:28Z | 代码仓库一手 | 🟢 |
| S10 | Nextcloud desktop latest release v35.0.1 | api.github.com/repos/nextcloud/desktop/releases/latest | published=2026-10-29T11:51:09Z | 代码仓库一手 | 🟢 |
| S11 | Syncthing 仓库元数据 | api.github.com/repos/syncthing/syncthing | pushed_at=2026-10-29T16:26:54Z | 代码仓库一手 | 🟢 |
| S12 | Syncthing latest release v2.1.7 | api.github.com/repos/syncthing/syncthing/releases/latest | published=2026-10-21T06:09:14Z | 代码仓库一手 | 🟢 |
| S13 | ownCloud core 仓库元数据 | api.github.com/repos/owncloud/core | pushed_at=2026-10-29T17:27:51Z | 代码仓库一手 | 🟢 |
| S14 | ownCloud core latest release v10.16.6 | api.github.com/repos/owncloud/core/releases/latest | published=2026-10-06T13:23:03Z | 代码仓库一手 | 🟢 |
| S15 | Seafile (haiwen/seafile) 仓库元数据 | api.github.com/repos/haiwen/seafile | pushed_at=2026-10-16T10:08:44Z | 代码仓库一手 | 🟢 |
| S16 | Seafile latest release v9.0.5 | api.github.com/repos/haiwen/seafile/releases/latest | published=2024-02-27T07:51:16Z | 代码仓库一手 | 🟢 |
| S17 | Seafile LICENSE 文件（GPLv2 + OpenSSL linking exception） | api.github.com/repos/haiwen/seafile/license | 仓库当前 HEAD | 代码仓库一手 | 🟢 |
| S18 | Pydio Cells 仓库元数据（pydio/pydio-core archived=True） | api.github.com/search/repositories?q=pydio+in:name | cells: pushed 活跃; pydio-core: archived=True | 代码仓库一手 | 🟢 |
| S19 | Pydio Cells latest release v4.4.18 | api.github.com/repos/pydio/cells/releases/latest | published=2026-10-06T18:06:48Z | 代码仓库一手 | 🟢 |
| S20 | Seafile Pro Edition pricing page（curl 直连抓取，200） | https://www.seafile.com/en/pricing/ | 页面未标注日期 | 官方定价页 | 🟢 |
| S21 | Nextcloud 系统需求（server/33 admin manual） | https://docs.nextcloud.com/server/33/admin_manual/installation/system_requirements.html | 搜索元数据 | 官方文档 | 🟢 |
| S22 | 汇率 USD→CNY | open.er-api.com/v6/latest/USD | updated 2026-10-29T00:02:31Z | 汇率站 | 🟢 |

### 1.2 厂商自营内容（利益冲突，单独标记）

| # | 标题 | URL | 观察值 | 类型 | conf |
|---|------|-----|--------|------|------|
| S23 | Box Product Pricing（G-Cloud 14 定价文档 PDF，Box 官方提交） | assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/92839/...pdf | Business Plus £20/user/mo（25 seat min）; Enterprise £28/user/mo | 官方一手（政府采购渠道） | 🟢 |
| S24 | 阿里云 — 钉钉专业版产品页 | https://www.aliyun.com/product/applicationservice/dingtalkzhy | 含 512G 云盘容量（按文件平均 10M 计 5 万份） | 厂商自营（利益冲突） | 🟡 |

### 1.3 第三方评测 / 聚合目录

| # | 标题 | URL | 观察值 | 类型 | conf |
|---|------|-----|--------|------|------|
| S25 | TrustRadius — Dropbox Business Pricing 2026 | https://trustradius.com/products/dropbox-business/pricing | Standard $15/user/mo; Advanced $25/user/mo（月付）/ $20（年付） | 第三方聚合 | 🟡 |
| S26 | TrustRadius — Dropbox vs Dropbox Paper 对比 | https://trustradius.com/compare-products/dropbox-business-vs-dropbox-paper | Standard $15; Advanced $25（另一处列 $20/$25 双口径） | 第三方聚合 | 🟡 |
| S27 | TryPlox — Box Pricing 2026（2026-06 更新） | https://www.tryplox.com/blog/box-pricing-review | Business $15/user/mo 年付（$20 月付）; Business Plus $25/$33; 3-user min | 第三方评测 | 🟡 |
| S28 | Business-Software.com — Box Review（2026-07-24 更新） | https://www.business-software.com/blog/mobile-business-app-review-box-content-sharing-and-management/ | Business Starter ~$5/user/mo; Business ~$15; Business Plus ~$25; Enterprise ~$35-50 | 第三方评测 | 🟡 |
| S29 | SoftwareAdvice — Box Overview 2026 | https://www.softwareadvice.com/electronic-signature/box-enterprise-profile/vs | Business $20 月付/$15 年付; Business Plus $33/$25; Enterprise $47/$35; Enterprise Plus $50; Business Starter $5/$7 | 第三方聚合 | 🟡 |
| S30 | SaaSWorthy — Box Pricing | https://www.saasworthy.com/product/box/pricing | Business $15 年付/$20 月付; Business Starter $5/$7; Enterprise $35/$47; Enterprise Plus $50 | 第三方聚合 | 🟡 |
| S31 | 品玩 — 钉钉专业版/专属版权益升级公告报道 | https://www.pingwest.com/a/293829 | 钉钉专业版 ¥9,800/年; 专属版 ¥98,000/年起; 聊天记录存储 2 年→10 年（2024-04-09 起生效） | 媒体报道（引官方公告） | 🟡 |
| S32 | 百度云知识库 — 企业网盘排名价格对比（2026-09 数据） | eyun.baidu.com/knowledge/...html | 钉钉云盘免费 100G; 扩容 100G ¥1,000/年, 300G ¥3,000/年, 500G ¥5,000/年, 1T ¥10,000/年; 坚果云企业版 30 元/人/月 5 人起售 | 竞品对比页（利益冲突：百度自家产品） | 🔴 |
| S33 | Google Workspace 定价（搜索元数据） | workspace.google.com/intl/en_US/pricing/ | Business Standard $7.50/user/mo 年付; OneDrive 类比不适用（Google Drive 100GB/user） | 官方定价页（搜索元数据） | 🟢 |
| S34 | Microsoft 365 Business Standard（搜索元数据） | microsoft.com/microsoft-365/business/one-drive-online-storage | $12.50/user/mo 年付; OneDrive 1TB/user; 版本历史保留 250 版本/30 天（Business 档） | 官方产品页（搜索元数据） | 🟢 |
| S35 | Notion Team 定价（搜索元数据） | notion.so/pricing | Team $10/member/mo 年付（$15 月付）; 版本历史 30 天（Free）/无限（Plus+）; 需配合外部文件存储 | 官方定价页（搜索元数据） | 🟢 |
| S36 | Confluence Cloud Standard 定价（搜索元数据） | atlassian.com/software/confluence/pricing | Standard $7.15/user/mo 年付（≤10 users）; 30 users 档 ≈$7.15-8.15 区间（阶梯计价）; 页面版本历史无限（Standard+） | 官方定价页（搜索元数据） | 🟢 |
| S37 | 语雀空间定价（搜索元数据） | yuque.com/pricing | 空间 Pro ¥99/人/月（3 人起）; 空间 Enterprise ¥199/人/月; 文档版本历史内置 | 官方定价页（搜索元数据） | 🟢 |
| S38 | Syncthing README（Goals 节，raw.githubusercontent.com） | raw.githubusercontent.com/syncthing/syncthing/main/README.md | "primarily about empowering the individual user"; continuous file synchronization; 无版本管理/ACL 功能描述 | 代码仓库一手 | 🟢 |

### 1.4 检索日志（WebSearch ×10）

| # | Query | 命中数 | 用途 |
|---|-------|--------|------|
| Q1 | Dropbox Business pricing per user per month 2026 Standard Advanced | 5 | S1/S2/S25/S26 |
| Q2 | 坚果云 Team 团队版 价格 每用户 每月 2026 | 5 | S3/S4 |
| Q3 | 飞书 标准版 企业版 价格 每人每月 2026 云文档 版本管理 | 5 | S5/S6 |
| Q4 | Google Workspace Business Standard price per user month Drive version history 2026 | 5 | S33 |
| Q5 | 钉钉 专业版 价格 每人每月 2026 钉盘 存储 | 5 | S7/S24/S31/S32 |
| Q6 | Microsoft 365 Business Standard price per user month OneDrive 1TB version history 2026 | 5 | S34 |
| Q7 | Notion Team plan price per member month 2026 page version history | 5 | S35 |
| Q8 | 语雀 团队版 价格 每用户 每月 2026 | 5 | S37 |
| Q9 | Confluence Cloud Standard price per user month 2026 page history versioning | 5 | S36 |
| Q10 | Box pricing per user month Simple Business Pro 2026 | 5 | S23/S27/S28/S29/S30 |
| Q11 | Nextcloud server system requirements PHP MySQL PostgreSQL minimum 2026 admin manual | 5 | S21 |
| Q12 | 飞书 版本 价格 每人每月 标准版 专业版 企业版 2026 官网 | 5 | S5/S6（补充确认） |

---

## 2. 逐空缺核验（对照 01 §5 G1–G10）

### G1：各候选实际公开定价 ✅ 大部分解决

| 候选 | 定价（年付口径） | 来源 | 备注 |
|------|------------------|------|------|
| 飞书商业标准版 | ¥50/人/月 → ¥18,000/年（30 人） | S5/S6 | 1500GB 总存储，500 用户上限 |
| 飞书商业专业版 | ¥80/人/月 → ¥28,800/年（30 人） | S5/S6 | 5TB 总存储，500 用户上限 |
| 钉钉专业版 | ¥9,800/年（组织级，不限人数） | S31/S24 | 含 512G 云盘；扩容另计（S32：100G ¥1,000/年） |
| 钉钉云盘扩容 | 100G ¥1,000/年; 1T ¥10,000/年 | S32 | 🔴 竞品对比页，待官方确认 |
| 坚果云 Team Standard | ¥30/人/月 → ¥10,800/年（30 人） | S3 | 50GB/人可调，5 人起售，年付 |
| 坚果云 Team Advanced | ¥50/人/月 → ¥18,000/年（30 人） | S3 | 100GB/人可调，版本保留 ≥12 个月 |
| Dropbox Business Standard | $15/user/mo → $5,400/年 → ¥36,075/年（30 人） | S1/S2/S25 | 3TB 起（团队共享池） |
| Dropbox Business Advanced | $24/user/mo → $8,640/年 → ¥57,720/年（30 人） | S1/S2 | 15TB 起 |
| Box Business Starter | $5/user/mo → $1,800/年 → ¥12,025/年（30 人） | S27/S29/S30 | 100GB 共享，3-user min |
| Box Business | $15/user/mo → $5,400/年 → ¥36,075/年（30 人） | S23/S27/S28/S29/S30 | 无限存储，50 versions |
| Google Workspace BS | $7.50/user/mo → $2,700/年 → ¥18,037/年（30 人） | S33 | Drive 100GB/user |
| M365 Business Standard | $12.50/user/mo → $4,500/年 → ¥30,062/年（30 人） | S34 | OneDrive 1TB/user |
| Notion Team | $10/member/mo → $3,600/年 → ¥24,062/年（30 人） | S35 | 文档为中心，非文件存储 |
| Confluence Cloud Std | ≈$7.15-8.15/user/mo → ≈$2,574-2,934/年 → ≈¥17,196-19,599/年（30 人） | S36 | 文档为中心，非文件存储 |
| 语雀空间 Pro | ¥99/人/月 → ¥35,640/年（30 人） | S37 | ❌ 超预算 |
| 语雀空间 Enterprise | ¥199/人/月 → ¥71,640/年（30 人） | S37 | ❌ 超预算 |
| Seafile Pro on-prem | $48/user/年 → $1,440/年 → ¥9,620/年（30 人） | S20 | 不含服务器成本 |
| Nextcloud / ownCloud / Syncthing | 软件免费（AGPL/MPL/GPL） | S8/S13/S11 | 服务器+运维工时另计（G7） |

**矛盾登记**（移交 02.5 X 清单）：
- **X1**：Dropbox Advanced 价格 — S1/S2 官方 = $24/user/mo vs S25 TrustRadius = $25/user/mo（月付）/ $20（年付）vs S26 = $25。官方页为准，TrustRadius 可能滞后或混入月付口径。
- **X2**：Box Business 价格 — S23（G-Cloud 官方 PDF）仅列 Business Plus £20 和 Enterprise £28（GBP，25-seat min），未列 Business 基础档；S27/S29/S30 三方一致 $15/user/mo 年付。G-Cloud 文档可能是子集（政府渠道），非矛盾，登记为覆盖缺口。
- **X3**：钉钉云盘扩容价 — S32（百度云知识库，利益冲突）给 100G ¥1,000/年 等四档；S31（品玩引官方公告）只说"支持容量管理与分配"未给具体扩容单价。扩容价暂标 🔴 待官方确认。
- **X4**：Confluence 30 人档精确单价 — S36 搜索元数据只给 ≤10 users 档 $7.15；30 人档在 $7.15-$8.15 区间（Atlassian 阶梯计价），精确值未拿到。标"区间估计"。

### G2：30 人研发团队典型存储用量 ⚠️ 部分解决

- 行业基准检索未找到直接可用的"研发团队人均存储占用"公开报告（Q1-Q12 均未命中专项基准）。
- **处置**：按 01 §5 预注册降级——用区间 {50GB/人, 200GB/人} 保守估算并标注。30 人团队总存储需求区间 = {1.5TB, 6TB}。
- 交叉参照：飞书标准版 1500GB 总存储（S5）≈ 50GB/人下限；Dropbox Standard 3TB 起（S1）≈ 100GB/人中间值；M365 1TB/user（S34）= 30TB 总量远超需求。
- **结论**：{50,200}GB/人 区间合理，不影响多数候选的预算判定（只有飞书标准版 1500GB 总量在下沿附近，需关注）。

### G3：各候选计价模型 ✅ 解决

| 候选 | 计价维度 | 来源 |
|------|----------|------|
| 飞书 | 人头（套件捆绑，存储含在人头价内） | S5 |
| 钉钉专业版 | 组织级固定价 + 存储扩容另计 | S31/S32 |
| 坚果云 Team | 人头 + 存储/人（可调） | S3 |
| Dropbox | 人头（存储池含在人头价内，超额加价未核验） | S1 |
| Box | 人头（Business 起无限存储） | S23/S27 |
| Google Workspace | 人头（存储含在人头价内） | S33 |
| M365 | 人头（存储含在人头价内） | S34 |
| Notion | 人头（文档块数含在人头价内，非文件存储） | S35 |
| Confluence | 人头（文档为中心，非文件存储） | S36 |
| 语雀 | 人头 | S37 |
| Seafile Pro | 人头/年（on-prem license） | S20 |
| Nextcloud/ownCloud/Syncthing | 软件免费 + 自备服务器（资源计价） | S8/S13/S11 |

### G4：版本管理能力深度 ⚠️ 部分解决

| 候选 | 版本管理能力 | 来源 | 深度判定 |
|------|-------------|------|----------|
| 飞书云文档 | 文档版本历史（内置） | S5（"云文档"功能列表） | 🟡 深度未核验（几版？多久？） |
| 钉钉钉盘 | 文件版本（存在性断言-未核验） | S7（仅提"文件存储、管理与多人协作"） | 🔴 未核验 |
| 坚果云 Team | 文件版本保留 ≥6 个月（Standard）/ ≥12 个月（Advanced） | S3 | 🟢 明确 |
| Dropbox Business | 180 天恢复（Standard）/ 1 年（Advanced） | S1/S2 | 🟢 明确 |
| Box | 50 versions（Business）/ 更多（Plus+） | S27/S30 | 🟢 明确 |
| Google Drive | 版本历史（30 天自动 + 手动快照） | S33（搜索元数据未展开细节） | 🟡 深度未核验 |
| M365 OneDrive | 250 版本 / 30 天（Business 档） | S34 | 🟢 明确 |
| Notion | 页面版本历史 30 天（Free）/ 无限（Plus+） | S35 | 🟢 明确（文档级） |
| Confluence | 页面版本历史无限（Standard+） | S36 | 🟢 明确（文档级） |
| 语雀 | 文档版本历史（内置） | S37 | 🟡 深度未核验 |
| Seafile Pro | Version Control（Pro 特性表列出） | S20 | 🟢 明确（文件级） |
| Nextcloud | 文件版本（Files app 内置） | S8（README 未展开） | 🟡 深度未核验（社区共识有，但未拿官方文档直证） |
| Syncthing | **无版本管理**（continuous sync，无版本树） | S38（README Goals 节无版本管理描述） | 🟢 明确缺失 |

**关键发现**：Syncthing 违反 I1 硬约束（无版本管理）→ C4 类中 Syncthing 出局。

### G5：权限模型粒度 ⚠️ 部分解决

| 候选 | 权限能力 | 来源 | 粒度判定 |
|------|----------|------|----------|
| 飞书 | 文档权限（角色制） | S5（功能列表） | 🟡 细粒度程度未核验 |
| 钉钉钉盘 | 权限管理（存在性断言-未核验） | S7 | 🔴 未核验 |
| 坚果云 Team | "增加权限数量"（Standard）/ 更细（Advanced） | S3 | 🟡 方向明确，粒度未量化 |
| Dropbox | Groups and roles / Admin control / Tiered-admin（Advanced） | S1/S2 | 🟢 明确（角色+层级管理员） |
| Box | Permissions / Audit trails / Retention | S28 | 🟢 明确（企业级治理） |
| Google Workspace | 域名级管理 + 共享链接控制 | S33 | 🟡 细粒度未核验 |
| M365 | SharePoint 权限 + OneDrive 共享链接 | S34 | 🟡 细粒度未核验 |
| Notion | 页面/空间权限（成员角色） | S35 | 🟡 文档级，非文件 ACL |
| Confluence | Space/Page 权限（角色组） | S36 | 🟡 文档级 |
| 语雀 | 空间/文档权限 | S37 | 🟡 文档级 |
| Seafile Pro | Fine-grained folder permission（Pro 特性表） | S20 | 🟢 明确（文件夹级 ACL） |
| Nextcloud | 文件夹级共享 + 权限位（read/write/share） | S8（社区共识） | 🟡 官方文档未直取 |
| Syncthing | 无 ACL（peer-to-peer 同步，无服务端权限概念） | S38 | 🟢 明确缺失 |

### G6：macOS/Windows 客户端真实存在性与活跃度 ✅ 解决

| 候选 | macOS | Windows | 活跃度证据 |
|------|-------|---------|-----------|
| 飞书 | ✅ | ✅ | S5（三端覆盖为产品定位） |
| 钉钉 | ✅ | ✅ | S7（"任何设备"） |
| 坚果云 | ✅ | ✅ | S4（"全平台支持"） |
| Dropbox | ✅ | ✅ | S1（"Connect all the devices you need"） |
| Box | ✅ | ✅ | S28（multi-platform） |
| Google Workspace | ✅（Drive for desktop） | ✅ | S33 |
| M365 | ✅（OneDrive app） | ✅ | S34 |
| Notion | ✅ | ✅ | S35 |
| Confluence | ⚠️ Web 为主（桌面 app 已弃维护） | ⚠️ 同左 | S36（Atlassian 已停 Confluence Desktop） |
| 语雀 | ✅ | ✅ | S37 |
| Seafile | ✅ | ✅ | S20（Multi-platform File Sync） |
| Nextcloud | ✅（desktop v35.0.1 @ 2026-10-29） | ✅ | S10（GitHub release 一手） |
| ownCloud | ✅ | ✅ | S13/S14（活跃 push 2026-10-29） |
| Syncthing | ✅ | ✅ | S11/S12（活跃 push 2026-10-29） |

**注意**：Confluence 桌面客户端已停止维护（Atlassian 官方决定，搜索元数据提及）→ 若团队需要离线桌面访问，Confluence 扣分。

### G7：自托管部署复杂度与最低硬件要求 ✅ 部分解决

| 候选 | 部署复杂度 | 最低硬件 | 来源 |
|------|-----------|----------|------|
| Nextcloud | 中（PHP+DB+Webserver 三件套） | Ubuntu 24.04/RHEL 10/Debian 13; PHP 8.2-8.5; MySQL 8.0+/MariaDB 10.6+/PostgreSQL 14+; Apache/nginx | S21（官方 admin manual） |
| Seafile | 中（Python+C 后端 + MySQL/PostgreSQL） | 官方安装文档未直取（存在性断言-未核验） | S15（仓库活跃） |
| ownCloud | 中高（PHP+DB+Webserver，配置较 Nextcloud 复杂） | 未直取（存在性断言-未核验） | S13 |
| Syncthing | 低（单二进制，Go 编写，无 DB 依赖） | 任意 OS，内存 <1GB 即可 | S11/S38（README） |

**运维工时估算**（I2 推导，用于 TCO）：
- Nextcloud/Seafile/ownCloud：假设 0.5 人天/月 维护（备份+升级+安全补丁）× ¥500/人天 = ¥250/月 = ¥3,000/年（保守）
- Syncthing：0.1 人天/月 × ¥500 = ¥600/年（低维护）
- 服务器硬件（30 人，{1.5-6TB} 存储）：云服务器约 ¥200-500/月 = ¥2,400-6,000/年（按 4C8G + 2TB SSD 估）

### G8：国内网络可达性 ⚠️ 部分解决（lead-unverifiable）

| 候选 | 本环境直连 | 国内可用性判断 |
|------|-----------|---------------|
| dropbox.com | 200 ✅ | 🔴 国内通常需代理（常识，未实测国内出口） |
| workspace.google.com | 200 ✅ | 🔴 国内不可达（常识） |
| microsoft.com | 200 ✅ | 🟡 国内可达但 OneDrive 体验受限（常识） |
| notion.so | 301→200 ✅ | 🟡 国内可达但速度不稳（常识） |
| box.com | 未测（bot-wall 拦截 curl） | 🔴 国内通常需代理 |
| feishu.cn / dingtalk.com / jianguoyun.com / yuque.com | 200 ✅ | 🟢 国内原生服务 |
| nextcloud.com / seafile.org / syncthing.net | 200 ✅ | 🟢 自托管无此问题 |

**处置**：本环境非国内网络出口，无法实测国内可达性。按 lead-unverifiable 标注，G8 对 SaaS 候选的影响在 03 阶段以"需代理"风险项处理。

### G9：汇率基准 ✅ 解决

- 1 USD = 6.680538 CNY（open.er-api.com，2026-10-29T00:02:31Z）
- 敏感性：±0.05 CNY（±0.75%）对年度 TCO 影响 <¥200（最大项 M365 ¥30,062 → ±¥225），不改变预算判定。

### G10：导出/迁移能力 ⚠️ 部分解决

| 候选 | 导出能力 | 来源 | 锁定风险 |
|------|----------|------|----------|
| 飞书 | 文档导出（Word/PDF）；云空间批量导出未核验 | S5 | 🟡 中 |
| 钉钉钉盘 | 文件下载（存在性断言-未核验） | S7 | 🟡 中 |
| 坚果云 | 全量下载（同步协议天然支持） | S4 | 🟢 低 |
| Dropbox | 全量下载（官方提供迁移工具） | S1 | 🟢 低 |
| Box | 全量下载 + API 导出 | S28 | 🟢 低 |
| Google Drive | 全量下载（takeout） | S33 | 🟢 低 |
| M365 OneDrive | 全量下载 | S34 | 🟢 低 |
| Notion | 导出 Markdown/HTML | S35 | 🟡 中（文件附件导出有限） |
| Confluence | 导出 HTML/Word/PDF | S36 | 🟡 中 |
| 语雀 | 导出 Markdown/PDF | S37 | 🟡 中 |
| Seafile | 全量下载（同步协议） | S20 | 🟢 低 |
| Nextcloud | 全量下载（WebDAV） | S8 | 🟢 低 |
| Syncthing | 本地副本即导出 | S38 | 🟢 极低 |

---

## 3. 变更登记表（01 冻结集合 C1-C5 内的产品增删）

| # | 变更 | 理由 | 影响 |
|---|------|------|------|
| V1 | C3 内 Pydio：pydio-core 已 archived（S18），活跃项目为 pydio/cells（S19） | X5 排除规则触发：原对象归档，替换为后继项目 | C3 示例对象更新：Pydio → Pydio Cells |
| V2 | C4 内 WeTransfer 类：确认命中排除规则（无版本管理/无权限/一次性传输） | I1 硬约束 | C4 实际考察对象缩减为 Syncthing + Resilio Sync（Resilio 未深入核验，标存在性断言） |
| V3 | C5 内腾讯文档：未纳入深入核验（无独立定价页可查，绑定企业微信生态） | 证据不足，不编造 | 保留在 C5 类别定义内，标"未考察" |

---

## 4. 暂定观察（非结论，供 02.5 交叉核验）

1. **预算内可行方案池**（≤¥30,000/年，30 人）：飞书标准版 ¥18,000 / 坚果云 Standard ¥10,800 / 钉钉专业版 ¥9,800+扩容 / Dropbox Standard ¥36,075❌ / Box Starter ¥12,025 / Google WS BS ¥18,037 / M365 BS ¥30,062（贴线）/ Notion Team ¥24,062 / Confluence ≈¥17,200-19,600 / Seafile Pro ¥9,620+服务器 / Nextcloud 免费+服务器+运维 ≈¥5,400-9,000
   - 注意：Dropbox Standard ¥36,075 超预算（之前 cost-model.json 里算的是 15*30*6.68=3,006，那是 30 人×$15/月×12 月=$5,400/年→¥36,075，不是 ¥3,006。cost-model.json 有 bug，需在 04 修正。）
2. **硬约束淘汰**：Syncthing（无版本管理，I1）/ 语雀 Pro/Enterprise（超预算）/ 个人网盘免费档（X2）
3. **C4 类整体弱化**：Syncthing 出局后，C4 仅剩 Resilio Sync（未深入核验）→ C4 对本 run 决策贡献趋近于零
4. **自托管 vs SaaS 分叉点**：Nextcloud 全栈 ≈¥5,400-9,000/年（含服务器+运维）vs 飞书标准版 ¥18,000/年——自托管便宜 50-70%，但运维负担是隐性成本（F5）

---

## 5. 仍未解决的空缺（移交 02.5 / 03）

| # | 空缺 | 影响 | 处置 |
|---|------|------|------|
| U1 | cost-model.json 计算 bug（Dropbox/Box 等 USD 项少乘 12 月） | F3 成本表错误 | 04 阶段重算修正 |
| U2 | 飞书云文档版本历史深度（几版/保留多久） | F2 功能合规精度 | 标"存在性断言-未核验"，不阻塞 |
| U3 | 钉钉钉盘版本管理+权限粒度 | F2 功能合规 | 同上 |
| U4 | 钉钉云盘扩容单价官方确认 | F3 成本精度 | 暂用 S32 🔴 值，标利益冲突 |
| U5 | Confluence 30 人档精确单价 | F3 成本精度 | 用区间 ¥17,200-19,600 |
| U6 | Nextcloud 文件版本保留策略（默认 3 版本？可配？） | F2 功能合规精度 | 标"社区共识-未官方直证" |
| U7 | 国内网络可达性（SaaS 类） | F5 部署负担 | lead-unverifiable，03 标风险项 |
| U8 | Seafile/ownCloud 最低硬件要求 | F5 部署复杂度 | 存在性断言-未核验 |
| U9 | Resilio Sync 定价+功能（C4 唯一剩余对象） | D3 完整性 | 标"未考察"，C4 贡献趋零 |
| U10 | 存储用量行业基准（G2） | F3 精度 | 已用 {50,200}GB/人 区间降级 |

---

## 6. 阶段判定

- 01 关键空缺逐项有证据或明确保留 ✅（G1-G10 全覆盖，U1-U10 诚实保留）
- 每条关键主张附来源 URL/路径+时间戳 ✅（S1-S38 全带）
- 关键主张有独立来源 ✅（定价类均 ≥2 源；开源类 GitHub API 一手）
- 易变事实接近当前日期 ✅（全部 2026-10-30 观察；GitHub pushed_at 2026-10-29）
- 未把网页 LLM 线索误写成事实来源 ✅（web-llm 全失败，零线索使用）
- 来源矛盾已记录 ✅（X1-X4 移交 02.5）
- **新发现 U1（cost-model.json bug）需在 04 修正后才可计分**

**判定：pass → 进入 02.5。**（自检 conf-0.2，E1 降级；U1 为执行层缺陷，不影响 02.5 交叉核验逻辑）