# Web Interface Search Initialization Error

## Issue Description
The web interface requires pre-built search indices (`embeddings.npy`, `indices.json`, and `hashes.json`) to function properly, but these files are not automatically generated. Currently, users need to manually run `search_semantic.py` before starting the web interface, which is not documented and leads to errors.

## Current Behavior
- Web interface fails on first run due to missing search indices
- No clear error message or guidance for users
- Manual step required but not documented

## Expected Behavior
- Search indices should be automatically generated when needed
- Clear feedback during index generation
- Indices should update when markdown files change
- Files should be properly ignored by Git

## Technical Details
- Affects search functionality in web interface
- Related files: `web_interface.py`, `search_semantic.py`
- Environment: All platforms

## Labels
- bug
- enhancement
- documentation 