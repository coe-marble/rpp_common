"""Filesystem helpers shared by RPP packages."""

import logging
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def restore_on_failure(*, files=(), trees=(), created_trees=None):
    """Restore files and directory trees after an exception.

    ``created_trees`` may be a list populated inside the context with newly
    created folders. These are removed on failure without taking backups.
    Rollback errors are logged; the original exception is re-raised.
    """
    paths = {Path(path) for path in files}
    trees = [Path(path) for path in trees]
    existing_directories = set()
    for tree in trees:
        if tree.exists():
            existing_directories.add(tree)
            for path in tree.rglob("*"):
                if path.is_dir():
                    existing_directories.add(path)
                elif path.is_file():
                    paths.add(path)
    originals = {path: path.read_bytes() if path.exists() else None for path in paths}
    missing_directories = set()
    for path in [*paths, *trees]:
        parent = path.parent
        while not parent.exists():
            missing_directories.add(parent)
            parent = parent.parent

    try:
        yield
    except Exception:
        directories = set(missing_directories)
        for tree in [*trees, *map(Path, created_trees or ())]:
            try:
                if tree.exists():
                    if tree not in existing_directories:
                        directories.add(tree)
                    for path in tree.rglob("*"):
                        if path.is_dir():
                            if path not in existing_directories:
                                directories.add(path)
                        elif path.is_file():
                            paths.add(path)
            except Exception:
                logging.getLogger(__name__).exception(
                    "Could not inspect directory during rollback: %s", tree)
        for path in paths:
            try:
                original = originals.get(path)
                if original is None:
                    path.unlink(missing_ok=True)
                elif not path.exists() or path.read_bytes() != original:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(original)
            except Exception:
                logging.getLogger(__name__).exception(
                    "Could not roll back file %s", path)
        for directory in sorted(directories, key=lambda path: len(path.parts), reverse=True):
            try:
                if directory.exists():
                    directory.rmdir()
            except Exception:
                logging.getLogger(__name__).exception(
                    "Could not remove directory %s", directory)
        raise


