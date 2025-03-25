import os
import zipfile
import pytest
import shutil
import sys

# Add src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from zip_archive import create_zip_archive


@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    # Create a directory for test files
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    
    # Create sample files
    file1 = test_dir / "test1.txt"
    file1.write_text("Content of test file 1")
    
    file2 = test_dir / "test2.txt"
    file2.write_text("Content of test file 2")
    
    return [str(file1), str(file2)]


def test_create_zip_archive_basic(sample_files, tmp_path):
    """Test basic zip archive creation"""
    archive_path = str(tmp_path / "test_archive.zip")
    
    # Create zip archive
    result = create_zip_archive(sample_files, archive_path)
    
    # Verify successful creation
    assert result is True
    assert os.path.exists(archive_path)
    
    # Verify contents of zip file
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        assert set(zipf.namelist()) == set(os.path.basename(f) for f in sample_files)


def test_create_zip_archive_no_extension(sample_files, tmp_path):
    """Test creating zip with no extension"""
    archive_path = str(tmp_path / "test_archive")
    
    # Create zip archive
    result = create_zip_archive(sample_files, archive_path)
    
    # Verify successful creation with .zip extension added
    assert result is True
    assert os.path.exists(archive_path + '.zip')


def test_create_zip_archive_empty_files_list():
    """Test error handling for empty files list"""
    with pytest.raises(ValueError, match="At least one file must be provided"):
        create_zip_archive([], "test_archive.zip")


def test_create_zip_archive_nonexistent_file(tmp_path):
    """Test error handling for nonexistent files"""
    archive_path = str(tmp_path / "test_archive.zip")
    
    with pytest.raises(FileNotFoundError, match="File not found"):
        create_zip_archive(["/path/to/nonexistent/file.txt"], archive_path)


def test_create_zip_archive_multiple_directories(sample_files, tmp_path):
    """Test creating zip with files from multiple directories"""
    # Create an additional file in a different directory
    extra_dir = tmp_path / "extra_files"
    extra_dir.mkdir()
    extra_file = extra_dir / "extra.txt"
    extra_file.write_text("Extra file content")
    
    # Combine files from different directories
    all_files = sample_files + [str(extra_file)]
    archive_path = str(tmp_path / "multi_dir_archive.zip")
    
    # Create zip archive
    result = create_zip_archive(all_files, archive_path)
    
    # Verify successful creation
    assert result is True
    assert os.path.exists(archive_path)
    
    # Verify contents of zip file
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        assert set(zipf.namelist()) == set(os.path.basename(f) for f in all_files)