# 阶段 03：具体行动分解（无 owner 组件）

**任务目标**：基于阶段 02 的核验结论，制定 Cal.com 自托管方案的具体实施步骤。
**核心策略**：采用 **Cal.com Self-Hosted (Docker Compose)** 作为最终交付方案。
**预算约束**：总显性成本控制在 ¥2,000 以内（预留缓冲），隐性运维时间计入人力成本但不占用现金预算。
**关键依赖**：公司 IT 环境需确认使用 Microsoft 365 (Graph API) 或 Google Workspace。

---

## 1. 前置准备与环境确认 (Phase 0: Pre-flight)

在开始部署前，必须完成以下信息收集，否则后续 OAuth 配置将失败。

### Step 1.1: 确认日历后端架构
*   **输入**: IT 部门提供的邮件/日历服务类型说明。
*   **动作**:
    1.  询问 IT 管理员：Outlook 用户是连接至 `outlook.office365.com` (M365 Cloud) 还是本地 Exchange Server？
    2.  若为 M365 Cloud -> 标记为 `GRAPH_API_SUPPORTED`。
    3.  若为本地 Exchange -> 标记为 `ICAL_ONLY_RISK`（需告知业务方双向同步可能受限，仅支持单向订阅或需额外开发）。
    4.  确认 Google Calendar 是否已开通且允许第三方应用访问。
*   **依赖**: IT 部门响应。
*   **预期产出**: 《日历环境兼容性确认单》（明确 GCal 和 Outlook 的支持级别）。
*   **验收方式**: 获得 IT 负责人的书面/邮件确认，明确技术路径（OAuth 2.0 vs iCal）。

### Step 1.2: 注册云资源与域名
*   **输入**: 阿里云/腾讯云账号、企业邮箱用于验证。
*   **动作**:
    1.  购买轻量应用服务器（推荐：2核4G，Linux Ubuntu 22.04 LTS）。
    2.  购买 `.com` 或 `.cn` 域名。
    3.  配置 DNS 解析：将域名的 `A` 记录指向服务器公网 IP。
    4.  配置安全组：开放 80 (HTTP), 443 (HTTPS), 22 (SSH, 限制源 IP)。
*   **依赖**: 无。
*   **预期产出**: 可 SSH 登录的 Linux 服务器，域名解析生效。
*   **验收方式**: 浏览器访问域名 IP 地址能连通；`ping domain.com` 返回正确 IP。

---

## 2. 基础设施部署 (Phase 1: Infrastructure)

### Step 2.1: 安装 Docker 与 Docker Compose
*   **输入**: 服务器 Root/Admin 权限。
*   **动作**:
    1.  更新系统包：`apt update && apt upgrade -y`。
    2.  安装 Docker Engine 及 Docker Compose Plugin。
    3.  创建非 root 用户 `calcom`，加入 docker 组，以该用户执行后续操作（最佳实践）。
    4.  配置 UFW 防火墙（可选，若云厂商安全组已严格则跳过）。
*   **依赖**: Step 1.2 完成。
*   **预期产出**: 服务器具备容器运行环境。
*   **验收方式**: `docker --version` 和 `docker compose version` 正常输出版本号。

### Step 2.2: 初始化 Cal.com 数据目录与配置
*   **输入**: Cal.com 官方 GitHub 仓库 (`calcom/cal.com`) 中的 `docker-compose.yml` 模板。
*   **动作**:
    1.  克隆仓库或下载最新的 `docker-compose.yml` 到 `/opt/calcom` 目录。
    2.  修改 `.env` 文件：
        *   `DOMAIN`: 设置为实际使用的域名（如 `meet.company.com`）。
        *   `POSTGRES_PASSWORD`: 生成强随机密码。
        *   `REDIS_PASSWORD`: 生成强随机密码。
        *   `NEXTAUTH_SECRET`: 使用 `openssl rand -base64 32` 生成密钥。
    3.  确保 PostgreSQL 和 Redis 的数据卷挂载路径正确，以便后续备份。
*   **依赖**: Step 2.1 完成。
*   **预期产出**: 配置好的 `docker-compose.yml` 和 `.env` 文件。
*   **验收方式**: 配置文件语法检查通过（`docker compose config` 无报错）。

---

## 3. 应用启动与基础配置 (Phase 2: Application Setup)

### Step 3.1: 启动服务栈
*   **输入**: 配置好的 Compose 文件。
*   **动作**:
    1.  执行 `docker compose up -d`。
    2.  监控日志：`docker compose logs -f api` 直到看到 "Application ready" 或类似成功提示。
    3.  等待 Nginx/Next.js 完全加载（通常 1-3 分钟）。
*   **依赖**: Step 2.2 完成。
*   **预期产出**: Cal.com Web 界面可通过 HTTPS 访问。
*   **验收方式**: 浏览器访问 `https://<domain>`，能看到 Cal.com 登录页面。

### Step 3.2: SSL 证书自动化配置
*   **输入**: 域名 DNS 已指向服务器。
*   **动作**:
    1.  利用 Cal.com 内置的 Let's Encrypt 集成（Nginx 配置中通常包含 certbot 自动续期逻辑，或手动配置 ACME 客户端）。
    2.  若官方镜像未自动处理，手动安装 Certbot 并配置定时任务申请证书。
    3.  确保证书颁发成功，Nginx 正确引用证书路径。
*   **依赖**: Step 3.1 完成。
*   **预期产出**: 网站显示绿色锁图标，HTTPS 连接安全。
*   **验收方式**: 在线 SSL 检测工具显示证书有效，无混合内容警告。

### Step 3.3: 创建管理员账户与组织
*   **输入**: 管理员邮箱。
*   **动作**:
    1.  首次访问引导页，创建超级管理员账户。
    2.  设置组织名称（Organization Name）。
    3.  邀请其他 5 名核心组织者（Tech Leads/PMs）加入组织，赋予“Admin”或“Member”权限。
    4.  其余 25 人暂时不添加为组织成员，而是通过后续生成的“共享链接”进行预约（符合 Cal.com Free Plan 逻辑，但自托管版所有用户均可免费创建日程，故建议全员加入以获得完整功能体验，因为自托管无席位费限制）。
    *   *修正*: 由于是自托管，**无需付费席位**。建议将所有 30 人全部邀请进入组织，每人拥有独立 Profile，便于管理个人偏好和门禁联动身份识别。
*   **依赖**: Step 3.1 完成。
*   **预期产出**: 30 个活跃用户账户存在于系统中。
*   **验收方式**: 后台用户列表显示 30 人，且每人能独立登录。

---

## 4. 日历集成配置 (Phase 3: Integration)

**这是最关键的环节，直接决定硬性条件是否满足。**

### Step 4.1: 配置 Google Calendar 集成
*   **输入**: Google Cloud Console 项目 ID, Client ID, Client Secret。
*   **动作**:
    1.  登录 Cal.com 管理后台 -> Settings -> Integrations -> Google Calendar。
    2.  填写 Google OAuth 凭据（需在 Google Cloud Console 预先创建 OAuth Client ID，回调地址填 `https://<domain>/api/integrations/google/callback`）。
    3.  测试连接：选择一个测试用户，点击“Connect”，授权成功后，查看其日历事件是否同步到 Cal.com。
*   **依赖**: Step 3.3 完成；Google Cloud 项目配置完成。
*   **预期产出**: 用户可在 Cal.com 中看到 Google Calendar 的事件，并在 Cal.com 创建会议时同步回 GCal。
*   **验收方式**:
    1.  在 GCal 创建一个测试事件 -> 刷新 Cal.com -> 事件出现。
    2.  在 Cal.com 创建一个会议室预订 -> 刷新 GCal -> 事件出现且包含会议室地点。

### Step 4.2: 配置 Microsoft 365 / Outlook 集成
*   **输入**: Azure AD App Registration (Client ID, Tenant ID, Client Secret)。
*   **动作**:
    1.  在 Azure Portal 创建新应用，添加 API 权限：`Calendars.ReadWrite`, `User.Read`.
    2.  在 Cal.com 管理后台 -> Settings -> Integrations -> Microsoft.
    3.  填入 Azure 凭据。
    4.  **关键步骤**: 确认回调 URL 配置正确。
    5.  测试连接：选择一名使用 M365 的用户，授权连接。
*   **依赖**: Step 3.3 完成；Azure 应用注册完成；Step 1.1 确认为 M365 环境。
*   **预期产出**: M365 用户的 Outlook 日历与 Cal.com 双向同步。
*   **验收方式**:
    1.  在 Outlook 网页版创建事件 -> 刷新 Cal.com -> 同步成功。
    2.  在 Cal.com 预订会议室 -> 刷新 Outlook -> 同步成功。
    *   *注意*: 若 Step 1.1 判定为本地 Exchange，此步骤将失败或仅支持单向。此时需启用 iCal 备用方案（见 Step 4.3）。

### Step 4.3: (备选) iCal 单向同步配置（针对纯本地 Outlook 或故障降级）
*   **输入**: 用户的 iCal 订阅链接。
*   **动作**:
    1.  若双向同步不可用，指导用户在 Cal.com Profile 中粘贴其 Outlook 导出的 iCal 公开链接。
    2.  Cal.com 将定期拉取该链接获取忙碌状态（Read-only）。
    3.  告知用户：在此模式下，Cal.com 创建的会议**不会**自动写回 Outlook，用户需手动复制或使用脚本辅助。
*   **依赖**: Step 4.2 失败时触发。
*   **预期产出**: 至少能避免时间冲突（Cal.com 知道 Outlook 忙闲）。
*   **验收方式**: 在 Outlook 标记忙碌时段，Cal.com 对应时段显示不可预订。

---

## 5. 会议室资源建模 (Phase 4: Resource Modeling)

### Step 5.1: 定义会议室实体
*   **输入**: 物理会议室清单（名称、位置、容纳人数、设备）。
*   **动作**:
    1.  在 Cal.com 中创建“Resources”（资源）类别，命名为“Meeting Rooms”。
    2.  为每间物理会议室创建一个 Resource 对象（例如：Room A, Room B）。
    3.  设置每个 Resource 的容量为 1（表示同一时间只能被一个会议占用）。
    4.  （可选高级功能）如果某间大会议室可拆分，可使用 Cal.com 的“Multiple Resources per Booking”功能，但初期建议保持简单，1房间=1资源。
*   **依赖**: Step 3.3 完成。
*   **预期产出**: 系统中存在 N 个可用的会议室资源。
*   **验收方式**: 在创建日程时，下拉菜单中出现所有定义的会议室名称。

### Step 5.2: 创建标准预约类型 (Booking Types)
*   **输入**: 常见会议时长需求（15min, 30min, 60min, 90min）。
*   **动作**:
    1.  创建多个 Booking Type，分别对应不同时长。
    2.  在每个 Booking Type 中：
        *   关联相应的会议室资源（Resource）。
        *   设置时区为办公室所在时区。
        *   设置提前预订限制（如：不能预订过去的时间）。
        *   设置最大提前预订天数（如：30天）。
    3.  启用“Require Location”选项，强制填写会议室。
*   **依赖**: Step 5.1 完成。
*   **预期产出**: 员工可选择特定时长和特定会议室进行预订。
*   **验收方式**: 模拟预订流程，确认能锁定指定会议室的指定时间段。

---

## 6. 门禁联动开发（可选加分项）(Phase 5: Optional Hardware Integration)

*注意：此项为非阻塞性任务，若时间紧张可延后至 Phase 6 之后迭代。*

### Step 6.1: 设计 Webhook 中间件
*   **输入**: 门禁系统 API 文档（假设门禁系统提供 REST API，接受 Token 开门）。
*   **动作**:
    1.  编写一个简单的 Node.js 或 Python 微服务（FastAPI/Express）。
    2.  该服务监听 Cal.com 的 Webhook 事件：
        *   `booking.created`: 提取参会者邮箱/ID，调用门禁 API 预生成临时通行码或发送开门指令。
        *   `booking.updated` / `booking.cancelled`: 撤销通行权限。
    3.  将中间件部署在同一台服务器上（Docker 容器化）。
    4.  在 Cal.com 后台配置 Webhook URL 指向该中间件。
*   **依赖**: Step 3.1 完成；门禁系统 API 可用。
*   **预期产出**: 会议开始时，参会者刷卡/扫码即可进入会议室。
*   **验收方式**: 创建一个测试会议，观察门禁系统日志是否收到正确的开门请求。

---

## 7. 测试与验收 (Phase 6: QA & Acceptance)

### Step 7.1: 端到端功能测试 (E2E)
*   **输入**: 30 名真实用户名单（或测试账号）。
*   **动作**:
    1.  **三端测试**:
        *   macOS Safari/Chrome: 访问 Web 界面，测试 PWA 安装到桌面。
        *   Windows Edge/Chrome: 访问 Web 界面，测试 PWA 安装到桌面。
        *   Mobile (iOS/Android): 访问 Web 界面，测试 PWA 安装。
    2.  **日历同步测试**:
        *   GCal 用户：双向同步测试（创建、修改、删除）。
        *   Outlook 用户：双向同步测试（基于 M365）。
    3.  **并发冲突测试**:
        *   两名用户同时尝试预订同一会议室同一时间段，验证第二人是否收到“冲突”提示。
*   **依赖**: Phase 2-5 完成。
*   **预期产出**: 《功能测试报告》，列出所有通过/失败的用例。
*   **验收方式**: 所有 P0/P1 级用例通过率 100%。

### Step 7.2: 性能与稳定性压测（轻量级）
*   **输入**: 模拟 30 人同时在线查询空闲时段。
*   **动作**:
    1.  使用 JMeter 或 k6 模拟 30 个并发请求查询未来一周的空闲会议室。
    2.  监控服务器 CPU/Memory 使用率。
    3.  确保平均响应时间 < 500ms。
*   **依赖**: Step 7.1 完成。
*   **预期产出**: 性能基准数据。
*   **验收方式**: 服务器资源占用低于 70%，无超时错误。

### Step 7.3: 用户培训与文档交付
*   **输入**: 最终系统 URL, 常见问题 FAQ。
*   **动作**:
    1.  编写《员工使用指南》（含如何安装 PWA, 如何绑定日历, 如何预订）。
    2.  编写《IT 运维手册》（含 Docker 重启命令, 备份恢复流程, 日志查看方法）。
    3.  召开 30 分钟线上培训会，演示操作流程。
*   **依赖**: Step 7.1 通过。
*   **预期产出**: 两份 PDF 文档 + 培训录屏。
*   **验收方式**: 随机抽取 5 名员工，能独立在 3 分钟内完成一次会议室预订。

---

## 8. 成本复核与最终报告

### Step 8.1: 实际支出核对
*   **输入**: 云厂商账单截图, 域名发票。
*   **动作**:
    1.  统计云服务器首年费用（预估 ¥1,500）。
    2.  统计域名首年费用（预估 ¥80）。
    3.  统计对象存储费用（预估 ¥50）。
    4.  合计显性成本。
*   **依赖**: Phase 1 完成后即可初步核算，正式报告在 Phase 6 后出具。
*   **预期产出**: 《实际成本明细表》。
*   **验收方式**: 总金额 ≤ ¥2,000（留有余地应对汇率波动或云厂商涨价）。

### Step 8.2: 输出最终选型与实施报告
*   **输入**: 阶段 02 报告, 阶段 03 所有步骤的执行结果, 测试报告, 成本表。
*   **动作**:
    1.  汇总推荐方案（Cal.com 自托管）的实施细节。
    2.  重申被淘汰方案（Resource Guru, BookRoom, 飞书/钉钉, 自研）的理由。
    3.  附上完整的成本