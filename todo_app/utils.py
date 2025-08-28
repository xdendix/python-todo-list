from datetime import datetime
from typing import Optional

def validate_date_format(date_string: str) -> bool:
    """
    Validasi format tanggal YYYY-MM-DD
    
    Args:
        date_string: String tanggal yang akan divalidasi
        
    Returns:
        bool: True jika format valid, False jika tidak
    """
    if not date_string:
        return False
        
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_past_deadline(deadline: str) -> bool:
    """
    Cek apakah deadline sudah lewat
    
    Args:
        deadline: String tanggal dalam format YYYY-MM-DD
        
    Returns:
        bool: True jika deadline sudah lewat, False jika belum
    """
    if not deadline or not validate_date_format(deadline):
        return False
        
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        return deadline_date < datetime.now()
    except ValueError:
        return False

def format_deadline_display(deadline: str) -> str:
    """
    Format tampilan deadline dengan indikator jika sudah lewat
    
    Args:
        deadline: String tanggal dalam format YYYY-MM-DD
        
    Returns:
        str: String yang diformat untuk ditampilkan
    """
    if not deadline:
        return "-"
    
    if is_past_deadline(deadline):
        return f"{deadline} ⚠️ (terlewat)"
    
    return deadline
