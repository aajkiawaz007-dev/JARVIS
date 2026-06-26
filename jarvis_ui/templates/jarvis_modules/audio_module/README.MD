## Data Manager

Functions Available

- load_data()
- save_data()
- update_data()
- delete_data()

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

