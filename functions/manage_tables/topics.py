import sqlite3

from ..create_id import last_id


def show_topics():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT topic_id, topic FROM topics")
    topics = [i for i in cursor.fetchall()]
    db.close()
    return topics


def is_new_topic(topic):
    is_new_topic = True
    all_topics = show_topics()
    topics = [(topic[1]) for topic in all_topics]
    for i in topics:
        if topic == i:
            is_new_topic = False
    return is_new_topic


def get_topic_id(topic):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT topic_id FROM topics WHERE topic = '" + topic + "'")
    topic_id = cursor.fetchone()[0]
    db.close()
    return topic_id


def create_topic(topic):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        select_topic = "SELECT topic FROM topics"
        id = last_id(select_topic) + 1

        cursor.execute("INSERT INTO topics VALUES('" + str(id) + "', '" + topic + "')")
        db.commit()
        db.close()
        topic_id = get_topic_id(topic)
        return topic_id
    except sqlite3.Error as error:
        print("Error: ", error)


def use_topic(topic_id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT topic FROM topics WHERE topic_id = '" + topic_id + "'")
    topic = cursor.fetchone()[0]
    db.close()
    return topic
