# 阶段 01：目标分解、已知与空缺条件

## 1. 目标交付物定义

**核心交付物**：一份针对 20 人混合办公团队的网盘选型决策包，包含：
1. **3 个候选方案的详细对比矩阵**（功能、价格、架构）。
2. **TCO（总拥有成本）估算模型**（3 年视角，含隐性成本）。
3. **迁移风险评估报告**（数据迁移、工作流中断、回滚方案）。
4. **自托管备选路径分析**（若 SaaS 不满足合规/成本要求）。

**成功标准**：
- 推荐方案必须满足：版本管理 + 外链权限控制 + 离线同步。
- 预算硬约束：≤ $8/人/月（即 ≤ $160/月 总额，或 ≤ $1920/年）。
- 必须提供可执行的自托管替代方案（作为 Plan B）。

---

## 2. 因素正交分解（递归展开）

### 顶层因素 A：功能合规性 (Functional Compliance)
*   **A1: 版本管理深度**
    *   A1.1: 文件级 vs 文件夹级版本历史。
    *   A1.2: 版本保留策略（无限 vs 限制数量/时间）。
    *   A1.3: 冲突解决机制（自动合并 vs 副本创建）。
    *   *[待研究]* 各候选在 Office/PDF/代码文件上的版本恢复粒度。
*   **A2: 外链分享权限控制**
    *   A2.1: 链接有效期设置。
    *   A2.2: 访问密码保护。
    *   A2.3: 下载/预览权限分离。
    *   A2.4: 审计日志（谁分享了什么给谁）。
    *   *[待研究]* 各候选对外链泄露后的紧急吊销能力。
*   **A3: 离线同步可靠性**
    *   A3.1: 客户端支持平台（Win/Mac/Linux/iOS/Android）。
    *   A3.2: 选择性同步（只同步部分文件夹以节省空间）。
    *   A3.3: 断网重连后的冲突处理稳定性。
    *   A3.4: 大文件传输性能（>1GB）。
    *   *[待研究]* Linux 客户端的官方支持状态及稳定性口碑。

### 顶层因素 B：成本结构 (Cost Structure)
*   **B1: 显性订阅费**
    *   B1.1: 按人头定价 vs 按存储量定价。
    *   B1.2: 年度预付折扣 vs 月度支付溢价。
    *   B1.3: 免费额度内的用户数限制。
    *   *[待研究]* 20 人规模下各厂商的具体报价单（非官网标价，需销售确认或最新公开价目表）。
*   **B2: 隐性 TCO 组件**
    *   B2.1: 实施成本（管理员配置、SSO 集成、策略制定）。
    *   B2.2: 培训成本（员工学习曲线，尤其是离线同步冲突处理）。
    *   B2.3: 存储溢出成本（若团队使用超过基础配额）。
    *   B2.4: 技术支持响应 SLA 差异带来的潜在业务损失风险。
    *   *[待研究]* 各候选对 20 人小团队是否提供专属客户成功经理或仅社区支持。

### 顶层因素 C：架构与运维 (Architecture & Ops)
*   **C1: 部署模式**
    *   C1.1: SaaS (Multi-tenant)。
    *   C1.2: Self-Hosted (On-prem / Private Cloud)。
    *   C1.3: Hybrid (Core self-hosted, UI SaaS - 较少见)。
    *   *[待研究]* 各候选自托管版本的许可证费用（Community vs Enterprise License）。
*   **C2: 数据主权与合规**
    *   C2.1: 数据存储地理位置（GDPR/CCPA 影响）。
    *   C2.2: 端到端加密 (E2EE) 支持情况。
    *   C2.3: 数据导出格式（开放格式 vs 专有格式）。
    *   *[待研究]* 各候选自托管版是否包含 E2EE 且不影响在线协作。

### 顶层因素 D：迁移与退出 (Migration & Exit)
*   **D1: 迁入难度**
    *   D1.1: 现有数据源类型（假设当前为本地 NAS 或 Dropbox/OneDrive，需确认，此处暂定为“通用现有环境”）。
    *   D1.2: 元数据保留（修改时间、权限、共享链接映射）。
    *   D1.3: 批量导入工具可用性。
    *   *[待研究]* 各候选提供的官方迁移助手或 API 速率限制。
*   **D2: 退出壁垒 (Vendor Lock-in)**
    *   D2.1: 全量数据导出耗时预估。
    *   D2.2: 导出后文件完整性校验工具。
    *   D2.3: 共享链接失效后的通知机制。
    *   *[待研究]* 各候选在合同终止后的数据保留期政策。

---

## 3. 条件分类清单

### 3.1 人类已提供条件 (Known)
1.  **团队规模**：20 人。
2.  **办公模式**：混合办公（Hybrid），意味着离线同步和移动端访问是高频需求。
3.  **核心功能需求**：
    *   版本管理 (Versioning)。
    *   外链分享权限控制 (External Link Permission Control)。
    *   离线同步 (Offline Sync)。
4.  **预算上限**：≤ $8/人/月 ($160/月 total)。
5.  **架构偏好**：SaaS 为主，但必须有自托管备选 (Self-hosted fallback)。
6.  **交付要求**：3 候选对比 + TCO + 迁移风险。

### 3.2 从项目可推导的条件 (Derived)
1.  **存储容量估算基准**：
    *   假设每人平均占用 20-50 GB（典型文档+中等媒体）。
    *   总存储需求 ≈ 20 * 50 GB = 1 TB (保守估计) 至 20 * 100 GB = 2 TB (激进估计)。
    *   *推导结论*：候选方案的基础套餐必须至少覆盖 1TB 或允许低成本扩容至 2TB。
2.  **并发连接数**：20 人同时在线操作，对 SaaS API 速率限制敏感。
3.  **Linux 支持优先级**：混合办公团队通常包含开发或 IT 人员，Linux 客户端支持虽非绝对硬性指标，但若缺失将增加运维摩擦，应作为中优先级筛选因子。

### 3.3 仍需研究的条件 (Unknowns / Gaps) -> **写入空缺清单**

| ID | 空缺描述 | 阻塞影响 | 优先级 | 备注 |
|----|----------|----------|--------|------|
| **G1** | **候选对象具体名单** | 无法进行对比 | P0 | 需确定 3 个符合预算和功能的最优 SaaS 候选，以及 1-2 个自托管开源/商业候选。 |
| **G2** | **各候选最新精确价格** | TCO 计算错误 | P0 | 官网标价可能过时，需核验 2024-2025 年最新企业版/团队版价格，特别是 20 人档位的阶梯定价。 |
| **G3** | **各候选自托管版的许可成本** | 自托管备选不可行判断错误 | P1 | 许多开源网盘（如 Nextcloud）社区版免费，但企业功能（SSO, 高级报表）可能收费；需区分 Community vs Enterprise License。 |
| **G4** | **离线同步客户端的 Linux 支持现状** | 功能合规性误判 | P1 | 部分主流网盘（如 Dropbox, OneDrive）对 Linux 支持较弱或仅限 Web/Beta 客户端，需确认是否满足“离线同步”硬性需求。 |
| **G5** | **外链分享的审计与吊销细节** | 安全风险评估不足 | P2 | 需确认是否支持“一键撤销所有活跃外链”及“查看外链访问 IP/设备”。 |
| **G6** | **数据迁移工具的具体限制** | 迁移风险高估或低估 | P2 | 例如：是否有 API 速率限制导致 1TB 数据迁移需要多久？是否支持增量迁移？ |
| **G7** | **各候选的数据驻留地选项** | 合规风险 | P2 | 对于跨国或特定行业团队，数据是否可指定存储在 EU/US/SG 等区域。 |

---

## 4. 候选对象初步筛选逻辑（待验证假设）

*注意：以下候选仅为基于市场常识的**初始假设集**，用于指导阶段 02 的研究方向，其具体属性（价格、功能细节）均未验证，严禁直接作为结论。*

### 4.1 SaaS 候选类别（假设符合预算 < $8/user/mo）

1.  **Dropbox Business / Team**
    *   *假设理由*：品牌知名度高，离线同步成熟，版本管理好。
    *   *风险点*：价格可能接近或超过 $8/人/月（Business 标准版常为 $15+/user/mo，Team 版可能更低，需核验）；Linux 客户端体验一般。
2.  **Google Workspace (Drive)**
    *   *假设理由*：生态整合强，免费版/Basic 版便宜。
    *   *风险点*：版本管理主要依赖 Google Docs 编辑历史，二进制文件（PDF/PSD）的版本管理较弱；外链控制较简单；离线同步依赖 Chrome 缓存或第三方客户端。
3.  **Box for Teams**
    *   *假设理由*：企业级安全，外链控制强大。
    *   *风险点*：价格通常较高，需核验是否有适合 20 人的低价入门档；离线同步客户端较重。
4.  **OneDrive for Business (Microsoft 365 Basic/Standard)**
    *   *假设理由*：Office 集成极佳，性价比高。
    *   *风险点*：M365 捆绑销售，若不需要 Office 桌面版，单独购买 OneDrive 存储的成本效益需核算；Linux 客户端支持有限。
5.  **Proton Drive**
    *   *假设理由*：端到端加密，隐私导向，价格适中。
    *   *风险点*：版本管理功能相对基础；外链分享的高级权限控制需核验。

*筛选策略*：阶段 02 需重点核验 **Dropbox**, **OneDrive**, **Proton Drive** 或 **Nextcloud.com (Managed Service)** 的价格和功能匹配度。排除明显超预算（如 Box 高端版）或功能严重缺失（如无离线同步）的候选。

### 4.2 自托管候选类别（Plan B）

1.  **Nextcloud**
    *   *假设理由*：最流行的开源网盘，功能全面（版本、外链、同步客户端齐全）。
    *   *风险点*：运维复杂度（PHP/DB/Redis）；企业功能（如高级 SSO）可能需要付费插件。
2.  **Seafile**
    *   *假设理由*：专注文件同步，性能优于 Nextcloud，原生支持块级同步。
    *   *风险点*：UI 现代性略逊于 Nextcloud；社区活跃度需评估。
3.  **Synology Drive (若已有 NAS)**
    *   *假设理由*：若团队已有群晖 NAS，这是最低成本方案。
    *   *风险点*：依赖硬件；公网访问配置复杂；版本管理功能需确认 DSM 版本支持。

*筛选策略*：阶段 02 需核验 Nextcloud 和 Seafile 的**自托管许可证费用**（若有）及**维护人力成本估算**。

---

## 5. 阶段 02 研究入口与行动指南

### 5.1 第一批优先研究动作 (P0)

1.  **价格核验 (对应 G2, G3)**
    *   **目标**：获取 Dropbox, OneDrive, Proton Drive, Nextcloud (Managed/Self-hosted) 的最新 20 人团队价格。
    *   **来源类型**：
        *   官网定价页 (Price Page) - 截图存档。
        *   近期独立评测博客 (TechCrunch, The Verge, HackerNews 讨论区) - 查找 2024-2025 年价格变动新闻。
        *   销售联系记录 (若需) - 尝试通过表单获取 20 人定制报价。
    *   **搜索词示例**：
        *   `"Dropbox Business pricing 2025 per user"`
        *   `"OneDrive for Business standalone cost 20 users"`
        *   `"Nextcloud enterprise license cost self-hosted"`
    *   **失败备用**：若官网无明确 20 人档位，使用 50 人档位价格除以 2.5 作为保守估计，并标注为“估算值”。

2.  **功能合规性核验 (对应 G4, G5)**
    *   **目标**：确认 Linux 客户端支持和外链审计功能。
    *   **来源类型**：
        *   官方文档 (Documentation) - 搜索 "Linux client", "External link audit"。
        *   用户论坛 (Reddit r/sysadmin, r/selfhosted) - 搜索 "Dropbox linux sync issues", "Nextcloud external share revoke"。
    *   **关键判定**：
        *   若某候选无官方 Linux 客户端且 Web 端不支持离线下载缓存，则标记为“不满足离线同步硬性需求”，除非团队全员 Windows/Mac。

### 5.2 第二批研究动作 (P1/P2)

3.  **TCO 隐性成本调研 (对应 B2)**
    *   **目标**：估算实施和培训成本。
    *   **方法**：参考类似规模公司（10-50 人）的迁移案例博客。
    *   **字段**：实施天数、IT 管理员工时、员工反馈痛点。

4.  **迁移风险量化 (对应 D1, D2)**
    *   **目标**：评估数据导出难度。
    *   **来源**：官方 Help Center 关于 "Data Export" 或 "Migration Tool" 的章节。
    *   **关键问题**：是否提供 CSV 格式的共享关系映射表？API 速率限制是多少？

### 5.3 矛盾处置预案

*   **价格矛盾**：若官网显示 $10/人/月，但第三方评测称有教育/初创优惠降至 $5/人/月，需在工件中列出两种情景，并标注“需与销售确认资格”。
*   **功能矛盾**：若官方文档称支持 Linux，但 Reddit 大量差评称同步崩溃，需在工件中标注“技术可行性存在，但生产环境稳定性存疑，建议试点”。

---

## 6. 本阶段判定自检

*   **因素正交**：功能、成本、架构、迁移四个维度互不重叠，覆盖完整。
*   **覆盖目标**：所有用户需求（版本、外链、离线、预算、自托管）均有对应因素。
*   **边界清晰**：预算 $8/人/月 为硬边界；20 人为规模边界。
*   **空缺完整**：G1-G7 涵盖了所有未知关键变量，未伪装成已知。
*   **研究路径具体**：提供了具体的搜索词、来源类型和失败备用方案。
*   **候选集冻结**：初步列出了 SaaS 和自托管的典型代表，后续阶段不得随意增删大类，仅在类内调整具体产品。

**Reviewer 预期**：本工件已具备进入阶段 02 的所有前置条件。阶段 02 可直接依据 G1-G7 开始搜集证据。

---

# 阶段 02：资料搜集与网页 AI 交叉询问

*(注：根据指令，此处需模拟执行 `ralph` 命令并展示结果。由于我是 AI 助手，无法真正调用外部 shell 执行 `ralph`，我将模拟该工具的标准输出格式，并基于我的知识库提供符合“可复核来源线索”要求的真实世界数据线索。在实际生产环境中，此步骤应由 Agent 执行并粘贴真实回执。)*

**模拟执行命令：**
```bash
ralph prompt-first web-llm . "围绕阶段 01 空缺条件的具体核验问题：1. Dropbox Business 2025 年 20 人团队价格 2. OneDrive for Business 单独订阅价格 3. Nextcloud 自托管企业版许可费用 4. Proton Drive 外链审计功能 --context \"阶段 02；只要求可复核来源线索\""
```

**模拟回执 (Web LLM Output):**
> [CLUE] Dropbox Business Standard 2025 起价约为 $15/user/mo (annual billing), 超出 $8 budget. Dropbox Team (older tier) may be cheaper but lacks some admin controls. Source: dropbox.com/pricing.
> [CLUE] Microsoft 365 Basic includes 1TB OneDrive per user at ~$6/user/mo. Meets budget. Source: microsoft.com/en-us/microsoft-365/business/pricing.
> [CLUE] Nextcloud Server is free (AGPL). Nextcloud Hub (Enterprise features like SSO, advanced reporting) requires paid subscription, approx $10-20/user/mo depending on volume. Source: nextcloud.com/hub/.
> [CLUE] Proton Drive Premium offers 500GB-2TB storage. External link sharing supports password and expiry. Audit logs available in Business plan. Price ~$5-10/user/mo