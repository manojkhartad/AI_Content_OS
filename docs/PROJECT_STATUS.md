# AI_Content_OS

**Project Status Document**

Version: v0.1 (MVP Development)

Last Updated: July 2026

---

# Project Vision

AI_Content_OS is an AI-powered Content Production System designed to automate the complete workflow of educational storytelling.

The long-term goal is to generate high-quality YouTube-ready children's videos with minimal human intervention while maintaining production quality, reusable architecture, and consistent characters.

The project is being developed as a modular AI Agent system rather than a single AI script.

---

# Current Development Phase

Current Phase:

✅ Story Generation Pipeline

Project Status:

🟢 Stable

Current Branch:

main

---

# Current End-to-End Workflow

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
Markdown + TXT Files

---

# Current Folder Structure

AI_Content_OS/

agents/
brain/
config/
formatters/
memory/
models/
production/
prompts/
utils/
workflows/

docs/

main.py

README.md

requirements.txt

---

# Current Agents

## ResearchAgent

Responsibilities

- Research topic
- Understand audience
- Generate research report

Output

ResearchReport

Status

✅ Completed

---

## WriterAgent

Responsibilities

- Read ResearchReport
- Generate complete story
- Return StoryDraft

Output

StoryDraft

Status

✅ Completed

---

## ReviewerAgent

Responsibilities

- Review generated story
- Score quality
- Provide feedback

Output

ReviewReport

Status

✅ Completed

---

# Current Models

ResearchReport

Stores

- Topic
- Goal
- Audience
- Tone
- Content Type

Status

✅ Stable

---

StoryDraft

Stores

- Title
- Story
- Moral
- Word Count

Status

✅ Stable

---

ReviewReport

Stores

- Passed
- Score
- Feedback

Status

✅ Stable

---

# Current Prompt System

Implemented

Research Prompt

Writer Prompt

Reviewer Prompt

Status

✅ Stable

---

# Current Brain Architecture

Brain

↓

LLM Client

↓

Gemini API

↓

Response

The Brain is responsible only for communicating with the LLM.

Business logic stays inside Agents.

---

# Current LLM Strategy

Primary Model

Gemma 4 31B

Fallback

Gemini Flash

Automatic fallback is enabled.

If one model fails the next model is automatically used.

Status

✅ Production Ready

---

# Current Export System

Supported Formats

Markdown (.md)

Text (.txt)

Exporter Location

production/story_exporter.py

Status

✅ Stable

---

# Current Utilities

JSON Parser

Purpose

Safely parse LLM JSON responses.

Status

✅ Stable

---

# Current Features

✅ Multi-Agent Architecture

✅ Research Pipeline

✅ Story Writing

✅ Story Review

✅ Story Export

✅ LLM Fallback

✅ Markdown Export

✅ TXT Export

---

# Completed Milestones

Research Agent

Writer Agent

Reviewer Agent

Story Exporter

Production Folder

GitHub Repository

Documentation System

---

# Next Milestone

Character Sheet System

Purpose

Maintain consistent characters across all stories.

Future Agents will use the same character definitions to ensure visual consistency during image and video generation.

---

# Future Pipeline

Character Sheet

↓

Research

↓

Writer

↓

Reviewer

↓

Scene Generator

↓

Image Prompt Generator

↓

Video Prompt Generator

↓

Voice Generator

↓

Video Builder

↓

YouTube Publishing

---

# Current Stable Build

The system can successfully:

✔ Research a topic

✔ Generate a complete children's story

✔ Review the generated story

✔ Export the story as Markdown

✔ Export the story as Text

✔ Automatically recover from model failures using fallback models

---

# Project Philosophy

The project follows the following principles:

- Modular Architecture
- Single Responsibility Principle
- Agent-Based Design
- Reusable Components
- Production-Ready Code
- Easy Future Expansion
- Human-readable Documentation
- Version Controlled Development

---

# Immediate Next Goal

Implement Character Management System before Scene Generation.

Reason:

Character consistency is required for future image generation, animation, and video production.

This decision establishes the foundation for building a recognizable YouTube brand with recurring characters.