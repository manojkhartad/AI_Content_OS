# AI_Content_OS

# System Architecture

Version: 1.0

Last Updated: July 2026

---

# Purpose

This document defines the complete architecture of AI_Content_OS.

It serves as the single source of truth for how the system is organized, how data flows between components, and how future modules should integrate with the existing architecture.

Every new feature must follow the architectural principles defined in this document.

---

# Project Vision

AI_Content_OS is a modular AI-powered Content Production Studio.

The long-term goal is to transform a single topic into a complete YouTube-ready educational video using multiple specialized AI agents.

The system is designed around reusable components instead of monolithic scripts.

---

# Core Design Principles

The architecture follows these principles.

- Modular Design
- Single Responsibility Principle
- Agent-Based Workflow
- Reusable Components
- Separation of Concerns
- Production-Ready Code
- Scalable Architecture
- Human Readable Documentation

Every component should perform one responsibility exceptionally well.

---

# High-Level Pipeline

Topic
│
▼
Research Agent
│
▼
Research Report
│
▼
Writer Agent
│
▼
Story Draft
│
▼
Reviewer Agent
│
▼
Review Report
│
▼
Story Exporter
│
▼
Production Files

This is the current stable production pipeline.

---

# Future Production Pipeline

Topic
│
▼
Character Manager
│
▼
Research Agent
│
▼
Research Report
│
▼
Writer Agent
│
▼
Story Draft
│
▼
Reviewer Agent
│
▼
Review Report
│
▼
Scene Generator
│
▼
Scene Report
│
▼
Image Prompt Generator
│
▼
Video Prompt Generator
│
▼
Voice Generator
│
▼
Video Builder
│
▼
YouTube Assets

This represents the long-term architecture of AI_Content_OS.

---

# Current Folder Structure

AI_Content_OS/

agents/

brain/

config/

docs/

formatters/

memory/

models/

production/

prompts/

utils/

workflows/

main.py

README.md

requirements.txt

Each folder owns a single responsibility.

---

# Brain Architecture

Purpose

The Brain acts as the communication layer between the application and the Large Language Model.

Responsibilities

- Receive prompts
- Send prompts to the LLM
- Receive responses
- Return responses

The Brain does not contain business logic.

Business decisions always belong to Agents.

---

# LLM Layer

Current Provider

Google Gemini API

Current Strategy

Primary Model

Gemma 4 31B

Fallback Models

Gemini Flash

Automatic model fallback is enabled.

If the first model fails, the next model is automatically used.

This makes the pipeline resilient to temporary model failures.

---

# Agent Architecture

Agents are responsible for business logic.

Current Agents

ResearchAgent

WriterAgent

ReviewerAgent

Future Agents

CharacterAgent

SceneAgent

ImagePromptAgent

VideoPromptAgent

VoiceAgent

ThumbnailAgent

SEOAgent

PublisherAgent

Every Agent should perform exactly one responsibility.

---

# Model Architecture

Models represent structured data flowing through the pipeline.

Current Models

ResearchReport

StoryDraft

ReviewReport

Future Models

CharacterProfile

SceneReport

ImagePrompt

VideoPrompt

NarrationScript

VideoProject

Models should never contain business logic.

They only transport structured data.

---

# Prompt Architecture

All prompt engineering is isolated from business logic.

Current Prompts

Story Prompt

Writer Prompt

Reviewer Prompt

Future Prompts

Character Prompt

Scene Prompt

Image Prompt

Video Prompt

Voice Prompt

Prompt files should only generate prompts.

They should never call the LLM directly.

---

# Formatter Architecture

Formatters convert internal models into readable output.

Current Formatter

Research Report Formatter

Story Formatter

Future Formatters

Scene Formatter

Video Formatter

Formatter responsibilities include presentation only.

---

# Export Architecture

Exporters create production-ready assets.

Current Export Formats

Markdown

Text

Future Export Formats

JSON

PDF

HTML

Subtitle Files

YouTube Metadata

Exporters never generate content.

They only save content.

---

# Utility Layer

Utilities provide reusable helper functions.

Current Utilities

JSON Parser

Future Utilities

Logger

Retry Manager

File Manager

Prompt Validator

Utilities must remain independent from business logic.

---

# Workflow Architecture

Workflows coordinate the execution of Agents.

Current Workflow

Story Workflow

Future Workflows

Video Workflow

Blog Workflow

Shorts Workflow

Podcast Workflow

Workflows should coordinate Agents without implementing business logic.

---

# Current Data Flow

Topic

↓

ResearchAgent

↓

ResearchReport

↓

WriterAgent

↓

StoryDraft

↓

ReviewerAgent

↓

ReviewReport

↓

StoryExporter

↓

Production Files

Every step produces structured output.

No component depends on printed text.

---

# Future Data Flow

Topic

↓

CharacterProfile

↓

ResearchReport

↓

StoryDraft

↓

SceneReport

↓

ImagePrompt

↓

VideoPrompt

↓

Narration

↓

VideoProject

↓

YouTube Assets

Every stage transforms one structured model into another.

---

# Character Architecture (Planned)

Character Manager will become the foundation of the production pipeline.

Responsibilities

- Character Database
- Appearance
- Personality
- Relationships
- Speaking Style
- Memory
- Prompt Injection

Every downstream module will use the same character information.

---

# Scene Architecture (Planned)

The Scene Generator will convert stories into cinematic production units.

Each scene will contain

- Scene Number
- Narration
- Characters
- Environment
- Action
- Emotion
- Camera Notes

Scenes become the source for image and video generation.

---

# Image Generation Architecture

Image prompts will include

- Character Appearance
- Environment
- Art Style
- Camera Angle
- Lighting
- Composition
- Negative Prompt

These prompts will be optimized for AI image models.

---

# Video Generation Architecture

Video prompts will include

- Character Motion
- Camera Motion
- Facial Expressions
- Environment Motion
- Timing
- Scene Continuity

Primary Target

Google Flow / Veo

---

# Voice Architecture

Narration generation will support

- Story Narration
- Character Voices
- Emotion Tags
- Timing

Long-term objective

Use original family voices to create a unique and recognizable channel identity.

---

# Error Handling Strategy

The system follows graceful failure.

Current Implementation

Automatic model fallback.

Future Improvements

Retry Policies

Logging

Error Reports

Recovery Strategies

---

# Documentation Architecture

Project documentation is divided into dedicated responsibilities.

PROJECT_STATUS.md

Current state of the project.

ROADMAP.md

Future development plan.

DEVLOG.md

Development history.

ARCHITECTURE.md

System design and technical blueprint.

DECISIONS.md

Important architectural decisions.

Universal Research Report

Research system documentation.

Each document has a single purpose.

---

# Design Rules

All future development must follow these rules.

- Brain communicates with the LLM only.
- Agents own business logic.
- Models transport data.
- Prompts generate prompts.
- Formatters format data.
- Exporters save files.
- Utilities provide reusable functions.
- Workflows coordinate execution.
- Components should remain loosely coupled.
- Avoid duplicate responsibilities.
- Prefer composition over unnecessary inheritance.

---

# Long-Term Architecture Vision

AI_Content_OS is designed to evolve beyond story generation.

The final system will function as a complete AI-powered Content Production Studio capable of generating stories, scenes, images, videos, narration, thumbnails, metadata, and publishing assets while maintaining consistent characters, reusable modules, and production-ready architecture.

The architecture emphasizes scalability, maintainability, and modularity so that future expansion can occur without major redesign.