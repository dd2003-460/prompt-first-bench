# 阶段 01：目标分解、已知与空缺条件

## 1. 目标交付物定义
**最终交付物**：一份可交付的《30人研发团队文件协作/网盘选型报告》。
**核心内容要求**：
1. **推荐方案**（1个）：基于约束条件的最优解。
2. **备选方案**（1-2个）：次优但可行的替代解。
3. **淘汰理由**：针对未入选的主流候选，说明其违反哪条硬性约束或为何在关键维度上显著劣于推荐项。
4. **成本明细**：年度总花费 < 3万元人民币的具体构成（含许可费、存储费、增值服务等）。

## 2. 影响因素正交分解 (Top-Level Factors)

我们将选型决策分解为以下五个互相正交且覆盖完整目标的影响因素：

### 因素 A: 平台兼容性 (Platform Compatibility)
*   **定义**：客户端必须原生支持 Web、macOS、Windows。
*   **子因素**:
    *   A1: Web端功能完整性（是否仅预览还是可编辑/同步）。
    *   A2: macOS/Windows 客户端稳定性及资源占用。
    *   A3: 多端同步冲突处理机制（非强制，但影响体验）。
*   **状态**: **已知/硬约束**。任务书明确指定“客户端要覆盖 Web、macOS、Windows”。任何不满足此三项之一（如仅移动端或仅Linux服务器端无Web）的方案直接淘汰。

### 因素 B: 核心功能 - 版本管理 (Version Control)
*   **定义**：文档必须具备历史版本记录、回溯能力。
*   **子因素**:
    *   B1: 版本保留策略（无限保留 vs 时间/数量限制）。
    *   B2: 版本对比功能（Diff视图）。
    *   B3: 版本恢复便捷性（一键回滚 vs 下载旧版）。
    *   B4: 二进制文件 vs 文本文件的版本管理差异（研发团队常涉及代码片段、配置、设计稿等混合文件）。
*   **状态**: **已知/硬约束**。任务书明确指定“两个核心功能是...文档版本管理”。需验证各候选产品对非Office文档（如PDF, CAD, Code snippets）的版本支持程度。

### 因素 C: 核心功能 - 细粒度权限控制 (Granular Permission Control)
*   **定义**：能够针对用户/角色设置具体的读写、分享、下载、打印等权限。
*   **子因素**:
    *   C1: 权限层级深度（文件夹级 vs 文件级 vs 字段级）。
    *   C2: 外部协作者权限隔离（能否邀请外部人员并限制其只能看特定文件）。
    *   C3: 权限继承与例外（父目录权限是否自动应用于子文件，能否单独覆盖）。
    *   C4: 审计日志（谁在何时访问/修改了什么，虽非核心功能但通常伴随权限系统存在，作为加分项考量）。
*   **状态**: **已知/硬约束**。任务书明确指定“两个核心功能是...细粒度的权限控制”。这是企业级网盘区别于个人网盘的关键，需重点考察。

### 因素 D: 成本约束 (Cost Constraint)
*   **定义**：30人团队，年度总花费 ≤ 30,000 RMB。
*   **子因素**:
    *   D1: 计价模式（按人头订阅 vs 按存储空间计费 vs 混合）。
    *   D2: 最小起购量（是否有10人/50人起步门槛）。
    *   D3: 隐性成本（超额存储费、高级功能解锁费、数据迁移费、技术支持费）。
    *   D4: 汇率与支付渠道（若为海外产品，需考虑美元/欧元定价及国内支付便利性）。
*   **状态**: **已知/硬约束**。上限3万RMB/年。平均每人每年预算约1000 RMB（~$14 USD）。这是一个相对紧凑的企业级预算，许多国际大厂标准版可能超标，需仔细核算。

### 因素 E: 离线使用能力 (Offline Capability) [加分项]
*   **定义**：在无网络环境下能否打开、编辑本地缓存的文件，并在联网后自动同步。
*   **子因素**:
    *   E1: 离线编辑支持范围（仅查看 vs 可编辑）。
    *   E2: 冲突解决策略（Last-write-wins vs 智能合并）。
    *   E3: 缓存大小限制。
*   **状态**: **待研究/加分项**。任务书指出“如果支持离线使用算加分项”。这意味着它不是淘汰理由，但在同等条件下权重更高。

## 3. 条件状态区分 (Known vs Derived vs Unknown)

| 条件类别 | 具体内容 | 来源/依据 | 备注 |
| :--- | :--- | :--- | :--- |
| **人类已提供 (Human Provided)** | 团队规模: 30人 | 任务书 | 固定值 |
| | 预算上限: 30,000 RMB/年 | 任务书 | 固定值 |
| | 平台要求: Web + macOS + Windows | 任务书 | 固定值 |
| | 核心功能: 版本管理 + 细粒度权限 | 任务书 | 固定值 |
| | 加分项: 离线使用 | 任务书 | 加权因子 |
| **项目可推导 (Derived)** | 人均预算: ~1,000 RMB/人/年 | 计算: 30000/30 | 用于快速筛选明显超标的产品 |
| | 候选对象类别: 企业云盘/协作平台 | 领域常识 | 排除纯个人网盘（如百度网盘个人版）、排除纯代码托管（如GitLab，因缺乏通用文件协作和细粒度非代码权限） |
| | 潜在痛点: 研发团队文件类型多样 | 领域常识 | 需关注非Office文档的版本和权限 |
| **仍需研究 (Unknown/To Research)** | **[空缺 U1]** 主流候选产品的最新官方定价（2024-2025版） | 厂商官网 | 价格易变，需实时核验 |
| | **[空缺 U2]** 各候选产品在"细粒度权限"上的具体实现深度（是否支持文件级ACL） | 厂商文档/评测 | 区分"团队可见"与"单文件授权" |
| | **[空缺 U3]** 各候选产品在"版本管理"上对二进制/大文件的限制 | 厂商文档/评测 | 区分文本diff与快照存储 |
| | **[空缺 U4]** 各候选产品是否提供稳定的离线同步客户端 | 厂商文档/用户反馈 | 验证加分项 |
| | **[空缺 U5]** 国内合规性与数据驻留政策（若选海外产品） | 法律/行业共识 | 虽非硬约束，但影响可用性风险，需评估 |
| | **[空缺 U6]** 免费额度或试用期时长 | 厂商官网 | 影响POC测试可行性 |

## 4. 空缺清单与阻塞影响 (Gap Analysis)

| 空缺ID | 描述 | 阻塞的后续判断 | 优先级 | 阶段02研究动作 |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | 候选产品A/B/C/D的具体年费（30席位） | 无法确定哪些方案在预算内，导致无法进入功能对比环节 | P0 | 访问官网Pricing页，搜索"Enterprise plan 30 users price" |
| **U2** | 候选产品X的权限模型是否支持"文件级只读/编辑/下载"分离 | 无法判定是否满足"细粒度权限"硬约束 | P0 | 查阅Help Center关于Permissions/ACL的文档，寻找截图或案例 |
| **U3** | 候选产品Y对PDF/ZIP文件的版本保留数量限制 | 无法判定版本管理功能的实际可用性 | P1 | 查阅Storage/Versioning限制文档，搜索用户论坛关于版本丢失的投诉 |
| **U4** | 候选产品Z的macOS/Windows客户端是否支持Offline Sync | 无法计算加分项得分 | P2 | 查阅Client Features文档，搜索"offline mode"关键词 |
| **U5** | 海外产品在中国大陆的访问速度与稳定性 | 影响实际用户体验，可能导致推荐失败 | P1 | 搜索近期用户测评（知乎/V2EX/Reddit），关注"速度"、"打不开"等关键词 |

## 5. 候选对象集合冻结 (Candidate Set Freeze)

基于"30人研发团队"、"文件协作/网盘"、"Web/Mac/Win"、"版本+权限"、"<3万RMB/年"这些特征，我们初步划定以下**候选类别**和**初始候选对象列表**。
*注意：以下对象仅为基于市场认知的假设，其属性（价格、功能）均标记为**[待验证]**，未经阶段02核验前不得视为事实。*

### 候选类别 1: 国内主流企业协同办公套件 (Domestic Suites)
*特点：合规性好，中文支持佳，通常打包销售，价格敏感。*
*   **候选 1.1: 飞书 (Feishu/Lark)**
    *   待验证属性: 企业版/旗舰版30人价格；云文档版本数限制；文件夹/文件级权限颗粒度；离线功能。
*   **候选 1.2: 钉钉 (DingTalk)**
    *   待验证属性: 专业版/专属版30人价格；钉盘版本管理能力；权限控制细节；离线同步支持。
*   **候选 1.3: 腾讯企业微信 (WeCom) + 微盘**
    *   待验证属性: 微盘独立购买价格；版本历史功能；权限设置深度。

### 候选类别 2: 国际主流协作/网盘平台 (International Platforms)
*特点：功能强大，生态成熟，但需注意价格和国内访问稳定性。*
*   **候选 2.1: Microsoft 365 Business Standard / Premium**
    *   待验证属性: 30用户年费（USD->RMB换算）；OneDrive for Business版本限制；SharePoint/OneDrive权限粒度；离线桌面应用功能。
    *   *风险提示*: 价格可能接近或超过3万RMB上限，需精确计算。
*   **候选 2.2: Dropbox Business**
    *   待验证属性: 30用户年费；File version history limits; Shared link permissions; Desktop app offline support.
    *   *风险提示*: 国内访问速度不稳定，需评估可用性。
*   **候选 2.3: Box**
    *   待验证属性: 30用户年费；Versioning policies; Access controls; Offline sync.
    *   *风险提示*: 通常定位较高，价格可能超标。

### 候选类别 3: 专注文件同步/网盘的专业工具 (Specialized Sync/Storage)
*特点：以文件为核心，版本和同步能力强，可能不含IM/日历等重型功能。*
*   **候选 3.1:坚果云 (Jianguoyun) 企业版**
    *   待验证属性: 企业版30人价格；版本保留策略（是否无限）；权限组管理；离线客户端性能。
    *   *优势假设*: 在国内以同步速度和稳定性著称，适合研发团队。
*   **候选 3.2: Nextcloud (自建 or 托管服务)**
    *   *排除理由预判*: 除非有现成的低成本SaaS托管且包含运维，否则自建不符合"挑选方案"的低运维预期，且30人团队自建安全维护成本高。暂列为**低优先级观察**，若前两类无法满足预算再考虑。
*   **候选 3.3: Seafile 企业版**
    *   待验证属性: 商业版价格；权限与版本功能；部署复杂度。

### 排除对象 (Explicit Exclusions)
*   **百度网盘企业版**: 虽然有名，但其核心强项是存储，**细粒度权限**和**文档在线编辑/版本对比**能力较弱（主要依赖第三方插件或基础功能），可能不满足"文档版本管理"的核心需求（特指文档内容的版本演进，而非文件替换）。*待阶段02确认其是否具备真正的文档版本对比功能，若无则正式淘汰。*
*   **GitLab/GitHub**: 虽是研发必备，但它们是代码版本控制系统，不适合通用的"文件协作/网盘"场景（如设计图、合同、会议纪要）。权限模型过于复杂且面向代码库，不适合作为通用网盘替代品。

## 6. 阶段 02 研究路径 (Research Path for Phase 02)

为了填补上述空缺，阶段 02 应执行以下具体行动：

### 第一步：价格与套餐核验 (Priority P0)
1.  **目标**: 获取每个候选对象在30席位下的确切年度费用（含税/不含税）。
2.  **来源**:
    *   首选: 各厂商官方网站 Pricing/Plans 页面。
    *   备用: 各大B2B采购平台（如阿里云市场、腾讯云市场）上的报价，或联系销售获取报价单（若公开价不明）。
3.  **搜索词示例**:
    *   "Feishu Enterprise Plan price per user annual"
    *   "Microsoft 365 Business Standard price 30 users"
    *   "Dropbox Business pricing 30 members"
    *   "坚果云 企业版 价格"
4.  **动作**: 制作表格，列出 `Product` | `Plan Name` | `Price per User/Year` | `Total for 30` | `Currency` | `Exchange Rate Used` | `Final RMB Cost` | `Within Budget? (Y/N)`。

### 第二步：功能深度核验 (Priority P0/P1)
1.  **目标**: 验证"细粒度权限"和"版本管理"。
2.  **来源**:
    *   官方 Help Center / Documentation。
    *   独立评测文章（Gartner, TechRadar, 国内IT媒体如InfoQ, 36氪）。
    *   用户社区（V2EX, Reddit r/sysadmin, Stack Overflow）。
3.  **具体检查点**:
    *   **权限**: 搜索 "file-level permission", "read-only share", "download restriction", "external guest access control"。
    *   **版本**: 搜索 "version history limit", "document diff view", "restore previous version", "binary file versioning"。
4.  **动作**: 对每个候选，记录 `Feature` | `Supported? (Y/N/Partial)` | `Evidence URL` | `Limitations`。

### 第三步：离线与体验核验 (Priority P2)
1.  **目标**: 验证离线功能和国内可用性。
2.  **来源**: 用户评论、GitHub Issues（如果是开源组件）、社交媒体吐槽。
3.  **搜索词**: "[Product Name] offline sync issues", "[Product Name] China speed slow".
4.  **动作**: 总结离线支持的广度（哪些文件类型）和国内访问的平均延迟评价。

### 第四步：交叉询问 (Web LLM)
1.  **指令**: "请比较飞书、钉钉、微软365、Dropbox、坚果云在30人研发团队场景下，关于'文件细粒度权限'和'文档版本管理'的具体功能差异，并指出哪个最符合'研发团队协作'的需求。同时估算它们在30人规模下的大致年度成本区间。"
2.  **用途**: 快速获取结构化对比线索，作为人工核验的辅助参考，不作为唯一证据。

## 7. 判定与下一步

*   **分解完成判定**:
    *   所有顶层因素（平台、版本、权限、成本、离线）已识别并正交。
    *   所有叶子因素（如权限层级、版本保留策略）已细化到可研究的最小单元。
    *   已知条件与未知条件已清晰分离。
    *   候选集已冻结，排除了明显不符的对象。
    *   阶段02的研究路径具体、可执行。
*   **结论**: 本阶段工件已准备好移交 Reviewer 进行质检，若通过则直接进入阶段 02 开始资料搜集。

**(Self-Correction/Refinement during drafting):**
*   *Initial thought*: Should I include Google Workspace?
*   *Correction*: Google Workspace is strong on docs but weak on general binary file storage/versioning compared to OneDrive/Dropbox. It's a valid candidate but might be less ideal for "R&D team files" which often include large binaries. I will keep it as a secondary candidate in Category 2 if budget allows, but prioritize OneDrive/Dropbox/Jianguoyun first due to the "Netdisk/File Collaboration" emphasis. Actually, let's stick to the strongest contenders to avoid analysis paralysis. The current list covers Domestic Suites, International Leaders, and Specialized Sync tools. This is sufficient coverage.
*   *Budget Check*: 30k RMB is tight for M365 Premium or Box. M365 Business Basic might fit, but lacks some advanced admin controls. M365 Business Standard (~$12.50/user/mo -> ~$180/year/user -> $5400 total -> ~39k RMB) is likely over budget. This suggests that **International options might fail the cost constraint**, making **Domestic Options** or **Specialized Sync (like Jianguoyun)** more likely winners. This insight guides Phase 02 to pay extra attention to the exact pricing of these specific tiers.