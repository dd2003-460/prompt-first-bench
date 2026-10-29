# Goal: R5.2-sourcepath-hardening — assert-packet-symmetry.py source_path 强制完整相对路径

> 创建：2026-10-30 · ralph loop runner（goal-queue 新导出候选，R5.2 04.5 W1 登记）
> 依据：`loop-artifacts/stages/04.5/R5.2-review.md` W1 + `tasks/goal-queue.md` 候选行

## 【目标】
`r5/assert-packet-symmetry.py` 的 `file_reachable()` 现有 basename glob 兜底（L92-96）：当 source_path 中的路径 token 在已知 base 下 join 不到时，退化为"该文件名出现在 WS/PFB 任意目录即算可达"——run1/run2/run3 各有同名 execution-log.md / loop-state.json，兜底可能把指向 run1 的路径误判为 run2 的文件满足。本 goal 交付：
1. **去掉 basename glob 兜底**：source_path 必须给出可在已知 base（WS / PFB / workspace 根）下直接 join 命中的完整相对路径；命中不了 = FAIL（不再静默降级到 glob）。
2. **packet v2 的 source_path 字段规范化**（若存在触发兜底的条目）：改成完整相对路径形式，使脚本在严格模式下全绿。
3. 重跑脚本 → exit 0，PASS 数不降（67 或等量），FAIL=0。

## 【阶段】
bench 度量基础设施加固（R5.2 的 W1 收口）。前置事实已定：packet v2 已交付且对称性断言 67/0 通过（r102, baff4b3）；本 goal 只改断言脚本的可达性判定逻辑 + 必要的 source_path 文本规范化，不改任何字段值与分数。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `bench/self-opt-tester/r5/assert-packet-symmetry.py`（**改造对象**，尤其 file_reachable L72-97）
- `bench/self-opt-tester/r5/evidence-packet-r4-v2.json`（source_path 字段承载面）
- `bench/self-opt-tester/bench.md`（R5.2 节，追加 hardening 结果）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `R5.2hard-*`
2. 01：定位所有当前依赖 glob 兜底才通过的 source_path 条目（先跑一个诊断版列出哪些 check 走了兜底分支）
3. 02：web-llm 强制步骤执行并留回执（预期三 provider 仍 error → 记录失败继续）
4. 02.5：矛盾/风险登记（如某 source_path 确实无法规范化为完整路径 → 处置方式裁决）+ 对抗核验停止理由
5. 03：每步标 owner=user/agent
6. 04：脚本改造落盘 + packet v2 source_path 规范化（如需）+ 重跑 exit 0 且 PASS 数 ≥ 原 67（严格化不应减少有效检查）
7. 04.5：反方复核 verdict + repair_stage
8. bench.md R5.2 节追加 hardening 一句话结果
9. commit + push 分支 `ralph/r5.2-sourcepath-hardening` + ls-remote 验证

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续本地证据提取，不阻塞
- 某 source_path 无法规范化（原始证据只在 git 对象库、无工作树路径）→ 保留其 "commit <hash>:<path>" 形式（git show 可达性检查本就独立于 glob），不算违规；仅禁止"裸 basename 靠 glob 命中"的路径
- 严格化导致某条原本 PASS 的检查 FAIL 且无法规范化 → 回退该条为显式豁免清单（脚本内 EXEMPT 列表 + 注释原因），不得静默恢复 glob 兜底