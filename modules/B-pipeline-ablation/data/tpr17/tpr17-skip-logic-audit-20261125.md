# T-PR-17 resume skip-logic 审计（2026-11-25 04:13）

**审计问题**：`tpr17-pilot-resume.sh` 的 skip 判据会不会有 q7 那种 cp-copy 假成功缺陷（旧文件被当成功跳过，实则没真跑）？

## 方法
1. 读脚本 skip 逻辑（`tpr17-pilot-resume.sh` L36-77）
2. 核查被 skip 的 cell json（`canonical_r3_r1.json`）
3. grep 脚本 + runner 有无 `cp`/文件复制逻辑（q7 假成功根源）
4. 核查 seed / 采样参数（rep 独立性）

## 发现
1. **skip 判据健全**：文件存在 + `n_nodes>=CKPT_FLOOR(381)` + `n_llm_calls>=MIN_LLM(50)`，且跑前跑后双重校验（L41-48 跑前、L58-65 跑后）。非退化才 skip。
2. **无 cp-copy 文件逻辑**：脚本无 `cp`；runner 的 `import copy`（L20）是 Python 对象浅拷贝，非文件复制。→ **无 q7 式假成功路径**。
3. **被 skip 的 canonical r1 是真成功**：`n_nodes=719`(=budget 719，跑满)、`n_llm_calls=86`、`ts=2026-11-25T03:15:45`、mtime=03:15（ts/mtime 一致，非陈旧文件）、`final_state=rework`。文件 ts(03:15) 早于 resume 启动(03:37)，是被正确跳过的既有成功。
4. **rep 独立性成立**：`rng = random.Random(f"{seed}:{rep}")`（runner L201，复合种子）→ 同 seed 不同 rep 独立 shuffle 流；主生成 `temperature=0.7, top_p=0.95`（s5 L462/557/1579，随机采样）→ rep 间方差真实，n≥3 的 CI 有效。
5. **`final_state=rework` 非失败**：是状态机在跑满 budget(719 节点)时的终止态，非提前崩溃。n_nodes=budget 是关键信号=跑满。

## 判决
**skip 逻辑健全，无 cp-copy 缺陷，被 skip 的 cell 是真成功。pilot resume 可信。**
residual：无阻塞项。pilot 运行中（PID 53387），vLLM 200，1 SKIP / 0 FAIL，canonical r2 执行中。
