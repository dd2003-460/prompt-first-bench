I'll execute Phase 02. Let me start by checking the environment and the `ralph` executable, then gather evidence for each open question (U1-U7).

<tool_call>
<function=Bash>
<parameter=command>
which ralph && ralph --version 2>&1 | head -5; echo "---"; ls -la /Users/duff/.agents/skills/ralph-loop/ 2>&1 | head
</parameter>
<parameter=description>
Check ralph executable availability
</parameter>
</function>
</tool_call>