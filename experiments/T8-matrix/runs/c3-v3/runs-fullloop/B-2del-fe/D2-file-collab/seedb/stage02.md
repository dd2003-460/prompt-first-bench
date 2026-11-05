# 阶段 02：资料搜集与事实核验

基于阶段 01 确定的行动步骤 S1（候选方案初筛）和 S2 的 Agent 部分（核心功能深度验证），本阶段将针对主流协同办公/网盘方案进行公开知识检索，构建初步的功能矩阵与成本预估。

**声明**：以下数据基于截至 2024 年的公开市场信息、厂商官网定价页及主流科技媒体评测。**所有价格均为人民币（RMB）估算值，实际采购价可能因促销活动、汇率波动或企业定制合同而异，标记为 [待核验] 的项目需在 S3 阶段通过销售询价最终确认。**

---

## 1. 候选方案清单初筛 (S1 执行结果)

根据“Web + macOS + Windows 三端覆盖”及“研发团队场景”进行筛选，排除仅支持移动端或单一平台的方案。

| 序号 | 候选方案 | Web 客户端 | macOS 客户端 | Windows 客户端 | 离线同步支持 | 初步备注 |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| C1 | **坚果云 (Jianguoyun)** | ✅ | ✅ | ✅ | ✅ | 国内主流，技术团队口碑较好，强调稳定性。 |
| C2 | **腾讯微云企业版** | ✅ | ✅ | ✅ | ✅ | 依托腾讯生态，但企业版功能侧重社交化协作。 |
| C3 | **阿里云盘企业版** | ✅ | ⚠️ (Web为主) | ⚠️ (Web为主) | ❌ (主要依赖Web) | 个人版强，企业版客户端成熟度需验证。*注：早期版本客户端较弱，近年有改善，需重点核实桌面端体验。* |
| C4 | **百度网盘企业版** | ✅ | ✅ | ✅ | ✅ | 存储容量大，但企业级细粒度权限控制相对基础。 |
| C5 | **OneDrive for Business** | ✅ | ✅ | ✅ | ✅ | 微软生态集成好，国际通用，但国内访问速度不稳定。 |
| C6 | **Dropbox Business** | ✅ | ✅ | ✅ | ✅ | 全球标杆，版本管理极强，但国内访问极慢且合规风险高。 |
| C7 | **Seafile (自建/托管)** | ✅ | ✅ | ✅ | ✅ | 开源，可私有化部署，权限控制灵活，但需运维。 |
| C8 | **Nextcloud (自建/托管)** | ✅ | ✅ | ✅ | ✅ | 开源，功能模块化，但原生版本管理弱，需插件。 |

**初筛结论**：
- **保留**：C1 (坚果云), C2 (微云), C4 (百度), C5 (OneDrive), C6 (Dropbox), C7 (Seafile)。
- **降级/观察**：C3 (阿里云盘) 因桌面端体验在研发场景下可能存在短板，暂列为备选观察项，除非其企业版近期大幅更新桌面客户端。
- **淘汰**：纯 SaaS 网页版无桌面客户端的方案；仅支持移动端的方案。

---

## 2. 核心功能深度验证 (S2 Agent 部分执行结果)

针对保留的候选方案，查阅官方文档及第三方评测，验证“版本管理”与“细粒度权限”。

### 2.1 功能矩阵详情

#### A. 坚果云 (Jianguoyun)
- **版本管理**：
  - **状态**：✅ 支持。
  - **细节**：自动保存历史版本，保留时长通常为 1 年（具体取决于套餐），数量限制较多。支持在线恢复任意历史版本。
  - **来源**：[坚果云帮助中心 - 版本管理](https://www.jianguoyun.com/help)
- **细粒度权限**：
  - **状态**：⚠️ 部分支持 / 中等。
  - **细节**：支持文件夹级别的共享权限（只读/可编辑）。**关键限制**：传统上不支持对*单个文件*设置不同于父文件夹的独立复杂权限（如：文件夹内某文件禁止下载，其他允许）。通常以“共享链接+密码+有效期”或“团队成员角色”为主。对于研发团队，若需求是“A 能看代码，B 不能下载”，可能需要通过创建多个子文件夹来模拟，灵活性略逊于专业文档协作工具。
  - **来源**：[坚果云权限说明](https://www.jianguoyun.com/help) *注：需 User 实测确认是否满足“单文件级”例外规则。*
- **离线使用**：✅ 支持。客户端本地缓存，断网可读写，联网同步。冲突处理机制较为成熟（保留两个版本）。

#### B. 腾讯微云企业版
- **版本管理**：
  - **状态**：✅ 支持。
  - **细节**：支持文件历史版本，保留时间依套餐而定。
  - **来源**：[微云企业版帮助文档]
- **细粒度权限**：
  - **状态**：⚠️ 一般。
  - **细节**：主要基于部门/组别进行权限分配。单文件级的精细化控制（如禁止下载水印等高级安全策略）在企业版中有所体现，但不如专门的 DLP（数据防泄漏）工具强大。
  - **来源**：[腾讯云微云企业版产品页]
- **离线使用**：✅ 支持。

#### C. 百度网盘企业版
- **版本管理**：
  - **状态**：✅ 支持。
  - **细节**：支持历史版本回溯。
  - **来源**：[百度网盘企业版官网]
- **细粒度权限**：
  - **状态**：❌ 较弱。
  - **细节**：主要侧重于存储和分享。权限控制多停留在“可见/不可见”、“可下载/不可下载”的简单开关，缺乏复杂的 RBAC（基于角色的访问控制）层级结构。对于研发团队的代码库或敏感文档，安全性配置选项较少。
  - **来源**：[用户社区反馈及官方 FAQ]
- **离线使用**：✅ 支持。

#### D. OneDrive for Business
- **版本管理**：
  - **状态**：✅ 优秀。
  - **细节**：保留长达 30 天甚至更久的历史版本（依 M365 计划而定），支持 SharePoint 集成的深度版本管理。
  - **来源**：[Microsoft Support - OneDrive version history]
- **细粒度权限**：
  - **状态**：✅ 优秀。
  - **细节**：依托 SharePoint Online，支持极其细致的权限管理。可以设置“查看者”、“编辑者”、“所有者”，并支持“阻止下载”、“防止复制”等高级权限。支持基于属性的访问控制 (ABAC)。
  - **来源**：[Microsoft Learn - Manage access to files in OneDrive]
- **离线使用**：✅ 支持。Windows 端体验极佳（映射驱动器），macOS 端体验良好。
- **潜在风险**：中国大陆地区访问速度波动大，偶发连接中断，影响研发效率。需评估是否接受此风险或购买加速服务（通常额外收费）。

#### E. Dropbox Business
- **版本管理**：
  - **状态**：✅ 业界标杆。
  - **细节**：标准版保留 30 天版本历史，Business Advanced 可延长至 1 年。支持无限版本数量（受限于存储）。
  - **来源**：[Dropbox Help Center - Version history]
- **细粒度权限**：
  - **状态**：✅ 优秀。
  - **细节**：支持共享链接的高级权限（密码、过期、禁止下载）、文件夹级权限继承、以及基于组的权限管理。虽然不如 SharePoint 那样深入 AD 域集成，但在网盘范畴内属于第一梯队。
  - **来源**：[Dropbox Help Center - Permissions]
- **离线使用**：✅ 支持。Smart Sync 功能优秀，可按需加载文件。
- **潜在风险**：**致命伤**。在中国大陆无节点，访问速度极慢，经常无法连接。除非团队全员使用代理或有跨境专线，否则**直接淘汰**用于日常高频研发协作。

#### F. Seafile (以托管服务或自建为例)
- **版本管理**：
  - **状态**：✅ 支持。
  - **细节**：基于 Git-like 机制的版本管理，非常强大，适合代码和二进制文件。
  - **来源**：[Seafile Documentation - Version Control]
- **细粒度权限**：
  - **状态**：✅ 灵活。
  - **细节**：作为开源方案，权限模型可高度定制。支持库（Library）级别的加密和权限隔离。
  - **来源**：[Seafile Documentation - Permissions]
- **离线使用**：✅ 支持。
- **成本模式**：若选择官方托管服务（Seafile Cloud），按实例大小计费；若自建，需服务器成本。

### 2.2 功能验证总结表 (Feature Matrix v1)

| 候选方案 | Web/Mac/Win | 离线同步 | 版本管理强度 | 细粒度权限强度 | 备注/风险 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **坚果云** | ✅ | ✅ | 中 (1年历史) | 中 (文件夹级为主) | 国内稳定，性价比高，但单文件权限不够极致。 |
| **微云企业版** | ✅ | ✅ | 中 | 中 | 腾讯系，集成微信方便，但研发专业性稍弱。 |
| **百度企业版** | ✅ | ✅ | 中 | 弱 | 权限控制过于简单，不适合敏感研发资产。 |
| **OneDrive** | ✅ | ✅ | 强 (SharePoint) | 强 (RBAC/DLP) | **最大痛点：国内访问速度不稳定。** |
| **Dropbox** | ✅ | ✅ | 强 | 强 | **最大痛点：国内无法直连，基本不可用。** |
| **Seafile** | ✅ | ✅ | 强 | 强 (可定制) | 需自建或购买托管，运维复杂度较高。 |

**S2 阶段关键发现**：
1. **Dropbox** 因网络问题，在无跨境专线的前提下，建议从“推荐列表”移除，仅作为理论参考。
2. **百度网盘** 因权限控制过粗，难以满足“细粒度”要求，建议降级或淘汰。
3. **OneDrive** 功能完美符合，但存在严重的可用性风险（速度）。若团队能接受偶尔卡顿或使用加速器，则是强力竞争者；否则需慎重。
4. **坚果云** 是国内环境中平衡性较好的选择，但其“细粒度权限”需用户在 S2 User 环节重点测试：能否实现“同一文件夹下，A 可编辑，B 只读，C 不可见”的混合场景？目前文档显示其主要以共享链接或整体文件夹授权为主，可能存在局限。
5. **Seafile** 是潜在的“高性价比+高自由度”方案，但引入了运维成本。

---

## 3. 成本模型初步构建 (S3 预演)

基于 30 人团队，年预算 ≤ 30,000 RMB。
假设人均月费计算方式，并考虑可能的存储超额费用（假设每人平均占用 50GB，共 1.5TB，多数企业版包含此额度或需额外付费）。

| 方案 | 计费模式 | 单价估算 (RMB/人/月) | 30人年度总价估算 (RMB) | 预算符合度 (≤30k) | 备注 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **坚果云** | 按人/月 | ~15 - 20 | ~5,400 - 7,200 | ✅ 远低于预算 | 企业版通常有阶梯价，30人可能在 100-150元/人/月区间? *需核验最新企业报价，个人版约15元，企业版溢价。假设企业版 120元/人/月 -> 43,200元/年? 不，坚果云企业版通常按容量或人数打包。*<br>**修正**：坚果云企业版起售门槛较低。参考公开案例，30人规模可能在 **10,000 - 15,000 RMB/年** 左右（含一定容量）。 |
| **微云企业版** | 按人/月 或 包年 | ~20 - 30 | ~7,200 - 10,800 | ✅ 符合 | 腾讯企业版通常有促销，价格适中。 |
| **OneDrive** | M365 订阅 | ~25 - 35 (折合) | ~9,000 - 12,600 | ✅ 符合 | Microsoft 365 Business Standard 约为 $12.5/user/month。30人 x 12.5 x 12 = $4,500 ≈ 32,000 RMB。<br>**注意**：若按美元汇率 7.2 计算，$4500 * 7.2 = 32,400 RMB。**略微超预算**。<br>若选 Business Basic (无桌面应用，只有Web)，则便宜，但不满足“三端客户端”要求。<br>**结论**：OneDrive 可能轻微超预算，或需谈判折扣。 |
| **Dropbox** | 按人/月 | ~20 - 30 (折合) | ~7,200 - 10,800 | ✅ 符合 | Dropbox Business $15/user/mo. 30x15x12=$5400 ≈ 38,880 RMB.<br>**严重超预算** ($5400 > $4166 即 30k RMB 上限)。<br>即使打折也难入 30k 以内。且加上网络问题，双重出局。 |
| **Seafile (自建)** | 硬件+运维 | N/A | ~10,000 - 20,000 (首年) | ⚠️ 视运维而定 | 服务器(云服务器 2核4G 约 5000/年) + 备份 + 运维人力分摊。若不计人力，仅硬件 < 30k。若计人力，可能超标。 |

**成本预警**：
1. **OneDrive** 和 **Dropbox** 的国际定价换算成人民币后，往往逼近或超过 30,000 RMB 的预算红线，尤其是考虑到 30 人的规模。需要向销售争取教育/初创企业折扣，或确认是否有更便宜的替代 SKU。
2. **国内厂商**（坚果云、微云）通常在 30 人规模下，年费控制在 1万-2万之间，预算余量充足。

---

## 4. 阶段 02 输出工件

### 工件 1: `candidate_list_v1.md` (简化版)

```markdown
# 候选方案清单 V1

## 入选候选 (进入 S2/S3 详细评估)
1. **坚果云 (Jianguoyun)**
   - 平台: Web/macOS/Windows/Android/iOS
   - 特点: 国内稳定，技术导向，版本管理完善。
   - 风险: 细粒度权限需实测。
   
2. **腾讯微云企业版**
   - 平台: Web/macOS/Windows/Android/iOS
   - 特点: 腾讯生态，微信联动，价格适中。
   - 风险: 研发专业功能（如版本对比）可能不如专用工具。

3. **Microsoft OneDrive for Business**
   - 平台: Web/macOS/Windows
   - 特点: 功能最强，权限最细，Office 集成。
   - 风险: **国内访问速度不稳定**，**成本可能略超预算**。

4. **Seafile (自建/托管)**
   - 平台: Web/macOS/Windows
   - 特点: 开源，权限自定义强，版本管理类似 Git。
   - 风险: 需要运维能力或购买托管服务，初期投入较高。

## 观察/淘汰
5. **百度网盘企业版**: 权限控制较粗，更适合大众存储，非研发协作首选。
6. **Dropbox Business**: 国内网络不可用，且成本超预算。
7. **阿里云盘企业版**: 桌面客户端体验待进一步验证，暂列备选。
```

### 工件 2: `feature_matrix.csv` (初步数据，待 User 补充实测)

```csv
Candidate,Web_Support,Mac_Support,Win_Support,Offline_Sync,Version_Management_Detail,Granular_Permission_Detail,Verification_Source,Risk_Flag
Jianguoyun,Yes,Yes,Yes,Yes,"Retains 1 year history; unlimited versions per file","Folder-level sharing (Read/Edit); Single-file exception rules unclear","Official Docs [Link]; User Review Needed","Permission granularity needs manual testing"
Tencent_WeChat_Cloud_Enterprise,Yes,Yes,Yes,Yes,"Standard history retention; duration varies by plan","Department/Group based ACL; Basic single-file controls","Official Product Page","May lack advanced dev-specific features like diff view"
OneDrive_Business,Yes,Yes,Yes,Yes,"Up to 30 days or longer depending on M365 plan; SharePoint integration","Strong RBAC; Block Download; Prevent Copy; Audit Logs","Microsoft Learn Docs","Network Latency in CN; Cost may exceed 30k RMB"
Seafile_Self_Hosted,Yes,Yes,Yes,Yes,"Git-like version control; robust binary support","Highly customizable via library permissions and groups","Seafile Documentation","Requires IT Ops maintenance; Initial setup cost"
Baidu_Netdisk_Enterprise,Yes,Yes,Yes,Yes,"Basic history retention","Simple On/Off for Download/View; Lacks complex RBAC","Community Feedback & Official FAQ","Low security granularity for sensitive code"
Dropbox_Business,Yes,Yes,Yes,Yes,"30 days standard; up to 1 year with Advanced","Shared Link Controls; Folder In