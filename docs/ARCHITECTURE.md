# AI_Content_OS

# System Architecture

Version: 2.0

Status: Active

Last Updated: July 2026

---

# Purpose

This document describes the overall architecture of AI_Content_OS.

It explains how every major component interacts, how information flows through the system, and the design principles that guide future development.

This document is the primary technical reference for developers contributing to the project.

---

# Architecture Goals

The system is designed to be:

- Modular
- Scalable
- Agent-based
- Production-ready
- Model-independent
- Easy to extend
- Easy to test
- Easy to maintain

---

# High-Level Architecture

```

                 User

                   │

                   ▼

              StoryWorkflow

                   │

      ┌────────────┼────────────┐

      ▼            ▼            ▼

Research      Character      Character Bible

 Agent          Agent            Agent

      │            │              │

      └────────────┼──────────────┘

                   ▼

             Writer Agent

                   ▼

            Reviewer Agent

                   ▼

          Production Exporters

                   ▼

           Production Assets

```

---

# Layered Architecture

The project follows a layered architecture.

```

Presentation Layer

↓

Workflow Layer

↓

Agent Layer

↓

Brain Layer

↓

LLM Layer

↓

Production Layer

```

Each layer has a single responsibility.

---

# Project Structure

```

AI_Content_OS/

│

├── agents/

├── brain/

├── config/

├── formatters/

├── memory/

├── models/

├── production/

├── prompts/

├── tests/

├── utils/

├── workflows/

└── main.py

```

---

# Component Overview

---

## 1. Workflows

Purpose

Coordinate the execution of multiple agents.

Responsibilities

- Control execution order
- Pass structured data
- Handle orchestration
- Coordinate exports

Current Workflow

StoryWorkflow

Future Workflows

- VideoWorkflow
- ImageWorkflow
- AnimationWorkflow

---

## 2. Agents

Purpose

Each agent performs one specialized AI task.

Current Agents

- Research Agent
- Character Agent
- Character Bible Agent
- Writer Agent
- Reviewer Agent

Future Agents

- Scene Agent
- Image Agent
- Voice Agent
- Animation Agent
- Thumbnail Agent
- SEO Agent
- Publishing Agent

Agents never communicate directly with each other.

Only workflows coordinate agents.

---

## 3. Brain

Purpose

Brain is the central AI execution engine.

Responsibilities

- Prompt execution
- Model selection
- Retry logic
- Fallback logic
- Error handling

Agents never access LLMs directly.

All AI communication passes through Brain.

---

## 4. LLM Layer

Current Priority

1. Gemma 4 31B
2. Gemini 3.5 Flash
3. Gemini 3.1 Flash Lite

Execution Strategy

```

Try Model 1

↓

If Failed

↓

Try Model 2

↓

If Failed

↓

Try Model 3

↓

Return Response

```

This provides automatic fault tolerance.

---

## 5. Prompt Layer

Purpose

Separate prompt engineering from business logic.

Each agent owns its own prompt.

Examples

Research Agent

↓

Research Prompt

Character Agent

↓

Character Prompt

Writer Agent

↓

Writer Prompt

This separation allows prompts to evolve independently.

---

## 6. Models

Purpose

Models define structured communication between agents.

Current Models

ResearchReport

CharacterProfile

CharacterBible

StoryDraft

ReviewReport

Advantages

- Strong typing
- Easier debugging
- Reliable parsing
- Better scalability

---

## 7. Memory Layer

Current State

Basic implementation.

Responsibilities

- Store runtime information
- Manage future long-term memory

Future Capabilities

- Character memory
- Story memory
- World memory
- User memory
- Project memory

---

## 8. Production Layer

Purpose

Export production-ready assets.

Current Exporters

Story Exporter

Exports

- Markdown
- Plain Text

Character Bible Exporter

Exports

- JSON

Future Exporters

- Scene Exporter
- Image Exporter
- Subtitle Exporter
- Voice Exporter
- Animation Exporter

---

# Current Data Flow

```

User Topic

↓

Research Agent

↓

ResearchReport

↓

Character Agent

↓

CharacterProfile[]

↓

Character Bible Agent

↓

CharacterBible[]

↓

Writer Agent

↓

StoryDraft

↓

Reviewer Agent

↓

ReviewReport

↓

Story Exporter

↓

Markdown

Text

↓

Character Bible Exporter

↓

JSON

```

---

# Production Assets

Current Outputs

```

production/

│

├── stories/

│

│     Story.md

│

│     Story.txt

│

└── characters/

      Character.json

```

Future Outputs

```

production/

│

├── stories/

├── scenes/

├── images/

├── audio/

├── subtitles/

├── videos/

├── thumbnails/

└── metadata/

```

---

# Design Principles

## Single Responsibility

Every class has one job.

---

## Separation of Concerns

Business logic

↓

Agent logic

↓

Prompt logic

↓

LLM logic

↓

Export logic

All remain independent.

---

## Modularity

Every component can be replaced independently.

Example

Writer Agent can change without affecting Research Agent.

---

## Scalability

Adding a new agent should require minimal modification.

Workflow

↓

New Agent

↓

Done

No existing agent should require major changes.

---

## Production First

Generated data should always be exportable.

Nothing important should exist only in memory.

---

## Structured Communication

Agents exchange objects.

Never raw paragraphs.

Example

ResearchReport

↓

CharacterProfile

↓

CharacterBible

↓

StoryDraft

↓

ReviewReport

---

# Error Handling

Brain is responsible for:

- Retry
- Model switching
- API failure recovery
- Quota recovery
- Exception handling

Agents remain simple.

---

# Testing Strategy

Every major component should be testable independently.

Current Tests

- Character Agent
- Character Bible Agent

Future Tests

- Research Agent
- Writer Agent
- Reviewer Agent
- Workflow Integration
- Export Validation

---

# Future Architecture

The current architecture represents only Phase 1.

Future pipeline

```

Research

↓

Characters

↓

Character Bible

↓

Story

↓

Scenes

↓

Images

↓

Voice

↓

Animation

↓

Video

↓

Publishing

```

Each stage will become an independent reusable production pipeline.

---

# System Characteristics

Architecture Style

Multi-Agent

Workflow

Orchestrated

Communication

Structured Models

AI Access

Centralized Brain

Prompt Strategy

Modular

Production

Export Driven

Scalability

High

Maintainability

High

Testing

Independent Modules

---

# Summary

AI_Content_OS follows a modular multi-agent architecture where workflows orchestrate specialized agents, the Brain manages all AI communication, structured models connect components, and exporters generate production-ready assets.

The architecture is intentionally designed to support future expansion into scene generation, image generation, animation, voice synthesis, and complete AI-driven content production while keeping every module independent, reusable, and easy to maintain.