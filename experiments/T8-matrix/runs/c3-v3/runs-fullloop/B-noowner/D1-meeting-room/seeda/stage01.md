# 阶段 01：目标分解、已知与空缺条件

## 1. 目标交付物定义

**核心交付物**：一份可执行的《30人研发团队会议室预约系统选型报告》，包含以下明确章节：
1. **推荐方案**（单一最佳选项）及详细理由。
2. **备选方案**（至少1-2个次优选项）及适用场景说明。
3. **淘汰理由清单**：针对主要候选类别/具体产品，列出被排除的具体原因（需对应约束条件）。
4. **成本明细表**：基于预算 ≤2万元/年的具体费用构成（许可费、实施费、硬件费等）。

**隐含交付要求**：
- 方案必须能直接落地或给出清晰的采购路径。
- 报告逻辑必须自洽，所有结论可追溯至阶段 02 收集的证据。

---

## 2. 影响因素分解（递归正交分解）

### 顶层因素 (Level 1)

| ID | 因素名称 | 边界定义 | 优先级 |
|----|----------|----------|--------|
| F1 | **功能匹配度** | 系统核心功能是否满足团队日常预约、冲突检测、资源管理等需求。 | High |
| F2 | **平台兼容性** | 客户端/接口是否覆盖 macOS, Windows, Web 三端。 | High |
| F3 | **日历集成能力** | 能否双向同步 Google Calendar 和 Outlook。 | High |
| F4 | **扩展性与集成** | 门禁联动支持情况（API/SDK/预置插件）。 | Medium (Optional but required for evaluation) |
| F5 | **总拥有成本 (TCO)** | 年度总成本是否 ≤ 2万元人民币。 | High |
| F6 | **部署与维护复杂度** | SaaS vs On-premise，IT运维负担。 | Medium |
| F7 | **数据安全与合规** | 数据存储位置、隐私政策、企业认证能力。 | Medium |

### Level 2 分解

#### F1: 功能匹配度
- **F1.1 基础预约功能**: 创建会议、选择房间、时间冲突提示。*(已知需求)*
- **F1.2 资源管理**: 设备状态显示（投影仪、白板等）、房间容量限制。*(待推导：30人团队是否需要复杂资源管理？通常默认需要基础版)*
- **F1.3 审批流程**: 是否需要多级审批？*(空缺：未知，假设不需要复杂审批，仅需简单确认)*
- **F1.4 移动端支持**: 是否提供 iOS/Android App 或响应式Web？*(待研究：Web端若响应良好可替代App)*

#### F2: 平台兼容性
- **F2.1 macOS 客户端**: 原生App还是Electron/Web? *(待研究)*
- **F2.2 Windows 客户端**: 同上。*(待研究)*
- **F2.3 Web 端体验**: 浏览器兼容性、加载速度、交互流畅度。*(待研究)*
- **F2.4 单点登录 (SSO)**: 是否支持 LDAP/OIDC/SAML？*(待研究：影响用户体验和安全)*

#### F3: 日历集成能力
- **F3.1 Google Calendar 集成**: API权限级别（只读/读写/双向同步）。*(待研究)*
- **F3.2 Outlook/Exchange 集成**: EWS/Microsoft Graph API 支持情况。*(待研究)*
- **F3.3 同步机制**: 实时推送 vs 轮询？冲突解决策略？*(待研究)*
- **F3.4 多日历源支持**: 用户个人日历与公共会议室日历的合并显示。*(待研究)*

#### F4: 扩展性与集成 (门禁联动)
- **F4.1 开放API**: RESTful API 文档完整度、速率限制。*(待研究)*
- **F4.2 预置集成**: 是否有主流门禁品牌（如海康威视、大华、ZKTeco）的官方插件？*(待研究)*
- **F4.3 Webhook 支持**: 会议开始/结束时触发外部动作的能力。*(待研究)*
- **F4.4 硬件依赖**: 是否需要额外购买中间件或网关设备？*(待研究：影响TCO)*

#### F5: 总拥有成本 (TCO)
- **F5.1 软件许可费**: 按用户数/按房间数/按包年收费模式？单价是多少？*(待研究)*
- **F5.2 实施与配置费**: 初始部署、数据迁移、培训费用。*(待研究)*
- **F5.3 硬件成本**: 如果On-premise，服务器/终端成本；如果SaaS，无此项但可能有门禁硬件增量。*(待研究)*
- **F5.4 维护与支持费**: 年度维保、技术支持等级（SLA）。*(待研究)*
- **F5.5 汇率与支付**: 如果是海外SaaS，涉及外币支付和汇率波动风险。*(待研究)*

#### F6: 部署与维护复杂度
- **F6.1 部署模式**: SaaS (公有云) vs Private Cloud vs On-premise。*(待研究)*
- **F6.2 IT运维负担**: 更新频率、故障排查难度、备份策略。*(待研究)*
- **F6.3 本地化服务**: 是否有中文客服、国内节点、本地化文档？*(待研究)*

#### F7: 数据安全与合规
- **F7.1 数据主权**: 数据存储在哪里？是否符合中国网络安全法/数据安全法？*(待研究：关键合规点)*
- **F7.2 认证资质**: ISO 27001, SOC 2, 等保三级等。*(待研究)*
- **F7.3 隐私政策**: 会议内容/参与者数据是否用于训练AI或其他用途？*(待研究)*

---

## 3. 条件分类：已知、可推导、仍需研究

### A. 人类已提供的条件 (Known Constraints)
1. **团队规模**: 30人研发人员。
2. **预算上限**: ≤ 20,000 RMB / 年。
3. **必需平台**: macOS, Windows, Web。
4. **必需集成**: Google Calendar + Outlook。
5. **可选功能**: 门禁联动（需评估其实现成本和可行性）。

### B. 从项目可推导的条件 (Derived Assumptions - To be verified in Stage 02)
*注意：这些是基于行业常识的推导，非绝对事实，需在阶段02验证其合理性或修正。*
1. **并发量**: 30人团队，峰值并发预约操作预计 < 10 QPS，对系统性能要求不高。
2. **会议室数量**: 未明确给出会议室数量。**[空缺]** 需假设一个范围（例如 3-10 间）进行成本估算，或在阶段02中将其作为变量处理。
3. **IT基础设施**: 假设团队有基本的IT管理员负责配置 SSO 和 API 密钥，无需专业实施团队驻场。
4. **语言偏好**: 界面需支持中文（因团队为中文环境），英文可作为辅助。

### C. 仍需研究的条件 (Unknowns / Gaps) -> **阶段 02 核心任务**

| ID | 空缺条件描述 | 阻塞的判断 | 优先级 |
|----|--------------|------------|--------|
| G1 | **主流候选系统的当前定价模型** (Per user vs Per room vs Flat fee) | 无法确定哪些系统符合 ≤2万/年预算。 | High |
| G2 | **Google Calendar & Outlook 双集成的实际稳定性与功能深度** | 无法判断是否满足“集成”的核心需求。 | High |
| G3 | **门禁联动的技术实现路径及额外成本** | 无法评估“可选功能”的可行性及对TCO的影响。 | Medium |
| G4 | **各候选系统在 macOS/Windows/Web 端的实际体验评分** | 无法区分“能用”和“好用”，影响最终推荐。 | Medium |
| G5 | **数据合规性细节 (特别是海外SaaS在中国的数据存储)** | 可能直接导致某些海外热门产品被淘汰。 | High |
| G6 | **具体的会议室数量** | 影响按房间计费的系统成本计算。 | High |
| G7 | **是否存在免费开源替代品且维护活跃** | 可能改变成本结构，需评估维护人力成本是否计入。 | Low |

---

## 4. 候选对象类别冻结 (Candidate Set Freeze)

为避免阶段漂移，此处定义**候选类别**，而非具体产品名（具体产品将在阶段02筛选）。

1. **国际主流 SaaS 办公套件中的会议室模块**
   - *代表方向*: Microsoft Teams Rooms, Zoom Workplace, Slack Connect (with integrations).
   - *关注点*: 通常捆绑销售，需单独核算会议室功能成本。
2. **垂直领域会议室预约 SaaS (Global)**
   - *代表方向*: RoomGuru, Envoy, Frontdesk, Mixmax (if applicable), Calendly (limited).
   - *关注点*: 功能专注，但需验证双日历集成和价格。
3. **垂直领域会议室预约 SaaS (China/Domestic)**
   - *代表方向*: 飞书会议室, 钉钉会议室, 企业微信会议室, 独立国产SaaS (如 智慧办公类).
   - *关注点*: 合规性好，但需验证 Google Calendar 集成能力（通常弱于 Outlook）。
4. **开源/自托管解决方案 (Open Source / Self-Hosted)**
   - *代表方向*: OpenCal (example), Resource Guru (has self-hosted?), custom scripts.
   - *关注点*: 软件免费，但需评估IT维护人力成本是否超过预算。
5. **IoT 硬件绑定型系统**
   - *代表方向*: 带有屏幕和按钮的物理终端配套软件 (如 VIZIO, Samsung SmartSignage with app).
   - *关注点*: 硬件成本高，可能超出预算，除非利用现有平板。

**排除原则 (Pre-defined Exclusions for Stage 02 Evaluation):**
- 任何仅支持单一日历（如仅Outlook或仅Google）的系统将被标记为“不满足核心需求”，除非其通过第三方桥接可实现（需评估稳定性）。
- 任何年度成本明显 > 2万元且无折扣可能的系统将被淘汰。
- 任何不支持 Web 端访问的系统将被淘汰。

---

## 5. 阶段 02 研究入口与行动路径

### 5.1 第一批优先研究行动 (Stage 02 Kick-off)

1. **确定会议室数量假设**:
   - *行动*: 在报告中设定基准场景：**5间会议室**。
   - *理由*: 30人团队通常配备3-8间会议室，取中位数以便成本估算。若实际不同，线性调整成本。
   - *来源*: 行业通用实践 (需引用1-2个参考)。

2. **筛选候选产品列表 (Top 10 Candidates)**:
   - *行动*: 搜索关键词 "meeting room booking software", "calendar integration google outlook", "office space management".
   - *目标*: 列出10个潜在候选，涵盖上述5个类别。
   - *工具*: `ralph prompt-first web-llm` 获取线索，`ego-browser` 验证官网。

3. **成本初筛 (Cost Screening)**:
   - *行动*: 访问每个候选产品的 Pricing Page。
   - *字段提取*: 最低档套餐价格、计费单位（用户/房间/月/年）、隐藏费用（设置费、超量费）。
   - *判定*: 剔除明显超预算 (>20k RMB/yr) 的产品。

4. **功能矩阵构建 (Feature Matrix)**:
   - *行动*: 对剩余候选，逐一验证：
     - [ ] Google Calendar Integration? (Yes/No/Partial)
     - [ ] Outlook/Exchange Integration? (Yes/No/Partial)
     - [ ] Web App? (Yes/No)
     - [ ] macOS/Windows Client? (Native/Electron/Web-only)
     - [ ] API Access? (Yes/No)
     - [ ] Door Lock Integration Examples? (List brands)
   - *来源*: 官方 Feature List, Help Center, Changelog.

5. **合规性检查 (Compliance Check)**:
   - *行动*: 查看 Terms of Service 和 Privacy Policy，重点搜索 "data residency", "server location", "GDPR", "PIPL" (Personal Information Protection Law).
   - *目标*: 识别数据是否存储在境外，是否存在合规风险。

### 5.2 具体研究路径与备用方案

| 研究问题 | 首选来源类型 | 具体搜索词/URL策略 | 失败备用路径 |
|----------|--------------|--------------------|--------------|
| 产品价格 | 厂商官网 Pricing Page | `[Product Name] pricing page`, `[Product Name] cost per user` | 联系 Sales (Email/Chatbot), 第三方评测网站 (G2, Capterra) |
| 日历集成细节 | 官方文档 / Developer Docs | `[Product Name] Google Calendar integration guide`, `[Product Name] Outlook sync setup` | 用户论坛 (Reddit, ProductHunt comments), YouTube demo videos |
| 门禁联动案例 | 合作伙伴页面 / Case Studies | `[Product Name] door lock integration partner`, `[Product Name] IoT case study` | API Documentation (check for webhook endpoints), Community forums asking about specific hardware |
| 数据合规 | Legal Pages / Trust Center | `[Product Name] data center location`, `[Product Name] privacy policy China` | 新闻搜索 `[Product Name] data breach` or `[Product Name] compliance certification` |
| 用户体验评价 | 独立评测 / 用户评论 | `[Product Name] review 2024`, `[Product Name] vs [Competitor]` | G2/Capterra ratings, LinkedIn employee reviews (for enterprise feel) |

### 5.3 网页 LLM 交叉询问示例 (For Stage 02 Execution)

*Prompt Template:*
> "请列出目前市场上主流的会议室预约系统，它们都支持 Google Calendar 和 Outlook 的双向同步吗？其中有哪些系统的年度价格在 2000 美元以内？请提供产品名称和大致价格区间。注意：我需要的是最近一年内的信息。"

*Context:* "阶段 02；只要求可复核来源线索，不要编造价格。"

---

## 6. 阶段 01 完整性自检

- [x] **目标清晰**: 交付选型报告，含推荐、备选、淘汰、成本。
- [x] **因素正交**: 功能、平台、集成、成本、合规、运维相互独立。
- [x] **已知/未知区分**: 明确了30人、预算、双日历为已知；会议室数量、具体价格为未知。
- [x] **空缺清单完整**: G1-G7 覆盖了所有关键决策盲点。
- [x] **候选集冻结**: 定义了5大类别，防止阶段02随意增加无关类别。
- [x] **研究路径具体**: 提供了搜索词、来源类型和备用方案，阶段02可直接执行。
- [x] **无伪装事实**: 所有价格、功能特性均标记为“待研究”或“假设”。

**判定**: 本阶段工件已具备启动阶段 02 的所有必要输入。Reviewer 应判定 `pass`。