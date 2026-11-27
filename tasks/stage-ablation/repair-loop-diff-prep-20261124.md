# T-REPAIR-1 repair loop — Fix-A / Fix-B diff prep（2026-11-24 · subagent 只读核验）

> origin: ai · 任务：读 `experiments/stage-ablation/s5_state_machine.py`（分支 tmp-lit-snowball，1867 行），
> 核实设计文档 `repair-loop-design-20261124.md` 声称的两个结构性缺陷，备好可直接 apply 的最小 diff。
> **SM 本体零改动**：全程只读；`git status` 对该文件 clean（md5 44f6c4b59e9185f427579ceffa5289cc 前后一致）。
> 行号均为本次实际 grep/sed 核实的真实行号（设计文档提示 L821/L1450 均属实）。

## §1 缺陷核实

### (a) directed-fix 路径不可达 — **证实** ✅

**路由条件（实际代码，L764-765，`_rework` 内）**：
```python
764:            events = contra_idx.get(node.id, [])
765:            mode = "directed" if events else "angle"
```
`contra_idx` 只由 `self.contradiction_events` 中未 fixed 的事件构建（L752-756）。
即 **directed 的唯一入口 = 节点出现在 contradiction_events 里**。

**为什么结构性不可达（因果链，全部有行号）**：
1. contradiction_events 只由 `_scan_contradictions` 产生，而它**只扫 verified 节点**：
   `L865: ver = [n for n in self.nodes if n.status == "verified"]`（L866 还有 `len(ver)<4 → return`）。
   事件里的 a/b 在检出时刻都是 verified（L885-890 append）。
2. rework 候选池 = **本轮 verify 后 unverified 的新节点**：
   `L1450: unverified = [n for n in deduped if n.status != "verified"]` → `L1453: self._rework(unverified)`。
3. 节点一旦 verified 永不回退（status 置 verified 仅 L823/L847 两处，均单向）；
   进入本轮 rework 池的节点是本轮 decompose 新建的（`L1407: self.nodes.extend(deduped)`），
   从未 verified 过 → **不可能出现在任何 contradiction_events 里**（那些事件的成员在更早的轮次已是 verified）。
   每轮内顺序也是 VERIFY(L1442) → REWORK(L1453) → SCAN(L1459)，本轮 scan 产生的事件最早下一轮才可见，
   但下一轮的 rework 池又是下一轮的新节点 —— 永远错开。
4. ⇒ `events` 对 rework 池内任何节点恒为空 → `mode` 恒为 `"angle"` → directed 分支（L775-779）恒不可达。
   唯一 claim 写回点确实在 directed 分支内：`L821: node.claim = corr2 or corrected`
   （全文件唯一的 `node.claim =` 赋值，grep 确认；angle 路径 L846-850 只改 status/query/evidence，不改 claim）。

**经验佐证（本地 checkpoint 语料，非设计文档转述）**：
扫 247 份 `meta.json`（`checkpoints/` + `experiments/stage-ablation/checkpoints/` +
`modules/B-pipeline-ablation/data/q7-budget-scan/checkpoints/`），
共 16,726 条 rework_events：`mode` 分布 = {angle: 14,268, 无 mode 字段(旧 ckpt): 2,458}，**directed = 0**。
（设计文档/workshop §5 的 "0/8,870" 是 80-run 语料的 node-level 口径；本扫是 event-level，结论一致。）

**活体复核（2026-11-24 23:4x，正在跑的 719-r3，round 3 / 246 节点）**：
- 70 条 node-level rework 事件全部 `mode=angle`、`attempt=1`，directed=0 —— 缺陷 (a) 在活体 run 上再次确认；
- 4 条 contradiction_events 全部 `fixed=False`，涉事节点均为 verified（符合 L865 只扫 verified 的设计）；
- 排查"contradiction 涉事 degraded 节点为何没被 directed 救回"时发现 ckpt 树混入陈旧子树
  （见下口径注记），涉事节点实为 verified、从未 rework —— 无矛盾，故事闭合。

### (b) 单次尝试（rework_count 恒=1）— **证实** ✅

**pool 构造（实际代码，L1449-1453，run 主循环内）**：
```python
1449:            # ── J_verify → REWORK? ──
1450:            unverified = [n for n in deduped if n.status != "verified"]
1451:            if unverified and self._should_rework(deduped):
1452:                self.state = State.REWORK
1453:                self._rework(unverified)
```
pool 只含**本轮** `deduped`（本轮新建节点，`rework_count` 初始 0，L377）。
rework 失败 → `L784-785: if not ok and node.status != "verified": node.status = "degraded"`；
上界检查在 `L760-761: if node.rework_count >= self.cfg.max_rework: node.status = "degraded"`，
`max_rework: int = 2`（L119）。

**为什么 rework_count 恒=1**：上轮 rework 失败的节点终态 degraded，而下轮 pool = 下轮 deduped 新节点
（rework_count≡0），degraded 节点没有任何路径回到 pool ⇒ 每个节点最多被 rework 一次
⇒ `rework_count` 只能取 1，`max_rework=2` 从未被行使（上限是 pool 组成的结构性问题，不是参数）。
旁证：`L1475` 的轮次统计 `"reworked": sum(1 for n in deduped if n.rework_count > 0)` 也只数本轮 deduped。

**经验佐证**：同上 16,726 条事件中 `attempt` 分布 = {1: 14,268, 无字段: 2,458}，**无 attempt≥2**。

**补充核验（本次新算，checkpoint 语料，按 (run 目录, 节点 id) 去重）**：
- `degraded & rework_count=1` = 10,041 个（≈127/run，79 runs）= Fix-B 的跨轮重入候选池规模；
- `verified & rework_count=1` = 348 个 → 去重口径节点级修复率 = 348/(348+10041) = **3.35%**，
  与 workshop §5 的 3.7%（331/8870，80-run 终态口径）同量级互证，缺陷 (b) 量级坐实。
- 另有 `pending & rework_count=1` 1,000 个：rework 中途被 run 截断（预算/深度到顶）的节点，
  Fix-B 重入时会被 `_rework` 的 L760 上界检查正确处理（rc=1 < max_rework=2 → 可再试一次）。
- ⚠️ 口径注记：共享 ckpt 目录跨 rep 累积陈旧子树（实测 q7 scan：`sm-q7-r3` 树内 759 个
  node.json / 365 个 distinct id，243 个 id 重复——不同 rep 复用同 qid 同 rN 目录，旧子树不清理）。
  上表已按 (run 目录, id) 去重；**event 级统计不受影响**（meta.json 的 rework_events 是单进程
  累计，16,726 条 / directed=0 / attempt≡1 结论不变）。此陈旧子树是 harness 卫生问题，
  不影响 T-REPAIR-1 两缺陷判定，但跑 4 臂时应给每臂独立 ckpt 目录（SM_CKPT_DIR 已支持）。

## §2 Fix-A diff（directed 可达）

**改法一句话**：把路由条件从"仅正式 contradiction_events"推广为一条更一般的规则——
**节点失败 evidence 命中 value_mismatch 特征（来源存在但与 claim 冲突）时，同样路由 directed-fix，
对立方 = 节点自己检索到的来源**（与 `repair-closure-dryrun.py` 的分类正则、`rework_events.reason`
的 `evidence[:80]` 记录口径完全一致，保证 `mode==directed` 事件集 ≡ 下游 value_mismatch 人口；
no_source 不命中 → 保持 angle，4.0% 基线口径不变）。不新增状态机分支，只复用现有 directed 路径；
`_rework_directed` 里加一个 self_conflict 块构造分支是因为其块模板假设 a≠b 两个树内节点，
自冲突时 a==b 会生成退化块（两侧同一 evidence），不修则路径"可达但无效"。

```diff
--- a/experiments/stage-ablation/s5_state_machine.py
+++ b/experiments/stage-ablation/s5_state_machine.py
@@ -35,6 +35,14 @@
 if _SM_SEED >= 0:
     _random.seed(_SM_SEED)
 
+# Fix-A (T-REPAIR-1, 2026-11-24): value_mismatch 失败特征 —— 与
+# modules/B-pipeline-ablation/research/repair-closure-dryrun.py 的分类口径一致。
+# directed-fix 分支的路由条件: 有正式 contradiction_events, 或该特征命中节点失败
+# evidence → directed（对立方 = 节点自己检索到的来源）。此前只有正式 contradiction_events
+# 能触发 directed, 但矛盾扫描只扫 verified 节点而 rework 候选是本轮 unverified 节点
+# → directed 结构性不可达（语料 0 事件）。
+_RE_VALUE_MISMATCH = re.compile(r'不一致|不匹配|矛盾|虚构|版本不|数值.{0,6}不符|量级|mismatch|contradict', re.I)
+
 
 # ─────────────────────────────────────────────
 # 防泄漏
@@ -762,6 +770,16 @@
                 continue
             node.rework_count += 1
             events = contra_idx.get(node.id, [])
+            if not events and _RE_VALUE_MISMATCH.search((node.evidence or "")[:80]):
+                # Fix-A: value_mismatch（来源存在但与 claim 冲突）同样路由 directed-fix,
+                # 对立方 = 节点自己的检索来源。no_source（检索失败/无来源）不命中该
+                # 特征 → 保持 angle, 基线口径不变。
+                # 口径 = evidence[:80]: 与 rework_events.reason 记录口径（本函数下方
+                # 记录的 node.evidence[:80]）及 repair-closure-dryrun.py 分类器完全一致,
+                # 保证 mode==directed 的事件集 ≡ 下游 value_mismatch 人口。
+                events = [{"a": node.id, "b": node.id, "self_conflict": True,
+                           "a_claim": node.claim[:80], "b_claim": "来源侧",
+                           "desc": "核验失败: 来源内容与 claim 冲突 (value_mismatch)"}]
             mode = "directed" if events else "angle"
             self.rework_events.append({
                 "node_id": node.id,
@@ -798,11 +816,21 @@
             if not other:
                 continue
             a_node = by_id.get(ev["a"])
-            blocks.append(
-                f"节点A {ev['a']}: {ev['a_claim']}\n  evidence: {(a_node.evidence[:200] if a_node else '（缺失）')}\n"
-                f"节点B {ev['b']}: {ev['b_claim']}\n  evidence: {other.evidence[:200]}\n"
-                f"矛盾描述: {ev['desc']}"
-            )
+            if ev.get("self_conflict"):
+                # Fix-A 自冲突: 对立方是节点自己的检索来源, 不是树内另一节点
+                _srcs = node.retrieval_sources or []
+                src_txt = "; ".join(str(s.get("title") or s.get("url") or "")[:60] for s in _srcs[:5])
+                blocks.append(
+                    f"claim侧 {ev['a']}: {ev['a_claim']}\n  evidence: {node.evidence[:200]}\n"
+                    f"来源侧（实际检索到的来源）: {src_txt or '（无来源）'}\n"
+                    f"矛盾描述: {ev['desc']}"
+                )
+            else:
+                blocks.append(
+                    f"节点A {ev['a']}: {ev['a_claim']}\n  evidence: {(a_node.evidence[:200] if a_node else '（缺失）')}\n"
+                    f"节点B {ev['b']}: {ev['b_claim']}\n  evidence: {other.evidence[:200]}\n"
+                    f"矛盾描述: {ev['desc']}"
+                )
         prompt = prompts.contradiction_adjudication_prompt(blocks, node.id, node.claim)
         out, _ = _cll(prompt, max_tokens=1500, temperature=0.0, retries=2)
         d = _extract_json(out or "") or {}
```

**已知边界（不扩 scope，记录备查）**：
- **预期触发规模（P-A 功效依据，本次新算）**：对本地语料 14,511 条 node-level rework 事件的
  reason（= rework 前 evidence[:80]，与 Fix-A 路由输入同构）用同一正则模拟分类：
  value_mismatch 1,467（**10.1%**，= Fix-A 将路由 directed 的事件）/ no_source 4,691（32.3%）/
  other 8,353（57.6%）。与 dry-run 80-run 语料的 8.7%（932/10,702）同量级，路由条件校准合理。
  按 Q6 budget=300 每 run ~50-150 条 node-level rework 事件估，directed 事件 ≈ 5-15/run，
  n=3 共 ~15-45 个 directed 样本——对 2.4% 基线做功效检验偏紧（judge 噪声 ~0.1），
  若 P-A 判"无效"需按设计文档 §验收走等效性检验而非"不显著"。
- **逐事件严格一致性核验（2026-11-25 00:05，闭合上条"同量级"的模糊表述）**：
  ① 正则字节级相同——dry-run `RE_VALUE_MISMATCH` 与 Fix-A `_RE_VALUE_MISMATCH` 字面量
  逐字符相等（`不一致|不匹配|矛盾|虚构|版本不|数值.{0,6}不符|量级|mismatch|contradict`），均 re.I；
  ② 输入同一字符串——SM L771 记录 `"reason": node.evidence[:80]`（路由 L765 之后、rework
  LLM 调用之前，无中间改写），全语料 14,511 节点级事件中 reason 长度 >80 的为 0，
  即 reason ≡ 路由时刻的 evidence[:80]；
  ③ 逐事件零偏差——对全部 14,511 事件：`RE_VM.search(reason[:80])` 命中 ⟺ dry-run
  classify(reason)=='value_mismatch'，不一致数 = **0**。
  结论：Fix-A 的 directed 事件集 ≡ 下游 value_mismatch 人口（构造上成立，非近似）。
- **口径重叠注记（P-A 解释用，本次新算）**：1,467 条 directed 路由中 169 条（11.5%）
  同时命中 no_source 正则（"数值量级缺乏来源支持"这类含冲突词又含缺源词的 evidence）。
  这不是误伤——dry-run 分类器口径本就是"VM 先、NS 后"（repair-closure-dryrun.py L25-26
  注释），这 169 条在该口径下归 value_mismatch，diff 路由与之一致（mode==directed ≡
  dry-run VM 人口，基线 2.4% 也是同一人口，对比公平）。但语义上这部分更接近缺源失败，
  directed 裁决可能产不出 corrected_claim（→ False → degraded，多耗一次 LLM 调用）。
  分析时注意：directed 修复率的分母含这 11.5% 语义稀释；**不建议**为此加"NOT NS"排除条件
  （会偏离 dry-run 口径、破坏基线可比性、且违反最小改动原则）。
- self_conflict 事件是临时的（不 append 进 `contradiction_events`）→ 不污染 D35 decompose 反馈块（L532-533）
  与 contradiction 度量；成功时 L826-827 的 `ev["fixed"]=True` 只作用于临时 dict，无副作用。
- 成本：value_mismatch 占比 ~8.7%（932/10,702，dry-run 口径）的 rework 事件改走 directed（max_tokens 1500 vs angle 800）。
- 裁决 prompt 文案说"两个已核验节点互相矛盾"，self_conflict 块头是 claim侧/来源侧 —— 措辞轻微不匹配，功能不受影响（未改 prompts.py，保单文件 diff）。
- **self_conflict 块运行时安全（2026-11-25 00:35 核验）**：块内引用 `node.retrieval_sources`
  （diff L47）——该字段确为 NodeRecord 成员（L382 `default_factory=list`，L622 填充，
  元素为 `{url,type,title}` dict，与 `s.get("title") or s.get("url")` 取值匹配）→ 无
  AttributeError 风险；空列表时 `src_txt or '（无来源）'` 兜底。
- **hunk 3 变量作用域 + 事件流自洽（2026-11-25 00:40 核验）**：hunk 3 在 `_rework_directed`
  （L790 `def _rework_directed(self, node, events)`）的 blocks 循环内，`node` 是方法参数 →
  作用域内必然可用，无 NameError。self_conflict 事件构造为 `a==b==node.id` → 循环里
  `other_id=ev["b"]=node.id`、`other=by_id.get(node.id)`=节点自身（非 None）→ 通过
  `if not other: continue` 守卫进入 self_conflict 分支，`node.evidence`/`node.retrieval_sources`
  取值自洽。整条 directed 路径（hunk 2 构造事件 → hunk 3 建块 → L806 裁决 prompt →
  L814 重搜重验 → L820-827 成功回写）无未定义变量/None 引用。

## §3 Fix-B diff（re-entry）

**改法一句话**：pool 构造处把"上轮 rework 失败节点"（终态 `degraded` 且 `0 < rework_count < max_rework`）
并入本轮 pool，使 reworked 节点可跨轮重入；已耗尽（rework_count 达 max_rework=2）的节点不再重入，
上界仍由既有 L760 检查兜底 —— 净效果 = 每个节点最多 2 次尝试，正好行使 `max_rework=2` 的语义。
gate `_should_rework(deduped)` 保持只判本轮批次（最小改动，不动 gate 语义）。

```diff
--- a/experiments/stage-ablation/s5_state_machine.py
+++ b/experiments/stage-ablation/s5_state_machine.py
@@ -1448,6 +1476,14 @@
 
             # ── J_verify → REWORK? ──
             unverified = [n for n in deduped if n.status != "verified"]
+            # Fix-B (T-REPAIR-1, 2026-11-24): 上轮 rework 失败的节点并入本轮 pool,
+            # 使 reworked 节点可跨轮重入。上轮 rework 失败以 status=degraded +
+            # rework_count>0 终态（见 _rework 失败分支）；此前 pool 只含本轮 deduped
+            # 新节点（rework_count≡0）→ rework_count≡1, max_rework=2 从未行使。
+            # 上界 = max_rework: 已耗尽的节点不再重入。
+            unverified = unverified + [n for n in self.nodes
+                                       if 0 < n.rework_count < self.cfg.max_rework
+                                       and n.status == "degraded"]
             if unverified and self._should_rework(deduped):
                 self.state = State.REWORK
                 self._rework(unverified)
```

**已知边界**：重入节点要等"本轮新批次也触发 rework gate"才会被重入（gate 只判 deduped）——
这是保留既有 gate 的最小改法；若后续想让重入独立于本轮 gate，需另改 gate（不在本 diff 范围）。
重入成功 → verified（L823/L847）；第二次失败 → degraded 且 rework_count=2 → 被
`0 < n.rework_count < max_rework` 排除，永久退出 pool。✓
另：contribution-filter 剪掉的节点（L1231 `p.status = "degraded"`）rework_count=0，
不满足 `rc>0` 条件 → 不进重入池，剪枝语义保持不变（只有"rework 过且失败"的节点才重入）。

**gate 语义正确性 + 搭便车延迟 + resume 跨 run 边缘（2026-11-25 00:30 新验证，闭合 §3 三条隐含假设）**：
- **gate 为何不能改判 `unverified`**（否则破坏基线可比性）：`_should_rework(batch)` =
  `verified/len(batch) < 0.85`（L730-734，verify_threshold=0.85）。`unverified` 按构造全非
  verified → rate≡0 → 恒 True → 每轮只要有失败就 rework，比基线激进得多。故 gate 必须留在
  `deduped`（当前 diff 正确），re-entered 节点是"搭便车者"：仅当本轮 gate 触发时才被 rework。
- **搭便车延迟量化**（实证）：251 个 run 的 meta 中 **100% 含 ≥1 条 node-level rework 事件**
  （median 37/run, mean 58, max 345）→ gate（verified_rate<0.85）在几乎所有 run 里触发，
  重入延迟 ≤1-2 轮，**不是瓶颈**（worst case：某 run 连续几轮全 good 才推迟，但语料未见）。
- **crash-resume 边缘**（关键正确性）：pool merge 扫 `self.nodes`（非 `deduped`）。resume 路径
  （L1719-1720）把同一 run 中断前的节点全量恢复进 `self.nodes`（含 rc=1 的 degraded 节点），
  L1734 重载 `rework_events` → 崩溃续跑后这些节点仍会被 merge 捕获并重入。✓ 若 merge 只扫
  `deduped` 则会漏掉"中断前已失败、续跑后应重试"的节点（本 diff 用 `self.nodes` 规避该坑）。
- **无重叠/无双重重入**：本轮 `deduped` 节点创建时 rc=0，`_verify_batch` 不改 rc，`_rework` 在
  pool 构造之后才调用 → 本轮内 deduped 节点 rc≡0，不满足 `0<rc` → 与 merge 列表零重叠；
  跨轮失败节点 rc=1 不在本轮 deduped → 只进 merge 列表。每轮每节点至多重入 1 次。✓
**A×B 交互量化（P-A+B 判别用，本次新算）**：Fix-B 重入候选（degraded rc=1）10,041 个中
1,089 个（10.8%）evidence 命中 VM 正则 —— A+B 组合下这些节点第 1 轮 directed 失败后
第 2 轮重入时**再次路由 directed**（evidence 未变仍命中），消耗 2 次 directed 尝试。
机制含义：A+B 臂的 directed 调用量 ≈ A 臂的 ~2 倍（针对这 10.8% 子群），
若第 2 次 directed 成功率与第 1 次相近 → 该子群修复率近可加（~2×p）；
若 evidence 已暴露"裁决无解"（如来源本身矛盾）→ 亚可加。这是 P-A+B 判别
（可加/亚可加/超可加）的预期行为基准，分析时按"重入节点 evidence 是否命中 VM"
分组看修复率即可分离交互项。

## §4 ready-to-apply 判定

**结论：两个 diff 均 ready-to-apply，相互无依赖、无冲突。**

验证记录（本机实际执行，SM 本体未被触碰，均在 scratch 副本上验证）：
| 检查 | 结果 |
|---|---|
| 组合 diff `git apply --check`（对 HEAD 工作树） | ✅ OK |
| 组合 diff 反向 `git apply -R`（回滚路径） | ✅ OK |
| 组合 diff 应用后 `python3 -m py_compile` | ✅ OK |
| Fix-A 单独 `git apply --check` + 应用后 py_compile | ✅ OK |
| Fix-B 单独 `git apply --check` + 应用后 py_compile | ✅ OK |
| 顺序 A→B（scratch 副本） | ✅ OK（区域不相交：A 在 L34-40/L764-772/L800-805 区，B 在 L1449-1453 区） |
| **运行时冒烟测试（2026-11-25 00:47，mock LLM/检索/核验，真实字节码端到端）** | ✅ 6/6 断言通过 |

**运行时冒烟测试明细**（scratch 副本 apply 组合 diff 后 import 真实 SM，mock
`ablation_harness.call_llm` / `search_node` / `verify_node`，脚本
`~/.hermes/cache/scratch/repair_smoke_test.py` 可复跑）：
1. Fix-A 路由触发：无正式 contradiction_events 的失败节点（evidence 含"不一致/版本不匹配"）
   → 第 1 次 rework `mode=directed`（原始 SM 同场景 = `angle`，A/B 对照证实路由差异确由 Fix-A 引起）
2. 失败终态：directed 失败 → `degraded` + `rework_count=1`
3. Fix-B 重入：pool merge 表达式捞到该 degraded rc=1 节点
4. 第 2 次尝试：`attempt=2`（max_rework=2 首次在真实字节码上被行使）+ directed 成功
   → `verified` + claim 回写（3.35TB/s → 900GB/s）
5. 上界兜底：rc=2 达 max_rework 后第 3 次拒绝重入（L760 检查生效，rc 保持 2）
6. self_conflict 块无运行时异常（hunk 3 的 `node`/`node.retrieval_sources` 取值自洽，
   第 1/4 项的 directed 调用全程走过 hunk 3 建块路径）

- **依赖**：A、B 正交（路由条件 vs pool 组成），可单独 apply 也可组合；2×2 四臂实验直接对应
  baseline / A / B / A+B。
- **冲突**：无。所有锚点在文件中唯一（grep -c 逐一确认）。
- **应用方式**：repo 根 `/Users/a1-6/Desktop/workspace/pfb` 下
  `git apply experiments/stage-ablation/tasks/repair-loop-fix-a.diff`（同理 fix-b / combined）。
- **时序硬约束（设计文档 §时序）**：必须等 T-PR-17 pilot 完成、确认 SM 不再被 import 后才 apply
  （r3 队列也在 import SM，双重冻结）；apply 前先 `git commit` 留回滚点。
- **队列实时状态（2026-11-24 23:45 观测）**：q7-budget-scan 队列 14/15 完成，仅剩
  719-r3（PID 16780，22:35 起，round 3 / 246 节点，budget=719 未饱和，按 719-r1/r2 的
  6,843/7,982s wall 估 ~1-2.2h 内完成）；其后 waiter（PID 88305）自动串行启 9-cell pilot
  （3 臂 × n=3，每 cell resume r3 ckpt 跑到 budget 719，fail-fast）。
  ⇒ SM 冻结预计持续到明日白天；解冻判据 = `grep 'PILOT COMPLETE'
  modules/B-pipeline-ablation/data/tpr17/tpr17-pilot-report-*.md`（**只 grep report 文件，
  勿 grep 整个目录**——2026-11-25 00:48 发现 `tpr17-morning-runbook.md` 正文含
  "PILOT COMPLETE" 字样（描述触发条件），全目录 grep 会误判已解冻；waiter 实际把
  `PILOT COMPLETE — 9/9 cells` 写入 `$REP=tpr17-pilot-report-$(date +%Y%m%d-%H%M%S).md`，
  见 tpr17-pilot-waiter.sh L11/L65）+ `ps` 无 s5_state_machine 进程。
- **应用后核验建议**：跑 1 轮 Q6 冒烟，看日志出现 `[SM] rework-directed`（Fix-A 生效）
  与 `attempt: 2` 的 rework_events（Fix-B 生效）；对照 `rework_events.mode` 分布 directed>0。
- **⚠️ 4 臂执行序列（析因成立的前提，设计文档"应用 Fix-A/B → 跑 4 臂"的字面序有缺陷）**：
  2×2 的 **baseline 臂必须跑未修改的 SM**，若先 apply 再跑 4 臂，baseline 会跑在已修补的
  SM 上 → 析因作废。正确序列（每臂独立 `SM_CKPT_DIR`，防陈旧子树污染，见 §1 口径注记）：
  1. `git commit`（留回滚点，此时 SM 仍为原始版）→ 记录 commit hash `H0`
  2. 跑 **baseline**（SM=H0，Q6，budget=300，n=3，`SM_CKPT_DIR=.../arms/baseline`）
  3. `git apply tasks/repair-loop-fix-a.diff` + commit（`H_A`）→ 跑 **A 臂**（独立 ckpt 目录）
  4. `git apply tasks/repair-loop-fix-b.diff` + commit（`H_AB`）→ 跑 **A+B 臂**
  5. `git apply -R tasks/repair-loop-fix-a.diff` + commit（回到 `H_B`，只含 B）→ 跑 **B 臂**
     （反向 apply 已验证可回滚；每步 commit 留痕，任意臂可 `git checkout` 复现）
     **反向序列无残留已严格验证**（临时 git repo 模拟，2026-11-24 23:5x）：
     H_B = (H_AB `git apply -R fix-a`) 与 (H0 直接 `git apply fix-b`) **md5 逐字节相同**
     （a25a39e325c1c5971241cf49232256d6），且 H_B 态 Fix-B marker=1 / Fix-A marker=0 /
     py_compile OK —— 反向 apply 无 hunk 残留，4 臂序列可行。
  注：臂间顺序无关（各臂独立 ckpt 目录 + 独立 seed 约定），但**每臂的 SM 版本必须如上固定**；
  4 臂同 budget=300 / Q6（`bench/questions/Q6-network-arch.txt`，已确认存在）/ 同 seed。

**落盘文件**：
- 本文档：`experiments/stage-ablation/tasks/repair-loop-diff-prep-20261124.md`
- 可直接 apply 的 diff（从本文档机械生成并经上述验证）：
  `tasks/repair-loop-fix-a.diff` / `tasks/repair-loop-fix-b.diff` / `tasks/repair-loop-fixes-combined.diff`
- **回滚点 commit**：`a769da809`（tmp-lit-snowball，2026-11-24 23:59，含上述 5 文件；
  SM 本体未含在内——apply 前的 SM 状态 = 该 commit 的 `experiments/stage-ablation/s5_state_machine.py`，
  任意臂失败可 `git checkout a769da809 -- <file>` 或 `git revert` 恢复）。
