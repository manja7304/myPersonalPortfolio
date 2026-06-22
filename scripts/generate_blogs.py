#!/usr/bin/env python3
"""Generate blog posts and blog index from POSTS metadata."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"

POSTS = [
    # Existing 11
    {"slug": "llm-security-strategies", "title": "7 LLM Security Strategies for Production AI Systems", "cat": "security", "tags": ["LLM Security", "Production"], "visual": "security", "emoji": "🛡️", "date": "Jun 2026", "read": "12 min", "excerpt": "Defense-in-depth for prompt injection, tool abuse, data leakage, and agent guardrails.", "sections": [("Treat the LLM as Untrusted", "Never assume the model refuses malicious input. Every tool action needs independent authorization and schema validation."), ("Layer Input Sanitization", "Separate system, context, and user layers. Tag retrieved content as untrusted."), ("Tool Allowlists", "Each agent gets only the tools required for its surface — web agents don't need cloud MCP tools.")]},
    {"slug": "owasp-llm-top-10-production", "title": "OWASP LLM Top 10: What It Means in Production", "cat": "security", "tags": ["OWASP", "LLM Top 10"], "visual": "security", "emoji": "📋", "date": "Jun 2026", "read": "11 min", "excerpt": "Mapping each OWASP LLM risk category to concrete engineering controls.", "sections": [("LLM01: Prompt Injection", "Instruction hierarchy, untrusted context tagging, dual-LLM guardrails."), ("LLM07: Insecure Plugin Design", "Tool allowlists, parameter validation, read-only defaults on MCP servers."), ("LLM08: Excessive Agency", "Human-in-the-loop for destructive operations.")]},
    {"slug": "prompt-injection-defense", "title": "Prompt Injection & AI Red Teaming: A Defense Guide", "cat": "security", "tags": ["Red Team", "Prompt Injection"], "visual": "security", "emoji": "⚔️", "date": "Jun 2026", "read": "10 min", "excerpt": "Indirect injection, tool hijacking, and layered controls that work.", "sections": [("Attack Taxonomy", "Direct, indirect, tool hijacking, and multi-turn manipulation."), ("Red Team Methodology", "Map attack surface, build injection corpus, automate regression tests."), ("Defenses That Work", "Dual-LLM pattern, structured outputs, human-in-the-loop, canary tokens.")]},
    {"slug": "autonomous-pentesting-ai-agents", "title": "Building Autonomous Pentesting with AI Agents", "cat": "security", "tags": ["Pentesting", "Agentic AI"], "visual": "security", "emoji": "🎯", "date": "Jun 2026", "read": "10 min", "excerpt": "Surface-specialized agents, evidence-first architecture, OWASP WSTG alignment.", "sections": [("Surface-Specialized Agents", "Web, API, Android, source code, and network each get dedicated agents."), ("Evidence-First Design", "Every finding links to reproducible evidence before entering reports."), ("Human Escalation", "Autonomous doesn't mean unsupervised — flag critical findings for review.")]},
    {"slug": "multi-agent-orchestration", "title": "Orchestrating 60+ AI Agents: Patterns That Scale", "cat": "ai", "tags": ["Agentic AI", "Temporal"], "visual": "ai", "emoji": "🤖", "date": "May 2026", "read": "11 min", "excerpt": "Supervisor/Router, parallel waves, checkpointing, and fault recovery.", "sections": [("Supervisor Pattern", "Routes to specialists without executing tools directly."), ("Parallel Waves", "Batch independent agents; checkpoint between dependent stages."), ("LiteLLM Routing", "Fast models for classification, capable models for analysis.")]},
    {"slug": "temporal-ai-workflows", "title": "Temporal Workflows for Reliable AI Agent Pipelines", "cat": "ai", "tags": ["Temporal", "Reliability"], "visual": "workflow", "emoji": "⏱️", "date": "May 2026", "read": "9 min", "excerpt": "Durable execution, checkpointing, and fault recovery for agent pipelines.", "sections": [("Why Temporal", "Durable state, automatic retries, workflow visibility."), ("Agents as Activities", "Map each agent call to a Temporal activity with timeouts."), ("Idempotency", "Design activities to survive retries without duplicate side effects.")]},
    {"slug": "rag-evaluation-ragas", "title": "RAG Evaluation with RAGAS: Stop Shipping Broken Retrieval", "cat": "rag", "tags": ["RAG", "MLOps"], "visual": "rag", "emoji": "📊", "date": "May 2026", "read": "9 min", "excerpt": "Faithfulness, relevancy, and regression gates for production RAG.", "sections": [("Core Metrics", "Faithfulness, answer relevancy, context precision, context recall."), ("Regression Gates", "Block deploys when metrics drop below baseline."), ("Golden Datasets", "Build from real user queries and known failure cases.")]},
    {"slug": "hybrid-search-agentic-rag", "title": "Hybrid Search for Agentic RAG: Vectors + Keywords", "cat": "rag", "tags": ["RAG", "Hybrid Search"], "visual": "rag", "emoji": "🔍", "date": "May 2026", "read": "8 min", "excerpt": "Combining embedding search and BM25 for technical security queries.", "sections": [("The Hybrid Pipeline", "Parallel vector + BM25 retrieval, reciprocal rank fusion, reranking."), ("Agent Routing", "CVE IDs route to keyword search; conceptual queries to semantic search."), ("Chunking", "Chunk security docs by logical sections, not fixed token windows.")]},
    {"slug": "mcp-security-best-practices", "title": "Securing MCP Servers: Tool Access Control for AI Agents", "cat": "security", "tags": ["MCP", "GRC"], "visual": "mcp", "emoji": "🔌", "date": "Apr 2026", "read": "10 min", "excerpt": "70+ cloud tools, credential isolation, and audit logging.", "sections": [("Read-Only by Default", "GRC evidence collection rarely needs write access."), ("Credential Isolation", "Short-lived scoped credentials per tenant."), ("Audit Every Invocation", "Log tool name, tenant, parameters — feed into GRC audit trail.")]},
    {"slug": "llm-cost-optimization", "title": "Cutting LLM Token Costs by 30% Without Sacrificing Quality", "cat": "ops", "tags": ["LLM Ops", "Cost"], "visual": "ops", "emoji": "💰", "date": "Apr 2026", "read": "8 min", "excerpt": "Model-tier routing, caching, and eval-gated prompt tuning.", "sections": [("Model-Tier Routing", "Cheap models for classification, capable models for reasoning."), ("Response Caching", "Hash prompts + context; invalidate on prompt version bumps."), ("Eval-Gated Changes", "Never optimize cost without measuring quality impact.")]},
    {"slug": "langgraph-agent-patterns", "title": "LangGraph Patterns: ReAct, Supervisor & Plan-and-Execute", "cat": "ai", "tags": ["LangGraph", "Patterns"], "visual": "framework", "emoji": "🔀", "date": "Apr 2026", "read": "10 min", "excerpt": "Choosing the right agent graph structure for production systems.", "sections": [("ReAct Loop", "Reason → Act → Observe — best for bounded tool sets."), ("Supervisor", "Routes to specialist sub-graphs with isolated tools."), ("Plan-and-Execute", "Planner upfront, executor sequential, replan on failure.")]},
    # New 19
    {"slug": "secure-prompt-engineering", "title": "Secure Prompt Engineering for Enterprise LLM Apps", "cat": "security", "tags": ["Prompt Engineering", "LLM Security"], "visual": "security", "emoji": "🔐", "date": "Jun 2026", "read": "9 min", "excerpt": "System prompt design that resists injection while maintaining output quality.", "sections": [("Instruction Hierarchy", "Immutable system layer, tagged context layer, adversarial user layer."), ("Output Schemas", "Force JSON/Pydantic outputs — never free-text tool invocation."), ("Few-Shot Safety", "Include examples of refused malicious requests in few-shot templates.")]},
    {"slug": "agent-memory-systems", "title": "Short & Long-Term Memory for AI Agents", "cat": "ai", "tags": ["Memory", "Agentic AI"], "visual": "ai", "emoji": "🧠", "date": "Jun 2026", "read": "8 min", "excerpt": "Designing agent memory for multi-turn sessions and audit trails.", "sections": [("Working Memory", "Current conversation context with token budget management."), ("Episodic Memory", "Store past engagement summaries in vector DB for retrieval."), ("Audit Memory", "Immutable logs of agent decisions for compliance and debugging.")]},
    {"slug": "function-calling-tool-design", "title": "Designing Tools for LLM Function Calling", "cat": "ai", "tags": ["Tool Calling", "MCP"], "visual": "mcp", "emoji": "🔧", "date": "Jun 2026", "read": "9 min", "excerpt": "Schema design, naming, and error handling for reliable agent tools.", "sections": [("Schema Clarity", "Descriptive parameter names and enums reduce hallucinated arguments."), ("Granular Tools", "Prefer many small tools over one mega-tool with optional params."), ("Error Messages", "Return actionable errors so agents can self-correct.")]},
    {"slug": "owasp-api-security-agents", "title": "OWASP API Security Top 10 for AI Agent Platforms", "cat": "security", "tags": ["API Security", "OWASP"], "visual": "security", "emoji": "🔗", "date": "May 2026", "read": "10 min", "excerpt": "Securing the REST APIs that expose agent orchestration to enterprise clients.", "sections": [("BOLA Prevention", "Scope every API key to tenant and resource IDs."), ("Rate Limiting", "Per-tenant quotas on agent invocations and token spend."), ("AuthN/AuthZ", "OAuth2 + scoped API keys; never trust agent output for authorization.")]},
    {"slug": "cloud-grc-automation", "title": "Automating GRC Evidence Collection with MCP Agents", "cat": "security", "tags": ["GRC", "Cloud"], "visual": "cloud", "emoji": "☁️", "date": "May 2026", "read": "9 min", "excerpt": "Multi-cloud compliance evidence via MCP across AWS, Azure, and GCP.", "sections": [("Evidence Mapping", "Map controls to automated fetch queries per cloud provider."), ("Scheduling", "Temporal workflows for periodic evidence refresh."), ("Audit Trail", "Every evidence artifact tagged with timestamp, source, and agent ID.")]},
    {"slug": "fine-tuning-vs-rag", "title": "Fine-Tuning vs RAG: When to Use Which", "cat": "rag", "tags": ["RAG", "Fine-Tuning"], "visual": "rag", "emoji": "⚖️", "date": "May 2026", "read": "8 min", "excerpt": "Decision framework for retrieval, fine-tuning, and hybrid approaches.", "sections": [("Use RAG When", "Knowledge changes frequently, you need citations, domain docs are large."), ("Use Fine-Tuning When", "Style/format consistency, specialized vocabulary, latency-critical paths."), ("Hybrid", "Fine-tune for behavior, RAG for facts — common in security report generation.")]},
    {"slug": "fastapi-llm-backend-patterns", "title": "FastAPI Patterns for Production LLM Backends", "cat": "ai", "tags": ["FastAPI", "Backend"], "visual": "ai", "emoji": "⚡", "date": "May 2026", "read": "9 min", "excerpt": "Async endpoints, streaming, dependency injection, and rate limiting for LLM APIs.", "sections": [("Streaming Responses", "SSE for token streaming; improve perceived latency."), ("Background Tasks", "Offload long agent workflows to Temporal, return job IDs immediately."), ("Dependency Injection", "Inject model clients, tenant context, and rate limiters per request.")]},
    {"slug": "docker-ai-production", "title": "Dockerizing AI Services for Production Deployment", "cat": "ops", "tags": ["Docker", "DevOps"], "visual": "ops", "emoji": "🐳", "date": "May 2026", "read": "7 min", "excerpt": "Multi-stage builds, health checks, and secrets management for AI stacks.", "sections": [("Multi-Stage Builds", "Separate build and runtime images; keep production images minimal."), ("Health Checks", "Liveness vs readiness — readiness should verify model/API connectivity."), ("Secrets", "Never bake API keys into images; use env vars or secret managers.")]},
    {"slug": "prometheus-ai-observability", "title": "Observability for AI Agents with Prometheus", "cat": "ops", "tags": ["Prometheus", "Observability"], "visual": "ops", "emoji": "📈", "date": "Apr 2026", "read": "8 min", "excerpt": "Metrics, dashboards, and alerts for agent latency, token spend, and error rates.", "sections": [("Key Metrics", "Token count, latency p95, tool call success rate, RAGAS scores."), ("Dashboards", "Grafana panels per agent type and per tenant."), ("Alerting", "Spike in token spend, drop in faithfulness score, agent loop detection.")]},
    {"slug": "sql-injection-automation", "title": "Automating SQL Injection Detection in Web Apps", "cat": "security", "tags": ["SQLi", "AppSec"], "visual": "security", "emoji": "💉", "date": "Apr 2026", "read": "8 min", "excerpt": "Payload strategies, detection heuristics, and remediation workflows.", "sections": [("Detection Patterns", "Error-based, boolean-based, time-based, and union-based SQLi."), ("Automation", "Python scripts integrated into agent web-scanning pipelines."), ("Remediation", "Parameterized queries, ORM usage, input validation at API layer.")]},
    {"slug": "xss-defense-deep-dive", "title": "XSS Defense: From Detection to Remediation", "cat": "security", "tags": ["XSS", "AppSec"], "visual": "security", "emoji": "🕷️", "date": "Apr 2026", "read": "9 min", "excerpt": "Reflected, stored, and DOM XSS — building scanners and fixing root causes.", "sections": [("XSS Types", "Reflected, stored, DOM — each needs different detection and fix."), ("Scanner Design", "Payload libraries, context-aware injection points, false positive reduction."), ("Prevention", "CSP headers, output encoding, framework auto-escaping.")]},
    {"slug": "api-security-testing-guide", "title": "API Security Testing for AI-Powered Platforms", "cat": "security", "tags": ["API Security", "Testing"], "visual": "security", "emoji": "🧪", "date": "Apr 2026", "read": "10 min", "excerpt": "Auth bypass, mass assignment, rate limits, and injection in REST/GraphQL APIs.", "sections": [("Auth Testing", "JWT tampering, scope escalation, expired token handling."), ("Input Validation", "Fuzzing endpoints with malformed JSON, oversized payloads, type confusion."), ("Agent API Specifics", "Test tool invocation endpoints for parameter injection.")]},
    {"slug": "network-recon-nmap", "title": "Network Reconnaissance with Nmap for Security Assessments", "cat": "security", "tags": ["Network", "Recon"], "visual": "security", "emoji": "🌐", "date": "Mar 2026", "read": "7 min", "excerpt": "Host discovery, port scanning, service detection, and OS fingerprinting.", "sections": [("Scan Types", "SYN scan, UDP scan, version detection, script scanning."), ("Automation", "Integrate Nmap output parsing into network agent pipelines."), ("Stealth vs Speed", "Trade-offs for authorized assessment engagements.")]},
    {"slug": "burp-suite-for-bug-hunters", "title": "Burp Suite Automation for Security Engineers", "cat": "security", "tags": ["Burp Suite", "Automation"], "visual": "security", "emoji": "🔍", "date": "Mar 2026", "read": "8 min", "excerpt": "Intruder, scanner, extensions, and API integration for repeatable testing.", "sections": [("Core Tools", "Proxy, Repeater, Intruder, Scanner — when to use each."), ("Extensions", "Autorize for auth testing, Logger++ for traffic analysis."), ("Automation", "Burp REST API + Python for CI-integrated security scans.")]},
    {"slug": "mitre-attack-ai-mapping", "title": "Mapping MITRE ATT&CK to AI Security Controls", "cat": "security", "tags": ["MITRE ATT&CK", "Threat Model"], "visual": "security", "emoji": "🎯", "date": "Mar 2026", "read": "9 min", "excerpt": "Threat modeling AI platforms using ATT&CK tactics and defensive controls.", "sections": [("Initial Access", "Prompt injection as entry vector — map to LLM01 controls."), ("Exfiltration", "Agent tool abuse for data exfil — MCP scope restrictions."), ("Defense Mapping", "Link each tactic to detective and preventive controls in your platform.")]},
    {"slug": "vector-db-selection-rag", "title": "Choosing a Vector Database for Production RAG", "cat": "rag", "tags": ["Vector DB", "RAG"], "visual": "rag", "emoji": "🗄️", "date": "Mar 2026", "read": "8 min", "excerpt": "Pinecone vs Chroma vs pgvector — trade-offs for security AI workloads.", "sections": [("pgvector", "Single DB for app data + vectors; good for moderate scale."), ("Pinecone", "Managed, low ops overhead, strong for high-throughput retrieval."), ("Chroma", "Fast prototyping, embeddable, good for dev and small deployments.")]},
    {"slug": "embedding-models-comparison", "title": "Embedding Models for Security & Technical RAG", "cat": "rag", "tags": ["Embeddings", "RAG"], "visual": "rag", "emoji": "📐", "date": "Mar 2026", "read": "7 min", "excerpt": "Model selection, dimensionality, and evaluation for domain-specific retrieval.", "sections": [("Model Choice", "OpenAI, Cohere, open-source — benchmark on your domain docs."), ("Chunk Strategy", "512 vs 1024 tokens; overlap for context continuity."), ("Evaluation", "Use RAGAS context precision to compare embedding models empirically.")]},
    {"slug": "human-in-the-loop-agents", "title": "Human-in-the-Loop Patterns for High-Stakes AI Agents", "cat": "ai", "tags": ["HITL", "Agentic AI"], "visual": "ai", "emoji": "👤", "date": "Mar 2026", "read": "8 min", "excerpt": "When and how to insert human approval in autonomous agent workflows.", "sections": [("Approval Gates", "Destructive ops, cross-tenant actions, high-severity findings."), ("Review Queues", "Analyst dashboard for agent outputs before client delivery."), ("Feedback Loops", "Human corrections feed back into prompt and eval datasets.")]},
    {"slug": "spec-driven-ai-development", "title": "Spec-Driven Development for AI Platform Engineering", "cat": "ops", "tags": ["SpecKit", "Engineering"], "visual": "ops", "emoji": "📋", "date": "Mar 2026", "read": "7 min", "excerpt": "SpecKit workflow for auditable, maintainable AI feature delivery.", "sections": [("Spec First", "Write agent behavior specs before implementation."), ("Review Cycle", "Security and domain experts review specs before coding."), ("Traceability", "Link specs to tests, eval datasets, and deployment artifacts.")]},
]

ARTICLE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Manjunath K G</title>
    <meta name="description" content="{excerpt}">
    <link rel="stylesheet" href="../css/theme.css">
    <link rel="stylesheet" href="../css/nav.css">
</head>
<body>
    <div class="bg-animation"></div>
    <div class="grid-overlay"></div>
    <header class="main-nav" id="mainNav">
        <a href="../index.html" class="nav-brand"><span class="nav-brand-icon">M</span><span class="nav-brand-text">Manjunath<span class="accent">.</span></span></a>
        <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
        <div class="nav-panel" id="navPanel">
            <ul class="nav-links"><li><a href="../index.html">Home</a></li><li><a href="index.html" class="active">Blog</a></li><li><a href="../index.html#contact">Contact</a></li></ul>
            <a href="../CorrectResume.pdf" class="nav-resume-btn" download>Resume</a>
        </div>
    </header>
    <article class="article-wrap">
        <a href="index.html" class="back-link">← All articles</a>
        <header class="article-header">
            <div class="blog-tags">{tags_html}</div>
            <h1>{title}</h1>
            <div class="article-meta"><span>Manjunath K G</span><span>{date}</span><span>{read} read</span></div>
        </header>
        <div class="article-content">
            <p>{excerpt}</p>
            {sections_html}
            <p><em>Manjunath K G — AI/ML Trainee Engineer @ Ampcus Cyber · CEH v13 · Building agentic AI for security.</em></p>
        </div>
    </article>
    <footer class="site-footer"><p>&copy; 2026 Manjunath K G · <a href="index.html" style="color: var(--neon-blue);">More articles</a></p></footer>
    <script src="../js/nav.js"></script>
</body>
</html>
'''

INDEX_CARD = '''            <a href="{slug}.html" class="blog-card" data-category="{cat}">
                <div class="blog-card-visual {visual}">{emoji}</div>
                <div class="blog-card-body">
                    <div class="blog-tags">{tags_card}</div>
                    <h2>{title}</h2>
                    <p>{excerpt}</p>
                    <div class="blog-meta"><span>{date}</span><span>{read}</span></div>
                    <span class="read-link">Read →</span>
                </div>
            </a>
'''

INDEX_HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog — Manjunath K G | AI Engineering & LLM Security</title>
    <meta name="description" content="30 articles on agentic AI, LLM security, RAG, MCP, and production ML engineering.">
    <link rel="stylesheet" href="../css/theme.css">
    <link rel="stylesheet" href="../css/nav.css">
</head>
<body>
    <div class="bg-animation"></div>
    <div class="grid-overlay"></div>
    <header class="main-nav" id="mainNav">
        <a href="../index.html" class="nav-brand"><span class="nav-brand-icon">M</span><span class="nav-brand-text">Manjunath<span class="accent">.</span></span></a>
        <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
        <div class="nav-panel" id="navPanel">
            <ul class="nav-links">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../index.html#about">About</a></li>
                <li><a href="../index.html#projects">Projects</a></li>
                <li><a href="index.html" class="active">Blog</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
            </ul>
            <a href="../CorrectResume.pdf" class="nav-resume-btn" download>Resume</a>
        </div>
    </header>
    <header class="page-header">
        <span class="eyebrow">30 Articles · AI & Security</span>
        <h1>AI, ML & LLM Security Blog</h1>
        <p>Production lessons from building multi-agent systems, securing LLM pipelines, and shipping AI-powered security platforms.</p>
    </header>
    <div class="container">
        <div class="blog-filters">
            <button class="filter-btn active" data-filter="all">All (30)</button>
            <button class="filter-btn" data-filter="security">LLM Security</button>
            <button class="filter-btn" data-filter="ai">Agentic AI</button>
            <button class="filter-btn" data-filter="rag">RAG & MLOps</button>
            <button class="filter-btn" data-filter="ops">LLM Ops</button>
        </div>
        <div class="blog-grid">
'''

INDEX_FOOTER = '''        </div>
    </div>
    <footer class="site-footer"><p>&copy; 2026 Manjunath K G · <a href="../index.html" style="color: var(--neon-blue);">Back to Portfolio</a></p></footer>
    <script src="../js/nav.js"></script>
</body>
</html>
'''


def tag_html(tags, security_first=False):
    parts = []
    for t in tags:
        cls = ' class="blog-tag security"' if t.lower() in ("llm security", "owasp", "prompt injection", "pentesting", "mcp", "grc", "sqli", "xss", "api security", "red team", "llm top 10", "network", "burp suite", "mitre att&ck", "threat model", "cloud", "appsec", "testing", "recon", "automation") or "security" in t.lower() else ' class="blog-tag"'
        parts.append(f"<span{cls}>{t}</span>")
    return "\n                ".join(parts)


def sections_html(sections):
    out = []
    for i, (heading, body) in enumerate(sections, 1):
        out.append(f"<h2>{i}. {heading}</h2>\n            <p>{body}</p>")
    return "\n            ".join(out)


def generate_article(post):
    tags_html = tag_html(post["tags"])
    content = ARTICLE_TEMPLATE.format(
        title=post["title"],
        excerpt=post["excerpt"],
        tags_html=tags_html,
        date=post["date"],
        read=post["read"],
        sections_html=sections_html(post["sections"]),
    )
    path = BLOG / f"{post['slug']}.html"
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {path.name}")


def generate_index():
    cards = []
    for p in POSTS:
        tags_card = " ".join(
            f'<span class="blog-tag{" security" if p["cat"]=="security" else ""}">{t}</span>'
            for t in p["tags"][:2]
        )
        cards.append(INDEX_CARD.format(
            slug=p["slug"], cat=p["cat"], visual=p["visual"], emoji=p["emoji"],
            tags_card=tags_card, title=p["title"], excerpt=p["excerpt"],
            date=p["date"], read=p["read"],
        ))
    (BLOG / "index.html").write_text(INDEX_HEADER + "\n".join(cards) + INDEX_FOOTER, encoding="utf-8")
    print("  ✓ blog/index.html (30 posts)")


if __name__ == "__main__":
    print("Generating blog posts...")
    for post in POSTS:
        generate_article(post)
    generate_index()
    print("Done.")
