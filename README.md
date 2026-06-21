# 100hires-setup-task
Portfolio task: setting up Claude Code and Codex in Cursor


This repository documents the setup process for three AI-native development tools — Cursor IDE, Claude Code, and Codex — as part of a portfolio task for a Junior Growth Marketing Specialist application at 100Hires.

Tools Installed


1. Cursor IDE — AI-powered code editor (already installed prior to this task)
2. Claude Code (Anthropic) — installed via CLI inside WSL (Windows Subsystem for Linux), then connected to Cursor as an extension
3. Codex (OpenAI) — installed via npm inside WSL, then connected to Cursor
4. WSL2 (Ubuntu) — required as a prerequisite, since Claude Code does not run natively on Windows
5. Node.js / npm (via nvm) — required as a prerequisite for installing Codex


Steps Completed


1. Installed WSL2 with Ubuntu (wsl --install) to get a Linux environment on Windows
2. Installed the Claude Code CLI inside WSL using the official install script
3. Added ~/.local/bin to the PATH so the claude command would be recognized
4. Created this public GitHub repository and cloned it inside the WSL filesystem
5. Opened the project in Cursor directly from the WSL terminal (cursor .) so Cursor would treat it as a WSL project from the start
6. Installed the WSL extension in Cursor when prompted, for proper WSL integration
7. Ran claude from Cursor's integrated WSL terminal, logged in with my Anthropic account (OAuth via browser), and confirmed folder trust — this auto-installed the Claude Code extension in Cursor
8. Selected Sonnet 4.6 as the active model (the default model, Fable 5, was temporarily unavailable)
9. Installed Node.js and npm inside WSL using nvm, since neither was present
10. Installed Codex globally via npm install -g @openai/codex
11. Ran codex from Cursor's integrated terminal and logged in with my OpenAI/ChatGPT account (OAuth via browser)
12. Verified both Claude Code and Codex work correctly by asking each one to list the files in the project


Issues Ran Into and How I Solved Them

1. Claude Code does not run natively on Windows
Running claude --version in PowerShell returned a "command not found" error. Solution: installed WSL2 with Ubuntu and ran Claude Code from there instead, since the CLI requires a Linux environment.

2. claude command not recognized after install
After installing Claude Code, the CLI wasn't in the PATH. Solution: manually appended ~/.local/bin to PATH in .bashrc as instructed by the installer's own output, then reloaded the shell with source ~/.bashrc.

3. Cursor opened a PowerShell terminal instead of a WSL terminal
Even with the project located in the WSL filesystem, Cursor's default integrated terminal opened as PowerShell. Solution: manually selected "WSL"/"Ubuntu" as the default terminal profile via Terminal: Select Default Profile in the Command Palette.

4. Default AI model unavailable
On first run, Claude Code attempted to use a model (Fable 5) that was temporarily unavailable due to an export control restriction. Solution: switched to Sonnet 4.6 using the /model command inside Claude Code.

5. Extensions marketplace search returned no results at all
Cursor's Extensions search bar returned zero results for any query — even for extensions known to exist, like "Python." This made it impossible to find or install the Codex extension through the UI. Troubleshooting steps tried: checking for Cursor updates (none available) and manually adding a extensions.gallery configuration block to settings.json — neither fixed the underlying issue.
Solution: bypassed the marketplace entirely and installed Codex via its CLI (npm install -g @openai/codex), the same way Claude Code had been installed — running the tool once from the terminal triggered the editor integration automatically, without relying on the broken search.

6. Node.js/npm not installed
Installing Codex requires npm, which wasn't present in the WSL environment. Solution: installed Node.js via nvm (Node Version Manager), then installed the LTS version of Node, which included npm.

7. OAuth login error during Codex sign-in (invalid_state)
The first attempt to sign in to Codex with ChatGPT failed with an invalid_state error after completing the browser login flow. Solution: simply retried the login flow from scratch (codex → "Sign in with ChatGPT" again), which completed successfully on the second attempt.
