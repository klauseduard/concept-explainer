"""Shared utilities for search functionality."""

from sentence_transformers import SentenceTransformer
import numpy as np
import os
import hashlib
import json
from typing import Tuple, List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

def initialize_search_indices(
    directory: str = "./saved_concepts",
    model_name: str = 'all-MiniLM-L6-v2',
    embeddings_path: str = 'embeddings.npy',
    indices_path: str = 'indices.json',
    hashes_path: str = 'hashes.json'
) -> Tuple[List[str], np.ndarray, SentenceTransformer]:
    """Initialize search indices if they don't exist."""
    try:
        # Check if files exist and are valid
        if (os.path.exists(embeddings_path) and 
            os.path.exists(indices_path) and 
            os.path.exists(hashes_path)):
            logger.info("Loading existing search indices...")
            embeddings = np.load(embeddings_path, allow_pickle=True)
            with open(indices_path, 'r') as f:
                indices = json.load(f)
            with open(hashes_path, 'r') as f:
                stored_hashes = json.load(f)
            
            # Get current file hashes
            _, _, current_hashes = build_corpus_and_hashes(directory)
            
            # Check if any files were added, removed, or modified
            if (set(stored_hashes.keys()) != set(current_hashes.keys()) or
                any(stored_hashes[k] != current_hashes[k] 
                    for k in stored_hashes if k in current_hashes)):
                logger.info("Changes detected in markdown files, rebuilding indices...")
                return build_and_save_embeddings(directory, model_name, embeddings_path, indices_path, hashes_path)
            
            # Verify the files are valid
            if embeddings is not None and indices and stored_hashes:
                logger.info("Existing search indices loaded successfully.")
                model = SentenceTransformer(model_name)
                return list(indices.keys()), embeddings, model
    except Exception as e:
        logger.warning(f"Error loading existing indices: {e}")
    
    # If we get here, we need to build new indices
    logger.info("Building new search indices...")
    return build_and_save_embeddings(directory, model_name, embeddings_path, indices_path, hashes_path)

def build_corpus_and_hashes(directory: str) -> Tuple[List[str], List[str], Dict[str, str]]:
    """Build corpus and calculate hashes from markdown files."""
    corpus = []
    filenames = []
    hashes = {}
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")
        return filenames, corpus, hashes
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read()
                corpus.append(content)
                name = filename.replace('.md', '')
                filenames.append(name)
                hashes[name] = hashlib.md5(content.encode()).hexdigest()
    
    return filenames, corpus, hashes

def build_and_save_embeddings(
    directory: str,
    model_name: str,
    embeddings_path: str,
    indices_path: str,
    hashes_path: str
) -> Tuple[List[str], np.ndarray, SentenceTransformer]:
    """Build and save search indices."""
    filenames, corpus, hashes = build_corpus_and_hashes(directory)
    
    if not corpus:
        logger.warning("No markdown files found to index.")
        return [], np.array([]), None
    
    try:
        model = SentenceTransformer(model_name)
        embeddings = model.encode(corpus, convert_to_tensor=True)
        np.save(embeddings_path, embeddings.cpu().numpy())
        
        indices = {filename: index for index, filename in enumerate(filenames)}
        with open(indices_path, 'w') as f:
            json.dump(indices, f)
        with open(hashes_path, 'w') as f:
            json.dump(hashes, f)
        
        logger.info("Search indices built and saved successfully.")
        return filenames, embeddings.cpu().numpy(), model
    except Exception as e:
        logger.error(f"Error building search indices: {e}")
        return [], np.array([]), None 