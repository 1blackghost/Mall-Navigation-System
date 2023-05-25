import sqlite3


def reset_back_to_start() -> None:
    """
    Reset the database to the initial state.

    This function drops the existing 'locations' table and recreates it.

    Note:
        This action requires admin privilege.

    Returns:
        None
    """
    conn = sqlite3.connect('location.db')
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = input()
    c.execute("DROP TABLE IF EXISTS locations")
    if a in ("y", "yes"):
        c.execute('''CREATE TABLE IF NOT EXISTS locations
                    (uid INTEGER PRIMARY KEY AUTOINCREMENT,
                     place TEXT NOT NULL,
                     category TEXT NOT NULL,
                     coordinates TEXT NOT NULL
                     )''')

    conn.commit()
    c.close()
    conn.close()


def update_user(uid, place=None, category=None, coordinates=None) -> None:
    """
    Update user information in the database.

    Args:
        uid: User ID of the user to update.
        place: New place (optional).
        category: New category (optional).
        coordinates: New coordinates (optional).

    Returns:
        None
    """
    conn = sqlite3.connect('location.db')
    c = conn.cursor()
    update_fields = []

    if place is not None:
        update_fields.append(("place", place))
    if category is not None:
        update_fields.append(("category", category))
    if coordinates is not None:
        update_fields.append(("coordinates", coordinates))

    if len(update_fields) > 0:
        update_query = "UPDATE locations SET "
        update_query += ", ".join(f"{field} = ?" for field, _ in update_fields)
        update_query += " WHERE uid = ?"
        values = [value for _, value in update_fields]
        values.append(uid)
        c.execute(update_query, values)

    conn.commit()
    c.close()
    conn.close()


def insert_user(place="", category="", coordinates="") -> int:
    """
    Insert a new user into the database.

    Args:
        place: Place of the user.
        category: Category of the user.
        coordinates: Coordinates of the user.

    Returns:
        int: ID of the inserted user.
    """
    conn = sqlite3.connect('location.db')
    c = conn.cursor()

    c.execute("INSERT INTO locations (place, category, coordinates) VALUES (?, ?, ?)",
              (place, category, coordinates))
    uid = c.lastrowid
    conn.commit()
    c.close()
    conn.close()

    return uid


def read_user(place=None) -> list:
    """
    Read user details from the database.

    Args:
        place: Place name to retrieve user details. If None, retrieve all locations.

    Returns:
        list: User details as a list of tuples.
    """
    conn = sqlite3.connect('location.db')
    c = conn.cursor()

    if place is not None:
        c.execute("SELECT * FROM locations WHERE place = ?", (place,))
        result = c.fetchall()
    else:
        c.execute("SELECT * FROM locations")
        result = c.fetchall()

    c.close()
    conn.close()

    return result
