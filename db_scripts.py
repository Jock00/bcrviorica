import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT NOT NULL,
            image_resolution text NOT NULL,
            image_type text NOT NULL,
            description TEXT NOT NULL,
            title TEXT NOT NULL,
            date_upload TEXT NOT NULL,
            views INTEGER NOT NULL,
            tags text
        )
    ''')

    conn.commit()
    conn.close()


def insert_data(image_name, description, title, tags):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    image_resolution = "100x100"
    image_type = "jpeg"
    date_upload = datetime.now().strftime("%d %b %Y")
    sql_query = f"""
        insert into posts
        (image, image_resolution, image_type, description, title, date_upload, views, tags)
        values
        ('{image_name}', '{image_resolution}', '{image_type}', '{description}', '{title}', '{date_upload}', 0, '{tags}')
    """
    cursor.execute(sql_query)
    print("inserted!")
    conn.commit()
    conn.close()


def get_db_connection():
    conn = sqlite3.connect('app.db')  # Connect to the SQLite database
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn


def get_batch(batch_size=8, page=1):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")  # Execute the SQL SELECT statement
    rows = cursor.fetchall()  # Fetch all rows from the query result
    conn.close()  # Close the connection
    users = [dict(row) for row in rows][
            batch_size * (page - 1): batch_size * page]
    return users  # Return JSON response


def get_post_by_id(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM posts where id={post_id}")
    result = dict(cursor.fetchone())
    return result


def detele_all():
    sql_query = "delete from posts"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    print("deleted!")
    conn.commit()
    conn.close()

def update_count_view(post_id):
    sql_query = f"update posts set views=views+1 where id={post_id} "
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    print("view increased!")
    conn.commit()
    conn.close()

def rebase():
    detele_all()

    title = "Vincent van Gogh: The Starry Night"
    description = 'O interpretare unica a "Noptii instelate" de Van Gogh, cu culori vibrante si detalii personalizate ce redau cerul si peisajul nocturn intr-un stil distinct.'
    tags = "Peisaj | Vincent van Gogh"
    insert_data("1.jpeg", description, title, tags)

    title = "Buchet de Hortensii"
    description = 'O pictura delicata ce surprinde frumusetea hortensiilor in nuante de albastru si mov, asezate intr-o vaza simpla, oferind un aer calm si elegant.'
    tags = "Hortensii | Flori | Natura | Vaza | Pictura delicata | Culori pastel | Arta florala | Peisaj interior | Eleganta | Calm | Decor romantic"
    insert_data("2.jpeg", description, title, tags)

    title = "Flori in vaza albastra"
    description = "Un aranjament vibrant de flori rosii si albastre intr-o vaza decorata cu motive traditionale albastre, plasat pe un fundal intunecat pentru a evidentia contrastul culorilor si detaliile florale."
    tags = "flori | vaza albastra | aranjament floral | pictura artistica | contrast de culori | motive traditionale | natura statica | arta decorativa | design floral"
    insert_data("3.jpeg", description, title, tags)

    title = "Coliba de pe malul marii"
    description = "O scena linistita ce surprinde o coliba veche din lemn, asezata pe un ponton ce se intinde in largul marii. In prim-plan, o barca asteapta lin pe apa, sub un cer incarcat de nori albi."
    tags = "coliba | mare | barca | peisaj marin | ponton | natura statica | cer noros | scena linistita | peisaj pitoresc | arta peisagistica"
    insert_data("4.jpeg", description, title, tags)

    title = "Aranjament floral in vaza rustica"
    description = "O compozitie expresiva cu flori delicate in nuante de alb, galben si portocaliu, asezate intr-o vaza rustica de ceramica. Fundalul albastru creeaza un contrast subtil, iar detaliile adauga o nota de miscare si vitalitate."
    tags = "flori | vaza rustica | aranjament floral | pictura artistica | fundal albastru | natura statica | design floral | arta decorativa | expresivitate | compozitie dinamica"
    insert_data("5.jpeg", description, title, tags)

    title = "Flori albe in vaza de ceramica"
    description = "Un aranjament simplu si elegant cu flori albe delicate intr-o vaza de ceramica cu detalii subtile. Fundalul in tonuri de albastru si galben completeaza frumusetea naturala a compozitiei."
    tags = "flori | vaza de ceramica | aranjament floral | pictura artistica | natura statica | fundal albastru | eleganta simpla | design floral | arta decorativa | compozitie naturala"
    insert_data("6.jpeg", description, title, tags)

    title = "Flori portocalii in pahar de sticla"
    description = "Un buchet de flori portocalii si frunze verzi, asezat intr-un pahar de sticla transparent, surprins pe un fundal pastelat. Compozitia emana naturalete si o atmosfera linistita, cu detalii subtile ale petalelor si frunzelor cazute."
    tags = "flori | pahar de sticla | aranjament floral | natura statica | fundal pastelat | flori portocalii | design floral | pictura artistica | compozitie naturala | detalii subtile"
    insert_data("7.jpeg", description, title, tags)

    title = "Mos Craciun cu caciula verde"
    description = "O reprezentare simpatica a lui Mos Craciun purtand o caciula verde cu buline albe, inconjurat de fulgi de zapada pe un fundal roz pastelat. Pictura emana caldura si bucurie, potrivita pentru atmosfera sarbatorilor de iarna."
    tags = "Mos Craciun | caciula verde | fulgi de zapada | sarbatori de iarna | pictura artistica | fundal pastelat | atmosfera festiva | Craciun | decor de sarbatori | arta decorativa"
    insert_data("8.jpeg", description, title, tags)


if __name__ == "__main__":
    update_count_view(29)


