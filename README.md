# Hi, I'm Tim 👋

I design storytelling-style assessments where students **interact** with the material instead of just answering it.

---

##  Project in Production

###  Classroom Token Hub (v1.2.0) *formerly known as Classroom Economy*

A Progressive Web App (Flask + PostgreSQL) that models a student-driven economy:
-  Clock in/out logic to reward classroom currency based on attendance with automated payroll
-  Banking simulation (checking/savings accounts, interest, NSF fees)
-  Rent and Insurance bill systems
-  Storefront with item usage approval flow and bulk discount pricing
-  Student analytics dashboard with 12-month savings projections
-  Economy health monitoring with CWI (Classroom Wage Index) calculations
-  **Full PWA support** - installable mobile app with offline capabilities
-  **WCAG 2.1 AA accessibility** - inclusive design for all students
-  **Security hardened** - TOTP 2FA, encrypted PII, salted+peppered passwords

**Architecture Highlights:**
- Multi-tenant isolation with join-code scoping (teachers manage multiple class periods)
- 35+ SQLAlchemy models with Alembic migrations
- Service worker with intelligent caching strategies (cache-first for static, network-first for CDN)
- Responsive mobile-first UI with bottom navigation
- RESTful API with comprehensive error handling

**Latest Release (v.1.2.0 December 2025):**
- Progressive Web App with mobile installation ("Add to Home Screen")
- Mobile-optimized templates with responsive navigation
- Accessibility improvements (ARIA labels, keyboard navigation, screen reader support)
- Modern accordion-based admin UI to reduce scrolling
- Critical payroll multi-tenancy fix (proper join_code scoping)
- Improved terminology ("Start Work/Break Done" replaces "Tap In/Out")

**Version History:**
- **v1.2.0** (Dec 2025) - PWA, mobile experience, accessibility
- **v1.1.0** (Dec 2024) - Analytics dashboard, savings projections, UI redesign
- **v1.0.0** (Nov 2024) - First stable release (all critical security issues resolved)

**Tech Stack:** Flask, SQLAlchemy, PostgreSQL, Service Workers, Chart.js, Bootstrap
**License:** PolyForm Noncommercial 1.0.0

---

## Currently Developing

**Classroom Token Hub v1.3** - Multi-Teacher Hardening & Enhancements

**Active work:**
-  **Multi-teacher hardening** - Finalizing shared-student workflows and database constraints
-  **Data export capabilities** - CSV exports for rosters, transactions, attendance, and payroll history
-  **Enhanced test coverage** - Comprehensive tests for shared students across payroll and attendance
-  **Mobile refinements** - Continued UX improvements for touch interfaces
-  **Operational documentation** - Migration runbooks and safety checklists

**Upcoming roadmap:**
- **v1.4** - In-app messaging system, teacher announcement, transparent student-developer interactions.
- **v1.5** - Jobs marketplace (student employment system with applications and contracts)
- **v1.6+** - CWI Auto-Balancer (1-click solution to adjust pricing/pay rate)
---

## AP CSP Narrative Assessments

I design storytelling-style assessments where students **interact** with the material instead of just answering it:

- **"Is Leave Possible?"** — Data storytelling with Python & Google Forms
- **"Fragments of Truth"** — Data Unit: Time-loop paradox + student-induced anomalies
- **"The Halting Protocol"** (Under Development) — Algorithms Unit: Archivist AI and the halting problem

All projects blend Python (Trinket), narrative worldbuilding, and learning science.

---

## Project Stats

**Classroom Token Hub:**
- 35+ database models
- 100+ test cases with comprehensive coverage
- Full multi-tenancy isolation with join-code scoping
- Production-ready since November 2024
- PWA-enabled since December 2025
- Supporting multiple teachers and hundreds of students

---

## Connect

- Building tools for **financial literacy education**
- Designing **narrative-driven assessments** for AP Computer Science Principles
- Always learning: Currently exploring gamification patterns and accessibility best practices

---
> [!IMPORTANT]
> All of my public projects are licensed under the [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0/), which means:
>
> **You CAN:**
> - Use them in classrooms, clubs, and nonprofit educational settings
> - Modify or adapt them for school use, assignments, or personal learning
> - Share them with students or other educators
> - Use them for research or academic presentations (as long as they are not sold)
> 
> **You CANNOT:**
> - Use them as part of a commercial product or SaaS platform
> - Host a paid service or subscription that includes them
> - Incorporate them into any offering that generates revenue (e.g., paid courses, tutoring platforms)
> - Use them internally within a for-profit business, even if not publicly distributed
