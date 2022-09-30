import sqlite3

from ..create_id import last_id

# topics


def show_topics():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT topic_id, topic FROM topics")
    topics = []
    for i in cursor.fetchall():
        topics.append(i)
    return topics


def read_id_topic(topic):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT topic_id FROM topics WHERE topic = '" + topic + "'")
    return cursor.fetchone()[0]


def is_new_topic(topic):
    is_new_topic = True
    topics = show_topics()
    topics = [(topic[1]) for topic in topics]
    for i in topics:
        if topic == i:
            is_new_topic = False
    return is_new_topic


def create_topic(topic):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()

    cursor.execute("SELECT topic FROM topics")
    n_topics = cursor.fetchall()
    n = len(n_topics)

    select_topic = "SELECT topic FROM topics"
    the_last_id = last_id(select_topic)

    cursor.execute(
        "INSERT INTO topics VALUES('" + str(the_last_id + 1) + "', '" + topic + "')"
    )
    db.commit()
    db.close()

    topic_id = read_id_topic(topic)
    return topic_id


def use_topic(topic):
    topic_id = read_id_topic(topic)
    return topic_id
