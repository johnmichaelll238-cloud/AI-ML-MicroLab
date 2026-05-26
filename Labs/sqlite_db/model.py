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

def add_cve(cve_id, description, severity):
    #Details go here
    
    pass

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

def link_cve_to_version():
    #Associate specific vulnerabilities to particular versions of software for better security mitigation

    pass

def get_vulnerabilities(): #Will most likely be called in main.py as orchestrator function, Extract the associated vulnerabilities from any software version
    #Connect to database

    #JOIN Tables

    #Fetch rows

    #return results

    pass