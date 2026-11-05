# 阶段 01：目标分解、已知与空缺条件

## 1. 目标交付物定义
**最终交付物**：一份可执行的会议室预约系统选型报告。
**核心内容**：
1. **推荐方案**：满足所有硬性条件的最佳单一方案（或组合）。
2. **备选方案**：次优但可行的方案。
3. **淘汰方案及理由**：列出被排除的候选类别/具体产品，并给出基于硬性条件的淘汰逻辑。
4. **完整成本明细**：年度总成本 ≤ 20,000 CNY 的详细预算表。

## 2. 影响因素正交分解 (Top-Level Factors)

为了覆盖“选型”这一目标，我们将影响决策的因素分解为以下四个正交维度：

### A. 功能兼容性 (Functional Compatibility)
*   **A1. 多端支持**: 必须同时支持 macOS, Windows, Web。
    *   *子因素*: 客户端安装方式（原生 App vs Electron/PWA）、Web 端功能完整性（是否仅查看还是全功能）。
*   **A2. 日历集成**: 必须对接 Google Calendar (GCal) 和 Outlook (O365)。
    *   *子因素*: 双向同步能力、冲突检测机制、OAuth 授权流程稳定性。
*   **A3. 门禁联动 (可选)**: 有则加分。
    *   *子因素*: 支持的硬件协议（TCP/IP, HTTP API, MQTT）、主流门禁品牌兼容性（海康、大华等）。

### B. 部署与维护架构 (Deployment & Maintenance)
*   **B1. 部署模式**: SaaS (云端) vs Self-Hosted (自托管)。
    *   *推导*: 鉴于团队规模(30人)和预算(2万/年)，SaaS 通常更经济且免维护；Self-Hosted 需服务器成本和运维人力，除非数据合规强制要求。
*   **B2. 数据主权与安全**: 会议数据存储在何处？是否符合公司隐私政策？
    *   *空缺*: 公司是否有明确的数据出境禁令或本地化存储要求？（若无明确说明，默认接受公有云 SaaS，但需标记为待确认风险）。

### C. 成本结构 (Cost Structure)
*   **C1. 软件许可费 (License Fee)**: 按人头计费还是按会议室计费？免费额度是多少？
    *   *约束*: 年度总额 ≤ 20,000 CNY。
*   **C2. 基础设施成本 (Infra Cost)**: 若 Self-Hosted，服务器、数据库、备份费用。
*   **C3. 实施与集成成本 (Integration Cost)**: 是否需要开发人员进行二次开发以连接门禁或定制日历字段？
    *   *注意*: 此部分常被忽略，需纳入总预算考量。

### D. 用户体验与管理效率 (UX & Management)
*   **D1. 易用性**: 员工预约流程步骤数、界面直观性。
*   **D2. 管理后台**: IT 管理员配置会议室设备、权限、统计报表的能力。

---

## 3. 条件分类：已知、可推导、待研究

### 3.1 人类已提供的条件 (Given Facts)
| ID | 条件描述 | 来源 |
|----|----------|------|
| G1 | 团队规模：30 人研发团队 | 任务书 |
| G2 | 年度预算上限：20,000 CNY | 任务书 |
| G3 | 平台要求：macOS + Windows + Web 三端支持 | 任务书 |
| G4 | 日历要求：必须对接 Google Calendar 和 Outlook | 任务书 |
| G5 | 门禁联动：可选项，有则加分 | 任务书 |

### 3.2 从项目可推导的条件 (Derived Facts)
| ID | 推导结论 | 推导逻辑 |
|----|----------|----------|
| D1 | **首选 SaaS 模式** | 30人规模较小，自建服务器+运维人力成本极高（即使云服务器便宜，DevOps 时间成本高），且 SaaS 厂商通常已做好 GCal/Outlook 插件。预算 2 万/年 ≈ 666 元/月，足以覆盖大多数中小企业 SaaS 订阅。 |
| D2 | **需关注“免费层”限制** | 许多工具提供基础免费层，但可能限制会议室数量或高级功能。需验证 30 人团队是否超出免费额度。 |
| D3 | **“Web 端”通常指浏览器访问** | 现代 SaaS 均提供 Web Portal。关键点是 Web 端是否与桌面端功能对等，特别是预约和取消操作。 |

### 3.3 仍需研究的条件 (Open Questions / Gaps) -> **写入空缺清单**
*(注：以下内容在阶段 01 仅为假设或搜索方向，**非事实**)*

#### Gap List (待研究空缺)

| ID | 空缺描述 | 阻塞的判断 | 优先级 | 阶段 02 研究路径建议 |
|----|----------|------------|--------|----------------------|
| **GAP-01** | **主流候选 SaaS 的具体定价模型**<br>候选类别：<br>1. 专业会议室预订系统 (e.g., Roomle, BookRoom, Calendly Rooms)<br>2. 通用协作套件自带功能 (e.g., Microsoft Teams Rooms, Slack Connect, Zoom Workplace)<br>3. 开源/低代码自托管方案 (e.g., Nextcloud, Mattermost + Plugin, 或轻量级 Node.js/Python 自建)<br>**状态**: 未验证价格、席位限制、功能阉割情况。 | 决定哪个方案符合 ≤20k CNY 预算。 | High | 搜索词: "meeting room booking software pricing 30 users", "Google Calendar room booking app cost", "Microsoft Teams meeting room license cost". 来源: 官网 Pricing Page, G2/Capterra 评测。 |
| **GAP-02** | **GCal & Outlook 双日历集成的深度**<br>具体验证：<br>1. 是否支持**双向**实时同步？<br>2. 当两个日历源冲突时，系统如何处理？<br>3. 是否需要在每个用户端单独授权，还是集中式服务账号授权？<br>**状态**: 各候选方案对两套日历的支持程度差异巨大。 | 决定是否满足硬性条件 A2。 | High | 搜索词: "[Candidate Name] Google Calendar integration bidirectional", "[Candidate Name] Outlook O365 connector". 来源: 官方文档 (Docs), 独立技术博客评测。 |
| **GAP-03** | **门禁联动的可行性与成本**<br>具体验证：<br>1. 候选方案是否提供 Webhook/API 触发门禁开门？<br>2. 是否支持与国内主流门禁（海康威视/大华）的直接对接，还是需要中间件？<br>3. 中间件开发/采购额外成本是多少？<br>**状态**: 多数纯软件 SaaS 不直接控门禁，需 IoT 网关。 | 决定“加分项”能否实现及额外预算占比。 | Medium | 搜索词: "meeting room booking system access control integration API", "Hikvision API third party booking". 来源: 厂商 API Docs, GitHub 开源集成案例。 |
| **GAP-04** | **Web 端功能完整性**<br>具体验证：Web 端是否允许创建会议、邀请参会者、选择房间？还是仅用于查看日程？<br>**状态**: 部分移动端优先的工具 Web 端功能受限。 | 决定是否满足硬性条件 A1。 | High | 搜索词: "[Candidate Name] web portal features", "[Candidate Name] browser compatibility". 来源: 官方 Feature Matrix, 用户评论中的负面反馈。 |
| **GAP-05** | **隐性成本：实施与培训**<br>具体验证：首次部署、用户培训、IT 管理员配置所需工时估算。<br>**状态**: 虽无直接现金支出，但占用研发资源，间接影响 ROI。 | 辅助排序备选方案。 | Low | 经验法则估算：SaaS 通常为 0.5-1 人天；自建为 5-10 人天。无需外部搜索，作为内部评估参数。 |
| **GAP-06** | **数据合规性**<br>具体验证：数据存储地（中国大陆/海外）？是否满足《数据安全法》？<br>**状态**: 若团队处理敏感代码/数据，海外 SaaS 可能存在合规风险。 | 可能直接否决某些海外 SaaS。 | Medium | 搜索词: "[Candidate Name] data residency China", "[Candidate Name] GDPR CCPA compliance". 来源: 官网 Security/Privacy 页面。 |

---

## 4. 候选对象冻结集合 (Frozen Candidate Set for Stage 02)

为防止阶段 02 漂移，现冻结以下**候选类别**及初步**具体候选对象**（标注为*待验证假设*）：

### 类别 1: 垂直领域会议室预订 SaaS (Vertical SaaS)
*   **特点**: 专注房间预订，UI 简洁，通常有 API。
*   **候选对象 (待验证)**:
    1.  **Roomle** (假设: 支持多日历，需查价格)
    2.  **BookRoom** (假设: 欧美常用，需查中国可用性)
    3.  **ClickUp / Notion** (假设: 通过模板实现，非原生功能，需评估复杂度)
    4.  **国内垂直工具** (如: 钉钉/飞书自带的会议室模块 - *注意: 需验证是否支持非钉钉/飞书用户的 GCal/Outlook 接入*)

### 类别 2: 大型协作平台内置功能 (Suite-Native)
*   **特点**: 与现有 IM/邮件深度绑定，无需额外登录。
*   **候选对象 (待验证)**:
    1.  **Microsoft Teams** (假设: 若公司已用 M365，可能已含 License；需验证 Web 端体验及 GCal 互通性)
    2.  **Zoom Workplace** (假设: 需验证其“Rooms”功能的独立性及日历同步细节)
    3.  **Slack** (假设: 依赖第三方 App 如 “Meeting Scheduler”，需查集成稳定性)

### 类别 3: 自托管/开源轻量级方案 (Self-Hosted/Open Source)
*   **特点**: 数据私有，初始成本低，但运维成本高。
*   **候选对象 (待验证)**:
    1.  **Nextcloud** (假设: 通过插件实现房间预订，需查插件成熟度)
    2.  **Mattermost** (假设: 类似 Slack，需查 Room Booking Plugin)
    3.  **GitHub 上的轻量级 Booking App** (假设: 如 `room-reservation` 类仓库，需评估安全性与可维护性)

### 排除逻辑预置 (Pre-defined Exclusion Logic)
*   **排除标准 E1**: 不支持 Web 端全功能操作。
*   **排除标准 E2**: 无法同时连接 GCal 和 Outlook（单向同步或不支持其一）。
*   **排除标准 E3**: 30 用户年度成本 > 20,000 CNY（含必要基础设施）。
*   **排除标准 E4**: 仅支持 iOS/Android 移动端，无桌面/Web 支持。

---

## 5. 阶段 02 启动门槛检查

1.  **目标清晰**: 是，产出选型报告。
2.  **因素覆盖**: 是，功能、部署、成本、UX 四维度覆盖。
3.  **已知/未知区分**: 是，Gap List 明确列出了 6 个关键未知项。
4.  **研究路径具体**: 是，每个 Gap 都提供了搜索词和来源类型。
5.  **候选集冻结**: 是，三类候选及具体对象已列出，并标记为待验证。
6.  **无伪装事实**: 是，所有价格、兼容性均未写成确定事实，而是“假设”或“待验证”。

**判定**: 阶段 01 完成，允许进入阶段 02。

---

## 6. 阶段 02 第一批行动指令 (Action Items for Stage 02)

请执行以下步骤，重点填补 GAP-01 至 GAP-04：

1.  **执行 Web LLM 交叉询问**:
    *   命令: `ralph prompt-first web-llm . "对比 Roomle, BookRoom, Microsoft Teams Rooms, Nextcloud 插件在 30 人团队下的年度成本、Google/Outlook 双向同步支持情况及 Web 端功能完整性" --context "阶段 02；只要求可复核来源线索"`
    *   目的: 快速筛选出 2-3 个最有可能符合硬性条件的候选，缩小后续详细调研范围。

2.  **针对 Top 3 候选进行深度资料搜集**:
    *   **Price Verification (GAP-01)**: 访问官网 Pricing Page，记录 30 seats 的精确报价。注意货币单位（USD/EUR/CNY）及汇率换算。
    *   **Integration Check (GAP-02)**: 查阅官方 Docs，确认是否存在 "Calendar Sync" 章节，特别注明是否支持 "Two-way sync" 和 "Conflict resolution"。
    *   **Platform Support (GAP-04)**: 确认 Web URL 可公开访问，测试（或通过截图/视频）确认 Web 端可执行“新建预约”操作。
    *   **Access Control (GAP-03)**: 搜索 "API Documentation" 或 "Integrations" 页面，查找是否有 "Webhooks" 或 "Hardware Integration" 说明。若无，标记为“需自行开发中间件”，估算开发工时成本。

3.  **记录失败与矛盾**:
    *   若某候选官网无法访问或定价模糊，记录为“信息缺失”，不要猜测价格。
    *   若网页 LLM 给出的信息与官网不符，以官网为准，并记录差异。

4.  **输出**:
    *   更新后的证据表格（包含 URL、时间戳、观察结果）。
    *   临时淘汰列表（基于已获取的证据，哪些候选已违反 E1-E4）。
    *   剩余未解决的关键问题（若有）。