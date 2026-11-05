# RV3G3cdx-closure-gate-integration · 阶段 04.5 反方复核（r27）

> 反方视角：不重开研究，只攻击链条。对照 current-goal 五字段验收标准 ×5 + 禁区 ×3 + 阶段 01-04 全链。

## 八攻击

**A-1 「materials §2 方案 B 拦截力零是通用知识不是实证」——部分成立，已如实标注。**
仓库内证据上限 = 无 CI 配置可查（find *.yml 零命中 + .github 不存在），远端行为（protection rules 作用于 PR merge 时点）为 unverified 通用知识。§2 维度 1/4 与 §6.4 均已标 unverified + 证据上限声明，未虚构。残余风险：若成璐实际配过 branch protection 而本仓证据看不到（远端状态不可查），结论需修正——已在 §6.4 声明「无远端实测」。

**A-2 「staged 原型 exit 1 不可达 = 门禁形同虚设，备料误导裁定」——驳回（边界已显式声明）。**
04 执行记录 + materials §3.1 降级声明 + APPROVALS 条目第 4 点三处同源声明：staged 轨 = SIGNAL 提示形态（少拦不误拦的 fail-safe 方向），硬拦能力在 r148 手动工具轨（既有负样例 f8acff9/cc168bd 实跑 exit 1 指名道姓可查）。K4 O1-O4 选项把该边界作为显式裁定输入而非隐藏前提——成璐若要求 hook 硬拦，O3/新约定路径已预写。非误导，是把固有缺口摆上桌面。

**A-3 「hook 原型 (a) 检测逻辑有 bug：grep -qF "- [x] NAME " 尾部空格依赖行格式」——部分成立，登记不修。**
queue 行格式 `- [x] NAME | ...` 中短名后恒有空格+pipe（queue-format-contract C 条款五段式），尾空格匹配在当前 queue 形态下成立；但若未来出现 `- [x] NAME` 行尾直接结束（无后续段）则 miss。miss 方向 = 漏识别翻转 ⇒ 落 SIGNAL 分支（多提示，不误拦）⇒ fail-safe 方向安全。登记为 W1（同 r148 W1 `[~]` 形态边界同族），修复属执行 goal 范围。

**A-4 「豁免子句 staged 对应式用 HEAD 取代 <h>~1 是语义变更」——驳回。**
pre-commit 时点「本次 commit 的前驱」= HEAD，逐字等价替换非口径变更；且仅影响 (a) 豁免判定（白名单侧），(b)(c) 不受影响。materials §3.3 第 2 条已写明「HEAD 取代 <h>~1 是 staged 时点的自然对应，非语义变更」。

**A-5 「B8 沙盒用例太弱：N1 用例其实没触发 message 声称检查，证明不了什么」——部分成立，已登记偏差。**
staged 轨本就不做 message 声称检查（message 不可得）——N1 用例验证的是「diff 侧漏翻形态能被识别并指名道姓报出」，这正是 staged 轨的全部承诺面。验收 #3 原文要求「负样例 exit 1 拦截指名道姓」由手动工具轨满足（r148 既有实证），04 记录已逐项拆解双轨归属，未包装成单轨达标。

**A-6 「commit 落在 main 违反 runner 协议『开新分支干活』」——成立，已处置。**
会话启动时 HEAD 已在 main（环境漂移，非本轮动作）；stage 04 commit f6be883 落于 main，随后 `git branch -f ralph/closure-gate-integration-r27 f6be883` 使目标分支指向同一 commit（分支关系正确：main ⊇ 分支 tip）。按 CONTINUE_MSG P0 指令「不 merge main——Hermes 验证后 merge」，本轮不 push、不宣告收口；main 上的 f6be883 待 Hermes 验证后随分支一并处理（内容幂等，无重复 merge 风险）。

**A-7 「APPROVALS 条目说『无已执行操作』但实际改了 4 个文件，自相矛盾」——驳回（措辞精确）。**
「无已执行操作」指无**待裁定的不可逆操作**被执行（门禁未激活 = 核心待裁动作未动）；4 文件全部为纯新增/追加（备料件），影响面声明段已逐一列明。APPROVALS 队列语义 = 待裁定项登记，非变更日志。

**A-8 「十五脚本基线序列里 closure-checklist=2 / kappa-receipt=1 被混进『零漂移』叙事」——驳回（已区分）。**
04 记录明确标注：closure-checklist 的 2 = 无参调用 usage 路径（非异常）、kappa-receipt 的 1 = ablation 面常态 FAIL 基线（r148 起既有）。两者均为装前基线值，hook 未激活 ⇒ 无装后差异可言，D4 留给执行 goal。未把既有非零 exit 包装成「全绿」。

## verdict

**pass**。链条完整（01 F1-F6/K1-K5 → 02 A1-A6 → 03 B1-B9 → 04 全动作 + 04.5），验收标准 5/5 有对应证据（#3 的双轨拆解如实登记偏差），禁区 3/3 复核通过（命令可验），unverified 项 2 处均标注。薄弱点 = A-3 W1 登记项 + A-1 远端状态不可查 + A-6 分支落点处置——均不阻塞备料交付性质。

**残余风险**：本 goal 终态 = blocked-on-human（成璐对 K4 O1-O4 + 方案选择裁定）。裁定前 queue L27 保持 `[ ]`；裁定后按 materials §5 D1-D6 开执行 goal（含 hook 激活 D3 + 装后基线复跑 D4 + 负样例持久化 D2）。

**最有价值下一步**：成璐勾选 K4 四选项（APPROVALS 条目已列全决策输入）；若选 O1/O2 则执行 goal 首动作 = D2 负样例持久化 + D3 激活 + D4 双基线对比。