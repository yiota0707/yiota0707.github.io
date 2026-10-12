from pathlib import Path
import re

root = Path.cwd()

index_file = root / "index.html"
css_file = root / "style.css"
readme_file = root / "README.md"

html = index_file.read_text(encoding="utf-8")
css = css_file.read_text(encoding="utf-8")

# ============================================================
# HELPER
# ============================================================

def replace_required(text, old, new, name):
    if old not in text:
        print(f"WARNING: Could not find: {name}")
        return text
    print(f"OK: {name}")
    return text.replace(old, new, 1)


# ============================================================
# META / PAGE TITLE
# ============================================================

html = replace_required(
    html,
    """content="Academic website of Panayiota Papafiggou, an MSc Computer Science student at the University of Warwick with research interests in artificial intelligence, reinforcement learning and multi-agent systems.\"""",
    """content="Academic website of Panayiota Papafiggou, PhD Researcher in Intelligent Diagnostics and Condition Monitoring at the University of Sheffield, with research interests in artificial intelligence, machine learning, reinforcement learning and multi-agent systems.\"""",
    "Meta description"
)

html = replace_required(
    html,
    """Panayiota Papafiggou | Artificial Intelligence Research""",
    """Panayiota Papafiggou | AI, Intelligent Diagnostics & Multi-Agent Systems""",
    "Page title"
)


# ============================================================
# HEADER
# ============================================================

html = replace_required(
    html,
    """Artificial Intelligence Research""",
    """AI · Intelligent Diagnostics · Multi-Agent Systems""",
    "Header subtitle"
)


# ============================================================
# HERO
# ============================================================

html = replace_required(
    html,
    """Artificial Intelligence · Reinforcement Learning · Multi-Agent Systems""",
    """Artificial Intelligence · Intelligent Diagnostics · Multi-Agent Systems""",
    "Hero research areas"
)

html = replace_required(
    html,
    """<p class="hero-role">
                        MSc Computer Science Student
                        at the University of Warwick
                    </p>""",
    """<p class="hero-role">
                        PhD Researcher – Intelligent Diagnostics &amp; Condition Monitoring
                        <span>at The University of Sheffield</span>
                    </p>""",
    "Hero role"
)

html = replace_required(
    html,
    """<p class="hero-summary">
                        I am a computer scientist interested in artificial
                        intelligence, reinforcement learning and multi-agent
                        systems. My current research examines how cooperation
                        emerges between learning agents, with broader interests
                        in intelligent decision-making, formal methods and
                        machine learning for engineering applications.
                    </p>""",
    """<p class="hero-summary">
                        I am an artificial intelligence researcher working on
                        AI-based diagnostics and fleet-based condition monitoring
                        of electric vehicle motors. My broader interests include
                        machine learning, reinforcement learning, multi-agent
                        systems and autonomous intelligent systems.
                    </p>""",
    "Hero summary"
)


# ============================================================
# RESEARCH INTERESTS PANEL
# ============================================================

old_interests = """<ul class="research-interest-list">

                        <li>
                            Multi-Agent Reinforcement Learning
                        </li>

                        <li>
                            Cooperative Artificial Intelligence
                        </li>

                        <li>
                            Intelligent Decision-Making
                        </li>

                        <li>
                            AI for Engineering Systems
                        </li>

                        <li>
                            Formal Methods and Type Theory
                        </li>

                    </ul>"""

new_interests = """<ul class="research-interest-list">

                        <li>
                            Intelligent Diagnostics &amp; Condition Monitoring
                        </li>

                        <li>
                            Machine Learning for Engineering Systems
                        </li>

                        <li>
                            Multi-Agent Reinforcement Learning
                        </li>

                        <li>
                            Autonomous &amp; Intelligent Systems
                        </li>

                        <li>
                            Cooperative Artificial Intelligence
                        </li>

                    </ul>"""

html = replace_required(
    html,
    old_interests,
    new_interests,
    "Research interests"
)

html = replace_required(
    html,
    """<strong>Institution</strong>
                            University of Warwick""",
    """<strong>Institution</strong>
                            The University of Sheffield""",
    "Institution"
)

html = replace_required(
    html,
    """<strong>Location</strong>
                            United Kingdom""",
    """<strong>Location</strong>
                            Sheffield, United Kingdom""",
    "Location"
)


# ============================================================
# ABOUT
# ============================================================

html = replace_required(
    html,
    """<p>
                            My academic interests centre on how intelligent
                            systems learn, cooperate and make decisions in
                            complex environments.
                        </p>""",
    """<p>
                            My research interests centre on how artificial
                            intelligence can support intelligent, adaptive and
                            autonomous systems in complex engineering and
                            decision-making environments.
                        </p>""",
    "About introduction"
)

old_about = """<p>
                            I am currently completing an MSc in Computer
                            Science at the University of Warwick. My academic
                            background includes artificial intelligence,
                            machine learning, formal methods, software
                            engineering and data analysis.
                        </p>

                        <p>
                            My experience includes algorithm development,
                            computational modelling, large-scale simulation,
                            statistical evaluation and computer-assisted
                            mathematical proof development.
                        </p>

                        <p>
                            I am particularly interested in research that
                            connects rigorous computational methods with
                            real-world scientific and engineering problems.
                            My long-term aim is to pursue an academic career
                            involving both research and teaching.
                        </p>"""

new_about = """<p>
                            I am beginning a PhD in Electrical and Electronic
                            Engineering at the University of Sheffield, where
                            my research focuses on AI-based diagnostics for
                            fleet-based condition monitoring of electric
                            vehicle motors.
                        </p>

                        <p>
                            My previous research includes multi-agent
                            reinforcement learning, computational modelling,
                            large-scale simulation, maritime data analysis and
                            formal verification.
                        </p>

                        <p>
                            I am particularly interested in research at the
                            intersection of artificial intelligence, autonomous
                            systems and real-world engineering applications.
                            My long-term aim is to pursue an academic career
                            involving both research and teaching.
                        </p>"""

html = replace_required(
    html,
    old_about,
    new_about,
    "About text"
)


# ============================================================
# CURRENT FOCUS
# ============================================================

html = replace_required(
    html,
    """Cooperation in Multi-Agent Reinforcement Learning""",
    """AI-Based Intelligent Diagnostics &amp; Condition Monitoring""",
    "Current focus title"
)

html = replace_required(
    html,
    """My MSc dissertation investigates how assortative
                        matching and partner-selection mechanisms influence
                        cooperation between reinforcement learning agents in
                        repeated social dilemmas.""",
    """My PhD research focuses on machine-learning approaches
                        for intelligent diagnostics and fleet-based condition
                        monitoring of electric vehicle motors.""",
    "Current focus description"
)


# ============================================================
# RESEARCH SECTION INTRO
# ============================================================

html = replace_required(
    html,
    """My work spans multi-agent reinforcement learning,
                        maritime data analysis and formal mathematical
                        methods.""",
    """My research spans intelligent diagnostics, machine
                        learning, multi-agent reinforcement learning,
                        computational modelling, maritime data analysis and
                        formal methods.""",
    "Research section description"
)


# ============================================================
# ADD PHD RESEARCH BEFORE MSC RESEARCH
# ============================================================

msc_marker = """                <article class="research-entry reveal">

                    <div class="research-entry-meta">

                        <p>
                            MSc Dissertation
                        </p>"""

phd_research = """                <article class="research-entry reveal">

                    <div class="research-entry-meta">

                        <p>
                            PhD Research
                        </p>

                        <span>
                            The University of Sheffield
                        </span>

                        <span>
                            Starting 2026
                        </span>

                    </div>

                    <div class="research-entry-content">

                        <h3>
                            AI-Based Diagnostics for Fleet-Based Condition
                            Monitoring of Electric Vehicle Motors Using
                            Machine Learning Frameworks
                        </h3>

                        <p class="research-question">
                            How can machine learning support intelligent
                            diagnostics and fleet-based condition monitoring
                            of electric vehicle motors?
                        </p>

                        <p>
                            My PhD research focuses on developing machine-learning
                            approaches for intelligent diagnostics and fleet-based
                            condition monitoring of electric vehicle motors.
                        </p>

                        <p>
                            The research investigates data-driven approaches to
                            monitoring engineering systems, with a focus on
                            intelligent fault detection and diagnostic methods.
                        </p>

                        <div class="keyword-list">

                            <span>Machine Learning</span>
                            <span>Intelligent Diagnostics</span>
                            <span>Condition Monitoring</span>
                            <span>AI for Engineering</span>

                        </div>

                    </div>

                </article>


"""

if "PhD Research" not in html:
    html = replace_required(
        html,
        msc_marker,
        phd_research + msc_marker,
        "PhD research entry"
    )
else:
    print("SKIP: PhD research entry already exists")


# ============================================================
# MSC RESEARCH
# ============================================================

html = replace_required(
    html,
    """<span>
                            2025–Present
                        </span>""",
    """<span>
                            2025–2026
                        </span>""",
    "MSc research dates"
)

html = replace_required(
    html,
    """I developed baseline and hybrid Python models using
                            Q-learning, partner switching and assortative
                            rematching. The experimental programme includes
                            sensitivity analyses, ablation studies, population
                            studies, convergence analysis and behavioural
                            evaluation.""",
    """I developed baseline and hybrid Python models using
                            Q-learning, adaptive partner switching and assortative
                            rematching. The experimental programme included
                            large-scale simulation, parameter sweeps, sensitivity
                            analyses, population studies, ablation studies,
                            convergence analysis and behavioural evaluation.""",
    "MSc research methods"
)


# ============================================================
# CYPRUS RESEARCH
# ============================================================

html = replace_required(
    html,
    """The work considered practical limitations such as
                            reporting errors, missing observations, irregular
                            transmissions and message constraints.""",
    """The work considered practical limitations such as
                            reporting errors, missing observations, irregular
                            transmissions and message constraints. The research
                            was conducted under the supervision of Associate
                            Professor Herodotos Herodotou.""",
    "Cyprus research supervisor"
)


# ============================================================
# EXPERIENCE SECTION
# ============================================================

experience_pattern = re.compile(
    r'<section\s+id="experience".*?(?=<section\s+id="activities")',
    re.DOTALL
)

new_experience = """<section
            id="experience"
            class="content-section section-tinted"
        >

            <div class="page-width">

                <header class="section-heading reveal">

                    <p class="section-label">
                        Background
                    </p>

                    <h2>
                        Education and Experience
                    </h2>

                </header>

                <div class="experience-list">

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Starting Oct 2026
                        </p>

                        <div>

                            <p class="experience-type">
                                Education
                            </p>

                            <h3>
                                PhD in Electrical and Electronic Engineering
                            </h3>

                            <h4>
                                The University of Sheffield
                            </h4>

                            <p>
                                EPSRC-funded research in AI-based intelligent
                                diagnostics and fleet-based condition monitoring
                                of electric vehicle motors.
                            </p>

                        </div>

                    </article>

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Sep 2025–Sep 2026
                        </p>

                        <div>

                            <p class="experience-type">
                                Education
                            </p>

                            <h3>
                                MSc Computer Science
                            </h3>

                            <h4>
                                University of Warwick
                            </h4>

                            <p>
                                Machine learning, data analytics, agent-based
                                systems, algorithmic game theory and artificial
                                intelligence.
                            </p>

                        </div>

                    </article>

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Jun–Aug 2025
                        </p>

                        <div>

                            <p class="experience-type">
                                Research
                            </p>

                            <h3>
                                External Research Collaborator
                            </h3>

                            <h4>
                                Cyprus University of Technology
                            </h4>

                            <p>
                                Developed vessel-movement detection algorithms
                                using maritime AIS data.
                            </p>

                        </div>

                    </article>

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Jan–Jun 2025
                        </p>

                        <div>

                            <p class="experience-type">
                                Academic Community
                            </p>

                            <h3>
                                Computing Officer
                            </h3>

                            <h4>
                                University of Nottingham MedTech
                            </h4>

                            <p>
                                Supported interdisciplinary workshops, technical
                                events and hackathon organisation.
                            </p>

                        </div>

                    </article>

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Sep 2022–Jun 2025
                        </p>

                        <div>

                            <p class="experience-type">
                                Education
                            </p>

                            <h3>
                                BSc (Hons) Computer Science
                            </h3>

                            <h4>
                                University of Nottingham
                            </h4>

                            <p>
                                Artificial intelligence, software engineering,
                                formal methods, security and human–AI interaction.
                            </p>

                        </div>

                    </article>

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Jun–Jul 2024
                        </p>

                        <div>

                            <p class="experience-type">
                                Industry
                            </p>

                            <h3>
                                Software Engineer Intern
                            </h3>

                            <h4>
                                Amdocs
                            </h4>

                            <p>
                                Software testing, API validation, debugging and
                                CI/CD automation.
                            </p>

                        </div>

                    </article>

                    <article class="experience-entry reveal">

                        <p class="experience-date">
                            Jun–Sep 2023
                        </p>

                        <div>

                            <p class="experience-type">
                                Industry
                            </p>

                            <h3>
                                Summer Intern
                            </h3>

                            <h4>
                                Golden Union Shipping
                            </h4>

                            <p>
                                Supported migration to a cloud-based crew-management
                                platform through business-process analysis,
                                documentation and data verification.
                            </p>

                        </div>

                    </article>

                </div>

            </div>

        </section>


        """

if experience_pattern.search(html):
    html = experience_pattern.sub(new_experience, html, count=1)
    print("OK: Education and Experience")
else:
    print("WARNING: Experience section not found")


# ============================================================
# ACTIVITIES
# ============================================================

html = html.replace(
    """Computing Communities""",
    """Academic &amp; Computing Communities""",
    1
)


# ============================================================
# CSS — PROFESSIONAL GREEN
# ============================================================

colour_changes = {
    "#f5f8fc": "#f6f9f7",
    "#edf4fb": "#edf5f1",
    "#102a43": "#173f35",
    "#071b2d": "#0c2922",
    "#1f5f99": "#2f725e",
    "#dbeaf7": "#e3f0eb",
    "#b9d2e8": "#b8d5ca",
    "#d8e0e8": "#d8e3de",
    "rgba(16, 42, 67, 0.08)": "rgba(23, 63, 53, 0.08)",
    "#f8fbfe": "#f7faf8"
}

for old, new in colour_changes.items():
    css = css.replace(old, new)

print("OK: Green visual system")


# ============================================================
# README
# ============================================================

readme = """# Panayiota Papafiggou - Personal Academic Website

This repository contains the source code for my personal academic website.

**Website:** https://yiota0707.github.io/

## About Me

I am a PhD researcher in Intelligent Diagnostics and Condition Monitoring at
the University of Sheffield. My research focuses on AI-based diagnostics for
fleet-based condition monitoring of electric vehicle motors.

My broader research interests include:

- Intelligent Diagnostics and Condition Monitoring
- Machine Learning for Engineering Systems
- Multi-Agent Reinforcement Learning
- Autonomous and Intelligent Systems
- Cooperative Artificial Intelligence
- AI for Engineering Applications

My previous research spans multi-agent reinforcement learning, computational
modelling, large-scale simulation, maritime data analysis and formal verification.

## Website

The website includes information about my:

- Research
- Academic background
- Technical projects
- Education and experience
- Research interests
- Curriculum Vitae
- Contact information

## Contact

I welcome enquiries regarding research collaborations, academic projects and
interdisciplinary work in artificial intelligence and engineering.

**Website:** https://yiota0707.github.io/

---

© 2026 Panayiota Papafiggou
"""


# ============================================================
# WRITE FILES
# ============================================================

index_file.write_text(html, encoding="utf-8")
css_file.write_text(css, encoding="utf-8")
readme_file.write_text(readme, encoding="utf-8")

print()
print("========================================")
print("WEBSITE UPDATE COMPLETE")
print("========================================")
print("Updated: index.html")
print("Updated: style.css")
print("Updated: README.md")
print("Unchanged: script.js")
print("Unchanged: cv.pdf")
print("Backups remain untouched.")
