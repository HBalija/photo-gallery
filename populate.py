import os

from app import db, Photo


folder_list = os.listdir('static/img')

obj_list = [obj.filename for obj in Photo.query.all()]


def populate():
    for pic in folder_list:
        pic_path = os.path.join('static/img', pic)
        if pic not in obj_list and os.path.isfile(pic_path):
            new_obj = Photo(name=pic, desc=format_desc(pic))
            db.add(new_obj)

    db.commit()


def format_desc(value):
    return value.split('.')[0].replace('_', ' ')


if __name__ == '__main__':
    db.create_all()
    populate()
