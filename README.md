# Hi, I’m Tim

I design narrative-driven learning systems where students interact with constraints, incentives, and consequences.

My work sits at the intersection of:
- computer science education
- financial literacy
- learning science
- systems thinking
- and a skepticism of shallow gamification

---

## Project in Production

### Classroom Token Hub (v1.8.0)  
formerly Classroom Economy

A production-grade Progressive Web App (Flask + PostgreSQL) that simulates a real classroom economy to support classroom management, reward system, and routines. Thoughtfully designed to make economic systems visible, debuggable, and fair for students.

This is my first fully functional app as a teacher developer and a step towards the dream of *"If I need a tool, I can just build it"*

---

### Core Systems
- Attendance-aware clock in/out with automated payroll
- Banking simulation (checking, savings, interest, NSF fees)
- Rent and insurance billing engines
- Storefront with approval workflows and bulk pricing
- Student analytics with weekly, monthly, and long-term projections
- Economy health monitoring via the Classroom Wage Index (CWI)
- In-app messaging and teacher announcements
- Full Progressive Web App support (installable, offline-capable)
- WCAG 2.1 AA accessibility throughout
- Security hardened: TOTP 2FA, encrypted PII, salted and peppered passwords

---

### Architecture and Engineering Highlights
- True multi-tenant isolation via join-code scoping
- 35+ SQLAlchemy models with Alembic migrations
- RESTful API with defensive authorization and null-safe logic
- Corruption-tolerant financial calculations (Decimal-safe, NULL-safe)
- Service worker caching (static: cache-first, dynamic: network-first)
- Mobile-first UI with bottom navigation
- Designed for real students touching real data

---

## Production Status
- Live since November 2024
- PWA-enabled since December 2025
- Actively used by multiple teachers and hundreds of students
- Continuous hardening against edge cases, corrupted data, and misuse
- Security issues tracked, documented, and patched with audit trails

See `CHANGELOG.md` for full technical detail.

---

## Narrative Assessments (AP Computer Science Principles)

I build story-first assessments where computation matters because the world reacts.

- Is Leave Possible?  
  Data storytelling with Python under real constraints

- Fragments of Truth  
  Data systems, time loops, and student-induced anomalies

- The Halting Protocol (in development)  
  Algorithms unit centered on an Archivist AI and the halting problem

Each project blends Python, narrative worldbuilding, learning science, and deliberate cognitive friction.


---

## What I Care About
- Making financial systems legible to students
- Designing assessments that reward thinking, not compliance
- Treating AI as a thinking partner, not a shortcut
- Accessibility as a design constraint, not a checklist
- Building systems that fail visibly and recover gracefully

---

## License

All public projects here are licensed under the PolyForm Noncommercial License 1.0.0.

You may:
- Use these projects in classrooms, clubs, and nonprofit educational settings
- Modify them for school use or personal learning
- Share them with students and other educators
- Use them in research or academic presentations (non-commercial)

You may not:
- Use them as part of a commercial product or SaaS platform
- Host paid services that include this code
- Bundle them into revenue-generating offerings
- Use them internally within for-profit organizations

---

I run on ADHD, Insanity, and the love for learning and building.
