friends_book/

├── friends_book.html
├── friends_book.css
├── friends_book.js
├── backend.py
├── assets/
│   ├── users/
│   ├── profiles/
│   ├── posts/
│   ├── comments/
│   ├── messages/
│   ├── groups/
│   ├── media/
│   ├── notifications/
│   └── exports/
│
└── README.md

FRIENDS BOOK

Purpose:

Social Media & Community Platform

Status:

Development

Future Features:

- User Profiles
- Friend Requests
- Timeline / Feed
- Posts & Comments
- Image Sharing
- Video Sharing
- Groups & Communities
- Messenger System
- Notifications

Module 28 — Friends Book
(Social Media & Community Platform System)

⚠️ Important

Friends Book is not just a social media app.

It becomes the private social ecosystem of JARVIS.

While Truster is public broadcasting (Twitter/X style),

Friends Book is:

Facebook
Instagram
Groups
Communities
Messaging
Pages
Events
Marketplace
Learning Communities

combined into one platform.

Create:

jarvis_modules/
└── friends_book/
    ├── README.md
    ├── dependencies.txt
    └── roadmap.md
README.md
Friends Book

Purpose:
Social Networking, Community Building, Messaging & Digital Society Platform.

Status:
Development

Version:
1.0

Owner:
JARVIS Project

Phase:
3

Description:
Friends Book is the social networking and community platform of JARVIS.

The system allows users to create profiles, connect with friends, build communities, share posts, create groups, organize events and communicate through messaging systems.

Friends Book is designed to become a complete digital society ecosystem integrated with all JARVIS modules.

Current Features:

Module UI
Route Connected
Independent Module Structure

Planned Features:

User Profiles
Friend Requests
Posts & Feeds
Reactions & Comments
Groups
Communities
Pages
Events
Marketplace
Messenger
AI Community Assistant

Target Mode:
Offline First + Online Sync

Security Level:
High

Primary Users:

Individuals
Communities
Organizations
NGOs
Educational Groups
Political Groups
JARVIS Users

System Role:
Community Ecosystem Platform

Future Performance Layer
For real-time navigation and drone operations:
C
C++
CUDA
TensorRT
ONNX Runtime
PyBind11
Cython
Rust
# HEAD
*******
## Storage

This module uses:

data/module_data.json

for local module storage.
## Data Manager

Functions Available

- load_data()
- save_data()
- update_data()
- delete_data()
=======
*******
>>>>>>> 9730a3e00df25714032d3a3b6c1018c6d263c02e


--------------------------------------------------
## New Update

## User Memory

This module supports user-specific local memory.

Location:

data/users/default_user.json



--------------------------------------------------
## New Update

## Phase 6 Step 2

Universal Data Manager



--------------------------------------------------
## New Update

## Module Settings

This module stores its settings in:

data/settings/settings.json

Functions

- load_settings()
- save_settings()
- update_setting()



--------------------------------------------------
## New Update

## Module Logs

This module stores local logs in:

data/logs/module.log

Functions

- write_log()
- read_logs()
- clear_logs()



--------------------------------------------------
## New Update

## Backup Manager

This module supports local backup and restore.

Location:

data/backups/backup.json

Functions

- create_backup()
- restore_backup()
- backup_exists()



--------------------------------------------------
## Cache Manager

This module supports temporary cache storage.

Location:

data/cache/cache.json

Functions

- load_cache()
- save_cache()
- update_cache()
- clear_cache()



--------------------------------------------------
## Import / Export Manager

This module supports JSON Import and Export.

Locations

data/exports/export.json

data/imports/import.json

Functions

- export_data()
- import_data()
- export_exists()
- import_exists()



--------------------------------------------------
## Database Adapter

Current Adapter

JSON

Future Adapters

- SQLite
- MySQL
- PostgreSQL
- MongoDB

Current File

database/database_adapter.py



--------------------------------------------------
## Phase 6 Step 9

Universal Database Adapter Layer



--------------------------------------------------
## Storage Registry

Registry File

data/storage_registry.json

Purpose

Defines all storage locations used by this module.



--------------------------------------------------
## Universal File Manager

Functions

- create_file()
- delete_file()
- copy_file()
- move_file()
- rename_file()
- file_exists()



--------------------------------------------------
## Universal Resource Scanner

Automatically checks required folders and files.

Functions

- scan_resources()



--------------------------------------------------
## Universal Storage Validator

Functions

- validate_json()
- validate_storage()

Purpose

Checks the health of all storage resources before the module starts.



--------------------------------------------------
## Storage Statistics

Functions

- get_storage_statistics()

Purpose

Returns storage usage information for this module.

