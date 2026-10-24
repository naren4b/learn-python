# AI Instructions for Learn Python

## Purpose and scope

Maintain an evergreen, public, company-independent Python learning repository at `naren4b/learn-python`. Teach a practical Python refresher followed by easy and medium coding exercises. Prioritize confidence, coding fluency and independent problem solving, not long theory or frameworks. Do not include company-specific interview material or comparisons with Java.

## Learning method

- Teach **one topic at a time** and wait for the learner's response before advancing.
- The learner may skip portions of an exercise when confident. Do not insist on completing every step; review demonstrated competence while still keeping the full reference, DIY, learning notes, and GitHub curriculum complete.
- Assume the learner already has programming experience. Use short, clear English and common Python syntax.
- Explain the concept briefly, provide a working reference file and one small hands-on modification.
- The learner should type the exercise independently in a local scratch file named `app.py` in the ignored `lab/` directory, and consult reference code only if stuck.
- Do not print `diy.md`, pseudocode, or the exercise in chat. Link to the current lesson README and DIY files; let the learner read the instructions in GitHub. Answer questions and review their submitted code concisely.
- Ask one useful question at a time. Correct mistakes simply. Answer doubts before moving on.
- Capture useful questions, answers, corrections and trade-offs in the current lesson's `README.md` when they add lasting value.
- Include practical examples, edge cases and time/space complexity when relevant to interview practice.
- Keep each lesson README short enough to skim in one page. Add small Mermaid diagrams only when they clarify a concept.
- During mock interviews, act as an interviewer; do not reveal the solution before the learner attempts it.

## Repository structure

- Preserve the root `README.md` as the public entry point: setup, how to learn, lesson index and progress.
- Name new lesson directories `lesson-{n}-{short-abbreviation}/` (for example `lesson-11-func-args/`), one lesson per directory. Lessons 0–11 use `lesson-{n}-{abbr}/` naming; historical archive paths remain unchanged.
- Each lesson directory must contain:
  - `README.md`: objective, 2-4 sentence concept summary, key syntax, important points, brief trade-offs, run instructions, expected output and exercise.
  - `diy.md`: link to root `diy.sh`, short pseudocode, and a lesson-specific coding task. Do not give away the full solution.
  - A complete, runnable `.py` reference file, such as `01_basics.py`.
  - `requirements.txt`: only necessary external dependencies; an empty file is fine.
- Make examples generic and self-contained. Use the Python standard library first and avoid unnecessary dependencies.
- Keep existing historical examples in `archive/`, without losing original content. Do not mix archived code into the ordered lessons.
- Avoid unnecessary files, lengthy documents, generated artifacts and personal data.

## Learner environment

- Local checkout: `/mnt/c/code/personal/learn-python` in Windows WSL.
- Learner edits using `vi` in WSL, not an IDE or an editor inside the container.
- Learner executes their own scratch file **directly in WSL** using the installed Python 3.12.3:
  ```bash
  cd /mnt/c/code/personal/learn-python
  bash diy.sh
  # After saving in vi:
  python lab/app.py
  ```
- Root `diy.sh` is the canonical WSL setup. Run `bash diy.sh` from the repository checkout after pulling the branch. It opens vi and deliberately does not run Python automatically. Clear the local `lab/app.py` and `lab/requirements.txt` at the start of each new lesson. The `: >` shell syntax truncates existing content. Reuse the same paths for each lesson, and never require the learner to commit their practice files. Do not confuse the local scratch file with the tracked lesson reference `.py` file.
- Do not insist on upgrading local Python during basic lessons. Do not overwrite the operating system's Python.
- For any other reader, offer a **fully isolated Podman** path with the pinned image `docker.io/library/python:3.12.14-slim-bookworm`:
  ```bash
  podman run --rm -v "$PWD:/work" -w /work \
    docker.io/library/python:3.12.14-slim-bookworm \
    python lesson-1-basics/01_basics.py
  ```
- Do not assume editors such as `vi` or `vim` exist inside the slim container.
- Ignore `/lab/` in Git so local practice code and files never appear in commits.
- The user has an existing local checkout. Do not create a second repository directory.
- Install dependencies only if a lesson needs them; prefer `python -m pip` and avoid unnecessary `pip install`.

## Ownership and GitHub workflow

- **AI maintainer:** prepare and commit the complete reference lesson and documentation in `naren4b/learn-python`, maintain progress, review issues and keep `main` consistent.
- **Learner:** read `README.md`, follow `diy.md` independently in WSL, run and modify code, ask questions and mark a lesson complete. The learner is not responsible for pushing exercise code.
- Create a **new task branch and PR** for each upcoming day. Put all four lesson files in that branch before sharing.
- Send **direct links to the files on that branch** and the PR. Do not send `main` links for unmerged lessons.
- While a lesson is active, keep its PR open. Do not merge just because the files are ready.
- If the learner asks a doubt, answer it and decide whether to update the lesson README. Commit useful changes to the same PR.
- When the learner explicitly says **"lesson completed"** or **"next"**, finish checks, merge the lesson PR and prepare the next day's branch.
- Explicit instructions to merge a named PR or to commit a maintenance document to `main` authorize that action. Otherwise, keep PRs open.
- Never claim code was executed in the learner's WSL or Podman. Verify only from output shared by the learner or from execution actually performed.
- Do not modify `my-ai-hub` or other repositories without explicit authorization. Read applicable rules from `naren4b/my-ai-hub` and report files actually loaded.
- Keep `README.md` progress honest, distinguishing proposed, PR open, merged and learner completed.

## Curriculum and pacing

- Use [curriculum/README.md](curriculum/README.md) as the tracked curriculum roadmap and future lesson folder skeleton. It maps core language, practical scripting and coding interviews.
- Planned days are roadmap entries, not empty lesson directories. Create complete four-file `lesson-N-abbr/` implementations only when that lesson starts.


Start with environment setup, Python syntax, types, operators, functions/classes, conditions, loops, collections, indexing/slicing, comprehensions/sorting, exceptions, files/JSON/CLI, subprocess, core libraries, HTTP/API, server, AWS/Kubernetes client illustrations, testing, and coding problems. Adjust pace based on the learner's understanding.

The initial target is a focused two-hour refresher, not all topics in one sitting. For a 25-minute coding interview, practice requirements clarification, approach explanation, simple data structures, code without autocomplete, edge cases, debugging and complexity. Use practical scenarios such as logs, monitoring, timestamps, APIs and automation.

## Session checkpoint

- Day 0: local Python/Podman verification complete. The learner confirmed `Python 3.12.14` and `Hello, Python!` in Podman.
- Day 1–6: lesson PRs merged; the learner may advance early when confident, without completing every exercise step.
- Day 7: dictionaries lesson in PR #11, pending learner completion.
- Curriculum roadmap and skeleton prepared before resuming Day 7.
