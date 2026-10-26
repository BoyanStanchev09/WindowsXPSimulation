from django.db import models


class ExtensionChoices(models.TextChoices):
    """
    All extension choices are AI generated so that the project
    can include as many as possible
    """
    # Text and document files
    TXT = "txt", "Plain text (.txt)"
    DOC = "doc", "Word document (.doc)"
    DOCX = "docx", "Word document (.docx)"
    ODT = "odt", "OpenDocument text (.odt)"
    RTF = "rtf", "Rich Text Format (.rtf)"
    PDF = "pdf", "PDF document (.pdf)"
    MD = "md", "Markdown (.md)"
    CSV = "csv", "CSV spreadsheet (.csv)"
    XLS = "xls", "Excel spreadsheet (.xls)"
    XLSX = "xlsx", "Excel spreadsheet (.xlsx)"
    ODS = "ods", "OpenDocument spreadsheet (.ods)"
    PPT = "ppt", "PowerPoint presentation (.ppt)"
    PPTX = "pptx", "PowerPoint presentation (.pptx)"
    ODP = "odp", "OpenDocument presentation (.odp)"

    # Web and markup files
    HTML = "html", "HTML document (.html)"
    CSS = "css", "CSS stylesheet (.css)"
    JS = "js", "JavaScript (.js)"
    TS = "ts", "TypeScript (.ts)"
    JSON = "json", "JSON data (.json)"
    XML = "xml", "XML document (.xml)"
    YAML = "yaml", "YAML data (.yaml)"
    PHP = "php", "PHP script (.php)"
    PY = "py", "Python script (.py)"
    RB = "rb", "Ruby script (.rb)"
    JAVA = "java", "Java source (.java)"
    C = "c", "C source (.c)"
    CPP = "cpp", "C++ source (.cpp)"
    H = "h", "C/C++ header (.h)"
    GO = "go", "Go source (.go)"
    RS = "rs", "Rust source (.rs)"
    SQL = "sql", "SQL script (.sql)"

    # Image files
    JPG = "jpg", "JPEG image (.jpg)"
    JPEG = "jpeg", "JPEG image (JPEG) (.jpeg)"
    PNG = "png", "PNG image (.png)"
    GIF = "gif", "GIF image (.gif)"
    BMP = "bmp", "Bitmap image (.bmp)"
    SVG = "svg", "SVG image (.svg)"
    WEBP = "webp", "WebP image (.webp)"
    TIFF = "tiff", "TIFF image (.tiff)"
    ICO = "ico", "Icon image (.ico)"
    PSD = "psd", "Photoshop document (.psd)"

    # Audio files
    MP3 = "mp3", "MP3 audio (.mp3)"
    WAV = "wav", "WAV audio (.wav)"
    AAC = "aac", "AAC audio (.aac)"
    FLAC = "flac", "FLAC audio (.flac)"
    OGG = "ogg", "Ogg audio (.ogg)"
    M4A = "m4a", "M4A audio (.m4a)"
    MIDI = "midi", "MIDI audio (.midi)"

    # Video files
    MP4 = "mp4", "MP4 video (.mp4)"
    AVI = "avi", "AVI video (.avi)"
    MKV = "mkv", "Matroska video (.mkv)"
    MOV = "mov", "QuickTime video (.mov)"
    WMV = "wmv", "Windows Media video (.wmv)"
    WEBM = "webm", "WebM video (.webm)"
    MPEG = "mpeg", "MPEG video (.mpeg)"
    M4V = "m4v", "M4V video (.m4v)"

    # Archives and compressed files
    ZIP = "zip", "ZIP archive (.zip)"
    RAR = "rar", "RAR archive (.rar)"
    SEVEN_Z = "7z", "7-Zip archive (.7z)"
    TAR = "tar", "TAR archive (.tar)"
    GZ = "gz", "Gzip archive (.gz)"
    BZ2 = "bz2", "Bzip2 archive (.bz2)"

    # Executables and disk images
    EXE = "exe", "Windows executable (.exe)"
    MSI = "msi", "Windows installer (.msi)"
    DLL = "dll", "Windows library (.dll)"
    APP = "app", "Application bundle (.app)"
    ISO = "iso", "Disk image (.iso)"
