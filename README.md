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

### Classroom Token Hub (v1.7.1)  
formerly Classroom Economy

A production-grade Progressive Web App (Flask + PostgreSQL) that simulates a real classroom economy—designed to make economic systems visible, debuggable, and fair for students.

This is my first fully functional app as a teacher developer and a step towards the dream of "If I need a tool, I can just build it"

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

---

## Recent Releases

### v1.7.1 – January 2026  
Stability and Data Integrity Release
- Fixed multiple critical Decimal and NULL transaction crashes
- Hardened earnings, spending, savings, and interest calculations
- Graceful handling of corrupted or partial transaction data
- Improved duplicate student-claim handling (IntegrityError-safe)
- Payroll import and admin route fixes

Security work (ongoing):
- Hardened Grafana proxy against XSS
- Removed unsafe function redefinitions in student routes
- Improved internal safety helpers and URL validation

See `CHANGELOG.md` for full technical detail.

---

## Active Development

### Classroom Token Hub – Current Focus

In progress:
- Multi-teacher workflows with shared-student constraints
- CSV exports for rosters, transactions, payroll, and attendance
- Expanded test coverage for cross-class and corruption scenarios
- Mobile UX refinements for high-friction workflows
- Operational documentation: migration runbooks and recovery checklists

Planned:
- Jobs marketplace (student applications, contracts, pay cycles)
- CWI auto-balancer for system-level economic tuning
- Advanced economy diagnostics and health alerts

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

## Project Snapshot

Classroom Token Hub:
- 35+ database models
- 100+ tests and growing
- Full join-code multi-tenancy isolation
- Decimal-safe financial engine
- Progressive Web App with offline support
- Production-hardened since 2024

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

I build slowly, deliberately, and in public—because classrooms are high-stakes systems, and students notice when you cut corners.
