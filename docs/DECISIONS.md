# AI_Content_OS

# Architecture Decisions

Version: 2.0

Status: Active

Last Updated: July 2026

---

# Purpose

This document records all major architectural and engineering decisions made during the development of AI_Content_OS.

Every significant design choice should be documented with its motivation, alternatives considered, and long-term impact.

The goal is to preserve engineering reasoning so future development remains consistent.

---

# Decision Format

Every decision follows this structure:

Decision ID

Status

Date

Decision

Reason

Alternatives Considered

Impact

---

# ADR-001

Decision

Adopt a Multi-Agent Architecture.

Status

Accepted

Reason

Different AI tasks require different responsibilities.

Separating Research, Writing, Reviewing, Character Generation, and Production into independent agents creates a modular and maintainable system.

Alternatives Considered

• Single monolithic prompt

• Single AI class

Impact

Positive

- Easier maintenance
- Independent agent upgrades
- Better scalability
- Easier testing

---

# ADR-002

Decision

Introduce a BaseAgent class.

Status

Accepted

Reason

Every agent performs common tasks such as initialization, logging, and execution flow.

Using inheritance removes duplicate code.

Alternatives Considered

Duplicate code in every agent.

Impact

Positive

- Cleaner architecture
- Standardized behavior
- Less maintenance

---

# ADR-003

Decision

Centralize all LLM communication inside Brain.

Status

Accepted

Reason

Agents should never communicate directly with language models.

Brain acts as the single interface responsible for model selection, retries, fallback logic, and future optimizations.

Alternatives Considered

Allow each agent to call the API directly.

Impact

Positive

- Centralized AI logic
- Easier debugging
- Easier provider migration

---

# ADR-004

Decision

Implement Automatic Model Fallback.

Status

Accepted

Reason

Large language models occasionally return quota errors, internal errors, or become temporarily unavailable.

Automatic fallback prevents workflow interruption.

Current Priority

1. Gemma 4 31B
2. Gemini 3.5 Flash
3. Gemini 3.1 Flash Lite

Impact

Positive

- Higher reliability
- Reduced failures
- Better user experience

---

# ADR-005

Decision

Use Structured Data Models.

Status

Accepted

Reason

Agents should exchange structured objects instead of raw text.

Current Models

- ResearchReport
- CharacterProfile
- CharacterBible
- StoryDraft
- ReviewReport

Impact

Positive

- Strong typing
- Easier validation
- Cleaner workflows

---

# ADR-006

Decision

Generate Characters before Story Writing.

Status

Accepted

Reason

Stories should be written around predefined characters instead of inventing new characters during writing.

Impact

Positive

- Consistent personalities
- Better storytelling
- Reusable characters

---

# ADR-007

Decision

Introduce Character Bible Layer.

Status

Accepted

Reason

Character consistency is critical for illustrations, animation, and future video generation.

Character Bible separates visual identity from story generation.

Impact

Positive

- Stable character design
- Consistent prompts
- Reusable production assets

---

# ADR-008

Decision

Export Production Assets.

Status

Accepted

Reason

Generated content should be stored independently from runtime memory.

Current Exports

Stories

- Markdown
- Plain Text

Character Bible

- JSON

Impact

Positive

- Easier production workflow
- Reusable assets
- Version control friendly

---

# ADR-009

Decision

Separate Prompts from Agent Logic.

Status

Accepted

Reason

Prompt engineering changes frequently.

Keeping prompts outside agent classes simplifies experimentation without modifying application logic.

Impact

Positive

- Cleaner codebase
- Easier prompt iteration
- Better maintainability

---

# ADR-010

Decision

Use Workflow Orchestration.

Status

Accepted

Reason

Business logic should exist inside workflows instead of individual agents.

StoryWorkflow coordinates the entire pipeline.

Current Flow

Research

↓

Character Generation

↓

Character Bible Generation

↓

Story Writing

↓

Story Review

↓

Production Export

Impact

Positive

- Centralized orchestration
- Easier expansion
- Better readability

---

# ADR-011

Decision

Keep Agents Stateless.

Status

Accepted

Reason

Agents should process inputs and return outputs without maintaining internal state.

State management belongs to workflows and future memory systems.

Impact

Positive

- Easier testing
- Predictable behavior
- Better scalability

---

# ADR-012

Decision

Adopt Production-Ready Folder Structure.

Status

Accepted

Reason

Separate source code from generated assets.

Current Structure

agents/

brain/

config/

formatters/

memory/

models/

production/

prompts/

tests/

utils/

workflows/

Impact

Positive

- Cleaner organization
- Easier navigation
- Better scalability

---

# ADR-013

Decision

Use JSON as the Primary Communication Format.

Status

Accepted

Reason

Structured JSON responses are easier to parse, validate, and reuse than plain text.

Impact

Positive

- Reliable parsing
- Future API compatibility
- Better automation

---

# ADR-014

Decision

Validate Stories Before Export.

Status

Accepted

Reason

Every generated story should pass quality checks before being considered production-ready.

Validation Includes

- Grammar
- Structure
- Word Count
- Educational Value
- Child Safety
- Moral

Impact

Positive

- Higher quality output
- Reduced manual review

---

# Pending Decisions

The following architectural decisions are expected in future versions:

- Scene Generation Pipeline
- Image Generation Pipeline
- Animation Pipeline
- Voice Generation Pipeline
- Memory Persistence
- Plugin System
- Knowledge Base
- Asset Management
- Multi-language Workflow
- Multi-modal Production Pipeline

---

# Decision Principles

When making future architectural decisions, follow these principles:

- Prefer modularity over complexity.
- Keep agents independent.
- Centralize shared logic.
- Separate data from behavior.
- Design for scalability.
- Optimize for production workflows.
- Maintain clear documentation.
- Favor reusable components over one-time solutions.

---

# Summary

The architecture of AI_Content_OS is intentionally modular, scalable, and production-oriented.

Every major design choice favors long-term maintainability, reusable components, and clear separation of responsibilities.

This document should evolve alongside the project and remain the authoritative record of all architectural decisions.