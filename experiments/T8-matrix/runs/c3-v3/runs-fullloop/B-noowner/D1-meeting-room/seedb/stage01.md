# 阶段 01：目标分解、已知与空缺条件

## 1. 目标交付物定义
本任务的最终交付物是一份**可交付报告**，包含以下核心组件：
1. **推荐方案**：满足所有硬性条件且综合成本/体验最优的单一会议室预约系统。
2. **备选方案**：至少一个次优但可行的替代方案。
3. **淘汰理由清单**：对每个未入选的主要候选类别或具体产品，给出明确的淘汰理由（基于硬性条件违背或性价比劣势）。
4. **完整成本明细**：年度总成本 ≤ 2万元人民币的详细拆解（License费、服务器费、集成开发费等）。

**核心约束（Hard Constraints）：**
- 预算上限：20,000 RMB / 年。
- 平台支持：必须同时支持 macOS、Windows、Web 三端。
- 日历集成：必须双向同步 Google Calendar 和 Outlook (Exchange/Microsoft 365)。
- 团队规模：30人研发团队。
- 可选加分项：门禁联动（Access Control Integration）。

---

## 2. 影响因素递归分解

### 顶层因素正交分解
我们将“选型”这一目标分解为四个互相正交且覆盖完整的影响维度：
1. **功能兼容性 (Functional Compatibility)**：是否满足多端支持和双日历集成的硬性要求。
2. **经济可行性 (Economic Feasibility)**：年度总拥有成本 (TCO) 是否在 2万 RMB 以内。
3. **技术实施复杂度 (Implementation Complexity)**：部署难度、维护成本及与现有基础设施（如门禁、SSO）的对接难度。
4. **用户体验与扩展性 (UX & Scalability)**：针对30人团队的易用性、移动端体验及未来扩展能力（含门禁联动潜力）。

### 递归分解子因素

#### 因素 A：功能兼容性
*   **A1: 终端覆盖**
    *   A1.1: Web 端可用性（浏览器兼容性）。
    *   A1.2: macOS 客户端（原生 App 或 PWA 封装效果）。
    *   A1.3: Windows 客户端（原生 App 或 PWA 封装效果）。
    *   *判定标准*：若仅支持 Web 但无原生移动/桌面体验，需评估是否接受“Web as Desktop”模式；若必须原生 App，则排除纯 Web 方案。
*   **A2: 日历集成深度**
    *   A2.1: Google Calendar API 接入能力（OAuth2, Event CRUD）。
    *   A2.2: Microsoft 365/Outlook API 接入能力（Graph API, Exchange Online）。
    *   A2.3: 双向同步机制（冲突检测、状态更新回写）。
    *   *关键空缺*：大多数轻量级开源工具只支持单向订阅或仅支持其中一种日历。需验证是否有现成插件或中间件。

#### 因素 B：经济可行性
*   **B1: 软件授权成本 (License Cost)**
    *   B1.1: SaaS 订阅费（按用户/月或按会议室/月）。
    *   B1.2: 自托管开源软件的潜在隐性成本（技术支持、升级服务）。
*   **B2: 基础设施成本 (Infrastructure Cost)**
    *   B2.1: 云服务器费用（若自托管）。
    *   B2.2: 域名与 SSL 证书费用。
*   **B3: 集成开发成本 (Integration Dev Cost)**
    *   B3.1: 日历对接开发工时（若无现成集成）。
    *   B3.2: 门禁联动开发工时（若有此需求且无现成接口）。
    *   *注意*：对于30人团队，通常假设内部有少量开发人员可承担简单集成，否则需外包，成本将大幅上升。此处假设由内部研发人员利用业余时间完成基础集成，不计入直接现金支出，但计入时间成本（需在报告中说明）。

#### 因素 C：技术实施复杂度
*   **C1: 部署模式**
    *   C1.1: SaaS 托管（零运维，依赖厂商 SLA）。
    *   C1.2: 私有化部署（高运维，数据可控，需服务器）。
*   **C2: 身份认证 (Auth)**
    *   C2.1: 是否支持 OAuth2/OIDC？
    *   C2.2: 能否对接公司现有的 SSO（如 Azure AD, Okta, or GitLab SAML）？
*   **C3: 门禁联动潜力**
    *   C3.1: 是否提供 Webhook 或 REST API 用于触发外部硬件？
    *   C3.2: 主流门禁系统（如 HID, ZKTeco, 海康威视）是否有官方或社区适配案例？

#### 因素 D：用户体验与扩展性
*   **D1: 核心流程效率**
    *   D1.1: 预订界面直观性（拖拽式 vs 表单式）。
    *   D1.2: 等待列表 (Waitlist) 与自动释放 (Auto-release) 机制。
*   **D2: 通知机制**
    *   D2.1: 邮件通知。
    *   D2.2: IM 集成（Slack/Teams/钉钉/飞书）——虽非硬性，但对研发团队体验影响大。

---

## 3. 条件分类：已知、可推导、待研究

### 3.1 人类已提供的条件 (Provided Facts)
| ID | 条件描述 | 来源 |
|----|----------|------|
| P1 | 团队规模：30人 | 任务书 |
| P2 | 年度预算上限：20,000 RMB | 任务书 |
| P3 | 必须支持 macOS, Windows, Web | 任务书 |
| P4 | 必须对接 Google Calendar 和 Outlook | 任务书 |
| P5 | 门禁联动为可选加分项 | 任务书 |

### 3.2 从项目可推导的条件 (Derived Assumptions)
| ID | 推导内容 | 逻辑依据 | 风险等级 |
|----|----------|----------|----------|
| D1 | 用户数 ≈ 30 + 访客/管理层缓冲 = ~35-40 License | 30人研发可能有会议邀请外部人员或经理 | 中 |
| D2 | 数据敏感性中等，但不涉及核心代码资产 | 会议室预约数据敏感度低于代码库，SaaS 可接受 | 低 |
| D3 | “对接 Outlook” 指 Microsoft 365 Business/Enterprise 环境 | 现代企业极少使用本地 Exchange Server 独立部署 | 低 |
| D4 | 内部有研发资源可进行轻量级 API 调用配置 | 既然是“研发团队”，具备基本编程能力，无需购买昂贵的定制开发服务 | 中 |

### 3.3 仍需研究的条件 (Open Questions / Gaps)
这些是阶段 02 必须解决的核心空缺：

| Gap ID | 空缺描述 | 阻塞的判断 | 优先级 |
|--------|----------|------------|--------|
| G1 | **候选 SaaS 产品的具体定价模型**：<br>主要竞品（如 Calendly, Acuity, RoomGuru, BookRoom, 以及国内产品如“小鹅通”、“腾讯会议预约”等是否适用？）的年费是否超过 20,000 RMB？<br>*注：Calendly 主要是个人/面试用，不适合会议室物理空间管理。需寻找专门针对“Physical Space/Meeting Room”的工具。* | 决定哪些产品因超预算被直接淘汰。 | 高 |
| G2 | **双日历双向同步的现成支持情况**：<br>主流会议室系统（如 RoomGuru, OfficeTime, 或开源的 Jitsi Meet? No, that's video conf. Need room booking specific tools like **BookRoom**, **Roomster**, **Mister Rooms**, **Zoho Workplace**, **Microsoft Teams Room Booking**）是否原生支持同时写入 Google Cal 和 MS Graph？还是需要通过 Zapier/Make.com 中间层？中间层成本是多少？ | 决定是否需要额外支付 Zapier 费用或开发工作量，从而影响总成本和可行性。 | 高 |
| G3 | **三端支持的真实性**：<br>候选方案在 macOS/Windows 上是否有原生 App？还是仅靠 Web Browser？若仅 Web，PWA 安装体验如何？是否满足“支持”的严格定义？ | 决定某些纯 Web 方案是否合规。 | 高 |
| G4 | **门禁联动的 API 开放程度**：<br>候选系统是否暴露 Webhook 以便触发门禁？若无，是否有第三方桥接器？ | 决定加分项的实现难度和成本。 | 中 |
| G5 | **开源自托管方案的许可证与维护成本**：<br>例如 **Jitsi** (视频), **BigBlueButton** (视频), 专门的会议室开源项目如 **Meet.io**? (No). 需要查找专门的 Open Source Meeting Room Booking systems (e.g., **Odoo** module? **Nextcloud**?). 其 Docker 部署的服务器成本估算。 | 决定自托管路线的 TCO。 | 中 |
| G6 | **国内网络访问稳定性**：<br>若选择海外 SaaS（如 RoomGuru），在中国大陆办公室的网络环境下，Web/App 加载速度是否可接受？是否需要代理？这会影响“Web 端支持”的实际可用性。 | 决定海外 SaaS 的可用性评分。 | 高 |

---

## 4. 候选对象类别冻结 (Candidate Set Freeze)

基于上述分解，我们冻结以下候选类别供阶段 02 研究。**不得在此后随意增删类别，除非在阶段 02 发现某类完全不存在或严重违反 P1-P5 约束。**

### 类别 1：专业会议室预约 SaaS (Niche SaaS)
*   **代表候选 (待验证)**：
    *   RoomGuru (roomguru.com)
    *   Mister Rooms (misterrooms.com)
    *   BookRoom (bookroom.co) - *Note: Check if still active/pricing*
    *   OfficeTime (officetime.io)
    *   Vibe (vibe.meeting)
    *   **国内候选**：
        *   腾讯会议 (Tencent Meeting) 的会议室预约模块 (通常绑定视频会议，但可能满足部分需求)
        *   钉钉/飞书 自带的会议室预约功能 (需确认是否支持外部日历双向同步)
*   **待验证属性**：价格/30人、双日历同步能力、三端支持、API/Webhook。

### 类别 2：通用生产力套件内置功能 (Productivity Suite Add-ons)
*   **代表候选 (待验证)**：
    *   Microsoft 365 / Teams 会议室预约 (如果公司已订阅 M365，边际成本为 0 或极低)。
    *   Google Workspace (Google Meet/Clock) 会议室资源管理 (如果公司已订阅 GWS，边际成本为 0)。
    *   Zoho Workplace (Workspace + Meetings + Rooms).
*   **待验证属性**：是否允许混合使用（即既连 Google 又连 Outlook）？通常这类套件是封闭生态，**大概率无法同时双向同步两个不同生态的日历**。这是一个关键的潜在淘汰点。

### 类别 3：开源自托管解决方案 (Self-Hosted OSS)
*   **代表候选 (待验证)**：
    *   **Odoo** (Community Edition + Meeting Module): 强大但重，学习曲线陡峭。
    *   **Nextcloud** (with meeting apps): 更多是文件/通讯，会议室预约非核心。
    *   **专用 OSS**: 搜索 "open source meeting room booking system github"。
        *   候选: `meetings-room-booking` (generic repos), `calcom` (mostly for scheduling people, not rooms?), `frappe` based apps.
        *   *特定关注*: **Jitsi Meet** 是视频，不是房间。需区分 Video Conferencing 和 Physical Room Booking。
        *   *潜在候选*: **LibreOffice**? No.
        *   *真实候选*: **Radicale**? No, that's calendar server.
        *   *Real Candidate*: **Cal.com** (Open source Calendly alternative) -> Does it support physical rooms? Likely no.
        *   *Real Candidate*: **Frappe Books**? No.
        *   *Search Term for Phase 02*: "self hosted physical meeting room booking software".
*   **待验证属性**：是否存在成熟的、可维护的、专门针对物理会议室的 OSS 项目？部署复杂度？

### 类别 4：低代码/自动化平台组合 (Low-Code + Automation)
*   **代表候选 (待验证)**：
    *   Airtable/Notion (作为数据库) + Zapier/Make.com (处理日历逻辑) + PWA Wrapper.
    *   **问题**：这种 DIY 方案很难做到真正的“双向实时同步”且 UI 体验差，难以称为一个完整的“系统”，但在预算极度受限时可能是唯一解。
*   **待验证属性**：Zapier 处理 30 人高频操作的成本和延迟。

### 排除的类别 (Pre-excluded in Phase 01)
*   **视频 conferencing platforms only** (Zoom, Webex, Tencent Meeting standalone): 它们主要解决“连接”问题，而非“物理空间资源分配”问题。虽然有些带房间锁功能，但通常不与 Google/Outlook 日历做深度的双向资源占用同步（即你在 Zoom 里占了房间，Outlook 里不会显示该房间忙碌，除非手动）。因此，纯视频平台不作为首选候选，除非其“Room Scheduling”模块被证实独立且强大。

---

## 5. 阶段 02 研究路径与行动入口

为了填补 G1-G6 的空缺，阶段 02 应执行以下具体动作：

### 5.1 针对 G1 (价格) 和 G3 (三端) 的研究
*   **目标网站**：各候选 SaaS 官网的 Pricing 页面。
*   **搜索词**：
    *   `"RoomGuru pricing 30 users"`
    *   `"Mister Rooms cost per user"`
    *   `"BookRoom subscription price"`
    *   `"Tencent Meeting room booking enterprise price"`
*   **字段提取**：
    *   单用户月费/年费。
    *   最低起购人数。
    *   是否包含移动端 App (iOS/Android/macOS/Windows) 或仅 Web。
*   **备用路径**：若官网隐藏价格，尝试发送销售询盘邮件模板，或通过 G2/Capterra 查看第三方报价评论。

### 5.2 针对 G2 (双日历同步) 的研究
*   **目标网站**：各候选 SaaS 的 Help Center / FAQ / API Documentation。
*   **搜索词**：
    *   `"RoomGuru Google Calendar integration"`
    *   `"Mister Rooms Outlook sync"`
    *   `"Meeting room booking software bidirectional calendar sync Google and Microsoft"`
*   **关键验证点**：
    *   文档中是否明确提到 "Two-way sync" (双向同步) 还是 "One-way publish" (单向发布)？
    *   是否支持同时连接两个不同的日历提供商？（很多工具只允许选择一个主日历源）。
    *   若不支持原生，检查其是否支持 ICS 订阅（单向）或提供 Webhook/API 供自行开发双向同步。

### 5.3 针对 G6 (国内网络) 的研究
*   **方法**：
    *   在办公网络环境下，尝试访问候选 SaaS 的 Web 登录页，记录加载时间。
    *   搜索用户社区（Reddit, V2EX, 知乎）关于该工具在国内访问速度的讨论。
    *   关键词：`"RoomGuru 国内访问速度"`, `"Mister Rooms 翻墙"`。

### 5.4 针对 G5 (开源方案) 的研究
*   **目标网站**：GitHub, SourceForge, Docker Hub.
*   **搜索词**：
    *   `github "meeting room booking" stars:>100`
    *   `docker hub "meeting room scheduler"`
*   **筛选标准**：
    *   Last commit date < 1 year (Active maintenance).
    *   Has a clear README with deployment instructions.
    *   Check issues section for "calendar sync" bugs.

### 5.5 针对 G4 (门禁联动) 的研究
*   **目标网站**：候选 SaaS 的 API Docs 或 Integrations 页面。
*   **搜索词**：
    *   `"RoomGuru webhook access control"`
    *   `"Meeting room system integrate smart lock API"`
*   **验证**：是否存在 "When room is booked -> Trigger HTTP Request" 的功能。

---

## 6. 总结与下一步

**阶段 01 结论**：
目前没有任何一个候选方案可以立即确认为“完美匹配”。最大的不确定性在于**“同时双向同步 Google 和 Outlook”**这一硬性条件。大多数商业 SaaS 倾向于锁定在一个生态内（要么 Google 系，要么 Microsoft 系）。因此，阶段 02 的首要任务是**证伪或证实**是否存在能跨生态双向同步的成熟产品。如果不存在，则可能需要考虑：
1.  使用支持 ICS 导入导出的工具，并通过脚本/中间件实现准双向同步（增加开发成本）。
2.  放弃其中一个日历的“双向”要求，改为“单向镜像”（需与业务方确认是否可接受，但任务书说是“必须对接”，通常暗示双向，若只能单向需标注为风险）。
3.  转向自托管开源方案，通过代码实现自定义的双日历适配器。

**给 Reviewer 的提示**：
本阶段已完成因素分解，明确了 6 个关键空缺 (G1-G6)，并提供了具体的搜索词和验证路径。候选集已冻结为 4 大类。阶段 02 可直接依据 §5 开始执行资料搜集。未验证的价格和兼容性均标记为