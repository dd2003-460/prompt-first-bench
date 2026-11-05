# 阶段 01：目标分解、已知与空缺条件

## 1. 目标定义
**交付物**：一份可执行的会议室预约系统选型报告。
**核心约束**：
- 团队规模：30人研发团队。
- 预算上限：≤ 2万元/年（约 $2,800 USD）。
- 平台支持：macOS, Windows, Web。
- 日历集成：Google Calendar (GCal) + Microsoft Outlook (MSO)。
- 可选功能：门禁联动（Access Control Integration）。
- 产出内容：推荐方案、备选方案、淘汰理由、详细成本明细。

## 2. 因素分解树 (Recursive Decomposition)

### 顶层因素 (Level 1)
1. **功能兼容性 (Functional Compatibility)**
2. **成本结构 (Cost Structure)**
3. **技术架构与部署 (Technical Architecture & Deployment)**
4. **用户体验与协作效率 (UX & Collaboration Efficiency)**
5. **扩展性与安全合规 (Scalability & Security/Compliance)**

---

### Level 2: 递归分解

#### 1. 功能兼容性
*   **1.1 客户端支持 (Client Support)**
    *   *1.1.1 原生应用 vs Web App*: 是否提供独立的 macOS/Windows 客户端，还是仅依赖浏览器？（影响离线能力、通知体验）
    *   *1.1.2 移动端支持*: 虽非硬性要求，但研发人员常需移动查看日程。（待研究：是否包含 iOS/Android 或 PWA）
*   **1.2 日历集成深度 (Calendar Integration Depth)**
    *   *1.2.1 双向同步*: 仅在系统中预约后，是否自动写入 GCal/Outlook？反之亦然？
    *   *1.2.2 冲突检测机制*: 当用户在 GCal 直接预订房间时，系统如何感知并更新状态？
    *   *1.2.3 多日历源支持*: 是否允许用户绑定多个日历（如个人工作日历+项目日历）？
*   **1.3 门禁联动 (Access Control Linkage - Optional)**
    *   *1.3.1 硬件兼容性*: 需要对接哪些主流门禁品牌（如 HID, ZKTeco, 海康威视等）？
    *   *1.3.2 接口标准*: 是否提供 API/Webhook 供第三方门禁系统调用？
    *   *1.3.3 授权逻辑*: 预约成功后，权限是实时下发还是有延迟？

#### 2. 成本结构
*   **2.1 许可费用 (Licensing Fees)**
    *   *2.1.1 计费模式*: 按席位 (Per Seat)、按房间 (Per Room)、还是整体打包 (Flat Rate)？
    *   *2.1.2 免费额度*: 是否有针对小团队的免费版？30人是否超出免费额度？
    *   *2.1.3 年度总价*: 必须 ≤ 20,000 CNY / 年。
*   **2.2 实施与维护成本 (Implementation & Maintenance)**
    *   *2.2.1 部署人力*: 是否需要 IT 团队投入时间进行配置？（隐性成本）
    *   *2.2.2 技术支持*: 包含在订阅中吗？额外付费吗？

#### 3. 技术架构与部署
*   **3.1 部署模式 (Deployment Model)**
    *   *3.1.1 SaaS (公有云)*: 数据存储在厂商云端。
    *   *3.1.2 On-Premise (本地部署)*: 数据存储在内部服务器。
    *   *3.1.3 Hybrid*: 混合模式。
    *   *决策点*: 研发代码敏感，是否强制要求 On-Premise？（若强制，SaaS 候选将被大幅削减）
*   **3.2 数据隐私与安全 (Data Privacy & Security)**
    *   *3.2.1 数据存储位置*: 中国大陆？美国？欧盟？（影响访问速度和合规性）
    *   *3.2.2 认证方式*: 是否支持 SSO (SAML/OIDC)？
    *   *3.2.3 审计日志*: 谁在何时预约了哪个房间？

#### 4. 用户体验与协作效率
*   **4.1 界面直观性 (UI/UX)**
    *   *4.1.1 查找房间*: 能否按设备需求（大屏、白板、视频摄像头）筛选？
    *   *4.1.2 操作路径*: 从打开应用到完成预约最少几步？
*   **4.2 资源管理 (Resource Management)**
    *   *4.2.1 动态释放*: 如果人没来，系统是否自动释放房间？（No-show policy）
    *   *4.2.2 共享给他人*: 能否将会议链接/邀请直接发送给参会者？

#### 5. 扩展性与安全合规
*   **5.1 厂商稳定性 (Vendor Viability)**
    *   *5.1.1 市场地位*: 初创公司还是成熟大厂？
    *   *5.1.2 更新频率*: 最近6个月是否有显著版本更新？
*   **5.2 合规性 (Compliance)**
    *   *5.2.1 中国法规*: 是否符合《数据安全法》和《个人信息保护法》？（若部署在中国境内，此为关键否决项）

---

## 3. 条件分类清单

### A. 人类已提供的确定条件 (Given Facts)
1.  团队人数：30人。
2.  预算上限：20,000 CNY / 年。
3.  必选平台：macOS, Windows, Web。
4.  必选集成：Google Calendar, Outlook。
5.  可选功能：门禁联动。
6.  行业背景：研发团队（暗示对技术稳定性、API开放性有一定要求，但不一定需要极致的本地化私有化部署，取决于具体敏感度，见空缺）。

### B. 从项目可推导的条件 (Derived Conditions)
1.  **人均预算**：20,000 / 30 ≈ 666 CNY / 人 / 年。这意味着无法选择高端企业级定制软件（通常 >$10/user/month），必须聚焦于 SMB (中小企业) 或标准化 SaaS 产品。
2.  **日历集成的必要性**：由于必须支持 GCal 和 MSO，纯自研脚本或极简开源方案可能难以满足“开箱即用”的双向同步需求，倾向于选择有成熟 Calendar API 封装的商业产品。
3.  **Web 端优先性**：既然要求 Web 支持，且研发人员常在多设备切换，Web 端的易用性是核心评估维度，原生 App 可能是加分项而非必须（除非有离线需求）。

### C. 仍需研究的空缺条件 (Open Questions / Gaps)
*(注：以下均为待验证假设或未知项，严禁在阶段 01 中当作事实)*

| ID | 空缺条件描述 | 阻塞的后续判断 | 优先级 |
|----|-------------|---------------|--------|
| **G1** | **数据驻留与合规要求**：团队是否位于中国境内？是否受严格的数据出境限制？是否强制要求数据存储在境内？ | 决定 SaaS (海外节点) 是否被一票否决。若强制境内存储，候选池缩小至国内厂商或特定国际厂商的中国区服务。 | **High** |
| **G2** | **SSO/AD 集成需求**：公司现有身份认证体系是什么？(Azure AD, Okta, 自建 LDAP?) | 影响部署复杂度和安全性评分。若无 SSO 支持，可能增加密码管理负担。 | Medium |
| **G3** | **门禁系统的具体型号/协议**：现有门禁品牌及是否开放 API？ | 决定“门禁联动”是标配功能还是需要额外开发中间件。若无 API，此功能可能不可行或成本超支。 | Low (Optional) |
| **G4** | **各主流候选产品的最新定价策略**：例如 Zoom Rooms, Microsoft Teams Rooms, Slack Connect, 以及国内竞品（如钉钉/飞书/企业微信自带的会议室模块，或独立工具如 BookRoom, Roomy 等）的具体价格表。 | 直接决定预算可行性。2万元/年的限制非常具体，需精确到每个候选方案的报价。 | **High** |
| **G5** | **Google Calendar & Outlook 双向同步的实际稳定性**：不同产品在处理日历冲突时的延迟和准确性评测。 | 影响用户体验评分。某些产品可能只支持单向推送。 | Medium |
| **G6** | **开源替代方案的维护活跃度**：如 `roomly`, `booking-system` 等 GitHub 项目的 Star 数、最后提交时间、Issue 响应速度。 | 若商业方案均超预算或不合规，需评估自建/开源自托管的成本（主要是运维人力）。 | Medium |
| **G7** | **Web 端在 macOS/Windows 上的性能表现**：是否存在兼容性问题？ | 影响技术架构评分。 | Low |

---

## 4. 阶段 02 研究入口与行动指南

基于上述分解，阶段 02 应执行以下具体研究动作：

### 4.1 候选对象初筛 (Hypothesis Candidates)
*注意：以下仅为搜索关键词方向，属性均未验证。*

1.  **国际主流 SaaS (Global SaaS)**
    *   *候选类别*: Zoom Rooms, Microsoft Teams (自带会议室调度), Slack (Connect/Integrations), Calendly (Team Plan), Acuity Scheduling.
    *   *研究重点*: 是否提供 30 席位的套餐？是否包含双日历同步？价格是否在 2万 CNY 内？数据服务器位置？
2.  **垂直领域会议室预约工具 (Vertical Tools)**
    *   *候选类别*: Roomy, BookRoom, Envoy (Workspace), Nexudus, Spacewell.
    *   *研究重点*: 专注度、UI 简洁性、API 开放性（用于门禁）、定价模型。
3.  **国内协同办公套件内置功能 (Domestic Suites)**
    *   *候选类别*: 钉钉 (DingTalk) 会议室, 飞书 (Feishu/Lark) 会议室, 企业微信 (WeCom).
    *   *研究重点*: 这些通常是免费或包含在企业版订阅中。需确认其日历同步能力（是否完美支持 GCal? 这点存疑，通常主要支持本土生态）和门禁对接能力。
4.  **开源/自托管方案 (Open Source/Self-hosted)**
    *   *候选类别*: `openmeetings`, `nextcloud rooms` (if applicable), 自定义 Next.js/React + Node.js 后端.
    *   *研究重点*: 部署难度、日历同步插件的成熟度、社区支持。*风险：隐性人力成本可能远超 2万预算。*

### 4.2 具体搜索词与来源类型

*   **搜索词示例**:
    *   `"meeting room booking software" "google calendar" "outlook" integration price per user`
    *   `"会议室预约系统" "钉钉" OR "飞书" "谷歌日历" 同步`
    *   `"Zoom Rooms" pricing 30 users annual cost`
    *   `"Roomy" pricing plan small business`
    *   `github "meeting room booking" open source star count`
*   **目标来源**:
    1.  官方定价页面 (Pricing Pages) - *一手证据，最准确的价格*.
    2.  官方博客/Release Notes - *确认新功能（如门禁 API）的支持情况*.
    3.  G2/Capterra/Trustpilot 评测 - *了解实际用户痛点（如同步延迟、客服响应）*.
    4.  厂商文档 (Documentation) - *确认技术细节（SSO, API endpoints）*.

### 4.3 失败备用路径
*   若所有国际 SaaS 因数据合规问题（G1）被排除：转向国内协同套件（钉钉/飞书）深入调研其开放平台能力。
*   若所有商业方案均超预算：转向开源方案，但需引入“IT 运维人力成本估算”作为对比基准，明确告知用户隐性成本。
*   若“门禁联动”在所有低价方案中均不支持：在报告中明确标记该功能为“不可行”或“需额外定制开发”，并给出预估开发成本范围（即使不实施，也要说明为何不选）。

## 5. 判定结论

本阶段已完成目标分解，明确了已知条件、推导条件和关键空缺。
*   **关键空缺**：G1 (数据合规/地域), G4 (具体价格), G3 (门禁接口现状)。
*   **阻塞影响**：G1 决定候选池范围；G4 决定最终选型。
*   **下一步**：阶段 02 可直接依据 4.2 中的搜索词和来源开始搜集证据。无需进一步细化阶段 01。

**Reviewer 建议判定**: `pass`
**Repair Stage**: N/A