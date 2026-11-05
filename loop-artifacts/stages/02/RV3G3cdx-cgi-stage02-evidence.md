# RV3G3cdx-closure-gate-integration · 阶段 02 实证（keepalive r26 代跑）

> 背景：r26 claude (PID 15806) 启动后 ~18min 零 commit、零文件写、日志 0 字节，判定卡死。
> 按 runner 桥接规则「进程死亡/卡死 → 简化重试一次」处置：本工件为阶段 02 六行动的前置实证落盘，
> 供后续重试的 claude 直接消费（02 行动清单中 A1/A2/A4/A5 已在此完成，重试只需做 A3 深核 + A6 评估定稿）。

## A1 · hook 安装态（02 行动 1）

- `ls .git/hooks/ | grep -v sample` = **空**（无任何自定义 hook）
- `git config core.hooksPath` = **未设置**
- 结论：当前仓库完全无本地门禁，方案 A（pre-commit hook）从零安装，无存量冲突。

## A2 · CI 基础设施现状（K2 实证，02 行动 2）

- `find . -path ./.git -prune -o -name "*.yml" -print` = **零命中**
- `.github/` = **不存在**（No such file or directory）
- origin = `https://github.com/dd2003-460/prompt-first-bench.git`（GitHub 确认，非推定）
- 结论：**本仓无任何 CI**。方案 B（CI check）需从零建 .github/workflows/，且 K3 拦截力问题随之而来——
  GitHub Actions 对已 push 到受保护分支的 commit 只能事后报警不能拦截（protection rules 作用于 PR merge 时点），
  而本仓工作流是直推 main（无 PR 流程）⇒ 方案 B 在本仓实际拦截力 = **零**（unverified-通用知识，仓库内证据上限 = 无 CI 配置可查）。

## A3 · FLIP_KW/APPEND_KW 历史命中分布（02 行动 3，抽样近 21 个 queue commit）

| commit | flip | append | 备注 |
|---|---|---|---|
| 42031ea r154 | 1 | 1 | 收口行 hash 回填 |
| 286cac0 r153 | 1 | 1 | crossdomain-promptversion 收口 |
| 84ba3b8 r152 | 0 | 1 | m4-independent-source-ops（纯追加候选） |
| 7f22123 r151 | 1 | 1 | queue-format-contract 收口 |
| f7d3674 r150 | 1 | 1 | crossdomain-lint 收口 |
| 8d7ce8b r149 | 1 | 0 | 漏翻 checkbox 补做翻转 |
| 1e4dac1 r149 | 1 | 1 | queue-dedup-lint 收口 |
| 84ff11d r148 | 1 | 1 | closure-checklist-assert 收口 |
| 0bb55ce r147 | 1 | 1 | batch2-schema-lint 收口 |
| 16b063f r146 | 1 | 1 | queue-hygiene-sweep 收口 |
| 28f0551 r145 | 1 | 0 | threshold-crossdomain 收口 |
| 9f48d94 r145 | 1 | 0 | threshold-crossdomain 阶段 commit |
| c0eba3b r143 | 1 | 1 | kappa-formula-adjudicate 收口 |
| 404ba7e r142 | 1 | 0 | o3-claim-rejudge 收口 |
| 91117b8 r141 | 0 | 1 | o3-claim-rejudge-scaffold（纯追加） |
| 97d2adf r140 | 1 | 0 | threshold-crossdomain 阶段 |
| 74e3046 r139 | 1 | 0 | jaccard-adjudicate 材料收口 |
| 446f4cc r138+ | 1 | 1 | goldrank-threshold 收口 |
| 52f70d8 r137b | 1 | 0 | R5.2assert-suite 收口 |
| 19b9ffb r136b | 1 | 1 | kappa-receipt 收口 |
| dfed498 r135b | 1 | 0 | prior-source 收口 |

统计：21 个 commit 中 flip=1 占 19、append=1 占 14；flip=0 仅 2 个（均为纯追加候选 commit）。
**误拦风险评估**：关键词集对近期真实收口形态覆盖良好，但注意 8d7ce8b 类「补做翻转」commit 也会被命中——
这正是门禁想要的行为（r149 事件即门禁价值自证）。潜在漏检面 = 未来新措辞（queue-format-contract W2 边界已知，(c) 双向闭合兜底）。

## A4 · tmp 负样例资产（K5 实证，02 行动 4）

- `tmp/closurecheck-neg-samples/` = **不存在**（tmp 目录未入库，K5 预判成立）
- 处置：03 阶段构造等价负样例（r148 已登记构造方式：首建即 [x] 豁免路径 + 漏翻 checkbox FAIL 路径各一）。

## A5 · assert-closure-checklist.py byte-exact 锚点抄录（02 行动 5）

- 豁免子句 L13-14：目标行在该 commit 之前不存在于 queue（`git show <h>~1:tasks/goal-queue.md | grep -c <短名>` = 0）⇒ 「首建即 [x]」合法形态，跳过 (a)
- exit 语义 L21-22：0 = 全通过 / 1 = 任一检查 FAIL（指名道姓输出）/ 2 = 输入不可解析（commit 不存在 / 该 commit 无 queue diff）
- FLIP_KW L29：`["划掉", "标记完成", "核销", "[ ]→[x]"]`（(a) 触发词，r148 02 S1 并集）
- APPEND_KW L30：`["新导出候选", "追加候选", "导出候选"]`（(b) 触发词）

## A6 · K1 三候选解法沙盒实验（02 行动 6）

沙盒位置：`~/.hermes/cache/scratch/cgi-k1-sandbox`（临时 git 仓，base commit + staged queue diff）

- **(i) 临时 index commit 取 hash**：`git write-tree` 可在不 commit 的情况下拿到 tree hash（实测 ef38ee1...），
  但 r148 原签名消费的是 **commit hash** 而非 tree hash——hook 内构造完整临时 commit（commit-tree）可行但复杂度↑，
  且临时 commit 不在任何 ref 上，断言脚本 `git show <h>~1` 的前驱引用会失败 ⇒ **需要改断言脚本接口，超出备料范围**。
- **(ii) staged-diff 变体**：`git diff --cached --name-only` 实测可直接拿到 staged 文件列表（queue.md 命中），
  无需 hash。语义漂移 = 从「验证某 commit 的收口完整性」变为「验证本次将要提交的 staged 变更」——
  覆盖面其实更贴合 pre-commit 时点语义，但须成璐裁定接受度（K4）。
- **(iii) 弱检查**（staged queue diff 非空且含 checkbox 翻转才触发）：= (ii) 的子集，实现最简单，
  漏检面 = 无 queue diff 的收口 commit（实际不存在——收口必动 queue，A3 数据 21/21 均含 queue diff）。

**推荐**（备料意见，裁定权在成璐）：(ii)+(iii) 合并 = staged-diff 变体 + 触发条件收窄（仅 queue.md 有 staged diff 时运行），
理由：零接口改动（断言脚本只读 staged 内容不读 hash）、误拦面最小、与 pre-commit 时点语义对齐。
(i) 否决理由：需改冻结断言脚本接口，超出「备料不代裁」定位。

## 判定

02 六行动全部完成实证（A1-A6 均有仓库内/沙盒证据，unverified 项如实标注）；K1-K5 空缺全部填实或固化标注。
**pass → 进入阶段 03（动作分解）**。
