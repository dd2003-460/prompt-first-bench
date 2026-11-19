# T53b 卡点清单 + 验证测试矩阵
# origin: ai
# 2026-11-20

## 1. 已发生的卡点（r04-r09 事故记录）

| Run | 卡点 | 根因 | 处置 | 状态 |
|-----|------|------|------|------|
| r04 | resume FileNotFoundError | SM os.chdir 后相对路径双重前缀 | 修 driver 传绝对路径 + 手动标 done | 已关 |
| r05 | 同上 | 同上 | 同上 | 已关 |
| r06 | SSL 握手卡死 | urlopen timeout 不覆盖 PySSL_select 内部 select | kill + 修 _probe_network | 已修 |
| r07 | 同上 | 同上（启动于修复前） | kill | 已修 |
| r08 | 同上 | 同上 | kill | 已修 |
| r09 | 同上 | 同上 | kill + r10 用新代码验证 | 已修 |

## 2. 所有可能的卡点（A-E 类）

### A 类：网络/SSL

| # | 卡点 | 根因 | 现有防护 | 残余风险 |
|---|------|------|---------|---------|
| A1 | SSL 握手卡死 | CPython PySSL_select 无 timeout，代理上游 TLS 握手中断时无限 poll | _probe_network guard（curl -m 8 硬超时，60s 缓存） | 低 |
| A2 | 代理上游完全不可达 | 198.18.1.104 断连 | KB 兜底（_LOCAL_CORPUS_DIRS 第一位） | 中（非 GPU query 降级到空） |
| A3 | 网络探测本身卡住 | curl 进程 hang | curl -m 8 + subprocess timeout=10 | 低 |

### B 类：进程/SM

| # | 卡点 | 根因 | 现有防护 | 残余风险 |
|---|------|------|---------|---------|
| B1 | SM 卡死（非 SSL） | LLM 响应超时/8787 挂/SM 内部死循环 | **无**（watchdog 只检测 batch 存活，不检测 SM 卡死） | **高** |
| B2 | 8787 vLLM 挂 | 容器 OOM/崩溃/上游断 | watchdog 每 60s 检测 8787 health | 中（检测后只 sleep 不重启 SM） |
| B3 | 双 SM 写冲突 | 多进程树并存（watchdog 误判 batch 死亡） | watchdog 清场 + PID 文件 + 二次确认 | 低 |
| B4 | SM FATAL 无 ckpt | 进度丢失，整轮白干 | driver resume 逻辑（最多 3 次） | 中 |

### C 类：记账/状态

| # | 卡点 | 根因 | 现有防护 | 残余风险 |
|---|------|------|---------|---------|
| C1 | resume 路径错误 | SM os.chdir 后相对路径双重前缀 | driver 传绝对路径（已修） | 低 |
| C2 | 502 burst 误标 done | cc-state 污染（网络抖动时误判完成） | 手动回滚 | 中 |
| C3 | cc-state.json 损坏 | 写中断/并发写 | 无 | 中 |
| C4 | 记账脚本出错 | python 异常（judge 失败/文件缺失） | driver 有 mtime 校验 | 低 |

### D 类：资源

| # | 卡点 | 根因 | 现有防护 | 残余风险 |
|---|------|------|---------|---------|
| D1 | 磁盘满 | 日志/checkpoint 累积 | 无 | 低（当前空间充足） |
| D2 | 内存不足 | SM 树太大 | 无 | 低 |
| D3 | 单 run 耗时过长 | driver 无超时（r01 实际 ~30min） | 无 | **高** |

### E 类：batch/watchdog

| # | 卡点 | 根因 | 现有防护 | 残余风险 |
|---|------|------|---------|---------|
| E1 | batch 进程死亡 | OOM/崩溃/被 kill | watchdog 60s 检测 + 清场 + 重启 | 低 |
| E2 | watchdog 本身死亡 | 无上层监控 | 无 | 中 |
| E3 | watchdog 误判（PID 复用） | PID 被其他进程复用 | 二次确认（ps -o command= grep） | 低 |

## 3. 验证测试矩阵

| # | 对应卡点 | 测试方法 | Pass 判据 | 优先级 | 自动化 |
|---|---------|---------|----------|--------|--------|
| T1 | A1 | 调 _probe_network，测返回时间 | ≤12s 返回（不卡死） | P0 | 是 |
| T2 | A1 | 强制 _network_healthy=False，调 _wiki_search | 返回 []，≤5s（不碰 urlopen） | P0 | 是 |
| T3 | A2 | 强制 _network_healthy=False，调 _local_corpus_search("H100") | 结果含 knowledge-base 来源 | P0 | 是 |
| T4 | B1 | 启动 SM 后 block 其 LLM 连接，观察 watchdog | watchdog 120s 内检测 stale 并 kill | P1 | 半自动 |
| T5 | B2 | 停 8787，跑一个 run | SM 报错退出（不卡死），watchdog 检测 8787 不健康 | P1 | 半自动 |
| T6 | B3 | 启动 2 个 SM 进程 | watchdog 杀残留，只留 1 个 | P1 | 半自动 |
| T7 | B4 | SM FATAL 后 resume | 从 ckpt 继续，不丢进度 | P1 | 半自动 |
| T8 | C1 | 验证 driver resume 路径是绝对路径 | 路径以 / 开头 | P0 | 是 |
| T9 | C3 | 读 cc-state.json | 合法 JSON，work_units 非空 | P0 | 是 |
| T10 | C4 | 读 ablation-results.json | 合法 JSON，runs 非空 | P0 | 是 |
| T11 | D1 | df 检查磁盘剩余 | > 10 GB | P2 | 是 |
| T12 | D3 | 检查 watchdog 有 SM stale 检测逻辑 | 脚本含 SM_STALE_THRESHOLD | P1 | 是 |
| T13 | E1 | 检查 watchdog 有 batch 重启逻辑 | 脚本含 nohup + t53b-batch.sh | P1 | 是 |
| T14 | E2 | pgrep watchdog 进程 | 进程存在 | P0 | 是 |

## 4. 执行方式

- 验证脚本：`experiments/stage-ablation/verify_checkpoints.py`
- 执行者：subagent（delegate_task）
- 组织：stage-gate goal（T53b-verify）
- 验收标准：
  - P0 测试（T1/T2/T3/T8/T9/T10/T14）全部 pass
  - P1 测试（T4-T7/T12/T13）≥ 80% pass
  - 验证结果落盘 `experiments/stage-ablation/verify-results.json`

## 5. watchdog 增强（2026-11-20）

新增 SM 卡死检测（解决 B1/D3）：
- 每 60s 检查当前 SM 进程的日志 mtime
- 如果日志 > 120s 未更新且 SM 进程还活着 → 判定 stale → kill SM
- driver 检测到 SM 被 kill（非正常退出）→ 不记账，保持 done=false
- 下次 watchdog 循环自动重启 driver 跑下一个 pending run
