import sqlite3

def create_tables(): #Data structure here:
    #Connect to database
    conn = sqlite3.connect("vulns.db")
    cursor = conn.cursor()
    #Create software table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS software (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
    )
    """)
    #Create CVE table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS cves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id TEXT UNIQUE,
    description TEXT,
    severity TEXT
    )
    """)
    #Create Version table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    software_id INTEGER,
    version TEXT,
    FOREIGN KEY (software_id)
    REFERENCES software(id)
    )
    """)
    # Keep older lab DBs compatible: add missing version column if needed.
    version_columns = [row[1] for row in cursor.execute("PRAGMA table_info(versions)").fetchall()]
    if "version" not in version_columns:
        cursor.execute("ALTER TABLE versions ADD COLUMN version TEXT")
    #Create mapping table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS version_cves (
    version_id INTEGER,
    cve_id INTEGER,
    
    FOREIGN KEY (version_id)
    REFERENCES versions(id),

    FOREIGN KEY (cve_id)
    REFERENCES cves(id)
    )
    """)
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

def add_software(name):  #Pass name here
    #Connect to database
    conn = sqlite3.connect("vulns.db")
    cursor = conn.cursor()
    #Insert software name
    cursor.execute("""
    INSERT OR IGNORE INTO software (name)
    VALUES (?)
    """, (name,))
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

def add_cve(cve_id, description, severity): #Details go here
    conn = sqlite3.connect("vulns.db")
    cursor = conn.cursor()
    cursor.execute(""" 
    INSERT OR IGNORE INTO cves (cve_id, description, severity)
    VALUES (?, ?, ?)
    """, (cve_id, description, severity))    
    
    conn.commit()
    conn.close()

def add_version(software_name, version):  #Add a version to software in question
    #Connect to database
    conn = sqlite3.connect("vulns.db")
    cursor = conn.cursor()
    #Resolve software name to its id.
    software_row = cursor.execute(
        "SELECT id FROM software WHERE name = ?",
        (software_name,),
    ).fetchone()
    if software_row is None:
        cursor.execute("INSERT OR IGNORE INTO software (name) VALUES (?)", (software_name,))
        software_row = cursor.execute(
            "SELECT id FROM software WHERE name = ?",
            (software_name,),
        ).fetchone()
    software_id = software_row[0]
    #Insert into versions table
    cursor.execute(""" 
    INSERT INTO versions(
    software_id,
    version
    )
    VALUES (?, ?)
    """, (software_id, version))
    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

def link_cve_to_version(version_id, cve_id):  #Associate specific vulnerabilities to particular versions of software for better security mitigation
    conn = sqlite3.connect("vulns.db")
    cursor = conn.cursor()
    cursor.execute(""" 
    INSERT INTO version_cves (
    version_id,
    cve_id
    )
    VALUES (?, ?)
    """, (version_id, cve_id))

    conn.commit()
    conn.close()

def get_vulnerabilities(): #Will most likely be called in main.py as orchestrator function, Extract the associated vulnerabilities from any software version
    #Connect to database
    conn = sqlite3.connect("vulns.db")
    cursor = conn.cursor()
    #JOIN Tables
    cursor.execute(""" 
    SELECT
        software.name,
        versions.version,
        cves.cve_id
        cves.severity

    FROM version_cves

    JOIN versions
    ON version_cves.version_id = versions.id

    JOIN software
    ON versions.software_id = software.id

    JOIN cves
    ON version_cves.cve_id = cves.id

    """)

    #Fetch rows
    results = cursor.fetchall()
    conn.close()
    #return results
    return results